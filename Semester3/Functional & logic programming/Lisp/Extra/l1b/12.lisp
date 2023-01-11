; 12.
; Return the list of a tree of type (2) accessed preorder.
; preorder(l1l2l3)
; nil , n = 0
; l1 U postorder(l2) U postorder(l3) 
(defun preorder (l)
    (cond  
        ((null l) nil)
        (t (append (list(car l)) (preorder (cadr l)) (preorder (caddr l))))
    )
)