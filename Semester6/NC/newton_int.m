function f=newton_int(xi, d, x)
    for k=1:length(x)
        v = x(k) - xi;
        c = [1,cumprod(v(1:end-1))];
        f(k) = d(1,:) * c';
    end
endfunction


