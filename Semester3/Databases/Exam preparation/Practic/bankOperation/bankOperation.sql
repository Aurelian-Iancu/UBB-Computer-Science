create database bankOperation
go

use bankOperation
go

create table Customers
(
	cid int primary key,
	name varchar(100),
	dOfBirth date
)

create table BankAccounts
(
	bid int primary key,
	IBAN int,
	currBal int,
	cid int foreign key references Customers(cid)
)

create table Cards
(
	caid int primary key,
	CVV int,
	bid int foreign key references BankAccounts(bid)
)

create table ATM
(
	aid int primary key,
	address varchar(100)
)

create table Transactions
(
	aid int foreign key references ATM(aid),
	caid int foreign key references Cards(caid),
	primary key (aid, caid) ,
	suma int,
	wTime time,
	wDate date
)

--drop table Customers
--drop table BankAccounts
--drop table Cards
--drop table ATM
--drop table Transactions

----inserts

insert into Customers values(1, 'customer1', '2002-05-15')
insert into Customers values(2, 'customer2', '2002-05-12')
insert into Customers values(3, 'customer3', '2002-05-13')
insert into Customers values(4, 'customer4', '2002-05-14')
insert into Customers values(5, 'customer5', '2002-05-15')
insert into Customers values(6, 'customer6', '2002-05-16')
insert into Customers values(7, 'customer7', '2002-05-17')

insert into BankAccounts values (1, 1234, 243, 1)
insert into BankAccounts values (2, 1235, 2434, 1)
insert into BankAccounts values (3, 1236, 243, 1)
insert into BankAccounts values (4, 1237, 2434, 1)
insert into BankAccounts values (5, 1238, 123, 2)
insert into BankAccounts values (6, 1239, 567, 4)
insert into BankAccounts values (7, 1240, 789, 7)
insert into BankAccounts values (8, 1241, 1000, 3)

insert into Cards values (1, 123, 1)
insert into Cards values (2, 124, 1)
insert into Cards values (3, 125, 7)
insert into Cards values (4, 126, 2)
insert into Cards values (5, 127, 7)
insert into Cards values (6, 128, 3)
insert into Cards values (7, 129, 4)
insert into Cards values (8, 130, 5)

insert into ATM values (1, 'address1')
insert into ATM values (2, 'address2')
insert into ATM values (3, 'address3')
insert into ATM values (4, 'address4')
insert into ATM values (5, 'address5')
insert into ATM values (6, 'address6')
insert into ATM values (7, 'address7')

insert into Transactions values (1, 1, 100, '11:11:11', '2002-05-15')
insert into Transactions values (1, 2, 100, '11:11:11', '2002-05-15')
insert into Transactions values (2, 3, 100, '11:11:11', '2002-05-15')
insert into Transactions values (2, 5, 100, '11:11:11', '2002-05-15')
insert into Transactions values (2, 7, 100, '11:11:11', '2002-05-15')
insert into Transactions values (2, 8, 100, '11:11:11', '2002-05-15')
insert into Transactions values (3, 7, 100, '11:11:11', '2002-05-15')
insert into Transactions values (4, 4, 100, '11:11:11', '2002-05-15')
insert into Transactions values (4, 5, 100, '11:11:11', '2002-05-15')
insert into Transactions values (5, 7, 100, '11:11:11', '2002-05-15')
insert into Transactions values (5, 5, 100, '11:11:11', '2002-05-15')
insert into Transactions values (6, 7, 100, '11:11:11', '2002-05-15')
insert into Transactions values (6, 1, 100, '11:11:11', '2002-05-15')
insert into Transactions values (7, 1, 100, '11:11:11', '2002-05-15')

insert into Transactions values (2, 1, 100, '11:11:11', '2002-05-15')
insert into Transactions values (3, 1, 100, '11:11:11', '2002-05-15')
insert into Transactions values (4, 1, 100, '11:11:11', '2002-05-15')
insert into Transactions values (5, 1, 100, '11:11:11', '2002-05-15')




------2. procedure
go
create procedure deleteCard
@cardId int 
as 
	declare @id int
	declare transactionCursor cursor for
	select C.caid from Cards C inner join Transactions T on C.caid = T.caid	
	open transactionCursor
	while @@FETCH_STATUS = 0
	begin
		fetch next from transactionCursor into @id
		if(@id = @cardId)
		begin 
			delete from Transactions where caid = @id
		end
	end
	close  transactionCursor
	deallocate transactionCursor

select * from Transactions
exec deleteCard 1

-----3. view

go
create or alter view allATMS 
as
	select C2.caid, C2.CVV
	from (
		select C.caid
		from Cards C inner join Transactions T on C.caid = T.caid
					 inner join ATM A on A.aid = T.aid 
		group by C.caid
		having count(A.aid) = (select count(*) from ATM)

	) t inner join Cards C2 on C2.caid = t.caid

--select * from allATMS

--- 4. function

go
create or alter function overSum ()
returns table
return
	select C2.caid, C2.CVV
	from (
		select C.caid
		from Cards C inner join Transactions T on C.caid = T.caid
		group by C.caid
		having sum(suma) > 300
	) t inner join Cards C2 on C2.caid = t.caid

go
select * from overSum ()



