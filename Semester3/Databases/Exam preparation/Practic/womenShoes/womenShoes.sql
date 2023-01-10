create database WomenShoes
go

use WomenShoes 
go 

create table PresShops
(
	psid int primary key, 
	name varchar(100),
	city varchar(100),
)

create table Women(
	wid int primary key,
	wName varchar(100),
	maxSpend int
	)

create table ShoeModels(
	smid int primary key,
	smName varchar(100),
	season varchar(100)
)

create table Shoes(
	sid int primary key,
	price int,
	smid int foreign key references ShoeModels(smid)
)

create table ShoesPresShops(
	sid int foreign key references Shoes(sid),
	psid int foreign key references PresShops(psid),
	primary key(sid, psid),
	nrShoes int
)

create table WomenShoes(
	wid int foreign key references Women(wid),
	sid int foreign key references Shoes(sid),
	primary key(wid, sid),
	nrBought int,
	value int
)

--drop table PresShops
--drop table Women 
--drop table Shoes 
--drop table ShoeModels 
--drop table ShoesPresShops
--drop table WomenShoes

----inserts
insert into PresShops values (1, 'presShop1', 'Cj')
insert into PresShops values (2, 'presShop2', 'Cj')
insert into PresShops values (3, 'presShop3', 'Cj')
insert into PresShops values (4, 'presShop4', 'Cj')
insert into PresShops values (5, 'presShop5', 'Cj')
insert into PresShops values (6, 'presShop6', 'Cj')
insert into PresShops values (7, 'presShop7', 'Cj')
insert into PresShops values (8, 'presShop8', 'Cj')

insert into Women values (1, 'woman1', 100)
insert into Women values (2, 'woman2', 100)
insert into Women values (3, 'woman3', 100)
insert into Women values (4, 'woman4', 100)
insert into Women values (5, 'woman5', 100)
insert into Women values (6, 'woman6', 100)
insert into Women values (7, 'woman7', 100)
insert into Women values (8, 'woman8', 100)
insert into Women values (9, 'woman9', 100)
insert into Women values (10, 'woman10', 100)


insert into ShoeModels values (1, 'shoeModel1', 'summer')
insert into ShoeModels values (2, 'shoeModel2', 'summer')
insert into ShoeModels values (3, 'shoeModel3', 'summer')
insert into ShoeModels values (4, 'shoeModel4', 'summer')
insert into ShoeModels values (5, 'shoeModel5', 'summer')
insert into ShoeModels values (6, 'shoeModel6', 'summer')
insert into ShoeModels values (7, 'shoeModel7', 'summer')
insert into ShoeModels values (8, 'shoeModel8', 'summer')
insert into ShoeModels values (9, 'shoeModel9', 'summer')
insert into ShoeModels values (10, 'shoeModel10', 'summer')

insert into Shoes values (1, 50, 1)
insert into Shoes values (2, 50, 3)
insert into Shoes values (3, 50, 4)
insert into Shoes values (4, 50, 2)
insert into Shoes values (5, 50, 3)
insert into Shoes values (6, 50, 4)
insert into Shoes values (7, 50, 5)
insert into Shoes values (8, 50, 6)
insert into Shoes values (9, 50, 2)
insert into Shoes values (10, 50, 7)
insert into Shoes values (11, 50, 8)

insert into ShoesPresShops values (1, 1, 20)
insert into ShoesPresShops values (2, 3, 20)
insert into ShoesPresShops values (1, 2, 20)
insert into ShoesPresShops values (1, 3, 20)
insert into ShoesPresShops values (1, 4, 20)
insert into ShoesPresShops values (3, 1, 20)
insert into ShoesPresShops values (4, 1, 20)
insert into ShoesPresShops values (5, 1, 20)
insert into ShoesPresShops values (6, 1, 20)
insert into ShoesPresShops values (7, 1, 20)
insert into ShoesPresShops values (8, 1, 20)
insert into ShoesPresShops values (9, 1, 20)
insert into ShoesPresShops values (10, 1, 20)
insert into ShoesPresShops values (11, 1, 20)
insert into ShoesPresShops values (2, 1, 20)
insert into ShoesPresShops values (7, 4, 20)
insert into ShoesPresShops values (8, 5, 20)
insert into ShoesPresShops values (7, 6, 20)
insert into ShoesPresShops values (8, 7, 20)
insert into ShoesPresShops values (6, 8, 20)
insert into ShoesPresShops values (7, 5, 20)
insert into ShoesPresShops values (8, 6, 20)

insert into WomenShoes values (1, 1, 3, 75)
insert into WomenShoes values (1, 2, 3, 75)
insert into WomenShoes values (1, 3, 3, 75)
insert into WomenShoes values (1, 4, 3, 75)
insert into WomenShoes values (1, 5, 3, 75)
insert into WomenShoes values (1, 6, 3, 75)
insert into WomenShoes values (1, 7, 3, 75)
insert into WomenShoes values (1, 8, 3, 75)
insert into WomenShoes values (1, 9, 3, 75)
insert into WomenShoes values (1, 10, 3, 75)
insert into WomenShoes values (1, 11, 3, 75)
insert into WomenShoes values (2, 3, 1, 75)
insert into WomenShoes values (3, 4, 1, 75)
insert into WomenShoes values (4, 5, 1, 75)
insert into WomenShoes values (5, 6, 1, 75)
insert into WomenShoes values (6, 7, 1, 75)
insert into WomenShoes values (7, 8, 1, 75)
insert into WomenShoes values (8, 9, 1, 75)
insert into WomenShoes values (9, 10, 3, 75)

delete from WomenShoes

----2. procedure
go
create or alter procedure addShoe
@shoeId int,
@presShopId int,
@numberOfShoes int
as
	declare @nr int;
	set @nr = 0;
	set @nr = (select count(*)
				from ShoesPresShops
				where sid = @shoeId and @presShopId = psid)
	if(@nr = 0)
	begin 
		insert into ShoesPresShops values (@shoeId, @presShopId, @numberOfShoes)
	end		
	else
	begin
		update ShoesPresShops set nrShoes = nrShoes + @numberOfShoes
	end

select * from ShoesPresShops

exec addShoe 11, 2, 3

---3 View 
go
create or alter view showWomen
as
	select W2.wid, W2.wname
	from(
		select distinct WS.wid
		from WomenShoes WS
		where WS.nrBought >= 2
	) t inner join Women W2 on W2.wid = t.wid

--select * from showWomen

----4. function

go
create or alter function atLeastShoes(@t int)
returns table
as
return 
	select S2.sid, SM.smName, SM.season
	from(
		select S.sid
		from ShoesPresShops S
		group by S.sid 
		having count(S.psid) >= @t
	) t inner join Shoes S2 on S2.sid = t.sid inner join ShoeModels SM on S2.smid = SM.smid

--select S.sid, count(S.psid)
--from ShoesPresShops S
--group by S.sid

--select * from atLeastShoes (3)




