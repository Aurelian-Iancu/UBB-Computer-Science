use Lab3_DBMS
go
--part 2: the row is changed while T2 is in progress, so we will see both values for name
set tran isolation level read committed
begin tran
--see first insert
select * from Beers
waitfor delay '00:00:06'
select * from Beers
commit tran

--delete from Beers where bid = 2