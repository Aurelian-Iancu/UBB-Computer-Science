% Problem 9.
% a. Insert an element on the positionn in a list.

% insertPos(l1l2...ln, pos, elem)
% [elem], n = 0, pos = 0
% insertPos(l2...ln, pos-1, elem), pos > 0
% elem U insertPos(l2...ln, pos, elem), pos = 0

%insertPos(L - list, P - pos, E - elem, R - result list)
%flow(i,i,i,i), (i,i,i,o)

insertPos(L, 0, E, [E|L]):-!.
insertPos([H|T], P, E, [H|R]):-
    P1 is P - 1,
    insertPos(T, P1, E, R).

% b.Define a predicate to determine the greatest common divisor of allnumbers froma list.

% gcd2(a,b)
% 1, a = 1
% 1, b = 1
% a, a = b
% gcd(a-b, b), a > b
% gcd(a, b-a), b > a

%gcd2(A-number,B-number,R-result)
%flow(i,i,i),(i,i,o)

gcd2(_,1,1).
gcd2(1,_,1).
gcd2(A,A,A).
gcd2(A, B, R):-
    A > B,
    A1 is A - B,
    gcd2(A1, B, R).
gcd2(A, B, R):-
    B > A,
    B1 is B - A,
    gcd2(A, B1, R).

% gcdList(l1l2...ln) = 
% l1, n = 1
% gcd2(l1, gcd(l2...ln)), otherwise

%gcdList(L - list, R -number)
% flow(i,i), (i,o)

gcdList([H], H).
gcdList([H|T], R1):-
    gcdList(T, R),
    gcd2(H, R, R1).
