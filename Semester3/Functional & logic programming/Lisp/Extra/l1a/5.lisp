;5.
;a)Write twice the n-th element of a linear list. 
;Example: for (10 20 30 40 50) and n=3 will produce (10 20 30 30 40 50).

; addNth(l1l2...ln, n, pos) = 
; nil, n = 0
; {l1} U {l1} U addNth(l2...ln, n, pos + 1), if n = pos
; {l1} U addNth(l2...ln, n, pos + 1), otherwise

(defun addNth(l n pos)
    (cond  
        ((null l) nil)
        ((= n pos) (cons (car l) (cons (car l) (addNth (cdr l) n (+ pos 1)))))
        (t (cons (car l) (addNth (cdr l) n (+ pos 1))))
    )
)

(defun mainAddNth(l n)
    (addNth l n 1)
)

;b)Write a function to return an association list with the two lists given as parameters. 
;Example: (A B C) (X Y Z) --> ((A.X) (B.Y) (C.Z)).

; associationList(l1l2...ln, p1p2...pm) = 
; nil, n = 0
; {cons(l1, l2)} U associationList(l2...ln, p2...pm)

(defun associationList(l p)
    (cond  
        ((null l) nil)
        (t (cons (cons (car l) (car p)) (associationList (cdr l) (cdr p))))
    )
)

; c) Write a function to determine the list of all sublists of a given list, on any level.
; A sublist is either the list itself, or any element that is a list, at any level. Example:
; (1 2 (3 (4 5) (6 7)) 8 (9 10)) => 5 sublists :
; ( (1 2 (3 (4 5) (6 7)) 8 (9 10)) (3 (4 5) (6 7)) (4 5) (6 7) (9 10) )
(defun all_sublists (l)
    (cond
        ((atom l) nil)
        (T (apply 'append (list l) (mapcar 'all_sublists l)))
    )
)

; d) Write a function to return the number of all numerical atoms in a list at superficial level.
; numberOfNumbers(l1l2...ln) = 
; 0, n = 0
; 1 + numberOfNumbers(l2...ln), if l1 is numerical atom
; numberOfNumbers(l2...ln), otherwise

(defun numberOfNumbers (l)
    (cond  
        ((null l) 0)
        ((numberp (car l)) (+ 1 (numberOfNumbers (cdr l))))
        (t (numberofnumbers(cdr l)))
    )
)

