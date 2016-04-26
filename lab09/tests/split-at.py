test = {
  'name': 'split-at',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (car (split-at '(1 2 3 4 5) 3))
          7585771ecc8eac10b0735a645ecb8a79
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cdr (split-at '(1 2 3 4 5) 3))
          034d782bcafd58238fbace6927d3ca53
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (car (split-at '(1 2 3 4 5) 10))
          e0d0673c631a6427e97aac354fdb7c5b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cdr (split-at '(1 2 3 4 5) 10))
          f9ebafa0bfa75e2a858c464aa39a573d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (car (split-at '(0 1 1 2 3) 0))
          f9ebafa0bfa75e2a858c464aa39a573d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cdr (split-at '(0 1 1 2 3) 0))
          23438739dcd29b6922bbe40f7a033d5d
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
