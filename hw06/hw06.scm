(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (square x) (* x x))

(define (pow b n)
  (expt b n)
)

(define (ordered? s)
  (if
    (or (null? (cdr s)) (null? s)) True
    (and (>= (cadr s) (car s)) (ordered? (cdr s)))
  )
)

(define (no-repeats s)
'YOUR-CODE-HERE
nil)

(define (nodots s)
  'YOUR-CODE-HERE
  nil
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ((= (car s) v) true)
          ((> (car s) v) false)
          (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)
(define (add s v)
    (cond ((empty? s) (list v))
          ((contains? s v) s)
          ((< v (car s)) (cons v s))
          ))
(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          'YOUR-CODE-HERE
          (else nil) ; replace this line
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          'YOUR-CODE-HERE
          (else nil) ; replace this line
          ))

; A data abstraction for binary trees where nil represents the empty tree
(define (tree label left right) (list label left right))
(define (label t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf label) (tree label nil nil))
(define (in? t v)
    (cond ((empty? t) false)
          'YOUR-CODE-HERE
          (else nil)
          ))

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.label == v:
;         return True
;     elif s.label < v:
;         return contains(s.right, v)
;     elif s.label > v:
;         return contains(s.left, v)
(define (as-list t)
    'YOUR-CODE-HERE
    (else nil)
    )
