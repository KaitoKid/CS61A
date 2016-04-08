(define (deep-map fn s)
  (cond
    ((null? s) '())
    ((list? s)
      (cons
        (deep-map fn (car s))
        (deep-map fn (cdr s))
      ))
    (else
      (fn s)
    )
  )
)
