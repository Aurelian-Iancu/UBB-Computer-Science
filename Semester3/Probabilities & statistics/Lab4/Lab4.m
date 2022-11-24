pkg load statistics

%1)
rand
%2 a)
% Bernoulli distribution p(0,1)
% X( 0 1)
%  (1-p p)

% r random number < p => succes
clear;

p = input("probability = ");
x = 0;
n = input("number of trials = ");
for i=1:n
  r = rand;
  x(i) = r < p;
end

v_x = unique(x);
n_x = hist(x, length(v_x))
result = n_x/n


%Binomial distribution
% p = probability of success
% n = nr of trials
% k = nr of successes

clear;

p = input("probability = ");
n = input("number of trials = ");
N = input("number of simulations = ");
r = rand(n,N);

x = sum(r < p);
v_x = unique(x);
n_x = hist(x, length(v_x))

k = 0:n;
pk = binopdf(k,n,p);
plot(k,pk,'o', v_x, n_x/N, '*');

%Geometric distribution
% 000001 5
% 001 3
%clear;

p = input("probability = ");
N = input("number of simulations = ");

for i = 1:N
  x(i) = 0;
  while rand >= p
    x(i) = x(i) + 1;
  endwhile
end

v_x = unique(x);
n_x = hist(x, length(v_x))

k = 0:10;
pk = geopdf(k,p);
plot(k,pk,'o',v_x,n_x/N,'*');

%2 d)
% Pascal distribution
% negative binomial
% nbinpdf
clear;
x = 0;
y = 0;
p = input("probability = ");
N = input("number of simulations = ");
n = input("number of successes = ");

for i = 1:N
  for j = 1:n
    x(j) = 0;
    while rand >= p
      x(j) = x(j) + 1;
    endwhile
  endfor
  y(i) = sum(x);
 end

v_y = unique(y);
n_y = hist(y, length(v_y));

k = 0:50;
pk = nbinpdf(k,n,p);
plot(k,pk,'o',v_y, n_y/N,'*');

