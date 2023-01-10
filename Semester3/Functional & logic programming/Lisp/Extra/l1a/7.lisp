;7.
;a)Write a function to eliminate the n-th element of a linear list.
; removeNth(l1l2...ln, n, pos) = 
; nil, n = 0
; removeNth(l2...ln, n, pos + 1), if n = pos
; {l1} U removeNth(l2...ln, n, pos + 1), otherwise

(defun removeNth (l n pos)
    (cond  
        ((null l) nil)
        ((= n pos) (removeNth (cdr l) n (+ pos 1)))
        (t (cons (car l) (removeNth(cdr l) n (+ pos 1))))
    
    )
)

(defun mainRemove (l n)
    (removeNth l n 1)
)

;b)Write a function to determine the successor of a number represented digit by digit as a list, without transforming the representation of the number from list to number. 
;Example: (1 9 3 5 9 9) --> (1 9 3 6 0 0)

; carry(a b c) = 
; = 1 , if a + b + c > 9
; = 0 , if a + b + c <= 9

(defun carry(a b c)
  (cond
    (( > (+(+ a b) c) 9) 1)
    (t 0)
  )
)

; digit(a b c) = 
; (a + b + c) mod 10 , if a + b + c > 9
; a + b + c , if a + b + c <=9

(defun digit(a b c)
  (cond
    (( > (+ (+ a b) c) 9) (mod (+ (+ a b) c) 10))
    (t (+ (+ a b) c))
  )
)

; myAppend(l1l2...ln, p1p2...pm) = 
; = p1p2...pm, if n = 0
; = {l1} U myAppend(l2...ln, p1p2...pm) , otherwise

(defun myAppend(l p)
  (cond
    ((null l) p)
    (t (cons (car l) (myAppend (cdr l) p)))
  )
)

; myReverse(l1l2...ln) = 
; = nil , if n = 0
; = myAppend(myReverse(l2...ln), list(myReverse(l1))), if l1 is a list
; = myAppend(myReverse(l2...ln), list(l1)), otherwise


(defun myReverse(l)
  (cond
    ((null l) nil)
    ((listp (car l)) (myAppend (myReverse (cdr l)) (list (myReverse (car l)))))
    (t (myAppend (myReverse (cdr l)) (list (car l))))
  )
)

; myAdd(l1l2...ln, p1p2...pm, c, r) = 
; = c , if n = 0 and c = 1
; = nil , if n = 0 and c = 0
; = myAdd(l2...ln, nil, carry(l1, 0, c), {digit(l1, 0, c)} U r) , if m = 0
; = myAdd(nil, p2...pn, carry(0, p1, c), {digit(0, p1, c)} U r) , if n = 0
; = myAdd(l2...ln, p2...pn, carry(l1, p1, c), {digit(l1, p1, c)} U r) , otherwise

(defun myAdd(l p c r)
  (cond 
    ((and (and (null l) (null p)) (equal c 1)) (cons c r))
    ((and (and (null l) (null p)) (equal c 0)) r)
    ((null p) (myAdd (cdr l) nil (carry (car l) 0 c) (cons (digit (car l) 0 c) r)))
    ((null l) (myAdd nil (cdr p) (carry 0 (car p) c) (cons (digit 0 (car p) c) r)))
    (t (myAdd (cdr l) (cdr p) (carry (car l) (car p) c) (cons (digit (car l) (car p) c) r)))
  )
)

(defun mySuccessor(l)
  (myAdd (myReverse l) (list 1) 0 (list ))
)

;c)Write a function to return the set of all the atoms of a list.
;Exemplu: (1 (2 (1 3 (2 4) 3) 1) (1 4)) ==> (1 2 3 4)

;getList(l1l2...ln) =
; nil, n = 0
; myAppend(getList(l1), getList(l2...ln)), if l1 is a list
; myAppend(list(l1), getList(l2...ln)), otherwise

(defun getList(l)
    (cond  
        ((null l) nil)
        ((listp (car l)) (myAppend (getList (car l)) (getList (cdr l))))
        (t (myAppend (list (car l)) (getList (cdr l))))
    )
)

;removeAllOccurences(l1l2...ln, elem) = 
; nil, n = 0
; removeAllOccurences(l2...ln, elem), if l1 = elem
; {l1} U removeAllOccurences(l2....ln, elem), otherwise

(defun removeAllOccurences(l elem)
    (cond  
        ((null l) nil)
        ((equal (car l) elem) (removeAllOccurences(cdr l) elem))
        (t (cons (car l) (removeAllOccurences (cdr l) elem)))
    )
)

;toSet(l1l2...ln) =
; nil , n = 0
; {l1} U removeAllOccurences(toSet(l2...ln), l1)

(defun toSet (l)
    (cond 
        ((null l) nil)
        (t (cons (car l) (removeAllOccurences (toSet (cdr l)) (car l))))
    )
)


(defun toSetAllLvls (l)
    (toSet (getList l))
)

;d)Write a function to test whether a linear list is a set.
; numberOfOccurences(l1l2...ln, elem)
; nil, n = 0
; 1 + numberOfOccurences(l2...ln, elem), if l1 = elem
; numberOfOccurences(l2...ln, elem), otherwise

(defun numberOfOccurences(l elem)
    (cond 
        ((null l) 0)
        ((equal (car l) elem) (+ 1 (numberOfOccurences (cdr l) elem)))
        (t (numberOfOccurences (cdr l) elem))
    )
)

; isSet(l1l2...ln) =
; true, n = 0
; false, if numberOfOCcurences(l2...ln, l1) > 0
; isSet(l2...ln), otherwise

(defun isSet(l)
    (cond  
        ((null l) t)
        ((> (numberOfOccurences (cdr l) (car l)) 0) nil)
        (t (isSet (cdr l)))
    )
)