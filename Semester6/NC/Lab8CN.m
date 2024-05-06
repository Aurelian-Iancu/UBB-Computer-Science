#Exercise 1
xi=[0,1,2];
fi = 1./(1+xi);
d = divided_diff(xi,fi);
xx = linspace(0,2,100);
plot(xx,newton_int(xi,d,xx))

dfi = -1./(1+xi).^2;
[zi,d2] = divided_diff2(xi,fi,dfi);

hold on
plot(xx,newton_int(zi,d2, xx))

#Exercise 2

xi = [0,3,5,8,13];
fi = [0,225,383,623,993];
dfi = [0,77,80,74,72];

t = 10;

[zi,d2] = divided_diff2(xi,fi,dfi);

newton_int(zi,d2, t)

d = divided_diff(xi,dfi);
newton_int(xi, d, t)

d = divided_diff(fi, dfi);
newton_int(fi,d,728.911)
