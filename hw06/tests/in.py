test = {
  'name': 'in?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (in? tr 20)  ; True or False
          8ed0efeabc8e9866128f4f4e97c7ce8e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (in? tr 26) ; True or False
          c5337435f00ff38c841d94ea0082db92
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (in? tr 8)  ; True or False
          8ed0efeabc8e9866128f4f4e97c7ce8e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (in? tr 0)  ; True or False
          c5337435f00ff38c841d94ea0082db92
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (in? tr 36)  ; True or False
          c5337435f00ff38c841d94ea0082db92
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (in? tr 35)  ; True or False
          8ed0efeabc8e9866128f4f4e97c7ce8e
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw06)
      scm> (define tr
              (tree 20
                 (tree 19
                    (tree 10
                       (tree 4 (leaf 1) (leaf 8))
                       (tree 15 () (leaf 16)))
                    ())
                 (tree 30
                    (leaf 25)
                    (tree 35 (tree 33 () (leaf 34)) ()))))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
