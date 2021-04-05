from house import House


class Person:
    name: str
    age: int
    money: int
    realty: set

    def __init__(
            self,
            name: str,
            age: int,
            money: int = 0,
            realty: set = None
    ):
        if realty is None:
            self.realty = set()
        else:
            self.realty = realty
        self.name = name
        self.age = age
        self.money = money

    def info(self):
        print(f'{self.name} {self.age} [{self.money}]\n' + '\n'.join(self.realty))

    def earn_money(self, value: int):
        self.money += value

    def decrease_money(self, value: int):
        if self.money < value:
            raise ValueError('Не достаточно денег')
        else:
            self.money -= value

    def make_deal(self, house: House):
        try:
            self.decrease_money(house.cost)
        except ValueError as exc:
            print(f'Сделака не прошла: {exc}')
        else:
            self.realty.add(house)
