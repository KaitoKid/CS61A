test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          25
          >>> len(pokemon)
          3
          >>> pokemon['jolteon'] = 135
          >>> pokemon['ditto'] = 25
          >>> len(pokemon)
          5
          >>> sorted(list(pokemon.keys())) # Alphabetically sorted list of pokemon's keys
          ['ditto', 'dragonair', 'jolteon', 'mew', 'pikachu']
          >>> 'mewtwo' in pokemon
          False
          >>> pokemon['ditto'] = pokemon['jolteon']
          >>> sorted(list(pokemon.keys())) # Alphabetically sorted list of pokemon's keys
          ['ditto', 'dragonair', 'jolteon', 'mew', 'pikachu']
          >>> pokemon['ditto']
          135
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