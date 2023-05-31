use Lab3_DBMS
go

insert into Beers values (1, 'beer1', 10.5)

--part1
begin tran
waitfor delay '00:00:05'
update Beers
set name = 'beerUpdated'
where bid = 1
commit tran