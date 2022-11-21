% Problem 11.
% a. Write a predicate to substitute an element from a list with another element in the list.

% substitute(l1l2...ln, E, Rep)
% [], n = 0
% l1 U substitute(l2...ln), if E != Rep
% Rep U substitute(l2...ln), if E = Rep

%substitute(L-list, E-element, Rep - replacement element, R-result list)
% flow(i,i,i,o),(i,i,i,i)

substitute([], _, _, []).
substitute([H|T], E, Rep, [Rep|R]):-
    H =:= E,
    substitute(T,E,Rep,R).
substitute([H|T], E,Rep, [H|R]):-
    H =\= E,
    substitute(T,E,Rep,R).

% sublist(l1l2...ln, m, n, pos) = 
% [], n = 0
% l1 U sublist(l2...ln, m, n, pos + 1), if pos >= m and pos <= n
% sublist(l2...ln, m, n, pos + 1), otherwise

% sublist(L-list, m-number, n-number, pos-position,R-result list)
%flow(i,i,i,i,i),(i,i,i,i,o)

sublist([], _, N, P, []):- 
    P > N, !.
sublist([H|T], M, N, Pos, [H|R]):-
    Pos >= M,
    Pos =< N, !,
    Pos1 is Pos + 1,
    sublist(T,M,N,Pos1,R).
sublist([_|T], M, N, Pos, R):-
    Pos1 is Pos + 1,
    sublist(T,M,N,Pos1,R).

mainSublist(L, M,N,R):-
    sublist(L,M,N,0,R).
