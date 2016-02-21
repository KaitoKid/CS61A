test = {
  'name': 'To Boolean or not to Boolean',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ((0 or 5) and (False or '') and 1/0)
          be844f82d499beb06331e2570b74544a
          # locked
          >>> fi, foo = max, min
          >>> def switcheroo(foo):
          ...     foo = fi
          ...     return 10
          >>> foo(switcheroo(foo), 5)
          ba2ed30ea3c5a7b76de99e472ac02833
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}