% Problem1
% a. Write a predicate to determine the lowest common multiple of a list formed from integer numbers.

% gcd(a,b) = 
% 1, a = 1
% 1, b = 1
% a, a = b
% gcd(a-b,b), a > b
% gcd(a, b-a), b > a

% gcd(A-number, B-number, R-result)
%flow(i,i,o), (i,i,i)

gcd(_,1,1).
gcd(1,_,1).
gcd(A,A,A).
gcd(A,B,R):-
    A > B,
    A1 is A - B,
    gcd(A1,B,R).
gcd(A,B,R):-
    B > A,
    B1 is B - A,
    gcd(A, B1, R).


% lcm(a,b) = 
% 0, a = 0
% 0, b = 0
% a * b / gcd(a,b), otherwise

% lcm(A-number,B-number,R-result)
% flow(i,i,i), (i,i,o)

lcm(A,B,R):-
    P is A * B,
    gcd(A,B,G),
    R is P / G.

% listLcm(l1l2...ln) = 
% 1, n = 0
% l1, n = 1
% lcm(l1 U listLcm(l2...ln))

%listLcm(L - list, R - result)
%flow(i,i),(i,o)

listLcm([], 1).
listLcm([H],H).
listLcm([H|T], R):-
    listLcm(T, R1),
    lcm(H, R1, R).

% b. Write a predicate to add a value v after 1-st, 2-nd, 4-th, 8-th, ... element in a list.2.

%insertPos(l1l2...ln, elem, pos, index)
% [], if n = 0
% {l1} U {elem} U insertPos(l2...ln, pos*2, index+1), if pos = index
% {l1} U insertPos(l2...ln, pos, index+1), if pos != index

%insertPos(L - list, E, number, Pos-position, Index - index, R - result list)
%flow(i,i,i,i,o), (i,i,i,i,i)

insertPos([], _, _, _, []).
insertPos([H|T], E, Pos, Index, [H,E|R]):-
    Pos =:= Index,
    NewPos is Pos * 2,
    NewIndex is Index + 1,!,
    insertPos(T, E, NewPos, NewIndex, R).
insertPos([H|T], E, Pos, Index, [H|R]):-
    NewIndex is Index + 1,
    insertPos(T,E,Pos, NewIndex,R).
                  
%wrapper for insertPos
mainInsert(L, E, R):-
    insertPos(L,E,1,1,R).
