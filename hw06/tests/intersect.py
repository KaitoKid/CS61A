test = {
  'name': 'intersect',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (intersect odds (list 2 3 4 5))
          23f7ef6accb51ab360e5df1b2122e347
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (intersect odds (list 2 4 6 8))  ; Empty list is ()
          d17487605f66346bf68b6fb7c92f6257
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (intersect odds eight)
          8d122c22f95d3741fd80630adb71ef7c
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw06)
      scm> (define odds (list 3 5 7 9))
      scm> (define eight (list 1 2 3 4 5 6 7 8))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
