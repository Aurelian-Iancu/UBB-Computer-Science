;9.
;a) Write a function that merges two sorted linear lists and keeps double values

; mergeLists(l1l2...ln, p1p2...pm) = 
; l1l2...ln, if m = 0
; p1p2...pm, if n = 0
; l1 U mergeLists(l2...ln, p1p2...pm), if l1 < p1
; p1 U mergeLists(l1l2...ln, p2...pm), if l1 > p1
; l1 U mergeLists (l2...ln, p2...pm), if l1 = p1

(defun mergeLists (l p)
    (cond  
        ((null l) p)
        ((null p) l)
        ((< (car l) (car p)) (cons (car l) (mergeLists (cdr l) p)))
        ((> (car l) (car p)) (cons (car p) (mergeLists l (cdr p))))
        ((= (car l) (car p)) (cons (car l) (mergeLists (cdr l) (cdr p))))
    )

)

;b) Write a function to replace an element E by all elements of a list L1 at all levels of a given list L.
;insertList(l1l2...ln, p1p2...pm)
; 

; replace (l1l2...ln, e, list) = 
; nil, n = 0
; replace(l1, e, list) U replace(l2...ln, e, list), if l1 is a list
; list U replace(l2...ln, e, list), if l1 = e
; l1 U replace (l2...ln, e, list), otherwise

(defun myReplace (l e list)
    (cond  
        ((null l)nil)
        ((listp (car l)) (cons (myReplace (car l) e list) (myReplace (cdr l) e list)))
        ((= (car l) e) (append list (myReplace (cdr l) e list)))
        (t (cons (car l) (myReplace (cdr l) e list)))
    )  
)

; c) Write a function to determines the sum of two numbers in list representation, and returns the
; corresponding decimal number, without transforming the representation of the number from list to
; number.

(defun digit (l k c)
    (cond
        ((null l) (mod (+ k c) 10))
        ((null k) (mod (+ l c) 10))
        (T (mod (+ l k c) 10))
    )
)

(defun carry (l k c)
    (cond
        ((null l) (if (> (- (+ k c) (mod (+ k c) 10)) 9) 
                      (/ (- (+ k c) (mod (+ k c) 10)) 10) 
                      (mod (+ k c) 10)
                  )
        )
        ((null k) (if (> (- (+ l c) (mod (+ l c) 10)) 9)
                      (/ (- (+ l c) (mod (+ l c) 10)) 10) 
                      (mod (+ l c) 10)
                  )
        )
        (T (if (> (- (+ l k c) (mod (+ l k c) 10)) 9)
                      (/ (- (+ l k c) (mod (+ l k c) 10)) 10) 
                      (mod (+ l k c) 10)
                  )
        )
    )
)

(defun my_append (l k)
    (if (null l) 
        k
        (cons (car l) (my_append (cdr l) k))
    )
)

(defun my_reverse (l)
    (cond
        ((null l) nil)
        ((listp (car l)) (my_append (my_reverse (cdr l)) (list (my_reverse (car l)))))
        (T (my_append (my_reverse (cdr l)) (list (car l))))
    )
)

(defun sumList (l k c)
    (cond
        ((and (null l) (null k)) (if (= 1 c) (list 1) nil))
        (T (my_append (sumList (cdr l) (cdr k) (carry (car l) (car k) c)) (list (digit (car l) (car k) c))))        
    )
)

(defun solve (l k)
    (sumList (my_reverse l) (my_reverse k) 0)
)

; d) Write a function to return the greatest common divisor of all numbers in a linear list.

(defun _gcd (a b)
    (cond
        ((and (not (numberp a)) (not (numberp b))) nil)
        ((not (numberp a)) b)
        ((not (numberp b)) a)
        ((equal b 0) a)
        (T (_gcd b (mod a b)))
    )
)

(defun list_gcd (l)
    (cond
        ((and (atom (car l)) (null (cdr l))) (car l))
        ((listp (car l)) (_gcd (list_gcd (car l)) (list_gcd (cdr l))))
        (T (_gcd (car l) (list_gcd (cdr l))))
    )
)



