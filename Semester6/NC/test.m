pkg load statistics

x1 = [21.8, 22.6, 21.0, 19.7, 21.9, 21.6, 22.5, 23.1, 22.2, 20.1, 21.4, 20.5]
x2 = [36.5, 35.2, 36.2, 34.0, 36.4, 36.1, 37.5, 38.0, 36.3, 35.9, 35.7, 34.9]

% significance level
alpha = 0.05;

% the lengths
n1 = length(x1);
n2 = length(x2);

% the variances
v1 = var(x1);
v2 = var(x2);

% the averages
m1 = mean(x1);
m2 = mean(x2);
m = m1 - m2;

fprintf('alpha = 0.05 - significance level (prob. of rejecting a true hypothesis)\n');
fprintf('1 - alpha = 0.95 - confidence level (prob. that the conf. interval will contain the parameter)\n');
fprintf('we use a two tailed test\n');
fprintf('the null hypotheses is: v1 = v2\n');
fprintf('the alternative hypothesis is: v1 != v2\n');

fprintf('\n\n\n');


f1 = finv(alpha / 2, n1 - 1, n2 - 1);
f2 = finv(1 - alpha / 2, n1 - 1, n2 - 1);

[H, P, CI, ZVAL] = vartest2(x1, x2, "alpha", alpha, "tail", "both");


fprintf('The rejection region is (%6.4f, %6.4f) U (%6.4f, %6.4f)\n', -inf, f1, f2, inf);
fprintf('The value of the test statistic is %6.4f\n', ZVAL.fstat);
fprintf('The P-value for the variances test is %6.4f\n', P);

if H == 0
    fprintf('The null hypothesis is not rejected.\n');
    fprintf('The variances seem to be equal.\n');
    % sigma1 = sigma2 because the variances are equal
    sp = sqrt(((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2));
    t1 = tinv(1 - alpha / 2, n1 + n2 - 2);
    t2 = tinv(alpha / 2, n1 + n2 - 2);
    % get the confidence interval limits
    ci1 = m - t1 * sp * sqrt(1 / n1 + 1 / n2);
    ci2 = m - t2 * sp * sqrt(1 / n1 + 1 / n2);
    fprintf('C.I. for the difference of means = %3.4f (sigma1 == sigma2): (%3.4f, %3.4f)\n', m, ci1, ci2);
else
    fprintf('The null hypothesis is rejected.\n');
    fprintf('The variances seem to be different.\n');
    % sigma1 != sigma2 because the variances differ
    c = (v1 / n1) / (v1 / n1 + v2 / n2);
    n = 1 / (c ^ 2 / (n1 - 1) + (1 - c) ^ 2 / (n2 - 1));
    t1 = tinv(1 - alpha / 2, n);
    t2 = tinv(alpha / 2, n);
    ci1 = m - t1 * sqrt(v1 / n1 + v2 / n2);
    ci2 = m - t2 * sqrt(v1 / n1 + v2 / n2);
    fprintf('C.I. for the difference of means = %3.4f (sigma1 != sigma2): (%3.4f, %3.4f)\n', m, ci1, ci2);
end


