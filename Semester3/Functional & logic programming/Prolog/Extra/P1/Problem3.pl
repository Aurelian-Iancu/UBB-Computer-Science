% Problem3.
% a. Define a predicate to remove from a list all repetitive elements. 
% Eg.: l=[1,2,1,4,1,3,4] => l=[2,3])
% 
%numberOcc(l1l2...ln,e) = 
% = 0, if n = 0
% 1 + numberOcc(l2l3...ln,e), if l1 == e
% numberOcc(l2l3...ln,e), if l1 != e

% numberOcc(L - list, E - elem, R - result)
% flow(i,i,o), (i,i,i)
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

% removeRepetitive(l1l2...ln)
% = [], if n = 0
% {l1} U removeRepetitive(l2l3..ln), if number numberOcc(l1) <= 1
%  removeOcc(l1) U removeRepetitive(l2l3..ln), else
%  
%  removeRepetitive(L-List, R-result List)
%  flow(i,i), (i,o)

removeRepetitive([], []).
removeRepetitive([H|T], R):-
    numberOcc([H|T], H, NR),
    NR > 1,
    removeOcc([H|T], H, R1),
    removeRepetitive(R1, R).
removeRepetitive([H|T], [H|R]):-
    numberOcc([H|T], H, NR),
    NR < 2,
    removeRepetitive(T, R).

%b.Remove all occurrence ofa maximum value from a list on integer numbers.

%max2numbers(number1, number2)
% 0, if number1 = 0 and number2 = 0
% number1 if number1 > number2
% number2 if number2 > number1

%max2numbers(A-number, B-number, R-number)
%flow(i,i,i), (i,i,o)

max2numbers(0,0,0).
max2numbers(A,B,A):-
    A>=B.
max2numbers(A,B,B):-
    B > A.

% myMax(l1l2...ln)
% l1, if n = 1
% max2numbers(l1, myMax(l2...ln)), else

% myMax(L - list, R - result max)
% flow (i,i), (i,o)

myMax([X],X).
myMax([H|T], R):-
    myMax(T, RM),
    max2numbers(H, RM, R).

%removeMaxOcc(L-list, R-result list)
%flow(i,i), (i,o)
removeMaxOcc(L, R):-
    myMax(L, M),
    removeOcc(L, M, R).
	
