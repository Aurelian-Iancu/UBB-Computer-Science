USE Lab3_DBMS
GO


DROP TABLE IF EXISTS LogTable
CREATE TABLE LogTable(
	Lid INT IDENTITY PRIMARY KEY,
	TypeOperation VARCHAR(50),
	TableOperation VARCHAR(50),
	ExecutionDate DATETIME
);


-- use m:n relation Beers - Distributors

create or alter function validateString(@str varchar(30))
returns int
as
begin
	declare @return int
	set @return = 1
	if(@str is null or len(@str) < 2 or len(@str) > 30)
	begin
		set @return = 0
	end
	return @return 
end
go

CREATE OR ALTER FUNCTION validateInt (@int integer)
RETURNS INT
AS
BEGIN
	DECLARE @return INT
	SET @return = 1
	IF(@int < 0)
	BEGIN
		SET @return = 0
	END
	RETURN @return
END
GO

CREATE OR ALTER FUNCTION validateFloat (@float float)
RETURNS FLOAT
AS
BEGIN
	DECLARE @return FLOAT
	SET @return = 1
	IF(@float < 0)
	BEGIN
		SET @return = 0
	END
	RETURN @return
END
GO

create or alter procedure procedureAddBeers(@bid integer, @name varchar(50), @price float)
as
	SET NOCOUNT ON
	IF (dbo.validateString(@name) <> 1)
	BEGIN
		RAISERROR('Name is invalid', 14, 1)
	END
	IF (dbo.validateFloat(@price) <> 1)
	BEGIN
		RAISERROR('Price is invalid', 14, 1)
	END
	IF EXISTS (SELECT * FROM Beers B where B.bid = @bid)
	BEGIN
		RAISERROR('Beer already exists', 14, 1)
	END
	INSERT INTO Beers VALUES (@bid, @name, @price)
	INSERT INTO LogTable VALUES ('add', 'beer', GETDATE())
GO

create or alter procedure procedureAddDistributors(@did integer, @name varchar(50), @profit float)
as
	SET NOCOUNT ON
	IF (dbo.validateString(@name) <> 1)
	BEGIN
		RAISERROR('Name is invalid', 14, 1)
	END
	IF (dbo.validateFloat(@profit) <> 1)
	BEGIN
		RAISERROR('Profit is invalid', 14, 1)
	END
	IF EXISTS (SELECT * FROM Distributors D where D.did = @did)
	BEGIN
		RAISERROR('Distributor already exists', 14, 1)
	END
	INSERT INTO Distributors VALUES (@did, @name, @profit)
	INSERT INTO LogTable VALUES ('add', 'distributor', GETDATE())

go


create or alter procedure procedureAddDistributorsOfBeers(@bid integer, @did integer, @quantity integer, @buyingPrice FLOAT ,@sellingprice float)
as 
	SET NOCOUNT ON
	IF (dbo.validateInt(@quantity) <> 1)
	BEGIN
		RAISERROR('Quantity is invalid', 14, 1)
	END
	IF (dbo.validateFloat(@buyingPrice) <> 1)
	BEGIN
		RAISERROR('Buying price is invalid', 14, 1)
	END
	IF (dbo.validateFloat(@sellingprice) <> 1)
	BEGIN
		RAISERROR('Selling price is invalid', 14, 1)
	END
	IF EXISTS (SELECT * FROM DistributorsOfBeers DB where DB.bid = @bid AND DB.did = @did)
	BEGIN
		RAISERROR('Distributors of beers already exists', 14, 1)
	END
	INSERT INTO DistributorsOfBeers VALUES (@bid, @did, @quantity, @buyingPrice, @sellingprice)
	INSERT INTO LogTable VALUES ('add', 'distributorsOfBeers', GETDATE())
go

create or alter procedure addCommitScenario
as
	begin tran
	begin try
		exec procedureAddBeers 1, 'beer1', 10.2
		exec procedureAddDistributors 1, 'distributor1', 11.22
		exec procedureAddDistributorsOfBeers 1, 1, 10, 11.1, 11.2
		commit tran
	end try
	begin catch
		rollback tran
		return
	end catch
go

create or alter procedure addRollbackScenario
as
	begin tran
	begin try
		exec procedureAddBeers 1, 'beer1', 10.2
		exec procedureAddDistributors 1, 'distributor1', 'rollback'
		exec procedureAddDistributorsOfBeers 1, 1, 10, 11.1, 11.2
		commit tran
	end try
	begin catch
		rollback tran
		return
	end catch
go

EXEC addRollbackScenario
EXEC addCommitScenario


SELECT * FROM LogTable

SELECT * FROM Beers
SELECT * FROM Distributors
SELECT * FROM DistributorsOfBeers

delete from Beers where bid = 1
delete from Distributors where did = 1
delete from DistributorsOfBeers where bid = 1 and did = 1
