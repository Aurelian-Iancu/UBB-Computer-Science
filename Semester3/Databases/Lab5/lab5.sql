create database Lab5 
go


use Lab5
go

-- Create the tables

create table Beers(
	bid int primary key not null,
	price int unique,
	quantity int
);

create table Distributors(
	did int primary key not null,
	profit int
	);

create table DistributorsOfBeers(
	dobid int primary key not null,
	did int foreign key references Distributors(did),
	bid int foreign key references Beers(bid)
);

drop table Beers
drop table Distributors
drop table DistributorsOfBeers

-- generate random data for the tables

go
create or alter procedure insertIntoBeers (@rows int) as
begin
	declare @aux int
	set @aux = @rows*100 + 13
	while @rows > 0
	begin
		insert into Beers values(@rows, @aux, @aux % 123)
		set @rows = @rows - 1
		set @aux = @aux + 1
	end
end


go
create or alter procedure insertIntoDistributors(@rows int) as
    while @rows > 0 begin
        insert into Distributors values (@rows, @rows * 17)
        set @rows = @rows-1
    end

go
create or alter procedure insertIntoDistributorsOfBeers(@rows int) as
    declare @bid int
    declare @did int
    while @rows > 0 begin
        set @bid = (select top 1 bid from Beers order by NEWID())
        set @did = (select top 1 did from Distributors order by NEWID())
        insert into DistributorsOfBeers values (@rows, @bid, @did)
        set @rows = @rows-1
    end

-- insert data
exec insertIntoBeers 5000
exec insertIntoDistributors 5000
exec insertIntoDistributorsOfBeers 5000

select * from Beers
select * from Distributors
select * from DistributorsOfBeers

delete from Beers
delete from Distributors
delete from DistributorsOfBeers

/*
	Remarks (indexes automatically created):
		- clustered index for bid column from Beers
		- unique, nonclustered index for price column from Beers
		- clustered index for did column from Distributors
		- clustered index for dobid column from DistributorsOfBeers
*/

-- a)
-- cluster index scand for Beers - scan the entire table
select * 
from Beers

-- cluster index seek for Beers - returns a specific susbet of rows
select *
from Beers
where bid < 100

--nonclustered index scan for Beers
select price
from Beers 

--nonclustered index seek for Beers
select price
from Beers 
where price < 500200

-- key lookup - nonclustered index seek + key look up - the data is found in a nonclustered index, but additional data is required
select price, quantity
from Beers
where price = 500100

-- b)
-- Write a query on table Tb with a WHERE clause of the form WHERE b2 = value and analyze its execution plan. 
-- Create a nonclustered index that can speed up the query. Examine the execution plan again.
select *
from Distributors
where profit = 5015

go
if exists(select name from sys.indexes where name = N'Index_Distributors_Profit')
	drop index Index_Distributors_Profit on Distributors

go
create nonclustered index Index_Distributors_Profit on Distributors(profit)

-- cost before creating index: 0.0161894
-- cost after creating index: 0.0032831

-- c)
-- Create a view that joing at least 2 tables. Check whether existing indexes are helpful;
-- if not, reassess existing indexes / examine the cardinality of the tables

go 
create or alter view View1 as 
	select B.bid, D.did, DB.dobid
	from DistributorsOfBeers DB
	inner join Beers B on B.bid = DB.bid
	inner join Distributors D on D.did = DB.did
	where B.quantity = 10 and D.profit between  1000 and 5000


select * 
from View1

/*
	with existing indexes (automatically created ones + nonclustered index on profit in Distributors): 0.133297
	when adding a nonclustered index on quantity in Beers: 0.116552
	when deleting the nonclustered on quantity and profit: 0.133297
	automatically created ones + nonclustered on profit + nonclustered on quantity + nonclustered on (bid, did) in Tc: 0.0906752
*/

IF EXISTS (SELECT name FROM sys.indexes WHERE name = N'Index_Beers_Quantity')
	DROP INDEX Index_Beers_Quantity ON Beers

CREATE NONCLUSTERED INDEX Index_Beers_Quantity ON Beers(quantity)

IF EXISTS (SELECT name FROM sys.indexes WHERE name = N'Index_DistributorsOfBeers_biddid')
	DROP INDEX Index_DistributorsOfBeers_biddid ON DistributorsOfBeers

CREATE NONCLUSTERED INDEX Index_DistributorsOfBeers_biddid ON DistributorsOfBeers(bid, did)