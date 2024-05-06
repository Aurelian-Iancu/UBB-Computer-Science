[A, b] = no_name(500);
x0 = zeros(size(b));
maxint = 100;
err = 10^-5;

[x,nit] = noName2Jacobi(A, b, x0, maxint, err);

[x,nit] = noName2Gauss(A, b, x0, maxint, err);

#Exercise 2

#a

A = [10, 7, 8, 7; 7,5,6,5;8,6,10,9;7,5,9,10];
b = [32;23;33;31];

x = inv(A)*b

#b
btilda = [32.1;22.9;33.1;30.9];

xtilda = inv(A) * btilda

norm(b - btilda) / norm(b)

#c

Atilda = [10,7,8.1,7.2;7.8,5.04,6,5;8,5.98,9.89,9;6.99,4.99, 9, 9.98];

xtildaA = inv(Atilda) * b

normA = norm(x - xtildaA) / norm(x)


#d

conditioningNumber = norm(A) * norm(inv(A))

