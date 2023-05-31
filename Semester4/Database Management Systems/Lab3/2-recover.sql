USE Lab3_DBMS
GO

create or alter procedure procedureAddBeersRecover(@bid integer, @name varchar(50), @price float)
AS
	SET NOCOUNT ON
	BEGIN TRAN
	BEGIN TRY
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
		COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
	END CATCH
GO

create or alter procedure procedureAddDistributorsRecover(@did integer, @name varchar(50), @profit float)
AS
	SET NOCOUNT ON
	BEGIN TRAN
	BEGIN TRY
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
		COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
	END CATCH
GO


create or alter procedure procedureAddDistributorsOfBeersRecover(@bid integer, @did integer, @quantity integer, @buyingPrice FLOAT ,@sellingprice float)
as 
	SET NOCOUNT ON
	begin tran
	begin try
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
		commit tran
	end try
	begin catch
		rollback tran
	end catch
go

create or alter procedure badRecoverScenario
as
	exec procedureAddBeersRecover 2, 'beer2', 1.2
	exec procedureAddDistributorsRecover 2, 'distributor1', 'bad'
	exec procedureAddDistributorsOfBeersRecover 2, 2, 10, 11.3, 11.4
go


create or alter procedure goodRecoverScenario
as
	exec procedureAddBeersRecover 2, 'beer2', 1.2
	exec procedureAddDistributorsRecover 2, 'distributor1', 11.2
	exec procedureAddDistributorsOfBeersRecover 2, 2, 10, 11.3, 11.4
go

exec badRecoverScenario
select * from LogTable

exec goodRecoverScenario
select * from LogTable

SELECT * FROM Beers
SELECT * FROM Distributors
SELECT * FROM DistributorsOfBeers

delete from Beers where bid = 2
delete from Distributors where did = 2
delete from DistributorsOfBeers where bid = 2 and did = 2
	