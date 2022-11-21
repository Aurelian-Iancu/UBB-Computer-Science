% Problem 7.
%a. Write a predicate to compute the intersection of two sets.

% exists(l1l2...ln,e) = 
% true, l1 = e
% exists(l2...ln, e), otherwise

% exists(L-list, E -number)
% flow(i,i), (i,o)e

exists([E|_], E).
exists([_|T], E):-
    exists(T, E).

% interesct(a1a2...an, b1b2...bm) = 
% = [], n = 0 and m = 0
% = list1, m = 0
% = list2, n = 0
% = a1 U intersect(a2...an, b1b2...bm), if exists(b1b2...bm, a1)
% = intersect(a2...an, b1b2...bm), otherwise

% intersect(L1 - list, L2 - list, R - result list)
% flow(i,i,i), (i,i,o)

intersect([],[],[]).
intersect(_,[],[]).
intersect([], _, []).
intersect([H|T],B,[H|R]):-
    exists(B, H), !,
    intersect(T, B,R).
intersect([_|T], B, R):-
    intersect(T, B,R).

%b. Write a predicate to create a list (m, ..., n) of all integer numbers fromthe interval[m, n].
% interval(m,n) =
% m, m = n
% m U interval(m + 1, n)

% interval(M - number, N - number, R - result list)
% flow(i,i,o), (i,i,i)

interval(M, M, [M]).
interval(M, N, [M|R]):-
    M1 is M + 1,
    interval(M1, N, R). 
