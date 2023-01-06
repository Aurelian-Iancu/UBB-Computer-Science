;2.
;a) Write a function to return the product of two vectors.
; dotProduct(l1l2...ln, p1p2...pm)
; 0, if n = 0 or m = 0
; l1*p1 + dotProduct(l2...ln, p2...pm)

(defun dotProduct (l p)
    (cond
        ((or (null l) (null p)) 0)
        (t (+ (* (car l) (car p)) (dotProduct (cdr l) (cdr p))))
    )
)

;b)Write a function to return the depth of a list. Example: the depth of a linear list is 1.
;myMax(a, b) = 
; a, if a > b
; b otherwise
(defun myMax (a b)
    (cond 
        ((> a b) a)
        (t b)
    )

)

; depth(l1l2...ln, max)
; = max, n = 0
; = myMax(depth(l1, max + 1), depth(l2...ln, max + 1)), if l1 is a list
; = depth(l2...ln, otherwise)

(defun depth(l max)
    (cond 
        ((null l) max)
        ((listp (car l)) (myMax (depth (car l) (+ max 1)) (depth (cdr l) max)))
        (t (depth (cdr l) max))
    )

)

(defun mainDepth (l)
    (depth l 1)
)

;c)Write a function to sort a linear list without keeping the double values.
; isSorted(l1l2...ln) = 
; true, n = 0
; false, l2 > l1
; isSorted(l2...ln), otherwise

(defun isSorted (l)
    (cond 
    ((or (null l) (null (cdr l))) t)
    ((< (cadr l) (car l)) nil)
    (t (isSorted (cdr l)))
    )
)

;insert (l1l2...ln, elem) = 
; = list(elem), n = 0
; = l1l2...ln, l1 = elem
; = {elem} U l1l2...ln, l1 > elem
; = {l1} U insert(l2...ln, elem), otherwise

(defun insert (l elem)
    (cond
        ((null l) (list elem))
        ((= (car l) elem) l)
        ((> (car l) elem) (cons elem l))
        (t (cons (car l) (insert (cdr l) elem)))
    )

)

; sortare(l1l2...ln)
; nil, n = 0
; insert(sortare(l2....ln), l1), otherwise

(defun sortare (l)
  (cond
    ((null l) nil)
    (t (insert (sortare (cdr l)) (car l)))
  )
)

;d)Write a function to return the intersection of two sets.
; exists(l1l2...ln, elem)
; nil, n = 0;
; true, l1 = elem;
; exists(l2...ln, elem), otherwise

(defun exists(l elem)
    (cond 
        ((null l) nil)
        ((= elem (car l)) t)
        (t (exists (cdr l) elem))
    )
)

; removeElem(l1l2...ln, elem, c)
; nil, n = 0
; {l1} U removeElem(l2...ln, elem), if l1 != elem or c = 0
; removeElem(l2...ln, elem), if l1 = elem
(defun removeElem(l elem c)
    (cond
        ((null l) nil)
        ((or (= c 0) (not (= elem (car l))))(cons (car l) (removeElem (cdr l) elem c)))
        (t (removeElem(cdr l) elem (- c 1)))
    )
)

(defun mainRemove(l elem)
    (removeElem l elem 1)
)

; intersection(l1l2...ln, p1p2...pm)
; nil, n = 0 or m = 0
; {l1} U intersection(l2...ln, (mainRemove(p1p2...pm, l1))), if exists(p1p2...pm, l1)
; intersection(l2...ln, p1p2...pm), otherwise

(defun myIntersection(l p)
    (cond
        ((or (null l) (null p)) nil)
        ((exists p (car l)) (cons (car l) (myIntersection (cdr l) (mainRemove p (car l)))))
        (t (myIntersection (cdr l) p))
    )
)