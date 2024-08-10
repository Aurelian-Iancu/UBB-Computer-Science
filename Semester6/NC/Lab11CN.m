#Exercise 1

pi * sqrt(3) / 9;
[I,nf] = romberg(@(x) 1./(2+sin(x)), 0, pi/2, 10^(-6), 50);

#Exercise 2
#pi/2 = integral from -1 to 1 from sqrt(1-x^2) dx
[I,n,c] = gauss_quad(@(x)(x.^2+1)/(x.^2+1),2,2)
Result = 2 * I

[I,n,v]=gauss_quad(@(x) (sin(x.^2)),4,2)

I
#[I,n,c] = gauss_quad(@(x)(
#Exercise 4

