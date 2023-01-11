; 15.
; Return the list of a tree of type (2) accessed postorder.
; postorder(l1l2l3)
; nil , n = 0
; postorder(l2) U postorder(l3) U l1

(defun postorder (l)
    (cond  
        ((null l) nil)
        (t (append (postorder (cadr l)) (postorder (caddr l)) (list (car l))))
    )
)