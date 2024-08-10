function [z,ni]=bisect(f,a,b,err,maxn)
    if sign(f(a))*sign(f(b))>0
        error('no solution');
    end
    fa=f(a);
    fb=f(b);
    c=(a+b)/2;
    for k=1:maxn
        fc=f(c);
        if sign(fc)*sign(fb)<=0
            a=c;
            fa=fc;
        else
            b=c;
            fb=fc;
        end
        if abs(b-a)<err
            z=c;
            ni=k;
            return
        end
        c=(a+b)/2
    end
    error('too many difficult');
end

