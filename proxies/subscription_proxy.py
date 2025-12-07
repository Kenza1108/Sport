# proxies/subscription_proxy.py
class SubscriptionRepositoryProxy:
    def __init__(self, repo, user_role="user"):
        self._repo = repo
        self.user_role = user_role

    def add(self, item):
        print(f"[SUBSCRIPTION LOG] Adding subscription: {item.id_number}")
        if self.user_role != "admin":
            print("⚠️ Permission denied: only admin can add subscriptions")
            return
        self._repo.add(item)

    def get_all(self):
        return self._repo.get_all()

    def delete(self, id_number):
        if self.user_role != "admin":
            print("⚠️ Permission denied: only admin can delete subscriptions")
            return False
        return self._repo.delete(id_number)
