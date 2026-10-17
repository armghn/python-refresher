from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @property
    @abstractmethod
    def fee(self):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print(f"paid {amount}")

    @property
    def fee(self):
        return 0.3


card = CreditCard()
card.pay(500)
print(card.fee)
