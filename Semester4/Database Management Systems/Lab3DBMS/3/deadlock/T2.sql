use Lab3_DBMS
go


begin tran
--exclusive lock on Distributors
update Distributors set name = 'T2' where did = 20
waitfor delay '00:00:10'

--this transaction will be blocked because T1 already has an exclusive lock on Beers
update Beers set name = 'T2' where bid = 20
commit tran