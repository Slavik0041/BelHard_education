from house import House


class Townhouse(House):
    def __init__(self, address: str, cost: int):
        super().__init__(address, 60, cost)
