% B 1.

alfa = 0.05 % 100(1-alfa)% confidence interval

% a)

% Confidence intervals 1. first formula

% x barat = mean(x)
% n = length(x)
% z 1-alfa/2 = norminv(1 - alfa/2)

x = [7,7,4,5,9,9,4,12,8,1,8,7,3,13,2,1,17,7,12,5,6,2,1,13,14,10,2,4,9,11,3,5,12,6,10,7];
sigma = 5;
xmean = mean(x);
n = length(x);

zalfa = norminv(alfa/2);
zalfac = norminv(1 - alfa/2);

a1 = xmean - sigma/sqrt(n) * zalfac
a2 = xmean - sigma/sqrt(n) * zalfa

% miu is in the interval (a1, a2) which should be (5.4778, 8.7444)

% b) sigma unknown
% Confidence intervals 1. second formula

s = std(x);
talfa = tinv(alfa/2, n-1);
talfac = tinv(1-alfa/2, n-1);

b1 = xmean - s/sqrt(n) * talfac
b2 = xmean - s/sqrt(n) * talfa

% miu is in the interval (b1, b2) which should be (5.7107, 8.5115)

% c) sigma squared
% % Confidence intervals 2. formula

ssquared = var(x); % variance
xsquaredalfa = chi2inv(alfa/2, n-1);
xsquaredalfac = chi2inv(1-alfa/2, n-1);

% this is for the variance
c1 =  (n-1)* ssquared / xsquaredalfac
c2 = (n-1)* ssquared /xsquaredalfa

% this is for standard deviation
d1 = sqrt(c1)
d2 = sqrt(c2)

% B. 2.

premium = [22.4, 21.7, 24.5, 23.4, 21.6, 23.3, 22.4, 21.6, 24.8, 20.0];
regular = [17.7, 14.8, 19.6, 19.6, 12.1, 14.8, 15.4, 12.6, 14.0, 12.2];

% a) sigma1 = sigma2 known
% Confidence intervals 3. first formula

meanpremium = mean(premium);
meanregular = mean(regular);
lengthpremium = length(premium);
lengthregular = length(regular);
s1squared = var(premium);
s2squared = var(regular);
talfac = tinv(1-alfa/2, lengthpremium + lengthregular -2);

spsquared = ((lengthpremium-1)*s1squared + (lengthregular-1) * s2squared)/(lengthpremium + lengthregular - 2)

e1 = meanpremium - meanregular - talfac * sqrt(spsquared) * sqrt( 1/lengthpremium + 1/lengthregular)
e2 = meanpremium - meanregular + talfac * sqrt(spsquared) * sqrt( 1/lengthpremium + 1/lengthregular)
%e1 = 2.52
%e2 = 12.05

% b) sigma1 != sigma2

% COnfidence intervals 3. second formula

c = s1squared/lengthpremium / (s1squared/lengthpremium + s2squared/lengthregular);
invn = c * c / (lengthpremium - 1) + (1 - c) * (1 - c) / (lengthregular - 1);

n = 1 / invn;
talfac = tinv(1 - alfa/2, n);

f1 = meanpremium - meanregular - talfac * sqrt( s1squared/ lengthpremium + s2squared / lengthregular)
f2 = meanpremium - meanregular + talfac * sqrt( s1squared/ lengthpremium + s2squared / lengthregular)

% c) sigma1squared / sigma2squared

falfa = finv(alfa/2, lengthpremium - 1, lengthregular - 1);
falfac = finv( 1 - alfa/2, lengthpremium - 1, lengthregular - 1);

g1 = 1 / falfac * s1squared / s2squared
g2 = 1 / falfa * s1squared / s2squared


%A
% x = [20 * ones(1,2)
%ones(1,n) = [1 1 1 1 1 ... 1]

X = [20 * ones(1,2), 21 * ones(1, 1), 22* ones(1,3), 23 * ones(1,6), 24 * ones(1,5), 25* ones(1,9), 26 * ones(1, 2), 27 * ones(1, 2)];
Y = [75 * ones(1,3), 76 * ones(1, 2), 77 * ones(1,2), 78 * ones(1,5), 79 * ones(1,8), 80* ones(1,8), 81 * ones(1, 1), 82 * ones(1, 1)];


% a)

Xmean = mean(X)
Ymean = mean(Y)

% b)
  Xvar = var(X,1)
  Yvar = var(Y,1)

% c)
  cov = cov(X, Y, 1)

%d)
  corrcoef = corrcoef(X, Y)
  corrcoef(1,2)

