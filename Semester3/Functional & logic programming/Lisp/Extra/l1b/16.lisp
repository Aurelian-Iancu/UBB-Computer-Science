; 16. 
; Determine  if  a  tree  of  type  (2)  is ballanced  (the  differencebetween  the  depth  of  two  subtrees  is equal to 1).
; absoluteDiff(a, b) = 
; = a - b, if a > b
; = b - a, otherwise
(defun absoluteDiff(a b)
    (cond   
        ((> a b) (- a b))
        (t (- b a))
    )
)

; myMax(a, b) =
; a, a > b
; b otherwise
(defun myMax (a b)
    (cond  
        ((> a b) a)
        (t b)
    )
)

;getDepth(l1l2l3) = 
; 0, if l1l2l3 is null
; = 1 + myMax(getDepth(l2), getDepth(l3)), otherwise

(defun getDepth(l)
    (cond  
        ((null l) 0)
        (t (+ 1 (myMax (getDepth (cadr l)) (getDepth (caddr l)))))
    )
)

(defun balanced(l)
    (> 2 (absoluteDiff(getDepth (cadr l)) (getDepth (caddr l))))
)