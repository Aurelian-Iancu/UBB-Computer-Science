;8. Return the list of nodes of a tree of type (2) accessed inorder.
; nil, n = 0
; inorder (l2) U {l1} U inorder (l3)
(defun inorder(l)
    (cond  
        ((null l) nil)
        (t (append (inorder (cadr l)) (list (car l)) (inorder (caddr l))))
    )
)