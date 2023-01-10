use BeerStore

drop procedure setSalaryFromPositionsInt
drop procedure setSalaryFromPositionsFloat
drop procedure addIncomeToStores
drop procedure removeIncomeFromStores
drop procedure addDefaultConstraintToProfitFromDistributors
drop procedure removeDefaultConstraintToProfitFromDistributors
drop procedure addStidPrimaryKeyEarnings
drop procedure removeStidPrimaryKeyEarnings
drop procedure newCandidateKeyEmployees
drop procedure dropCandidateKeyEmployees
drop procedure addEvent
drop procedure dropEvent
drop procedure newForeignKeyEvent
drop procedure removeForeignKeyEvent
drop procedure goToVersion


--modify the type of a column;
create procedure setSalaryFromPositionsInt as
	alter table Positions alter column salary int

execute setSalaryFromPositionsInt

create procedure setSalaryFromPositionsFloat as
	alter table Positions alter column salary float

execute setSalaryFromPositionsFloat

--add / remove a column;
create procedure addIncomeToStores as
	alter table Stores add income int

execute addIncomeToStores

create procedure removeIncomeFromStores as
	alter table Stores drop column income

execute removeIncomeFromStores

--add / remove a DEFAULT constraint;
create procedure addDefaultConstraintToProfitFromDistributors as
	alter table Distributors add constraint DEFAULTCONSTRAINT default(0) for profit

execute addDefaultConstraintToProfitFromDistributors

create procedure removeDefaultConstraintToProfitFromDistributors as
	alter table Distributors drop constraint DEFAULTCONSTRAINT

execute removeDefaultConstraintToProfitFromDistributors

--add / remove a primary key;
create procedure addStidPrimaryKeyEarnings as
	alter table Earnings
		drop constraint EARNINGS_PRIMARY_KEY
	alter table Earnings
		add constraint EARNINGS_PRIMARY_KEY primary key(eaid, stid)


execute addStidPrimaryKeyEarnings


create procedure removeStidPrimaryKeyEarnings as
	alter table Earnings
		drop constraint EARNINGS_PRIMARY_KEY
	alter table Earnings
		add constraint EARNINGS_PRIMARY_KEY primary key (eaid)
	
execute removeStidPrimaryKeyEarnings

--add / remove a candidate key;
create procedure newCandidateKeyEmployees as
	alter table Employees add constraint EMPLOYEES_CANDIDATE_KEY unique (emid, poid, name)

execute newCandidateKeyEmployees


create procedure dropCandidateKeyEmployees as
	alter table Employees drop constraint EMPLOYEES_CANDIDATE_KEY

execute dropCandidateKeyEmployees

--create / drop a table.

create procedure addEvent as
	create table Event(
		evid int primary key not null,
		aid int not null,
		numberOfTickets int not null
		)

execute addEvent

create procedure dropEvent as
	drop table Event

execute dropEvent

--add / remove a foreign key;

create procedure newForeignKeyEvent as
	alter table Event add constraint EVENT_FOREIGN_KEY foreign key(aid) references Addresses(aid)

execute newForeignKeyEvent

create procedure removeForeignKeyEvent as
	alter table Event drop constraint EVENT_FOREIGN_KEY

execute removeForeignKeyEvent
-------------------
--version table
create table versionTable (
    version int
)

drop table versionTable

insert into versionTable values (1)
--------------------
--procedures table

create table proceduresTable (
    fromVersion int,
    toVersion int,
    primary key (fromVersion, toVersion),
    nameProc varchar(max)
)

drop table proceduresTable

insert into proceduresTable values(1,2, 'setSalaryFromPositionsInt')
insert into proceduresTable values(2,1, 'setSalaryFromPositionsFloat')
insert into proceduresTable values(2,3, 'addIncomeToStores')
insert into proceduresTable values(3,2, 'removeIncomeFromStores')
insert into proceduresTable values(3,4, 'addDefaultConstraintToProfitFromDistributors')
insert into proceduresTable values(4,3, 'removeDefaultConstraintToProfitFromDistributors')
insert into proceduresTable values(4,5, 'addStidPrimaryKeyEarnings')
insert into proceduresTable values(5,4, 'removeStidPrimaryKeyEarnings')
insert into proceduresTable values(5,6, 'newCandidateKeyEmployees')
insert into proceduresTable values(6,5, 'dropCandidateKeyEmployees')
insert into proceduresTable values(6,7, 'addEvent')
insert into proceduresTable values(7,6, 'dropEvent')
insert into proceduresTable values(7,8, 'newForeignKeyEvent')
insert into proceduresTable values(8,7, 'removeForeignKeyEvent')

--------------------------------
-- goToVersion procedure
create procedure goToVersion(@newVersion int) as
    declare @curr int
    declare @var varchar(max)
    select @curr=version from versionTable

    if @newVersion > (select max(toVersion) from proceduresTable)
        raiserror ('Bad version', 10, 1)

    while @curr > @newVersion begin
        select @var=nameProc from proceduresTable where fromVersion=@curr and toVersion=@curr-1
        exec (@var)
        set @curr=@curr-1
    end

    while @curr < @newVersion begin
        select @var=nameProc from proceduresTable where fromVersion=@curr and toVersion=@curr+1
        exec (@var)
        set @curr=@curr+1
    end

    update versionTable set version=@newVersion



execute goToVersion 8
--------------------------
