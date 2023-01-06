;3.
;a) Write a function that inserts in a linear list a given atom A after the 2nd, 4th, 6th, ... element.
; insert(l1l2...ln, elem, pos)
; nil, n = 0
; {l1} U {elem} U insert(l2...ln, elem, pos + 1), if pos % 2 = 0 and pos != 0
; {l1} U insert(l2...ln, elem, pos + 1), otherwise



(defun myInsert (l elem pos)
    (cond 
        ((null l) nil)
        ((and (not (= pos 0)) (= (mod pos 2) 0)) (cons (car l) (cons elem (myInsert (cdr l) elem (+ pos 1)))))
        (t (cons (car l) (myInsert (cdr l) elem (+ pos 1))))
    )

)

(defun mainInsert (l elem)
    (myInsert l elem 0)
)

;b) Write a function to get from a given list the list of all atoms, on any level, but reverse order. 
;Example:(((A B) C) (D E)) ==> (E D C B A)

;getList(l1l2...ln) =
; nil, n = 0
; {l1} U getList(l2..ln), if l1 is atom
; getList(l1) U getList(l2...ln), if l1 is a list
(defun getList (l)
    (cond
        ((null l) nil)
        ((atom (car l)) (append (list (car l)) (getList (cdr l))))
        ((listp (car l)) (append (getList (car l)) (getList (cdr l))))
    )
)

(defun myAppend(l p)
    (cond
        ((null l) p)
        (t (cons (car l) (myAppend (cdr l) p)))
    )
)

; reverseList(l1l2...ln)
; = nil, n = 0
; = append(reverseList(l2...ln), l1)

(defun reverseList(l)
    (cond
        ((null l) nil)
        (t(myAppend (reverseList (cdr l)) (list(car l)) ))
    )
)

(defun reverseListAllLvls(l)
    (reverseList (getList l))
)

;c) Write a function that returns the greatest common divisor of all numbers in a nonlinear list.
; gcd(a, b)
; a, a = b
; gcd(a-b, b), a > b
; gcd(a, b-a), b > a

(defun myGcd (a b)
    (cond 
        ((= a b) a)
        ((> a b) (myGcd (- a b) b))
        (t (myGcd a (- b a)))
    )
)

; listGcd(l1l2...ln)
; l1, if n = 1
; myGcd(l1, listGcd(l2...ln)), otherwise

(defun gcdForAllNumbers(l)
  (cond
    ((null (cdr l)) (car l))
    (t (myGcd (car l) (gcdForAllNumbers (cdr l))))
  )
)

;d) Write a function that determines the number of occurrences of a given atom in a nonlinear list.
; nrOfOccurences(l1l2...ln, elem)
; 0, n = 0
; nrOfOccurences(l1) + nrOfOccurences(l2...ln), if l1 is a list
; 1 + nrOfOccurences(l2...ln, elem), if l1 = elem and l1 is atom
; nrOfOccurences(l2...ln, elem), otherwise

(defun nrOfOccurences(l elem)
    (cond 
        ((null l) 0)
        ((listp (car l)) (+ (nrOfOccurences(car l) elem) (nrOfOccurences (cdr l) elem)))
        ((and (atom (car l)) (equal elem (car l))) (+ 1 (nrOfOccurences (cdr l) elem)))
        (t (nrOfOccurences (cdr l) elem))
    )
)