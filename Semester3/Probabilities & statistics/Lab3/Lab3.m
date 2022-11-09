pkg load statistics

%Exercise 1
%a) miu, sigma = input
%P(X <=0)
 %p1 = normcdf(0, miu, sigma)
% P(X >=0)
 %p2  = 1 - p1
% P(x = 0) = 0 and this is why you can do 1 - p1 without excluding P(x = 0)
%b) miu = 1, sigma = 5
% P(-1<=X<=1)
 %p3  = normcdf(1, miu, sigma) - normcdf(-1, miu, sigma)
% p(X <= -1 or X >=1)
 %p4 = 1 - p3
%c)
%xalfa = ? P(x- xalfa) = alfa between(0,1) norminv(alfa, miu, sigma)
  %p5 = norminv(alfa, miu, sigma)
%d)xbeta norminv(1-beta, miu, sigma)
  %p6 = norminv(1-beta, miu,sigma)
option = input('opt=', 's');
alfa = input('Alfa=');
beta = input('Beta=');
switch option
  case 'normal'
    miu = input('Miu=');
    sigma = input('Sigma=');
    p1 = normcdf(0, miu, sigma)
    p2  = 1 - p1
    p3  = normcdf(1, miu, sigma) - normcdf(-1, miu, sigma)
    p4 = 1 - p3
    p5 = norminv(alfa, miu, sigma)
    p6 = norminv(1-beta, miu,sigma)

  case 'Student'
    n = input('n=')
    p1 = tcdf(0,n)
    p2 = 1 - tcdf(0,n)
   case 'Fisher'
    m = input('m=')
    n = input('n=')
    p1 = fcdf(0,m,n)
    p2 = 1- fcdf(0,m,n)
   otherwise
    fprintf('Error');
    end
%Exercise 2
%Normal form
plots a graph once at 0.2 seconds. X and Y is limited
p = input('p=');

for n = 1:3:100
  k = 0:n;
  binopdf(k,n,p);
  prob = binopdf(k,n,p)
  plot(k,prob)
  xlim([0,100])
  ylim([0,0.15])
  pause(0.2)
end

%Poisson form
n = input('n=');
p = input('p=');
lambda = n*p;
k = 0:n
p1 = poisspdf(k, lambda);
p2 = binopdf(k,n,p);
plot(k,p1,k,p2);













