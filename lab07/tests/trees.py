test = {
  'name': 'Trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = Tree(1, Tree(2))
          Error
          >>> t = Tree(1, [Tree(2)])
          >>> t.label
          1
          >>> t.children[0]
          Tree(2)
          >>> t.children[0].label
          2
          >>> t.label = t.children[0].label
          >>> t
          Tree(2, [Tree(2)])
          >>> t.children.append(Tree(4, [Tree(8)]))
          >>> len(t.children)
          2
          >>> t.children[0]
          Tree(2)
          >>> t.children[1]
          Tree(4, [Tree(8)])
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}