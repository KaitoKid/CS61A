test = {
  'name': 'as-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (as-list (leaf 3))
          2dd0048d47b0b85909420d75aa6476cf
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (as-list ())
          d17487605f66346bf68b6fb7c92f6257
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (as-list (tree 20 (leaf 19) (leaf 30)))
          00e0189fd285f8fb70cb48d95572a4cf
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (as-list (tree 20 (tree 19 (leaf 10) ()) (tree 30 (leaf 25) (leaf 35))))
          37a5dae3e27f5989a0bc1205c23fb8b9
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw06)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
