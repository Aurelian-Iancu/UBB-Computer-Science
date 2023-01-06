;4.
; a)Write a function to return the sum of two vectors.
; (1, 2, 3) (2, 3, 4) => (3, 5, 7)

; vectorSum(l1l2...ln, p1p2...pm) = 
; nil, if n = 0 
; {l1 + p1} U vectorSum(l2...ln, p2...pm)

(defun vectorSum(l p)
    (cond 
        ((null l) nil)
        (t (cons (+ (car l) (car p)) (vectorSum (cdr l) (cdr p))))
    )
)

;b)Write a function to get from a given list the list of all atoms, on any level, but on the same order. 
;Example:(((A c) b) (D E)) ==> (A c b D E)l

;myAppend(l1l2...ln, p1p2...pm)
; p1p2...pm, if n = 0
; {l1} U myAppend(l2...ln, p1p2...pm)
(defun myAppend(l p)
    (cond 
        ((null l) p)
        ((cons (car l) (myAppend (cdr l) p)))
    )
)

; getList(l1l2...ln) =
; = nil, n = 0;
; append(l1, getList(l2...ln)), if l1 is atom
; append(getList(l1), getList(l2...ln)), if l1 is a list

(defun getList(l)
    (cond 
        ((null l) nil)
        ((listp (car l)) (myAppend (getList (car l)) (getList (cdr l))))
        (t (myAppend (list (car l)) (getList (cdr l))))

    )
)

;c) Write a function that, with a list given as parameter, inverts only continuous
;   sequences of atoms. Example:
;   (a b c (d (e f) g h i)) ==> (c b a (d (f e) i h g)


; invertCont (l1l2...ln, aux) = 
; = aux , if n = 0
; = myAppend(aux, myAppend(list(invertCont(l1, NIL)), invertCont(l2...ln, NIL))) , if l1 is a list
; = invertCont(l2...ln, myAppend(list(l1), aux)) , otherwise


(defun invertCont (l aux)
  (cond
    ((null l) aux)
    ((listp (car l)) (myAppend aux (myAppend (list (invertCont (car l) nil)) (invertCont (cdr l) nil))))
    (t (invertCont (cdr l) (myAppend (list (car l)) aux)))
  )
)

;d)Write a list to return the maximum value of the numerical atoms from a list, at superficial level.

;myMax(a, b) =
; a, a > b
; b, otherwise

(defun myMax(a b)
    (cond 
        ((> a b) a)
        (t b)
    )
)

;listMax(l1l2...ln)
; 0, n = 0
; max(l1, listMax(l2...ln)), if l1 is number
; listMax(l2...ln), otherwise

(defun listMax(l)
    (cond 
        ((null l) 0)
        ((numberp (car l)) (max (car l) (listMax (cdr l))))
        (t (listMax (cdr l)))
    )
)



