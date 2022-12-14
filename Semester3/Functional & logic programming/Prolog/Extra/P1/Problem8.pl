% Problem 8.
% a. Write a predicate to determine if a list has even numbers of elements without counting the elements from the list.
 
% verifyEvenLen(l1l2...ln) = 
% true, n = 0
% false, n = 1
% verifyEvenLen(l3...ln)  

% verifyEvenLen(L - list)
% flow(i)

verifyEvenLen([]).
verifyEvenLen([_,_|T]):-
    verifyEvenLen(T).

% min2numbers(a,b)
% a, a <= b
% b, b < a

%b. Write a predicate to delete first occurrence of the minimum number from a list.

% min2numbers(A - number, B - number, R - result)
% flow(i,i, o), (i,i,i)

min2numbers(A, B, A):-
    A =< B.
min2numbers(A,B,B):-
    A > B.

% myMin(l1l2...ln) = 
% 0, n = 0
% l1, n = 1
% min2numbers(l1 U myMin(l2..ln)), otherwise

%myMin(L - list, R - number)
%flow(i,i), (i,o)

myMin([], 0).
myMin([H], H).
myMin([H|T], R):-
    myMin(T, RM),
    min2numbers(H, RM, R).

% removeMin(l1l2...ln, k)
% [], n = 0
% l1 U removeMin(l2...ln,k), if l1 != min(l)
% removeMin(l2...ln, k-1), if l1 != min(l), k > 0

%removeMin(L-list, E - element, K-number, R - result list)
% flow(i,i,i,o), (i,i,i,i)

removeMin([],_,_,[]).
removeMin([H|T],E, K, R):-
    H =:= E,
    K > 0,
    K1 is K - 1,
    removeMin(T, E, K1, R).
    
removeMin([H|T], E, K, [H|R]):-
    removeMin(T, E, K, R).

%wrapper for removeMin
mainRemoveMin(L, R):-
    myMin(L, RM),
    removeMin(L, RM, 1, R).
