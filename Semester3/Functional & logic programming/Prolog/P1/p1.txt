%  Write a predicate to determine the difference of two sets.
% contains(l1l2...ln, e) = 
% = false, if n = 0
% = true, if l1 = e
% = contains(l2...ln, e) , otherwise

% contains(L:list, E:number)
% contains(i,i)

contains([V|_],V).
contains([_|T],V):- contains(T,V).

% difference(l1l2...ln, p1p2...pm) = 
% = [], if n = 0
% = difference(l2...ln, p1p2...pm) , if contains(p1p2...pm, l1) = true
% {l1} U difference(l2...ln, p1p2...pm), otherwise

% difference(A:list,B:list,R:list)
% difference(i,i,o)

difference([],_,[]).
difference([H|T],B,R):-
    contains(B,H),
    difference(T,B,R).
difference([H|T],B,[H|R]):-
    difference(T,B,R).

% Write a predicate to add value 1 after every even element from a list.

% insert(l1l2...ln)=  
% = [], if n =0
% {l1} U {1} U insert(l2...ln), if l1 % 2 = 0
% {l1} U insert(l2...ln), otherwise

% insert(L:list,R:list)
% insert(i,o)

insert([],[]).
insert([H|T],[H,1|R]):-
    H mod 2 =:= 0,
    insert(T,R).
insert([H|T],[H|R]):-
    H mod 2 =:= 1,
    insert(T,R).

% Write a predicate that tests the difference function
test_difference():-
    difference([1,2,3],[1,2],[3]),
    difference([],[1,2,3],[]),
    difference([1,2,3],[4,5,6],[1,2,3]),
    difference([1,2,3],[1,2,3],[]).

% Write a predicate that tests the insert function
test_insert():-
    insert([1,2,3],[1,2,1,3]),
    insert([1,1,1],[1,1,1]),
    insert([],[]),
    insert([2],[2,1]),
    insert([2,3,4,5,6],[2,1,3,4,1,5,6,1]).

