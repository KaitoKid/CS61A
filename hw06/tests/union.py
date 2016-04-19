test = {
  'name': 'union',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (union odds (list 2 3 4 5))
          b62af240bc25fc13906403241fd2644a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (union odds (list 2 4 6 8))
          52fe6c1cb0d21e6a4f00a3500ae7c00b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (union odds eight)
          425969f3293b733038c1215325aa48e5
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
