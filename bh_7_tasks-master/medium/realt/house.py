class House:
    address: str
    area: float
    cost: int

    def __init__(self, address: str, area: float, cost: int):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self, value: int):
        self.cost += value

    def decrease_cost(self, value: int):
        if self.cost > value:
            self.cost = 0
        else:
            self.cost -= value
