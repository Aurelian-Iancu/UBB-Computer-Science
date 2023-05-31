use Lab3_DBMS
go

--solution: set transaction isolation level to read commited
set tran isolation level read committed
begin tran
select * from Beers
waitfor delay '00:00:06'
select * from Beers
commit tran