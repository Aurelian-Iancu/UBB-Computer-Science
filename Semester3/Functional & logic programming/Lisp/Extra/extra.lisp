
; Exercise 1.
; Delete from a non-linear list all the sublists(linear) that have an even number of elements
; Example: (delete ' ((2 3 4)(6 (7 8) ((7 9) 8)) (6 8) 9)) -->((2 3 4) (6 (8)) 9)

;lengthList(l1l2...ln) =
; 0, n = 0
; 1 + lengthList(l2...ln), otherwise

(defun lengthList (l)
    (cond  
        ((null l) 0)
        (t (+ 1 (lengthList (cdr l))))
    
    )
)


(defun checkEvenLength(l)
    (= 0 (mod (lengthList l) 2))
)


; linearList(l1l2...ln) = 
; nil, n = 0
; false, if l1 is a list
; linearList(l2...ln), otherwise
(defun linearList (l)
    (cond  
        ((null l) t)
        ((listp (car l)) nil)
        (t (linearList (cdr l)))
    )
)

; THE THINKING PROCESS
; if(listp l1)
; {
;   if(linear && oddLength)
;       remove;
;   else if(linear && notOldLength)
;       cons;
;   else(notLinear)
;     removeEven2(l1) U removeEven2(l2...ln)
;}
; else
;   cons (car l)(removeEven2 (cdr l))

; removeEven(l1l2...ln) =
; = nil, n = 0
; = removeEven(l2...ln), if l1 is a list and linearList(l1) and checkEvenLength(l1)
; = {l1} U removeEven(l2...ln), if l1 is a list and linearList(l1) and not(checkEvenLength(l1))
; = removeEven(l1) U removeEven(l2...ln), if l1 is a list and not(linearList(l1))
; = {l1} U removeEven(l2...ln), otherwise

(defun removeEven (l)
    (cond  
        ((null l) nil)
        ((listp (car l))
            (cond 
                ((and (linearList (car l)) (checkEvenLength (car l))) (removeEven (cdr l)))
                ((and (linearList (car l)) (not (checkEvenLength (car l)))) (cons (car l) (removeEven (cdr l))))
                (t (cons (removeEven (car l)) (removeEven (cdr l))))
            )
        )
        (t (cons (car l) (removeEven (cdr l))))
    )
)

;-------------------------------
; Exercise 2.
;Write a functie that gets a linear list and returns back the set of all pairs of non-numerical atoms from the list.
;Example: (A 2 B 3 C D 1) --> ((A B) (A C) (A D) (B C) (B D) (C D))

(defun pairElement (el l)
    (cond 
    ((null l) nil)
    (t (cons (list el (car l)) (pairElement el (cdr l))))
    )
)

(defun pairs(l)
    (cond
    ((null l) nil)
    ((numberp (car l)) (pairs (cdr l)))
    (t(append (pairElement (car l) (cdr l)) (pairs (cdr l))))
    )
)

;Exercise 3.
; Sa se scrie o functie care insereaza un element dat pe toate pozitiile intr o lista liniara si returneaza o lista de liste
; Write a function that inserts a given element on all the positions of a linear list and returns a list of lists
; Exemplu (inserare 1 (2 3)) --> ((1 2 3) (2 1 3) (2 3 1))

; insertToPosition(l1l2...ln, e, n, pos)
; = nil, n = 0
; = {e} U insertPosition(l1l2...ln, e, n, pos + 1), if n = pos
; = {l1} U insertPosition(l2... ln, e, n, pos + 1), otherwise

(defun insertToPosition (l e n pos)
    (cond  
        ((null l) nil)
        ((= n pos) (cons e (insertToPosition l e n (+ pos 1))))
        (t (cons (car l) (inserttoposition (cdr l) e n (+ pos 1))))
    )
)

(defun myLength(l)
    (cond  
        ((null l) 0)
        (t (+ 1 (myLength (cdr l))))
    )
)


(defun insertEveryPosition (l e pos)
    (cond  
        ((= pos (+ (length l) 1)) (list (append l (list e))))
        ((<= pos (myLength l)) (cons (insertToPosition l e pos 1) (insertEveryPosition l e (+ pos 1))))
    )
)

; Exercise 4
; Write a function that removes the 1st, 2nd, 4th, 8th... element from it
; removePos(l1l2....ln, m, pos) =
; nil, n = 0
; removePos(l2...ln, m * 2, pos + 1), if pos = m
; l1 U removePos(l2...ln, m, pos + 1), otherwise

(defun removePos (l m pos)
    (cond  
        ((null l) nil)
        ((= pos m) (removePos (cdr l) (* m 2) (+ pos 1)))
        (t (cons (car l) (removePos (cdr l) m (+ pos 1))))
    )
)

(defun mainRemove(l)
    (removePos l 1 1)
)

;Exercise 5.
;Define a function that obtains from a nonlinear list a linear list formed out of all the non-numerical atoms
;on any level but in reverse order.
;Example: (((A B) 2 C) 3 (D 1 E)) --> (E D C B A)
(defun ex5 (l)
    (cond  
        ((null l) nil)
        ((listp (car l)) (append (ex5 (cdr l)) (ex5 (car l))))
        ((not(numberp (car l))) (append (ex5 (cdr l)) (list (car l))))
        (t (ex5 (cdr l)))
    )
)

;Exercise 6
;Define a function that obtains from a nonlinear list a linear list formed out of all the non-numerical atoms
;on any level.
(defun ex6 (l)
    (cond  
        ((null l) nil)
        ((listp (car l)) (append (ex6 (car l)) (ex6 (cdr l)) ))
        ((not(numberp (car l))) (append (list (car l)) (ex6 (cdr l))))
        (t (ex6 (cdr l)))
    )
)

;Exercise 7
;c)Write a function to replace each sublist of a list with its last element.A sublist is an element from the first level, which is a list.
;Example: (a (b c) (d (e (f)))) ==> (a c (e (f))) ==> (a c (f)) ==> (a c f)
;(a (b c) (d ((e) f))) ==> (a c ((e) f)) ==> (a c f)

(defun myAppend (l p)
    (cond  
        ((null l) p)
        (t (cons (car l) (myAppend(cdr l) p)))
    )
)

(defun myReverse (l)
    (cond  
        ((null l) nil)
        (t (myAppend (myReverse (cdr l)) (list (car l))))
    )
)

(defun lastElement (l)
    (cond  
        ((atom l) l)
        (t (lastElement (car (myReverse l))))
    )
)

; last(l1l2...ln) = 
; nil, n = 0
; lastElement(l1) U lastElement(l2...ln), l1 is a list
; {l1} U lastElement(l2...ln), otherwise

(defun myLast(l)
    (cond  
        ((null l) nil)
        ((listp (car l)) (cons (last_element (car l)) (myLast (cdr l))))
        (t (cons (car l) (myLast (cdr l))))
    )
)

; Exercise 8.
; Write a function to determine the number of all sublists of a given list, on any level. 
; A sublist is either the list itself, or any element that is a list, at any level. 
; Example: (1 2 (3 (4 5) (6 7)) 8 (9 10)) => 5 lists:

; numberOfLists(l1l2...ln) = 
; 1, n = 0
; 1 + numberOfLists(l2...ln), if l1 is a list and linearList(l1)
; nuberOfLists(l1) + numberOfLists(l2...ln), if l1 is a list and not(linearList(l1))
; numberOfLists(l2...ln)

(defun numberOfLists(l)
    (cond  
        ((null l) 1)
        ((and (listp (car l)) (linearList (car l))) (+ 1 (numberOfLists (cdr l))))
        ((and (listp (car l)) (not(linearList (car l)))) (+ (numberOfLists(car l)) (numberOfLists (cdr l))))
        (t (numberOfLists (cdr l)))
    )
)

;Exercise 9
;Write a function to return the set of all the atoms of a list.
;Exemplu: (1 (2 (1 3 (2 4) 3) 1) (1 4)) ==> (1 2 3 4)

; getList(l1l2...ln) = 
; nil, n = 0
; append(l1, getList(l2...ln)), otherwise

(defun getList(l)
    (cond  
        ((null l) nil)
        ((listp (car l)) (append (getList (car l)) (getList (cdr l))))
        (t (append (list (car l)) (getList (cdr l))))
    )
)

; removeOccurences(l1l2...ln, elem)
; nil, n = 0
; removeOccurences(l2...ln, elem), if l1 = elem
; {elem} U removeOccurences(l2...ln, elem), otherwise

(defun removeOccurences (l elem)
    (cond  
        ((null l) nil)
        ((equal elem (car l)) (removeOccurences (cdr l) elem))
        (t (cons (car l) (removeOccurences (cdr l) elem)))
    )
)

;toSet(l1l2...ln) =
; nil , n = 0
; {l1} U removeAllOccurences(toSet(l2...ln), l1)

(defun toSet (l)
    (cond 
        ((null l) nil)
        (t (cons (car l) (removeOccurences (toSet (cdr l)) (car l))))
    )
)

;getSetAllLvls(l1l2...ln)

(defun getSetAllLvls(l)
    (toSet (getList l))
)

;Exercise 10
; Build a function that returns the minimum numeric atom from a list, at any level

; myMin(a, b) = 
; = nil , if a is not a number and b is not a numbe
; = a , if b is not a numbe
; = b , if a is not a number
; = a , if a < b
; = b , otherwise

(defun myMin(a b)
  (cond
    ((and (not (numberp a)) (not (numberp b))) nil)
    ((not (numberp a)) b)
    ((not (numberp b)) a)
    ((< a b) a)
    (t b)
  )
)

; minList(l1l2...ln)
; l, n = 1
; myMin(minList(l1), minList(l2...ln)), if l1 is a list
; myMin(l1, minList(l2...ln)), if l1 is a number
; minList(l2...ln), otherwise

(defun minList (l)
    (cond  
        ((atom l) l)
        ((listp (car l)) (myMin (minList (car l)) (minList (cdr l))))
        ((numberp (car l)) (myMin (car l) (minList(cdr l))) )
        (t (minList (cdr l)))
    )

)

; Exercise 11
; Return the list of nodes of a tree of type (2) accessed inorder.
; inorder(l1l2l3)
; nil, n = 0
; inorder (l2) U {l1} U inorder (l3)
(defun inorder(l)
    (cond  
        ((null l) nil)
        (t (append (inorder (cadr l)) (list (car l)) (inorder (caddr l))))
    )
)

;Exercise 12
; Return the list of a tree of type (2) accessed postorder.
; postorder(l1l2l3)
; nil , n = 0
; postorder(l2) U postorder(l3) U l1

(defun postorder (l)
    (cond  
        ((null l) nil)
        (t (append (postorder (cadr l)) (postorder (caddr l)) (list (car l))))
    )
)

;Exercise 13
; Return the list of a tree of type (2) accessed preorder.
; preorder(l1l2l3)
; nil , n = 0
; l1 U postorder(l2) U postorder(l3) 
(defun preorder (l)
    (cond  
        ((null l) nil)
        (t (append (list(car l)) (preorder (cadr l)) (preorder (caddr l))))
    )
)

; Exercise 14
; Return the level of a node X in a tree of type (2). The level of the root element is 0.

; exists(l1l2...ln, elem)
; false, n = 0 
; true, l1 = elem
; exists(l1, elem) or exists(l2...ln, elem), if l1 is a list
; exists(l2...ln, elem) otherwise

(defun exists(l elem)
    (cond  
        ((null l) nil)
        ((equal (car l) elem) t)
        ((listp (car l)) (or (exists (car l) elem) (exists (cdr l) elem)))
        (t (exists(cdr l) elem))
    ) 
)

; nodeLevel(l1l2l3, x) = 
; 0, l1 = x
; 1 + nodeLevel(l2), if exists(l2, elem)
; 1 + nodeLevel(l3), if exists(l3, elem)
; nil, otherwise

(defun nodeLevel(l x)
    (cond  
        ((equal x (car l)) 0)
        ((exists(cadr l) x) (+ 1 (nodeLevel (cadr l) x)))
        ((exists(caddr l) x) (+ 1 (nodeLevel (caddr l) x)))
        (t nil)
    )
)

; Exercise 15.
;For a given tree of type (2) return the path from the root node to a certain given node X.
; path(l1l2l3, x) =
; l1, if l1 = x
; l1 U path(l2,x), if exists (l2, elem)
; l1 U path(l3,x), if exists (l3, elem)
; nil, otherwise
(defun path(l x)
    (cond  
        ((equal (car l) x) (car l))
        ((exists (cadr l) x) (cons (car l) (path (cadr l) x)))
        ((exists (caddr l) x) (cons (car l) (path (caddr l) x)))
        (t nil)
    )
)

; Exercise 16
; Determine  if  a  tree  of  type  (2)  is ballanced  (the  differencebetween  the  depth  of  two  subtrees  is equal to 1).
; absoluteDiff(a, b) = 
; = a - b, if a > b
; = b - a, otherwise
(defun absoluteDiff(a b)
    (cond   
        ((> a b) (- a b))
        (t (- b a))
    )
)

; myMax(a, b) =
; a, a > b
; b otherwise
(defun myMax (a b)
    (cond  
        ((> a b) a)
        (t b)
    )
)

;getDepth(l1l2l3) = 
; 0, if l1l2l3 is null
; = 1 + myMax(getDepth(l2), getDepth(l3)), otherwise

(defun getDepth(l)
    (cond  
        ((null l) 0)
        (t (+ 1 (myMax (getDepth (cadr l)) (getDepth (caddr l)))))
    )
)

(defun balanced(l)
    (> 2 (absoluteDiff(getDepth (cadr l)) (getDepth (caddr l))))
)

; Exercise 17
;11.Return the level (and coresponded list of nodes) with maximum number of nodes for a tree of type (2). The level of the root element is 0.

; myAppend(l1l2...ln, p1p2...pm) = 
; = p1p2...pm, if n = 0
; = {l1} U myAppend(l2...ln, p1p2...pm), otherwise


(defun myAppend (l p)
  (cond
    ((null l) p)
    (t (cons (car l) (myAppend (cdr l) p)))
  )
)

; findLevel(l1l2l3, counter) = 
; = counter, if l1l2l3 is empty
; = myMax(findLevel(l2, counter + 1),findLevel(l3, counter + 1)), otherwise

(defun findMaxLevel(l counter)
  (cond
    ((null l) counter)
    (t (myMax (findMaxLevel (cadr l) (+ 1 counter)) (findMaxLevel (caddr l) (+ 1 counter))))
  )
)

; nodesFromLevel(l1l2l3, level, counter)
; = nil, if l1l2l3 is empty
; = l1 , if counter = level
; = myAppend((list (nodesFromLevel(l2, level, counter + 1))) (list (nodesFromLevel(l3, level, counter + 1)))), otherwise

(defun nodesFromLevel(l level counter)
  (cond
    ((null l) nil)
    ((equal counter level) (list (car l)))
    (t (myAppend (nodesFromLevel (cadr l) level (+ 1 counter)) (nodesFromLevel (caddr l) level (+ 1 counter))))
  )
)

(defun main(l)
  (nodesFromLevel l (findMaxLevel l -1) 0)
)

; Exercise 18.
; addFromNtoN(l1l2...ln n elem pos)
; nil, n = 0
; {l1} U {elem} U addFromNtoN(l2...ln, n, elem, pos + 1), if pos % n = 0
; {l1} U addFromNtoN(l2...ln, n, elem, pos + 1), otherwise

(defun addFromNtoN (l n elem pos)
    (cond  
        ((null l) nil)
        ((= 0 (mod pos n)) (cons (car l) (cons elem (addFromNtoN (cdr l) n elem (+ pos 1)))))
        (t (cons (car l) (addFromNtoN (cdr l) n elem (+ pos 1))))
    )

)

(defun main(l n elem)
    (addFromNtoN l n elem 1)
)
