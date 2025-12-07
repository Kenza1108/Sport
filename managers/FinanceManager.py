# managers/subscription_repository.py

from models.subscription import Subscription
from interfaces.repository_interface import RepositoryInterface

class SubscriptionRepository(RepositoryInterface):
    def __init__(self):
        self.subscriptions = []

    # ---------------------------------------------
    # CREATE
    # ---------------------------------------------
    def add(self, subscription: Subscription):
        """Add a new subscription."""
        if any(sub.id_number == subscription.id_number for sub in self.subscriptions):
            print(f"⚠️ Subscription '{subscription.id_number}' already exists.")
            return False
        self.subscriptions.append(subscription)
        print(f"✅ Subscription '{subscription.id_number}' added successfully.")
        return True

    # ---------------------------------------------
    # READ
    # ---------------------------------------------
    def get_all(self):
        """Return all subscriptions."""
        return self.subscriptions

    def find_by_id(self, id_number: str):
        """Find a subscription by ID."""
        for sub in self.subscriptions:
            if sub.id_number == id_number:
                return sub
        return None

    # ---------------------------------------------
    # DELETE
    # ---------------------------------------------
    def delete(self, id_number: str):
        """Delete a subscription by ID."""
        sub = self.find_by_id(id_number)
        if sub:
            self.subscriptions.remove(sub)
            print(f"🗑️ Subscription '{id_number}' removed.")
            return True
        print(f"⚠️ Subscription '{id_number}' not found for deletion.")
        return False

    # ---------------------------------------------
    # EXTRA
    # ---------------------------------------------
    def calculate_total_income(self):
        """Calculate total income from all subscriptions."""
        return sum(sub.amount for sub in self.subscriptions)
