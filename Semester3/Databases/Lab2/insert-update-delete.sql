use BeerStore

delete from Addresses
delete from Stores
delete from Employees
delete from Positions
delete from ArtizanalBeers
delete from BeerRecipes
delete from Beers
delete from Distributors
delete from DistributorsOfBeers
delete from Earnings


--Insert into Addresses table
insert into Addresses values(1, 'Strada Florilor', 2, 'Cluj-Napoca', 'Romania')
insert into Addresses values(2, 'Strada Pinilor', null, 'Cluj-Napoca', 'Romania')
insert into Addresses values(3, 'Strada Aricilor', 15, 'Abrud', 'Romania')

--Insert into Stores table
insert into Stores values(1, 1, 'Aurelian''s beers-Florilor')
insert into Stores values(2, 2, 'Aurelian''s beers-Plopilor')
insert into Stores values(3, 3, 'Aurelian''s beers-Aricilor')

--Insert that should bring an error if i put null
insert into Stores values(4, null, 'Aurelian''s beers-Error')

--Insert in Positions table
insert into Positions values(1, 'seller', 2500)
insert into Positions values(2, 'manager', 3750)
insert into Positions values(3, 'cicerone', 4500)

--Insert into Employees table
--First Store
insert into Employees values(1, 1, 1, 'Adolfo Stanley')
insert into Employees values(2, 1, 1, 'Aldo Dudley')
insert into Employees values(3, 1, 1, 'Maribel Alex')
insert into Employees values(4, 1, 2, 'Maribel Byrd')
insert into Employees values(5, 1, 3, 'June Sanders')
--Second Store
insert into Employees values(6, 2, 1, 'Ellen Newton')
insert into Employees values(7, 2, 1, 'Glenn Watkins')
insert into Employees values(8, 2, 1, 'Thalia Gilbert')
insert into Employees values(9, 2, 2, 'Slade Humphrey')
insert into Employees values(10, 2, 3, 'Marley Horne')
insert into Employees values(11, 2, 2, 'Error Employee')

--Insert into ArtizanalBeers
insert into ArtizanalBeers values(1, 'Porter American', 200, 0)
insert into ArtizanalBeers values(2, 'Amăruie Belgiană', 125, 0)
insert into ArtizanalBeers values(3, 'Leffe', 180, 0)
insert into ArtizanalBeers values(4, 'India Pale Ale Speidel', 160, 0)

--Insert into BeerRecipes
insert into BeerRecipes values(1, 'Malt, Hamei, Drojdie, Cafea macinata', 5.30)
insert into BeerRecipes values(2, 'Malt, Hamei, Drojdie', 4.65)
insert into BeerRecipes values(3, 'Malt, Hamei, Drojdie, Coriandru', 5.19)
insert into BeerRecipes values(4, 'Malt, Hamei, Drojdie', 4.90)

--Insert into Beers
insert into Beers values(1, 'Heineken, 0.33', 2.54)
insert into Beers values(2, 'Heineken, 0.4', 2.67)
insert into Beers values(3, 'Kozel blonda, 0.33', 1.90)
insert into Beers values(4, 'Kozel bruna, 0.33', 1.92)
insert into Beers values(5, 'Tuborg, 0.33', 1.76)
insert into Beers values(6, 'Neumarkt, 0.5', 1.30)
insert into Beers values(7, 'Neumarkt, 0.33', 1.23)
insert into Beers values(8, 'Ursus, 0.33', 1.85)
insert into Beers values(9, 'Ursus Retro, 0.33', 2.0)
insert into Beers values(10, 'Desperados, 0.4', 3.17)
insert into Beers values(11, 'Custom Desperados, 0.4', 7.80)


--Insert into Distributors
insert into Distributors values(1, 'Distributor 1', 0, 0)
insert into Distributors values(2, 'Distributor 2', 0, 0)
insert into Distributors values(3, 'Distributor 3', 0, 0)


--Insert into DistributorsOfBeers
--Change Beer so that it has no price
--First Distributor
insert into DistributorsOfBeers values(1,1, 100, 2.33,2.54)
insert into DistributorsOfBeers values(2,1, 150, 2.50,2.67)
insert into DistributorsOfBeers values(5,1, 150, 1.50,1.76)
insert into DistributorsOfBeers values(8,1, 150, 1.67,1.85)
insert into DistributorsOfBeers values(9,1, 125, 1.89,2.0)
--Second Distributor
insert into DistributorsOfBeers values(1,2, 125, 2.40,2.54)
insert into DistributorsOfBeers values(2,2, 125, 2.55,2.67)
insert into DistributorsOfBeers values(3,2, 150, 1.70,1.90)
insert into DistributorsOfBeers values(4,2, 125, 1.70,1.92)
--Third Distributor
insert into DistributorsOfBeers values(10,3, 200, 2.89,3.17)


--Insert into Earnings
insert into Earnings values(1, 0, 1, 1, 1, null)
insert into Earnings values(2, 0, 1, 2, 1, null)
insert into Earnings values(3, 0, 2, 1, 2, null)
insert into Earnings values(4, 0, 2, 10, 3, null)
insert into Earnings values(5, 0, 3, null, null, 1)



---------------------------------------------- Finish the insertion in the tables

--Update section
update Positions set salary = 2500 where name = 'seller' -- usage of =
update BeerRecipes set ingredients = 'Malt, Hamei, Drojdie, Zahar brun' where brid = 2 and ingredients = 'Malt, Hamei, Drojdie' -- usage of AND
update BeerRecipes set ingredients = 'Malt, Hamei, Drojdie, Turmeric' where brid = 4 and ingredients = 'Malt, Hamei, Drojdie'
update Addresses set number = 0 where number is null -- usage of is NULL
update DistributorsOfBeers set quantity = 100 where did in (2,3) --usage of in

--Delete section 
delete from Employees where name like 'Error%' -- usage of like
delete from Beers where price between 7 and 20 -- usage of between



