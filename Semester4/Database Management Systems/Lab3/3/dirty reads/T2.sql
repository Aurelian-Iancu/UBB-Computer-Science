use Lab3_DBMS
go

-- we can read uncommitted data(dirty read)
set tran isolation level read uncommitted
begin tran
-- see update
select * from Beers
waitfor delay '00:00:06'
--update was rolled back
select * from Beers
commit tran

