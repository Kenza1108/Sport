# proxies/event_proxy.py
class EventRepositoryProxy:
    def __init__(self, repo, user_role="user"):
        self._repo = repo
        self.user_role = user_role
        self.real_repo = repo  # for checking existence

    def add(self, item):
        print(f"[EVENT LOG] Adding event: {item.event_name}")
        if self.user_role != "admin":
            print("⚠️ Permission denied: only admin can add events")
            return
        self._repo.add(item)

    def get_all(self):
        return self._repo.get_all()

    def delete(self, event_name):
        if self.user_role != "admin":
            print("⚠️ Permission denied: only admin can delete events")
            return False
        return self._repo.delete(event_name)
