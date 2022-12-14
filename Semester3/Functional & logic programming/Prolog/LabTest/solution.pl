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

% numberAtom(l1l2...ln) = 
% = [], if n = 0
% = [l1, myCount(l1l2...ln, l1)] U numberAtom(removeOcc(l2...ln, l1)), otherwise

%numberAtom(L:list, R:list)
%numberAtom(i,o)

numberAtom([],[]).
numberAtom([H|T], [[H, RC] | R]):-
    numberOcc([H|T], H, RC),
    removeOcc(T, H, RR),
    numberAtom(RR, R).
