function x = gauss_pivot(A, b)
  [r,n]=size(A);
  x=zeros(size(b));

  A=[A,b];
  for j=1:n-1
    [v,p]=max(abs(A(j:r,j)));
    p = p + j - 1;
    if (j != p)
      A([j,p],:) = A([p,j],:);
    endif

    for i=j+1:r
      m=A(i,j)/A(j,j);
      A(i,:)=A(i,:) - m*A(j,:);
    endfor
  endfor
  x = backward_subs(A(:,1:n), A(:,n+1));
endfunction
