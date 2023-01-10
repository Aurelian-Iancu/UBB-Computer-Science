use BeerStore
go

create procedure addAddressColumnToDistributors as
	alter table Distributors add aid int

execute addAddressColumnToDistributors

create procedure addAddressForeignKeyToDistributors as
	alter table Distributors add constraint DISTRIBUTORS_FOREIGN_KEY foreign key(aid) references Addresses(aid)

execute addAddressForeignKeyToDistributors

---added foreign key for Distributors an Address so that we can link all the 3 tables
---Addresses(primary key), Distributors(primary key, foreign key), DistributorsOfBeers(multiple-column primary-key)

create or alter procedure addAddresses
@n int
as
begin
	declare @i int = 0
	while(@i < @n)
	begin
		insert into Addresses values ((-1) * @i, concat('Address ', @i), 0, 'City', 'Country')
		set @i = @i + 1
	end
end

execute addAddresses 100

create or alter procedure removeAddresses
as
begin
	delete from Addresses where aid <= 0
end	

execute removeAddresses
----------------------first table
create or alter procedure addDistributors
@n int
as
begin
	declare @aid int = (select top 1 A.aid from Addresses A where A.street like 'Address %')
	declare @i int = 0
	while(@i < @n)
	begin
		insert into Distributors values ((-1) * @i, concat('Distributor ', @i) , 0, @aid)
		set @i = @i + 1
	end
end

execute addDistributors 100

create or alter procedure removeDistributors
as
begin
	delete from Distributors where did <= 0
end

execute removeDistributors
----------------second table
create or alter procedure addDistributorsOfBeers
@n int
as
begin
	declare @did int
	declare @bid int
	declare curs cursor
		for
		select d.did, b.bid from (select D.did from Distributors D where did <= 0) d cross join Beers b
	open curs
	declare @i int  = 1
	while @i <= @n
	begin
		fetch next from curs into @did, @bid
		insert into DistributorsOfBeers(bid,did, quantity, buyingPrice, sellingPrice) values (@bid, @did, -69 * @i, 0, 0)
		set @i = @i + 1
	end
	close curs
	deallocate curs
end
go



execute addDistributorsOfBeers 200

select * from DistributorsOfBeers where quantity < 0

create or alter procedure removeDistributorsOfBeers
as
begin
	delete from DistributorsOfBeers where quantity <= 0
end

execute removeDistributorsOfBeers
go
----------------third table

create or alter view firstView
as
	select * from Addresses
go

create or alter view secondView
as
	select D.did, D.name, A.aid, A.street from Distributors D inner join Addresses A on D.aid=A.aid
go

create or alter view thirdView
as 
	select D.did, D.name, count(*) as sells
	from DistributorsOfBeers DB 
	inner join Distributors D on D.did = DB.did
	group by D.did, D.name
go

create or alter procedure selectView
(@name varchar(100))
as
begin
	declare @sql varchar(250) = 'select * from ' + @name
	exec(@sql)
end
go

insert into Tables(Name) values ('Addresses')
insert into Tables(Name) values ('Distributors')
insert into Tables(Name) values ('DistributorsOfBeers')	

insert into Views(Name) values ('firstView')
insert into Views(Name) values ('secondView')
insert into Views(Name) values ('thirdView')

insert into Tests(Name) values ('addAddresses')
insert into Tests(Name) values ('removeAddresses')
insert into Tests(Name) values ('addDistributors')
insert into Tests(Name) values ('removeDistributors')
insert into Tests(Name) values ('addDistributorsOfBeers')
insert into Tests(Name) values ('removeDistributorsOfBeers')
insert into Tests(Name) values ('selectView')

--(7,1) (7,2) (7,3)
insert into TestViews([TestId], [ViewId]) values (7,1)
insert into TestViews([TestId], [ViewId]) values (7,2)
insert into TestViews([TestId], [ViewId]) values (7,3)


insert into TestTables([TestId], [TableId], [NoOfRows], [Position]) values (1, 1, 100, 1)
insert into TestTables([TestId], [TableId], [NoOfRows], [Position]) values (2, 1, 100, 3)
insert into TestTables([TestId], [TableId], [NoOfRows], [Position]) values (3, 2, 100, 2)
insert into TestTables([TestId], [TableId], [NoOfRows], [Position]) values (4, 2, 100, 2)
insert into TestTables([TestId], [TableId], [NoOfRows], [Position]) values (5, 3, 100, 3)
insert into TestTables([TestId], [TableId], [NoOfRows], [Position]) values (6, 3, 100, 1)

delete from TestTables

create or alter procedure runDeleteTests
as
begin
	declare @testId int
	declare @cmd varchar(max)

	declare fetchDeleteTests cursor
	for select TT.TestID, T.Name from TestTables TT join Tests T on TT.TestID = T.TestID where T.Name like 'remove%' order by TT.Position asc

	open fetchDeleteTests
	fetch fetchDeleteTests into @testId, @cmd
	while @@FETCH_STATUS = 0
	begin
		exec @cmd

		fetch fetchDeleteTests into @testId, @cmd
	end
	close fetchDeleteTests
	deallocate fetchDeleteTests
end
go

create or alter procedure runInsertTests
(@runTestId int)
as
begin
	declare @testId int
	declare @tableId int
	declare @numOfRows int
	declare @cmd varchar(max)

	declare fetchInsertTests cursor
	for select TT.TestID, TT.TableID, TT.NoOfRows, T.Name from TestTables TT join Tests T on TT.TestID = T.TestID where T.Name like 'add%' order by TT.Position asc

	open fetchInsertTests
	fetch fetchInsertTests into @testId, @tableId, @numOfRows, @cmd
	while @@FETCH_STATUS = 0
	begin
		declare @startTime datetime = GETDATE()

		exec (@cmd + ' ' + @numOfRows)

		declare @endTime datetime = GETDATE()
		insert into TestRunTables(TestRunID, TableID, StartAt, EndAt) values (@runTestId, @tableId, @startTime, @endTime)

		fetch fetchInsertTests into @testId, @tableId, @numOfRows, @cmd
	end

	close fetchInsertTests
	deallocate fetchInsertTests
end
go

create or alter procedure runViewTests
(@runTestId int)
as
begin
	declare @testId int
	declare @viewId int

	declare fetchViewTests cursor for
	select * from TestViews

	open fetchViewTests
	fetch fetchViewTests into @testId, @viewId
	while @@FETCH_STATUS = 0
	begin
		declare @cmd varchar(MAX) = (select Name from Tests where TestID = @testId)
		declare @args varchar(MAX) = (select Name from Views where ViewID = @viewId)
		declare @startTime datetime = GETDATE()
		
		exec (@cmd + ' ' + @args)

		declare @endTime datetime = GETDATE()
		insert into TestRunViews(TestRunID, ViewID, StartAt, EndAt) values (@runTestId, @viewId, @startTime, @endTime)

		fetch fetchViewTests into @testId, @viewId
	end

	close fetchViewTests
	deallocate fetchViewTests
end
go


create or alter procedure main
as 
begin 
	insert into TestRuns(startAt) values(getdate())
	declare @testId int = SCOPE_IDENTITY()
	exec runDeleteTests
	exec runInsertTests @testId
	exec runViewTests @testId

	update TestRuns set Description = 'delete + insert + view', EndAt = GETDATE() where TestRunID = @testId

	select * from TestRunTables
	select * from TestRunViews
	select * from TestRuns

end
go

create or alter procedure runTests
(@n int)
as
begin
	declare @i int = 0
	while @i < @n
	begin
		exec main
		set @i = @i + 1
	end

	select * from TestRunTables
	select * from TestRunViews
	select * from TestRuns
end
go

exec runTests 10

delete from TestRuns
delete from TestRunViews
delete from TestRunTables



