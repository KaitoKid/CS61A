test = {
  'name': 'Question 16',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define x 1)
          57775d5ff999af0ee4cbfa3aa0507be8
          # locked
          scm> (let ((x 5))
          ....    (+ x 3))
          47b3d31e7cbc26676385e887f119fbf1
          # locked
          scm> x
          7107157269a542fea41c45a208299f75
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (let ((x 1) (y x)) y)
          afe8b0293088a787c654885143501f84
          # locked
          # choice: SchemeError
          # choice: 1
          # choice: x
          # choice: y
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (let ((x 5))
          ....    (let ((x 2)
          ....          (y x))
          ....        (+ y (* x 2))))
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (square x) (* x x))
          square
          scm> (define (f x y)
          ....    (let ((a (+ 1 (* x y)))
          ....          (b (- 1 y)))
          ....        (+ (* x (square a))
          ....           (* y b)
          ....           (* a b))))
          f
          scm> (f 3 4)
          456
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define x 3)
          x
          scm> (define y 4)
          y
          scm> (let ((x (+ y 2))
          ....       (y (+ x 2)))
          ....      (cons x y))
          (6 . 5)
          scm> (let ((x 'hello)) x)
          hello
          scm> (define z 0)
          z
          scm> (let ((a (define z (+ z 1)))) z)
          1
          scm> (let ((x 1)
          ....       (y 3))
          ....    (define x (+ x 1))
          ....    (cons x y))
          (2 . 3)
          scm> (let ((a 1 1)) a)
          SchemeError
          scm> (let ((a 1) (2 2)) a)
          SchemeError
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
