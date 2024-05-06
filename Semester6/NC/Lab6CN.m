lagrange_int([1,2,3], [1,4,9], [5,4])

#Exercise 1



xi = linspace(-2,4,10);
fi = (xi + 1) ./ (3*xi.^2 + 2*xi + 1);

x = linspace(-2,4, 500);
f = (x + 1) ./ (3*x.^2 + 2*x + 1);

L9f = lagrange_int(xi, fi, x);

#plot(x, f, x, L9f, '-p');

plot(x, f, x, abs(f - L9f), '-r');

max(abs(f-L9f));

#d

abs( (1/2 + 1) ./ (3*1/2.^2 + 2*1/2 + 1) - lagrange_int(xi, fi, 1/2));

# Exercise 2

lagrange_barycentric([1,2,3], [1,4,9], [2,3]);

xi = [1980:10:2020];
fi = [4451, 5287, 6090, 6970, 7821];
x = [2005,2015];

lagrange_barycentric(xi,fi,x)

error = abs([6474,7405] - lagrange_barycentric(xi,fi,x))

#Exercise 3

sqrt(118)

xi = [100,121, 144];
fi = [10,11, 12];
lagrange_barycentric(xi,fi, 118)
