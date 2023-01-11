; 10.
; Return the level of a node X in a tree of type (2). The level of the root element is 0.

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

; nodeLevel(l1l2l3, x) = 
; 0, l1 = x
; 1 + nodeLevel(l2), if exists(l2, elem)
; 1 + nodeLevel(l3), if exists(l3, elem)
; nil, otherwise

(defun nodeLevel(l x)
    (cond  
        ((equal x (car l)) 0)
        ((exists(cadr l) x) (+ 1 (nodeLevel (cadr l) x)))
        ((exists(caddr l) x) (+ 1 (nodeLevel (caddr l) x)))
        (t nil)
    )
)