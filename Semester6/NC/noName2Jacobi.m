function [x,nit]=noName2Jacobi(A,b,x0,maxit,err)
  M=diag(diag(A));
  N=M-A;
  T=inv(M)*N;
  c=inv(M)*b;
  alpha=norm(T,inf);

  for k=1:maxit
    x=T*x0+c;
    if norm(x-x0,inf) < err * (1-alpha)/alpha
      nit = k;
      return;
    endif
    x0 = x;
  endfor
  nit = k;
endfunction
