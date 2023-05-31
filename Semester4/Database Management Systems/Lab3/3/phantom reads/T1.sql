use Lab3_DBMS
go


--part1
begin tran
waitfor delay '00:00:06'
insert into Beers values (3, 'Beer3', 10.43)
commit tran

--delete from Beers where bid = 3