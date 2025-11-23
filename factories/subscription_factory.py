# factories/subscription_factory.py
from models.subscription import Donation, MonthlySubscription, AnnualSubscription

class SubscriptionFactory:
    @staticmethod
    def create_subscription(sub_type: str, **kwargs):
        if sub_type == "donation":
            return Donation(**kwargs)
        elif sub_type == "monthly":
            return MonthlySubscription(**kwargs)
        elif sub_type == "annual":
            return AnnualSubscription(**kwargs)
        else:
            raise ValueError(f"Unknown subscription type: {sub_type}")
