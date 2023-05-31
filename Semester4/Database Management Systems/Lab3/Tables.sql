USE Lab3_DBMS;
drop table Beers;
drop table Distributors;
drop table DistributorsOfBeers;



create table Beers
(
	bid INT PRIMARY KEY NOT NULL,
	name VARCHAR(50) NOT NULL,
	price FLOAT NOT NULL
	)

create table Distributors
(
	did INT PRIMARY KEY NOT NULL,
	name VARCHAR(50) NOT NULL,
	profit FLOAT NOT NULL
	)

create table DistributorsOfBeers --many distributors to many beers
(
	bid INT FOREIGN KEY REFERENCES Beers(bid) NOT NULL,
	did INT FOREIGN KEY REFERENCES Distributors(did) NOT NULL,
	PRIMARY KEY(bid, did),
    quantity INT NOT NULL,
    buyingPrice FLOAT NOT NULL,
    sellingPrice FLOAT NOT NULL
	)

