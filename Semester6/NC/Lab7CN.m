#Exercise 1
xi = [0,1/3,1/2,1];
fi = cos(pi*xi);

d = divided_diff(xi, fi);

xx = linspace(0,1,100);

plot(xx, cos(pi*xx), xx, newton_int(xi, d, xx));

newton_int(xi, d, 1/5);


#Exercise 3

xi = [1000,1010,1020,1030,1040,1050];
fi = [3.0000000, 3.0043214, 3.0086002, 3.0128372, 3.0170333, 3.0211893];
dd = divided_diff(xi,fi);
newton_int(xi, dd, 1001:1009);
log10(1001:1009);

#Exercise 2
xi = [-4:4];
fi = 2.^xi;
aitken_int(xi,fi,1/2)
sqrt(2)



