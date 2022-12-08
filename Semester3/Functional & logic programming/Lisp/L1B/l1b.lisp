; 1. For a given tree of type (1) return the path from the root node to a certain given node X.


; pargurg_st(l1l2...ln, nrNoduri, nrMuchii) = 
; = nil, if n = 0
; = nil, if nrNoduri = 1 + nrMuchii
; = {l1} U {l2} U parcurg_st(l3...ln, nrNoduri + 1, l2 + nrMuchii), otherwise

(defun parcurg_st (l nrNoduri nrMuchii)
  (cond
    ((null l) nil)
    ((= nrNoduri ( + 1 nrMuchii)) nil)
    (t (cons (car l) (cons (cadr l) (parcurg_st (cddr l) (+ 1 nrNoduri) (+ (cadr l) nrMuchii)))))
  )
)


; parcurg_dr(l1l2...ln, nrNoduri, nrMuchii) =
; = nil, if n = 0
; = l1l2...ln, if nrNoduri = 1 + nrMuchii
; = parcurg_dr(l3...ln, nrNoduri + 1, nrMuchii + l2), otherwise


(defun parcurg_dr (l nrNoduri nrMuchii)
  (cond
    ((null l) nil)
    ((= nrNoduri (+ 1 nrMuchii)) l)
    (t (parcurg_dr (cddr l) (+ 1 nrNoduri) (+ (cadr l) nrMuchii)))
  )
)


;stang(l1l2...ln) = 
; = parcurg_st(l3...ln, 0,0)

(defun stang(l)
  (parcurg_st (cddr l) 0 0)
)


;drept(l1l2...ln) =
; = parcurg_dr(l3...ln, 0, 0)

(defun drept(l)
  (parcurg_dr (cddr l) 0 0)
)


; checkExistence(l1l2...ln, elem) = 
; = true, if l1 = elem
; = false , if n = 0
; = checkExistence(l2...ln, elem), otherwise


(defun checkExistence(l elem)
  (cond
    ((null l) nil)
    ((equal (car l) elem) t)
    (t (checkExistence (cdr l) elem))
  )
)


(defun checkExistenceLeft(l elem)
  (checkExistence (stang l) elem)
)

(defun checkExistenceRight(l elem)
  (checkExistence (drept l) elem)
)


; path(l1l2...ln, elem) = 
; = nil, if n = 0
; = list(elem), if elem = l1
; = {l1} U path(stang(l1l2...ln), elem), if checkExistenceLeft(l, elem) = true
; = {l1} U path(drept(l1l2...ln), elem), if checkExistenceRight(l, elem) = true


(defun path(l elem)
  (cond
    ((null l) nil)
    ((equal (car l) elem) (list elem))
    ((checkExistenceLeft l elem) (cons (car l) (path (stang l) elem)))
    ((checkExistenceRight l elem) (cons (car l) (path (drept l) elem)))
  )
)


;-----------------------------------------------------
;---------------------------TESTS---------------------

(defun report-result (result form)
  (format t "~:[FAIL~;pass~] ... ~a~%" result form)
  result)

;(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0)
;                         THE TREE
;         a
;        / \
;       b   d
;      / \  / \
;     c  f e   h
;    /  /
;   i  g

(defun testTree ()
  (progn
    (report-result (equal (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'a) '(a)) '(= (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'a) '(a)))
    (report-result (equal (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'b) '(a b)) '(= (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'b) '(a b)))
    (report-result (equal (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'c) '(a b c)) '(= (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'c) '(a b c)))
    (report-result (equal (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'd) '(a d)) '(= (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'd) '(a d)))
    (report-result (equal (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'e) '(a d e)) '(= (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'e) '(a d e)))
    (report-result (equal (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'f) '(a b f)) '(= (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'f) '(a b f)))
    (report-result (equal (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'g) '(a b f g)) '(= (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'g) '(a b f g)))
    (report-result (equal (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'h) '(a d h)) '(= (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'h) '(a d h)))
    (report-result (equal (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'i) '(a b c i)) '(= (path '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) 'i) '(a b c i)))
    )

)

