;8.
;a)Write a function to return the difference of two sets.

;exists(l1l2...ln, elem)
; = nil, n = 0
; true, l1 = elem
; exists(l2....ln), otherwise

(defun exists (l elem)
    (cond  
        ((null l) nil)
        ((equal (car l) elem) t)
        (t (exists (cdr l) elem))
    )
)

; differenceSets(l1l2...ln, p1p2...pm) = 
; = nil, n = 0
; diffrenceSets(l2...ln, p1p2...pm), if exists(p1p2...pm, l1)
; {l1} U differenceSets(l2...ln, p1p2...pm), otherwise

(defun differenceSets (l p)
    (cond  
        ((null l) nil)
        ((exists p (car l)) (differenceSets (cdr l) p))
        (t (cons (car l) (differenceSets (cdr l) p)))
    )
)

;b)Write a function to reverse a list with its all sublists, on all levels.
; myAppend(l1l2...ln, p1p2...pm) =
; p, if n = 0
; {l1} U myAppend(l2...ln, p1p2...pm)

(defun myAppend (l p)
  (cond
    ((null l) p)
    (t (cons (car l) (myAppend (cdr l) p)))
  )
)


; myReverse(l1l2...ln) = 
; nil, n = 0
; myAppend(myReverse(l2...ln), myReverse(l1)), if l1 is a list
; myAppend(myReverse(l2...ln), list(l1)), otherwise

(defun myReverse (l)
    (cond 
        ((null l) nil)
        ((listp (car l)) (myAppend (myReverse (cdr l)) (list (myReverse (car l)))))
        (t (myAppend (myReverse (cdr l)) (list (car l))))
    )
)

;c)Write a function to return the list of the first elements of all list elements of a given list with an odd number of elements at superficial level. 
;Example:(1 2 (3 (4 5) (6 7)) 8 (9 10 11)) => (1 3 9).

; lengthList(l1l2...ln) =
; 0, n = 0
; 1 + lengthList(l2...ln), otherwise

(defun lengthList(l)
    (cond  
        ((null l) 0)
        (t(+ 1 (lengthList (cdr l))))
    )
)


; length % 2 = 1
(defun checkOddLength (l)
    (= 1 (mod (lengthList l) 2))
)

; firstOdd(l1l2...ln, f) =
; nil, n = 0
; myAppend(firstOdd (l1, 0), firstOdd(l2...ln, f)), if l1 is a list
; l1 U firstOdd(l2...ln, 1), if checkOddLength = true and f = 0
; firstOdd(l2...ln, 1), otherwise

(defun firstOdd(l f)
    (cond  
        ((null l) nil)
        ((listp (car l)) (myAppend (firstOdd (car l) 0) (firstOdd (cdr l) f)))
        ((and (checkoddlength l) (= f 0)) (cons (car l) (firstOdd (cdr l) 1)))
        (t(firstOdd (cdr l) 1))

    )
)

(defun mainFirstOdd (l)
    (firstOdd l 0)
)

;d)Write a function to return the sum of all numerical atoms in a list at superficial level.
; sumSuperficial(l1l2..ln) = 
; 0, n = 0
; l1 + sumSperficial(l2...ln), if l1 is numerical
; sumSuperficial(l2....ln), otherwise

(defun sumSuperficial (l)
    (cond  
        ((null l) 0)
        ((numberp (car l)) (+ (car l) (sumSuperficial (cdr l))))
        (t (sumSuperficial (cdr l)))
    )
)