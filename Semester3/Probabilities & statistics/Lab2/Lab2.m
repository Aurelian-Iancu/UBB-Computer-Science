%Only exercise 2 is solved

pkg load statistics

clf; hold on; %to plot on the same graph. hold on opens a graph.
n = input('Nr of trials=');
p = input('Prob of succes=');
%pdf = probability distribution function
x = 0:n;
px = binopdf(x,n,p);
plot(x,px,'+');
%cdf = cumulative distribution function
%cdf is continuous and pdf not.
xx = 0:0.1:n;
cx = binocdf(xx,n,p);
plot(xx,cx,'-') % with or wihtout - will connect them. By default it's -

%Application a).
%X(0     1    2     3)
%  1/8 3/8   3/8   1/8
x1 = 0:0.1:3;
p1 = binocdf(x1,n,p);
plot(x1, p1);

y = binopdf(0,3,0.5);
fprintf('P(X=0) = %1.4f\n', y);

not1 = 1 - binopdf(1,3,0.5);
fprintf('P(X=0) = %1.4f\n', not1);

notSmallerEqualThan2 = binocdf(2, 3,0.5);
fprintf('P(X=0) = %1.4f\n', notSmallerEqualThan2);

notSmallerThan2 = binocdf(1,3,0.5);
fprintf('P(X=0) = %1.4f\n', notSmallerThan2);

higherEqualThan1 = 1 - binopdf(0,3,0.5);
higherThan1 = 1 - binocdf(1,3,0.5);

N = 1000;
rand() < 0.5;
C = rand(3,N);
D = C < 0.5;
E = sum(D);
hist(E); % histograme





