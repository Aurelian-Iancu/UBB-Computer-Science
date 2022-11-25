% a. Write a predicate to test equality of two sets without using the set difference.

% myLength(l1l2...ln) = 
% 0 , if n = 0
% 1 + myLength(l2...ln), otherwise

% myLength(L:list, R:number)
% (i,o)

myLength([],0).
myLength([_|T],R1):-
    myLength(T,R),
    R1 is R + 1.

% contains(l1l2...ln, elem)
% = true, if l1 = elem
% = contains(l2....ln, elem)

% contains(L:list,E:number)
% (i,i)

contains([V|_],V):-!.
contains([_|T],V):-
    contains(T,V).

% removeElement(l1l2...ln, elem) = 
% = [], if n = 0
% removeElement(l2...ln, elem), if l1 = elem
% {l1} U removeElement(l2...ln, elem), otherwise

% removeElement(L:list, E:number, R:list)
%(i,i,o)

removeElement([],_,[]).
removeElement([H|T],E,R):-
    H=:=E,
    removeElement(T,E,R).
removeElement([H|T],E,[H|R]):-
    H=\=E,
    removeElement(T,E,R).

% equalitySets(l1l2...ln, p1p2...pm) = 
% = true, if n = 0 and m = 0
% = equalitySets(removeElement(l2...ln, p1),removeElement(p2...pm, l1)),if m = n and contains(l1l2...ln, p1) = true
% and contains(p1p2...pm, l1) = true

% equalitySets(L:list,P:list)
% (i,i)

equalitySets([],[]):-!.
equalitySets([H1|T1],[H2|T2]):-
    myLength(T1,C1),
    myLength(T2,C2),
    C1=:=C2,
    contains([H1|T1],H2),
    contains([H2|T2],H1),
    removeElement(T1,H2,RE1),
    removeElement(T2,H1,RE2),
    equalitySets(RE1,RE2).

% b. Write a predicate to select the n-th element of a given list.

% selectElem(l1l2...ln, n) = 
% = l1, if n = 1
% = selectElem(l2...ln, n - 1), otherwise

% selectElem(L:list, N:number,R:number)
% (i,i,o)

selectElem([H|_],1,H):-!.
selectElem([_|T],N,R):-
    N1 is N-1,
    selectElem(T,N1,R).