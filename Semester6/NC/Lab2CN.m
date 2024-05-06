#1 a)
pkg load symbolic
syms x;
f = exp(x);
f1 = taylor(f, x, 0, 'Order', 2)
f2 = taylor(f, x, 0, 'Order', 3)
f3 = taylor(f, x, 0, 'Order', 4)
f4 = taylor(f, x, 0, 'Order', 5)

ezplot(f, [-3,3]);
hold on
ezplot(f1, [-3,3]);
ezplot(f2, [-3,3]);
ezplot(f3, [-3,3]);

#1 b)
warning("off")
vpa(exp(1), 7)
subs(f1, x,1)
vpa(subs(f4,x,1), 7)

for k = 6:20
  T = taylor(f, x, 0, 'Order', k);
  vpa(subs(T,x,pi/5),7)
 end;

 # 2 a)
 f = sin(x)
 f1 = taylor(f, x, 0, 'Order',4);
 f2 = taylor(f, x, 0, 'Order', 6);

 clf

 ezplot(f1, [-pi, pi]);
 hold on
 ezplot(f2, [-pi, pi]);

 # 2 b)
 warning("off")
 for k = 6:20
  T = taylor(f, x, 0, 'Order', k);
  vpa(subs(T,x,pi/5),6)
 end;

 #2 c)
 warning("off")
 for k = 6:20
  T = taylor(f, x, 0, 'Order', k);
  vpa(subs(T,x,-pi/3),6)
 end;

 #3 a)

 f = log(1 + x)
 f1 = taylor(f, x, 0, 'Order',2);
 f2 = taylor(f, x, 0, 'Order', 5);

 clf

 ezplot(f1, [-0.9, 1]);
 hold on
 ezplot(f2, [-0.9, 1]);

 #3 b)
 warning("off")
 for k = 6:20
  T = taylor(f, x, 0, 'Order', k);
  vpa(subs(T,x,2),6)
 end;
 #tricky question

 #3 c)
 taylor(log(1-x),x, 0, 'Order',8)

 #3 d)
 f = taylor(log(1+x),x, 0, 'Order',8) - taylor(log(1-x), x, 0, 'Order', 8)

 #3 e)
 warning("off")
 for k = 6:20
  T = taylor(f, x, 0, 'Order', k);
  vpa(subs(T,x,1/3),6)
 end;







