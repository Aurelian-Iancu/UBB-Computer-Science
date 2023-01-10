create database myPoetry
go

use myPoetry
go

create table Users
(
	uid int primary key,
	name varchar(20),
	penName varchar(20) unique,
	yearOfBirth date
)

create table ExternalAwards
(
	eaid int primary key, 
	name varchar(50),
	uid int foreign key references Users(uid)
)

create table Judges
(
	jid int primary key,
	name varchar(50)
)

create table Competitions
(
	cid int primary key,
	yearOfOrganization int,
	weekNumber int,
	unique(yearOfOrganization, weekNumber)
)

create table Poems
(
	pid int primary key,
	uid int foreign key references Users(uid),
	cid int foreign key references Competitions(cid),
	title varchar(50),
	text varchar(50)
)

create table JudgesPoems
(
	jid int foreign key references Judges(jid),
	pid int foreign key references Poems(pid),
	primary key(jid, pid),
	points int,
	constraint score_note check(1 <= points and points <= 10)
)

--drop table Users
--drop table ExternalAwards
--drop table Competitions
--drop table Poems
--drop table Judges
--drop table JudgesPoems

insert into Users values(1, 'u1', 'u1', '2023-07-01')
insert into Users values(2, 'u2', 'u2', '2023-07-01')
insert into Users values(3, 'u3', 'u3', '2023-07-01')

insert into ExternalAwards values (1, 'exa1', 1)
insert into ExternalAwards values (2, 'exa2', 2)
insert into ExternalAwards values (3, 'exa3', 3)

insert into Judges values (1, 'j1')
insert into Judges values (2, 'j2')
insert into Judges values (3, 'j3')
insert into Judges values (4, 'j4')

insert into Competitions values (1, 2022, 40)
insert into Competitions values (2, 2022, 39)
insert into Competitions values (3, 2023, 50)

insert into Poems values (1, 1, 2, 'p1', 'p1')
insert into Poems values (2, 1, 3, 'p2', 'p2')
insert into Poems values (3, 2, 1, 'p3', 'p3')
insert into Poems values (4, 2, 2, 'p4', 'p4')
insert into Poems values (5, 2, 3, 'p5', 'p5')
insert into Poems values (6, 3, 3, 'p6', 'p6')

insert into JudgesPoems values (1, 1, 2)
insert into JudgesPoems values (1, 2, 7)
insert into JudgesPoems values (1, 3, 5)
insert into JudgesPoems values (1, 4, 6)
insert into JudgesPoems values (1, 5, 8)
insert into JudgesPoems values (2, 3, 1)
insert into JudgesPoems values (2, 4, 2)
insert into JudgesPoems values (3, 1, 3)

delete  from JudgesPoems

select * from Judges
select * from JudgesPoems


--------
--2
go
create procedure deleteJudges 
@judgeName varchar(50)
as
	declare @name varchar(50)
	declare @id int
	declare jpCursor cursor for
	select J.name, J.jid from Judges J inner join JudgesPoems JP on J.jid = JP.jid
	open jpCursor
	fetch next from jpCursor into @name, @id
	if (@name = @judgeName)
	begin 
		delete from JudgesPoems where jid = @id
		delete from Judges where name = @name
	end
	while @@FETCH_STATUS = 0
	begin
		fetch next from jpCursor into @name, @id
		if (@name = @judgeName)
		begin 
			delete from JudgesPoems where jid = @id
			delete from Judges where name = @name
		end
	end
	close jpCursor
	deallocate jpCursor

--exec deleteJudges 'j1'

go
create or alter view showCompetitions as
	select C2.yearOfOrganization, C2.weekNumber
	from (select  C.cid as tcid
		  from Poems P inner join Competitions C on P.cid = C.cid
					 inner join JudgesPoems Jp on P.pid = Jp.pid
		  where P.pid not in (select distinct JP2.pid from JudgesPoems JP2 where JP2.points >= 5)
		  group by C.cid
		  having count(*) >= 2) t inner join Competitions C2 on T.tcid = C2.cid

--select * from showCompetitions

go
create or alter function listUsers (@number int)
returns table 
return 
	select U2.name, U2.penName
	from (
		  select U.uid
		  from Users U inner join Poems P on P.uid = U.uid
		  group by U.uid
		  having count(*) >= @number) t inner join Users U2 on t.uid = U2.uid


--select * from listUsers (3)


	