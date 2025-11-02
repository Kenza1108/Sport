# subscription_repository.py (enhanced)
from models.subscription import Subscription

class SubscriptionRepository:
    def __init__(self):
        self.all_subscriptions = []

    def add_subscription(self, id_number, amount, date, status):
        subscription = Subscription(
            id_number=id_number,
            amount=amount,
            date=date,
            status=status
        )
        self.all_subscriptions.append(subscription)
        print(f"✅ Subscription '{id_number}' added successfully.")

    def get_all_subscriptions(self):
        return self.all_subscriptions

    def calculate_total_income(self):
        return sum(s.amount for s in self.all_subscriptions)

    def find_subscription_by_id(self, id_number):
        for s in self.all_subscriptions:
            if s.id_number == id_number:
                return s
        return None
