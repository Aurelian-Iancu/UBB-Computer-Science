use Lab3_DBMS
go

--solution: set transaction isolation level to reapeatable read
set tran isolation level repeatable read
begin tran
--see first insert
select * from Beers
waitfor delay '00:00:06'
select * from Beers
commit tran
