use Lab3_DBMS
go

--update conflict
SET TRANSACTION ISOLATION LEVEL SNAPSHOT
BEGIN TRAN
select * from Beers where bid = 21
waitfor delay '00:00:10'
select * from Beers where bid = 4
--T1 has now updated and obtained a lock on this table
--trying to update the same row will result in an error (process is blocked)
update Beers set name = 'New name 21 2' where bid = 21
commit tran