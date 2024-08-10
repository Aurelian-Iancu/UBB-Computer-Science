function [z, ni] = newton(f, fd, x0, err, maxN)
  for k=1:maxN
    x1 = x0 - f(x0)/fd(x0);
    if abs(x1 - x0) < err
      z = x1;ni = k; return;
    endif

    x0 = x1;
  endfor

  error('too difficult');
endfunction
