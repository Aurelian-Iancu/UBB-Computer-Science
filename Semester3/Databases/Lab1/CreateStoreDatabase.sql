--drop table Addresses
--drop table ArtizanalBeers
--drop table Stores
--drop table Positions
--drop table Employees
--drop table BeerRecipes
--drop table Beers
--drop table DistributorsOfBeers
--drop table Earnings
--drop table Distributors




--create table Addresses
--(
--	aid INT PRIMARY KEY NOT NULL,
--	street VARCHAR(30) NOT NULL,
--	number TINYINT,
--	city VARCHAR(30) NOT NULL,
--	country VARCHAR(30) NOT NULL
--	)

--create table Stores --one Store to many Employees
--(
--	stid INT PRIMARY KEY NOT NULL,
--	aid INT FOREIGN KEY REFERENCES Addresses(aid) NOT NULL,
--	name VARCHAR(50) NOT NULL
--)

--create table Positions
--	(
--	poid INT PRIMARY KEY NOT NULL,
--	name VARCHAR(50) NOT NULL,
--	salary FLOAT NOT NULL
--	)


--create table Employees 
--(
--	emid INT NOT NULL,
--	stid INT FOREIGN KEY REFERENCES Stores(stid) NOT NULL,
--	poid INT FOREIGN KEY REFERENCES Positions(poid) NOT NULL,
--	name VARCHAR(50) NOT NULL
--	)

--create table ArtizanalBeers
--(
--	abid INT PRIMARY KEY NOT NULL,
--	name VARCHAR(50) NOT NULL,
--	quantity INT NOT NULL,
--	profit FLOAT NOT NULL
--	)

--create table BeerRecipes
--(
--	brid INT foreign KEY references ArtizanalBeers(abid) NOT NULL,
--	ingredients VARCHAR(70) NOT NULL,
--	price FLOAT NOT NULL,
--	primary key (brid)
--	)

--create table Beers
--(
--	bid INT PRIMARY KEY NOT NULL,
--	name VARCHAR(50) NOT NULL,
--	price FLOAT NOT NULL
--	)

--create table Distributors
--(
--	did INT PRIMARY KEY NOT NULL,
--	name VARCHAR(50) NOT NULL,
--	quantity INT NOT NULL,
--	profit FLOAT NOT NULL
--	)

--create table DistributorsOfBeers --many distributors to many beers
--(
--	bid INT FOREIGN KEY REFERENCES Beers(bid) NOT NULL,
--	did INT FOREIGN KEY REFERENCES Distributors(did) NOT NULL,
--	PRIMARY KEY(bid, did),
--    quantity INT NOT NULL,
--    buyingPrice FLOAT NOT NULL,
--    sellingPrice FLOAT NOT NULL
--	)

--create table Earnings --one earning to many Distributors or ArtizanalBeers
--(
--	eaid INT PRIMARY KEY NOT NULL,
--	value FLOAT NOT NULL,
--	stid INT FOREIGN KEY REFERENCES Stores(stid) NOT NULL,
--	bid INT,
--	did INT,
--	abid INT FOREIGN KEY REFERENCES ArtizanalBeers(abid),
--	foreign key (bid,did) references DistributorsOfBeers(bid,did)
--	)

	


	


