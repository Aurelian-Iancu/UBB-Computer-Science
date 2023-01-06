;1
;a) Write a function to return the n-th element of a list, or NIL if such an element does not exist;
;nthElement(l1l2...lm, n, pos) =
; = nil, m = 0
; = l1, if n = pos
; = nthElement(l2...lm, n, pos + 1), otherwise

(defun nthElement (l n pos)
    (cond
    ((null l) nil)
    ((= n pos) (car l))
    (t (nthElement (cdr l) n (+ pos 1)))
    )
)

(defun main (l n)
    (nthElement l n 0)
)

; b) Write a function to check whether an atom E is a member of a list which is not necessarily linear.
; checkAtom(l1l2...ln, elem) =
; = nil, if n = 0
; = true, if l1 = elem and l1 is atom
; = checkAtom(l1, elem) U checkAtom(l2...ln, elem), if l1 is a list;
; = checkAtom(l2...ln, elem), otherwise

(defun checkAtom (l elem)
    (cond
    ((null l) nil)
    ((and (atom (car l)) (= (car l) elem)) t)
    ((listp (car l)) (or (checkAtom (car l) elem) (checkAtom (cdr l) elem)))
    (T (checkAtom (cdr l) elem))
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

; d) Write a function to transform a linear list into a set.
; exist(l1l2...ln, elem) = 
; = nil, if n = 0
; = true, if l1 = elem
; exists(l2...ln, elem), otherwise
;

(defun exists (l elem)
    (cond
        ((null l) nil)
        ((= (car l) elem) t)
        (t (exists (cdr l) elem))
    )

)

; toSet(l1l2...ln) = 
; = nil, if n = 0
; l1 U toSet(l2...ln), if not exists(l2...ln, l1)
; toSet(l2...ln), otherwise

(defun toSet (l)
    (cond
        ((null l) nil)
        ((not (exists (cdr l) (car l))) (cons (car l) (toSet (cdr l))))
        (t (toSet (cdr l)))
    )

)



