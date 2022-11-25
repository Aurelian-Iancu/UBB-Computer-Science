% a. Transform a list in a set, in the order of the last occurrences of elements.
%  Eg.: [1,2,3,1,2] is transformed in [3,1,2].

% count(l1l2...ln, elem) = 
% = 0, if n = 0
% = 1 + count(l2...ln, elem), if l1 = elem
% = count(l2...ln, elem), otherwise

% count(L:list, E:number, R:number)
% (i,i,o)

myCount([],_,0).
myCount([H|T],E,R1):-
    H=:=E,
    myCount(T,E,R),
    R1 is R + 1.
myCount([H|T],E,R):-
    H=\=E,
    myCount(T,E,R).

% removeElem(l1l2...ln, elem, count) = 
% [], if n = 0
% removeElem(l2...ln, elem, count - 1), if elem = l1 and count > 1
% {l1} U removeElem(l2...ln, elem, count), otherwise

% removeElem(L:list, E:number, C:number, R:list)
% (i,i,i,o)

removeElem([],_,_,[]).
removeElem([H|T],E,C,R):-
    H=:=E,
    C > 1,
    C1 is C -1,
    removeElem(T,E,C1,R),!.
removeElem([H|T],E,C,[H|R]):-
    removeElem(T,E,C,R).

% set(l1l2...ln) = 
% = [] , if n = 0
% = set(removeElem(l1l2...ln, l1, c)), if c = count(l1l2...ln, l1) > 1
% = {l1} U set(l2...ln), otherwise

% set(L:list, R:list)
% (i,o)

set([],[]).
set([H|T],R):-
    myCount([H|T],H,RC),
    RC > 1,
    removeElem([H|T],H,RC,RE),
    set(RE,R), !.
set([H|T],[H|R]):-
    set(T,R).

% b. Define a predicate to determine the greatest common divisor of all numbers from a list.

% myGCD(a,b)=
% = a, if b = 0
% = b, if a = 0
% = myGCD(a % b, b), a >= b
% = myGCD(a, b % a), a < b

% myGCD(A:number,B:number,R:number)
% (i,i,o)

myGCD(0,B,B):-!.
myGCD(A,0,A):-!.
myGCD(A,B,R):-
    A>=B,
    A1 is A mod B,
    myGCD(A1,B,R).
myGCD(A,B,R):-
    A<B,
    B1 is B mod A,
    myGCD(A,B1,R).

% listGCD(l1l2...ln) = 
% = l1 , if n = 1
% myGCD(l1, listGCD(l2...ln)), otherwise

% listGCD(L:list,R:list)
% (i,o)

listGCD([H],H).
listGCD([H|T],R1):-
    listGCD(T,R),
    myGCD(H,R,R1).