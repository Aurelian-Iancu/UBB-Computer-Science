use Lab3_DBMS
go

--insert into Beers values(21, 'Beer21', 1.5)
--delete from Beers where bid = 21 

ALTER DATABASE Lab3_DBMS SET ALLOW_SNAPSHOT_ISOLATION ON
waitfor delay '00:00:10' 
BEGIN TRAN
UPDATE Beers SET name='name 21 1' WHERE bid=21;
commit tran

-- ALTER DATABASE Lab3_DBMS SET ALLOW_SNAPSHOT_ISOLATION OFF
-- UPDATE Beers SET Name = 'Name 126' WHERE ID = 21
-- SELECT * FROM Beers