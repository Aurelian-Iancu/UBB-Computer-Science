;13. 
;For a given tree of type (2) return the path from the root node to a certain given node X.
; exists(l1l2...ln, elem)
; false, n = 0 
; true, l1 = elem
; exists(l1, elem) or exists(l2...ln, elem), if l1 is a list
; exists(l2...ln, elem) otherwise

(defun exists(l elem)
    (cond  
        ((null l) nil)
        ((equal (car l) elem) t)
        ((listp (car l)) (or (exists (car l) elem) (exists (cdr l) elem)))
        (t (exists(cdr l) elem))
    ) 
)

; path(l1l2l3, x) =
; l1, if l1 = x
; l1 U path(l2,x), if exists (l2, elem)
; l1 U path(l3,x), if exists (l3, elem)
; nil, otherwise
(defun path(l x)
    (cond  
        ((equal (car l) x) (car l))
        ((exists (cadr l) x) (cons (car l) (path (cadr l) x)))
        ((exists (caddr l) x) (cons (car l) (path (caddr l) x)))
        (t nil)
    )
)