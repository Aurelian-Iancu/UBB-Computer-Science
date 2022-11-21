% a. Write a predicate to determine the sum of two numbers written in list representation.

% myCarry(a,b,c) = 
% = 1 , if a + b + c > 9
% = 0, otherwise

% myCarry(A:number, B:number, C:number, R:number) = 
% (i,i,i,o)

myCarry(A,B,C,1):-
    AB is A + B,
    ABC is AB + C,
    ABC > 9.
myCarry(A,B,C,0):-
    AB is A + B,
    ABC is AB + C,
    ABC =< 9.

% myDigit(a,b,c) = 
% = (a + b + c) mod 10 , if a + b + c > 9
% = a + b + c, otherwise

% myDigit(A:number, B:number, C:number, R:number) = 
% (i,i,i,o)

myDigit(A,B,C,R):-
    AB is A + B,
    ABC is AB + C,
    ABC > 9,
    R is ABC mod 10.
myDigit(A,B,C,ABC):-
    AB is A + B,
    ABC is AB + C,
	ABC =< 9.

% myAppend(l1l2...ln,e) = 
% = [e], if n = 0
% = {l1} U myAppend(l2...ln), otherwise

% myAppend(L:list, E:number, R:list)
% (i,i,o)

myAppend([],E,[E]).
myAppend([H|T],E,[H|R]):-
    myAppend(T,E,R).

% myReverse(l1l2...ln) = 
% = [], if n = 0
% = myAppend(myReverse(l2...ln),l1), otherwise

% myReverse(L:list, R:list)
% (i,o)

myReverse([],[]).
myReverse([H|T],NR):-
    myReverse(T,R),
    myAppend(R,H,NR).

% suma(l1l2...ln, p1p2...pm, c, r) = 
% = r , if c = 0 and n = 0 and m = 0
% = {c} U r , if n = 0 and m = 0 and c != 0
% = suma([],p2...pm, myCarry(0,p1,c), myDigit(0,p1,c) U r), if n = 0
% = suma(l2...ln, [], myCarry(l1,0,c), myDigit(l1,0,c) U r), if m = 0
% = suma(l2...ln, p2...pm, myCarry(l1,p1,c), myDigit(l1,p1,c) U r), otherwise

% suma(L:list, P:list, C:number, R:list, RR:list)
% (i,i,i,i,o)

suma([],[],0,[]).
suma([],[],1,[1]).
suma([],[H|T],C,[RD|R]):-
    myCarry(0,H,C,RC),
    myDigit(0,H,C,RD),
    suma([],T,RC,R).
suma([H|T],[],C,[RD|R]):-
    myCarry(H,0,C,RC),
    myDigit(H,0,C,RD),
    suma(T,[],RC,R).
suma([H1|T1],[H2|T2],C,[RD|R]):-
    myCarry(H1,H2,C,RC),
    myDigit(H1,H2,C,RD),
    suma(T1,T2,RC,R).

mainSum(L,P,R,RR):-
    myReverse(L,RL),
    myReverse(P,RP),
    suma(RL,RP,0,R),
    myReverse(R,RR).

% b. For a heterogeneous list, formed from integer numbers and list of digits, write a predicate to compute the
%    sum of all numbers represented as sublists.
%    Eg.: [1, [2, 3], 4, 5, [6, 7, 9], 10, 11, [1, 2, 0], 6] => [8, 2, 2]

% heterList(l1l2...ln) = 
% [], if n = 0
% suma(myReverse(l1), heterList(l2...ln)), if l1 is a list
% heterList(l2...ln), otherwise

% heterList(L:list, R:list)
% (i,o)

heterList([],[]).
heterList([H|T],RR):-
    is_list(H),
    !,
    heterList(T,R),
    myReverse(H,RH),
    suma(RH,R,0,RR).
heterList([_|T],R):-
    heterList(T,R).

mainHeterList(L,R,RR):-
    heterList(L,R),
    myReverse(R,RR).

testA():-
    mainSum([1,2,3], [1,2,4], [7,4,2], [2,4,7]),
    mainSum([1,2,3], [0], [3,2,1], [1,2,3]),
    mainSum([9,9,9],[1,0,1], [0,0,1,1], [1,1,0,0]),
    mainSum([], [1,2,3], [3,2,1], [1,2,3]).

testB():-
    mainHeterList([[1,2,3], 3, 4, 0, [1,2,4]], [7,4,2], [2,4,7]),
    mainHeterList([[], [1,2,3,4], 4,5,6], [4,3,2,1], [1,2,3,4]),
    mainHeterList([[], [], 1,2,3,4],[], []),
    mainHeterList([[9,9,9], [1,0,1], 1,1,5], [0,0,1,1], [1,1,0,0]).
            
            
            
            
            
