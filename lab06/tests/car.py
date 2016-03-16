test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.model
          'Model S'
          >>> hilfingers_car.gas = 10
          >>> hilfingers_car.drive()
          'Tesla Model S goes vroom!'
          >>> hilfingers_car.drive()
          'Tesla Model S cannot drive!'
          >>> hilfingers_car.fill_gas()
          Your car is full.
          >>> hilfingers_car.gas
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> Car.headlights
          2
          >>> hilfingers_car.headlights
          2
          >>> Car.headlights = 3
          >>> hilfingers_car.headlights
          3
          >>> hilfingers_car.headlights = 2
          >>> Car.headlights
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.wheels = 2
          >>> hilfingers_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> hilfingers_car.drive()
          'Tesla Model S cannot drive!'
          >>> Car.drive()
          Error
          >>> Car.drive(hilfingers_car)
          'Tesla Model S cannot drive!'
          >>> MonsterTruck.drive(hilfingers_car)
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> sumukhs_car = MonsterTruck('Monster', 'Batmobile')
          >>> sumukhs_car.drive()
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.drive(sumukhs_car)
          'Monster Batmobile goes vroom!'
          >>> MonsterTruck.drive(sumukhs_car)
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.rev(sumukhs_car)
          Error
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