use Lab3_DBMS
go

begin tran 
update Beers
set name = 'beerTransaction'
where bid = 2
waitfor delay '00:00:06'
rollback tran
