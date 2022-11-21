% Problem 5
% a. Write a predicate to compute the union of two sets.

% union(a1a2...an, b1b2...bm) = 
% = [], if n = 0, m = 0
% = list1, if m = 0
% = list2, if n = 0
% 
%

% union(L1 - list, L2 - list, R - result list)
% flow(i,i,i), (i,i,o)

union([],[],[]).
union(A,[], A).
union([], B, B).
union([H1|T1],[H2|T2],[H1|R]):-
    H1 =\= H2,
    union(T1, [H2|T2], R).
union([H1|T1],[H2|T2],[H1|R]):-
    H1 =:= H2,
    union(T1,T2,R).

% b. Write a predicate to determine the set of all the pairs of elements in a list.
% Eg.: L = [a b c d] => [[a b] [a c] [a d] [b c] [b d] [c d]].

% sets(l1l2...ln, k) = 
% = [], if k = 0
% = l1 + sets(l2...ln, k - 1), if k > 0
% = sets(l2...ln, k), if k > 0

% sets(L:list, K:number, R:list)
% (i,i,o)

sets(_,0,[]).
sets([H|T],K,[H|R]):-
    K1 is K - 1,
    sets(T,K1,R).
sets([_|T],K,R):-
     sets(T,K,R).   

% exists(l1l2...ln, e)
% true U exists(l2...ln,e), if l1 = e
% exists(l2...ln,e), otherwise

%exists(L - list, E - element)
%flow(i,i)
exists([E|_], E).
exists([_|R], E) :- exists(R,E).

% listToSet(l1l2...ln)
% [], n = 0
% l1 U listToSet(l1l2...ln), if 

% lisToSet(L - list, R - result list)
% flow(i,i), (i,o)
listToSet([], []).
listToSet([H|T], [H|R]):-
    not(exists(T,H)),
    listToSet(T, R).
listToSet([H|T], R):-
    exists(T,H),
    listToSet(T,R).

% genSets(l1..ln) =
% 	[], n = 0
% 	findall(sets(l1...ln, 2)) + listToSet, else

% genSets(L:list, R:list)
% genSets(i, o)

genSets([], []).
genSets(L, R1) :- 
    findall(RS, sets(L, 2, RS), R),
    listToSet(R, R1).
