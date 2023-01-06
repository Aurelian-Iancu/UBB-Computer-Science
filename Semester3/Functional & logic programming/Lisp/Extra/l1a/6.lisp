;6.
;a)Write a function to test whether a list is linear.
; linear(l1l2...ln)
; true, n = 0
; false, if l1 is a list
; linear(l2...ln), otherwise

(defun linear (l)
    (cond  
        ((null l) t)
        ((listp (car l)) nil)
        (t (linear (cdr l)))
    )
)

;b)Write a function to replace the first occurence of an element E in a given listwith an other element O.

; myReplace(l1l2...ln, elem1, elem2, c)
; nil, n = 0
; {elem2} U replace (l2...ln, elem1, elem2, c - 1), if l1 = elem1 and c = 1
; {l1} U replace (l2...ln, elem1, elem2, c), otherwise

(defun myReplace (l elem1 elem2 c)
    (cond  
        ((null l) nil)
        ((and (equal elem1 (car l)) (= c 1)) (cons elem2 (myReplace (cdr l) elem1 elem2 (- c 1))))
        (t (cons (car l) (myReplace (cdr l) elem1 elem2 c)))
    )
)

(defun mainReplace (l elem1 elem2)
    (myReplace l elem1 elem2 1)
)

;c)Write a function to replace each sublist of a list with its last element.A sublist is an element from the first level, which is a list.
;Example: (a (b c) (d (e (f)))) ==> (a c (e (f))) ==> (a c (f)) ==> (a c f)
;(a (b c) (d ((e) f))) ==> (a c ((e) f)) ==> (a c f)

(defun my_append (l k)
    (if (null l) 
        k
        (cons (car l) (my_append (cdr l) k))
    )
)

(defun my_reverse (l)
    (if (null l)
        nil
        (my_append (my_reverse (cdr l)) (list (car l)))
    )        
)

(defun last_element (l)
	(if (listp l) 
        (last_element (car (my_reverse l)))
        l
    )
)

; last(l1l2...ln) = 
; nil, n = 0
; lastElement(l1) U lastElement(l2...ln), l1 is a list
; l1 U lastElement(l2...ln), otherwise

(defun myLast(l)
    (cond  
        ((null l) nil)
        ((listp (car l)) (cons (last_element (car l)) (myLast (cdr l))))
        (t (cons (car l) (myLast (cdr l))))
    )
)

; d)Write a function to merge two sorted lists without keeping double values.
; mergeLists(l1l2...ln, p1p2...pm)
; p1p2...pm, if n = 0
; l1l2...ln, if m = 0
; {l1} U mergeLists(l2...ln, p1p2...pm), if l1 < p1 
; {p1} U mergeLists(l1l2...ln, p2...pm), if l1 > p1
; {l1} U mergeLists(l2...ln, p2...pm), if l1 = p1

(defun mergeLists(l p)
    (cond  
        ((null l) p)
        ((null p) l)    
        ((< (car l) (car p)) (cons (car l) (mergeLists (cdr l) p)))
        ((> (car l) (car p)) (cons (car p) (mergeLists l (cdr p))))
        (t (= (car l) (car p)) (cons (car l) (mergeLists (cdr l) (cdr p))))
    )
)
