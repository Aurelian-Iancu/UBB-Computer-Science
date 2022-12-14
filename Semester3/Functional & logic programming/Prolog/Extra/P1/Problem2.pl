% Problem 2.
% a. Write a predicate to remove all occurrencesof a certain atom from a list.

%removeOcc(l1l2..ln,e) =
% = [], if n = 0
% = {l1} U removeOcc(l2l3...ln,e), if l1 != e
% = removeOCc(l2l3...ln,e), if l1 = e

%removeOcc(L-list, E-elem, R-result list)
%flow(i, i, o), (i,i,i)
removeOcc([],_,[]).
removeOcc([H|T], E, [H|R]):-
    H =\= E, !,
    removeOcc(T,E,R).
removeOcc([_|T], E, R):-
    %H =:= E,
    removeOcc(T,E,R).

% b.Define a predicate to produce a list of pairs (atom n) from an initial list of atoms. 
% In this initial list atom has n occurrences.
% Eg.:numberatom([1, 2, 1, 2, 1, 3, 1], X) => X =[[1, 4], [2, 2], [3, 1]].

%numberOcc(l1l2...ln,e) = 
% = 0, if n = 0
% 1 + numberOcc(l2l3...ln,e), if l1 == e
% numberOcc(l2l3...ln,e), if l1 != e

%numberOcc(L - list, E - elem, R - result)
%flow(i,i,o), (i,i,i)
numberOcc([],_, 0).
numberOcc([H|T], E, New):-
    H =:= E, !,
    numberOcc(T,E,Old),
    New is Old + 1.
numberOcc([_|T],E,R):-
    numberOcc(T,E,R).

%numberAtom(l1l2...ln) =
% = [], if n = 0
% = [l1, numberOcc(l1l2...ln, l1)] U numberAtom(l2..ln), if n >= 1

%numberAtom(L-list, R-resultList)
%flow(i,o), (i,i)
numberAtom([],[]).
numberAtom([H|T], [[H,Nr]|R]):-
    numberOcc([H|T], H, Nr),
    removeOcc([H|T], H, R1),
    numberAtom(R1,R).
