use Lab3_DBMS
go


set tran isolation level repeatable read
begin tran
--inserted value does not exist yet
select * from Beers
waitfor delay '00:00:06'
-- we can see inserted value during the second read
select * from Beers
commit tran

