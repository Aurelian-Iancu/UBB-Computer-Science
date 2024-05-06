#A = [1,2;3,4]

#ans = A^2#(carot)
#A.^2

#[1, 2,3, ... 100]
#1 : 100
#B = 1:0.1:100
#B.^2
#diag([1,2,3]) #=> [1,0,0,0,2,0,0,0,3]

## end of introduction

#1) p(x) = x^5-5*x^4-16*x^3+16*x^2-17*x+21

#help polyval

p = [1, -5, -16, 16, -17, 21]
#compute p(-2.5)
polyval(p, -2.5)
#plot the graph of p on the interval [-4, 7.2]
#x=-4:0.1:7.2

#px= polyval(p, x)

#plot(x, px)

#c) roots of p
roots(p)


#Ex 2

x = linspace(0, 2*pi, 150) #default 100 for the last one(in how many pieces the interval should be plit)

#first mode to plot multiple graphs on the same image
plot(x, sin(x),x, sin(2*x), x, sin(3*x))
clf
#second mode
plot(x, sin(x))
hold on
plot(x, sin(2*x))
plot(x, sin(3*x))
hold off
clf
#third mode
f = @(x) sin(x)
f([1,2])

#fplot(f, [0, 2*pi])
#hold on

#subplot(3,1,1)
#fplot(f, [0,2*pi])
#subplot(3,1,2)
#fplot(@x sin(2*x), [0,2*pi])
#subplot(3,1,3)
#fplot(@x sin(3*x), [0,2*pi])
#hold off
#Ex3



t = linspace(0, 10*pi, 1000);
R = 3.8;
r = 1;
x = (R+r)*cos(t) - r* cos((R/r + 1) * t)
y = (R+r)*sin(t) - r* sin((R/r + 1) * t)

plot(x,y)

#Ex4
clf
#f(x,y) = sin(e^x) * cos(ln y)
[x,y] = meshgrid(linspace(-2,2), linspace(0.5,4.5));
f = sin(exp(x)) .* cos(log(y))

mesh(x, y, f)
plot3(x, y, f)

#Ex5

n = 2024
f = 2;
for i = 1: n
  f = 1 + 1/f;
end;

f #1.6180 = (1+sqrt(5)) /2
