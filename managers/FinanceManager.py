from models.subscription import Subscription

class SubscriptionRepository:
    def __init__(self):
        # قائمة تحتوي على جميع الاشتراكات
        self.subscriptions = []

    def add_subscription(self, subscription: Subscription):
        """إضافة اشتراك جديد (نموذج جاهز من نوع Subscription)."""
        self.subscriptions.append(subscription)
        print(f"✅ Subscription '{subscription.id_number}' added successfully.")

    def get_all_subscriptions(self):
        """إرجاع جميع الاشتراكات."""
        return self.subscriptions

    def find_subscription_by_id(self, id_number: str):
        """البحث عن اشتراك باستخدام رقم المعرف."""
        for sub in self.subscriptions:
            if sub.id_number == id_number:
                return sub
        return None

    def remove_subscription(self, id_number: str):
        """حذف اشتراك باستخدام رقم المعرف."""
        subscription = self.find_subscription_by_id(id_number)
        if subscription:
            self.subscriptions.remove(subscription)
            print(f"🗑️ Subscription '{id_number}' removed successfully.")
            return True
        return False

    def calculate_total_income(self):
        """حساب مجموع الدخل الكلي من جميع الاشتراكات."""
        return sum(sub.amount for sub in self.subscriptions)
