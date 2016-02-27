test = {
  'name': 'Sevens',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 3, [5, 7], 9] # Write the code that indexes into x to output the 7
          x[2][1]
          >>> x = [[7]] # Write the code that indexes into x to output the 7
          x[0][0]
          >>> x = [1, [2, [3, [4, [5, [6, [7]]]]]]] # Write the code that indexes into x to output the 7
          x[1][1][1][1][1][1][0]
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