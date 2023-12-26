from inspect import getmembers, isclass, isabstract
import payment_methods


class PaymentFactory(object):
    payment_dictionary = {}

    def __init__(self):
        self.load_payment_methods()

    def load_payment_methods(self):
        members = getmembers(
            payment_methods, lambda m: isclass(m) and not isabstract(m)
        )
        for name, _type in members:
            self.payment_dictionary[name] = _type

    def create(self, payment_type: str):
        if payment_type in self.payment_dictionary:
            return self.payment_dictionary[payment_type]()
        else:
            raise ValueError(
                f"{payment_type} is not currently supported as a payment method."
            )
