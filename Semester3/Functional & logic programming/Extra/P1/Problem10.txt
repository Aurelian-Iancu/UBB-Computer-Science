%Problem 10.
% a. Define a predicate to test if a list of an integer elements has a "valley" aspect 
% (a set has a "valley" aspect if elements decreases up to a certain point, and then increases. 

% valley(l1l2...ln, flag)
% true, flag = 1, n <=1
% valley(l2...ln, 0), if l1 < l2 and flag = 0
% valley(l2...ln, 0), if l1 >= l2 and flag = 0
% valley(l2...ln, 1), if l1 > l2 and flag = 1
% false, otherwise

%valley(L - list, F - flag)
%(i,i)
    

valley([_], 1).
valley([H1,H2|T], 0):-
    H1 > H2,
    valley([H2|T], 0).
valley([H1,H2|T], _):-
    H1 < H2,
    valley([H2|T], 1).

mainValley(L):-
    valley(L, 0).

% b. Calculate the alternatesum oflist’s elements(l1 -l2 + l3 ...).

% alternateSum(l1l2...ln) = 
% = 0, n = 0
% = l1 - l2 + alternateSum(l3...ln), otherwise

% alternateSum(L-list, R-result)
% flow(i,o), (i,i)

alternateSum([], 0).
alternateSum([H], H).
alternateSum([H1,H2|T], S2):-
             alternateSum(T, S),
             S1 is S + H1,
             S2 is S1 - H2.
