; 12. Write a function that substitutes an element through another one at all levels of a given list.

; substitute(l, elem, newElem) = 
; = {l}, if l != elem and l is an atom
; = {newElem}, if l = elem and l is an atom
; = substitute(l1) U substitute(l2) U ... U substitute(ln), where i = 1,n

(defun mySubstitute(l elem newElem)
  (cond
    ((and (atom l) (not (equal l elem))) l)
    ((and (atom l) (equal l elem)) newElem)
    (t (mapcar #' (lambda (a) (mySubstitute a elem newElem)) l))
  )
) 


(defun change (l elem newElem lvl)
  (cond 
    
    ((and (atom l) (equal l elem)(> lvl 1)) newElem)    
    ((atom l) l)
    (t (mapcar #' (lambda (a) (change a elem newElem (+ lvl 1))) l))
  )
)

(defun wrapper (l elem newElem)
  (change l elem newElem 0)
)

(defun report-result (result form)
  (format t "~:[FAIL~;pass~] ... ~a~%" result form)
  result)



(defun test ()
  (progn
    (report-result (equal (mySubstitute '(1 2 3) 1 9) '(9 2 3)) '(= (mySubstitute '(1 2 3) 1 9) '(9 2 3)))
    (report-result (equal (mySubstitute '(1 2 (1) 3) 1 9) '(9 2 (9) 3)) '(= (mySubstitute '(1 2 (1) 3) 1 9) '(9 2 (9) 3)))
    (report-result (equal (mySubstitute '(1 2 (1) 3) 1 9) '(9 2 (9) 3)) '(= (mySubstitute '(1 2 (1) 3) 1 9) '(9 2 (9) 3)))
    )

)