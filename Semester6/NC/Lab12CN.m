f = @(x) x - exp(-x)
fplot(f, [-1,2])
grid on
[z, ni] = bisect(f, 0, 1, 10^(-5), 50)
[z, ni] = secant(f, 0, 1, 10^(-5), 50)

fd = @(x) 1 + exp(-x)
x0 = 0
[z,ni] = newton(f,fd,0, 10^(-5), 50)
