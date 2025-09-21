class CashDesk:
    """Простая касса с балансом в целых единицах (например, рубли)."""

    def __init__(self, initial: int = 0):
        if initial < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self._balance = int(initial)

    @property
    def balance(self) -> int:
        """Текущий баланс кассы."""
        return self._balance

    def top_up(self, x: int) -> None:
        """Пополнить кассу на x."""
        if x <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += int(x)

    def count_1000(self) -> int:
        """Сколько целых тысяч в кассе."""
        return self._balance // 1000

    def take_away(self, x: int) -> None:
        """Забрать x из кассы. Бросает ошибку, если денег недостаточно."""
        if x <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if x > self._balance:
            raise ValueError("Недостаточно денег в кассе")
        self._balance -= int(x)


if __name__ == "__main__":
    k = CashDesk(2500)
    k.top_up(800)
    print(k.count_1000())
    k.take_away(1000)
    print(k.balance)
