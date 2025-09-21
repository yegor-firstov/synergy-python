class Turtle:
    def __init__(self, x: int = 0, y: int = 0, s: int = 1):
        if s <= 0:
            raise ValueError("Начальный шаг s должен быть ≥ 1")
        self.x = x
        self.y = y
        self.s = s

    def go_up(self) -> None:
        self.y += self.s

    def go_down(self) -> None:
        self.y -= self.s

    def go_left(self) -> None:
        self.x -= self.s

    def go_right(self) -> None:
        self.x += self.s

    def evolve(self) -> None:
        self.s += 1

    def degrade(self) -> None:
        if self.s - 1 <= 0:
            raise ValueError("Шаг s не может стать ≤ 0")
        self.s -= 1

    def count_moves(self, x2: int, y2: int) -> int:
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        if dx % self.s != 0 or dy % self.s != 0:
            return -1
        return dx // self.s + dy // self.s


if __name__ == "__main__":
    t = Turtle(x=0, y=0, s=3)
    print(t.count_moves(6, 9))
    print(t.count_moves(5, 5))
    t.evolve()
    print(t.count_moves(8, 12))
    t.go_right(); t.go_up()
    print(t.x, t.y, t.s)
