use Lab3_DBMS
go

select * from Distributors
select * from Beers

insert into Beers values (20, 'Beer20', 10.5)
insert into Distributors values(20, 'Distributor20', 10.51)

delete from Distributors where did = 20
delete from Beers where bid = 20



--part 1
begin tran
--exclusive lock on table Beers
update Beers set name = 'Transaction1' where bid = 20
waitfor delay '00:00:10'

--this transaction will be blocked because T2 already has an exclusive lock on Distributors
update Distributors set name = 'Transaction 1' where did = 20;
commit tran
