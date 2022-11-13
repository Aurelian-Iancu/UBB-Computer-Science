% Problem 6.
% a. Write a predicate to test if a list is a set
% 
% numberOcc(l1l2...ln,e) = 
% = 0, if n = 0
% 1 + numberOcc(l2...ln,e), if l1 = e
% numberOcc(l2...ln,e), otherwise

% numberOcc(L - list, E - element, R - result)
% flow(i,i,o), (i,i,i) 

numberOcc([], _, 0).
numberOcc([H|T], E, New):-
    H =:= E, !,
    numberOcc(T, E, Old),
    New is Old + 1.
numberOcc([_|T], E, R):-
    numberOcc(T,E,R).

% isSet(l1l2...ln) = 
% true, n = 0
% true U isSet(l2...ln), numberOcc(l1) <= 1

%isSet(L - list)
%flow(i)
isSet([]).
isSet([H|T]):-
    numberOcc([H|T], H, R),
    R =< 1,
    isSet(T), !.

% b. Write a predicate to remove the first three occurrencesof an element in a list.
% If the element occurs less than three times, all occurrenceswill be removed.

% remove3Occ(l1l2...ln,e,k) = 
% [], n = 0
% l1 U remove3Occ(l2...ln, e, k), l1 != e
% remove3Occ(l2...ln, e, k-1), l1 = e and k > 0

%remove3Occ(L -list, E-number, K - number, R - result list)
%flow(i,i,i,o), (i,i,i,i)

remove3Occ([], _, _, []).
remove3Occ([H|T], E, K, R):-
   	H =:= E,
    K > 0,
    K1 is K - 1, !,
    remove3Occ(T, E, K1, R).
remove3Occ([H|T], E, K, [H|R]):-
    remove3Occ(T,E,K,R).
