;Problem 8
;a) Write a function to return the difference of two sets
; Mathematical models

; exists(l1l2...ln, elem) = 
; = false(nil), if n = 0
; = true, if l1 = elem
; exists(l2...ln), otherwise 

(defun exists (l elem)
    (cond
        ((null l) nil)
        ((= (car l) elem) t)
        (t (exists(cdr l) elem))
    )
)

; diffSet(l1l2...ln, p1p2...pm)
; nil, if n = 0
; l1 U diffSet(l2...ln, p1p2...pm), if(not(exists(p1p2...pm, l1)))
; diffSet(l2...ln, p1p2...pm), otherwise

(defun diffSet(l p)
    (cond
        ((null l) nil)
        ((not (exists p (car l))) (cons (car l) (diffSet (cdr l) p)))
        (T (diffSet (cdr l) p))
    )
)

;b)Write a function to reverse a list with its all sublists, on all levels.

; myAppend(l1l2...ln, elem)
; elem, n = 0
; l1 U myAppend(l2...ln, elem), otherwise

(defun myAppend(l elem)
    (cond
        ((null l) elem)
        (t (cons (car l) (myAppend (cdr l) elem)))
    )
)

;myReverse(l1l2...ln)
; = nil, if n = 0
; = myAppend(myReverse(l2...ln), list(myReverse(l1))), if l1 is a list
; = myAppend(myReverse(l2...ln), list(l1)), otherwise

(defun myReverse(l)
    (cond
        ((null l) nil)
        ((listp (car l)) (myAppend (myReverse (cdr l)) (list (myReverse (car l)))))
        (t (myAppend (myReverse (cdr l)) (list (car l))))
    )

)

;c)Write a function to return the list of the first elements of all list elements of a given list with an odd number of elements at superficial level.
; myLength(l1l2...ln)
; 0, n = 0
; 1 + myLength(l2...ln), otherwise

(defun myLength(l)
    (cond
        ((null l) 0)
        (t (+ 1 (myLength (cdr l))))
    )
)

; checkOddLength(l1l2...ln) =
; true, if n % 2 = 1
; false, if n % 2 = 0
(defun checkOddLength(l)
    (= (mod (myLength l) 2) 1)
)

; firstElem(l1l2...ln, f) =
; = nil, if n = 0



;d) Write a function to return the sum of all numerical atoms in a list at superficial level.
; mySum(l1l2...ln) =
; 0, if n = 0
; l1 + mySum(l2...ln), if l1 is a number
; mySum(l2...ln), otherwise

(defun mySum(l)
    (cond 
        ((null l) 0)
        ((numberp (car l)) (+ (car l) (mySum (cdr l))))
        (t (mySum (cdr l)))
    )
)