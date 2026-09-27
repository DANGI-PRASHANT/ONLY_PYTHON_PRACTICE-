# Another example:
class Cash:
    def pay(self,amount):
        print(f"Rs.{amount} has been paid by cash.")

class Fonepay:
    def pay(self,amount):
        print(f"Rs.{amount} has been paid bt Fonepay")

class Esewa:
    def pay(self,amount):
        print(f"Rs.{amount} has been paid by Esewa.")


payments = [Cash(),Fonepay(),Esewa()]

# for payment in payments:
#     payment.pay(300)

def make_payment(payment_methods):
    payment_methods.pay(5000)

for payment in payments:
    make_payment(payment)


