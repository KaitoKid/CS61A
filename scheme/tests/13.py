test = {
  'name': 'Question 13',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (if True 1 0)
          7107157269a542fea41c45a208299f75
          # locked
          scm> (if False 1 0)
          9815d8391210230341d3c0942b067539
          # locked
          scm> (if 1 1 0)
          7107157269a542fea41c45a208299f75
          # locked
          scm> (if 0 1 0)
          7107157269a542fea41c45a208299f75
          # locked
          scm> (if 'a 1 0)
          7107157269a542fea41c45a208299f75
          # locked
          scm> (if (cons 1 2) 1 0)
          7107157269a542fea41c45a208299f75
          # locked
          scm> (if True 1)
          7107157269a542fea41c45a208299f75
          # locked
          scm> (if False 1)
          scm> (eval (if False 1))
          scm> (if True '(1))
          9f90814c29b45aacdbe10436cf085857
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define (f) False)
          5e9740437eba0d6fc4d5ab5f9dd3d30b
          # locked
          scm> (if (f) 1 0)
          9815d8391210230341d3c0942b067539
          # locked
          scm> (if f 1 0)
          7107157269a542fea41c45a208299f75
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define (true-condition) (print 'true-condition) #t)
          true-condition
          scm> (define (false-condition) (print 'false-condition) #f)
          false-condition
          scm> (define (result) (print 'result))
          result
          scm> (if (true-condition) (result) (/ 1 0))
          true-condition
          result
          scm> (if (false-condition) (/ 1 0) (result))
          false-condition
          result
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (if True)
          SchemeError
          scm> (if)
          SchemeError
          scm> (if True 'who 'where 'wat)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (no-mutation val)
          ....         (if val '(1 2) '(3 4)))
          no-mutation
          scm> no-mutation
          (lambda (val) (if val (quote (1 2)) (quote (3 4))))
          scm> (no-mutation True)
          (1 2)
          scm> (no-mutation False)
          (3 4)
          scm> no-mutation ; if-statements should not cause mutation
          (lambda (val) (if val (quote (1 2)) (quote (3 4))))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
