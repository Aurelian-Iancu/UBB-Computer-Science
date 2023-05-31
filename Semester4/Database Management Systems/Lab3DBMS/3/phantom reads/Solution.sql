USE Lab3_DBMS
GO

-- solution: set transaction isolation level to serializable

set tran isolation level serializable
begin tran
--inserted value does not exist yet
select * from Beers
waitfor delay '00:00:06'
-- we can see inserted value during the second read
select * from Beers
commit tran
