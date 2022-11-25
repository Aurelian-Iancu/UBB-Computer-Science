% a. Write a predicate to substitute in a list a value with all the elements of another list.

% Model matematic:
% insert(l1...ln, list) =
% 	list, n = 0
% 	{l1} U insert(l2...ln, list), otherwise

% insert(L:list, LIST:list, R:list)
% (i,i,o)

insert([],L,L).
insert([H|T],L,[H|R]):-
    insert(T,L,R).



% substituteElem(l1l2...ln, e1, p1p2...pm) = 
% = [], if n = 0
% = substituteElem(insert(p1p2...pm, l2...ln), e1, p1p2...pm), if l1 = e1
% = {l1} U substituteElem(l2...ln, e1, p1p2...pm), otherwise

% substituteElem(L:list, E:number, P:list, R:list)
% (i,i,i,o)

substituteElem([],_,_,[]).
substituteElem([H|T],E,P,R):-
    H=:=E,
    insert(P,T,RI),
    substituteElem(RI,E,P,R).
substituteElem([H|T],E,P,[H|R]):-
    H=\=E,
    substituteElem(T,E,P,R).

% b. Remove the n-th element of a list

% removeNthElem(l1l2...lk, n) = 
% [], if k = 0
% removeNthElem(l2...lk, n - 1), if n = 0
% {l1} U removeNthElem(l2...lk, n - 1), otherwise

% removeNthElem(L:list, N:number, R:list)
% (i,i,o)

removeNthElem([],_,[]).
removeNthElem([_|T],N,R):-
    N =:= 0,
    N1 is N - 1,
    removeNthElem(T,N1,R),!.
removeNthElem([H|T],N,[H|R]):-
    N1 is N - 1,
    removeNthElem(T,N1,R).