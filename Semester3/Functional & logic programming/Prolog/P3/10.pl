% 10. For a list a1... an with integer and distinct numbers, define a predicate to determine all subsets with
%     sum of elements divisible with n

% subsets(l1l2...ln) = 
% = [], if n = 0
% = {l1} U subsets(l2...ln), if n>=1
% = subsets(l2...ln), if n >= 1

% subsets(L:list, R:result list)
% (i,o)

subsets([],[]).
subsets([H|T],[H|R]):-
    subsets(T,R).
subsets([_|T],R):-
    subsets(T,R).


% computeSum(l1l2...ln) = 
% = 0, if n = 0
% = l1 + computeSum(l2...ln)

% computeSum(L:list, R:number)
% (i,o)

computeSum([],0).
computeSum([H|T], R1):-
    computeSum(T,R),
    R1 is H + R.

% checkDivisibility(s, n) = 
% = true, if s % n == 0
% = false, otherwise

% (checkDivisibility(S:number, N:number)
% (i,i)

checkDivisibility(S,N):-S mod N =:= 0.

% oneSol(L: list, N: number R:list)
%(i,i,o)

oneSol(L,N,R):-
    subsets(L,R),
    computeSum(R,RS),
    checkDivisibility(RS,N).


allSols(L,N,R):-
    findall(RPartial,oneSol(L,N,RPartial),R).

testAllSols():-
    allSols([1,2,3,4], 3, [[1, 2, 3], [1, 2], [2, 3, 4], [2, 4], [3], []]),
    allSols([1,2,3], 1, [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]),
    allSols([1,2], 4, [[]]).
