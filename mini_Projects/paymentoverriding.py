
# Base Class (Parent)
# -----------------------------
class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must override this method")


# -----------------------------
# Child Classes (Override pay())
# -----------------------------

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} using UPI...")
        print("UPI Payment Successful!")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} using Debit/Credit Card...")
        print("Card Payment Approved!")


class WalletPayment(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} using Wallet Balance...")
        print("Wallet Payment Completed!")


# -----------------------------
# Polymorphism in Action
# -----------------------------
def checkout(payment_method: Payment, amount):
    print("----- Checkout Process -----")
    payment_method.pay(amount)   # Overridden method is called
    print("---------------------------\n")


# -----------------------------
# Main Program
# -----------------------------
upi = UPIPayment()
card = CardPayment()
wallet = WalletPayment()

checkout(upi, 500)
checkout(card, 1200)
checkout(wallet, 300)
