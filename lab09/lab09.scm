;; Scheme ;;

; Q1
(define (over-or-under x y)
  'YOUR-CODE-HERE
)

; Q3
(define lst
  'YOUR-CODE-HERE
)

; Q4
(define (remove item lst)
  'YOUR-CODE-HERE
)

;;; Tests

(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q5
(define (filter f lst)
  'YOUR-CODE-HERE
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

; Q6
(define (make-adder num)
  'YOUR-CODE-HERE
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13

; Q7
(define (composed f g)
  'YOUR-CODE-HERE
)
