(defun report-result (result form)
  (format t "~:[FAIL~;pass~] ... ~a~%" result form)
  result)

;myAppend(l1l2...ln, p1p2...pm)
; = p1p2...pm, n = 0
; {l1} U myAppend(l2...ln, p1p2...pm)

(defun myAppend (l p)
    (cond  
        ((null l) p)
        (t (cons (car l) (myAppend (cdr l) p)))
    )
)

; getList(l1l2...ln)
; nil, n = 0
; myAppend(getList(l1), getList(l2...ln)), if l1 is a list
; myAppend(l1, getList(l2...ln)), otherwise

(defun getList (l)
    (cond  
        ((null l) nil)
        ((listp (car l)) (myAppend (getList (car l)) (getList (cdr l))))
        ((numberp (car l)) (myAppend (list (car l)) (getList (cdr l))))
        (t (getList (cdr l)))
    )
)

; removeOccurences(l1l2...ln, elem)
; = nil, n = 0
; removeOccurences (l2...ln, elem), if l1 = elem
; {l1} U removeOccurences(l2...ln, elem), otherwise

(defun removeOccurences (l elem)
    (cond  
        ((null l) nil)
        ((equal (car l) elem) (removeOccurences (cdr l) elem))
        (t (cons (car l) (removeOccurences (cdr l) elem)))
    )
)

; toSet(l1l2...ln)
; = nil, n = 0
; {l1} U removeOccurences(toSet(l2...ln), l1)
(defun toSet (l)

    (cond  
        ((null l) nil)
        (t (cons (car l) (removeOccurences (toSet (cdr l)) (car l))))
    )
)

; getNumericalAtoms(l1l2...ln) 
; = toSet(getList(l1l2...ln))

(defun getNumericalAtoms (l)
    (toSet (getList l))
)

(defun tests ()
    (progn 
        (report-result (equal (getNumericalAtoms '(1 F (2 (1 3 E (2 4) 3) E 1)(1 4)) ) '(1 2 3 4)) '(= (getNumericalAtoms '(1 F (2 (1 3 E (2 4) 3) E 1)(1 4)) ) '(1 2 3 4)))
        (report-result (equal (getNumericalAtoms '(1 (2 3 (4 5)6))) '(1 2 3 4 5 6)) '(= (getNumericalAtoms '(1 (2 3 (4 5)6))) '(1 2 3 4 5 6)))
        (report-result (equal (getNumericalAtoms '(A (B C D (E) F G))) '()) '(= (getNumericalAtoms '(A (B C D (E) F G))) '()))
        (report-result (equal (getNumericalAtoms '(1 B C (1 D 2 (A 2 A) E 1) H)) '(1 2)) '(= (getNumericalAtoms '(1 B C (1 D 2 (A 2 A) E 1) H)) '(1 2)))
    )
)