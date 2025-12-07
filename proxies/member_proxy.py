class MemberRepositoryProxy:
    def __init__(self, repo, user_role="user"):
        self._repo = repo
        self.user_role = user_role

    def add(self, item):
        print(f"[MEMBER LOG] Adding member: {item.full_name}")
        if self.user_role != "admin":
            print("⚠️ Permission denied: only admin can add members")
            return False
        return self._repo.add(item)

    def get_all(self):
        return self._repo.get_all()

    def find_member_by_email(self, email):
        return self._repo.find_member_by_email(email)

    def delete(self, email):
        if self.user_role != "admin":
            print("⚠️ Permission denied: only admin can delete members")
            return False
        return self._repo.delete(email)

    def update(self, email, new_member):
        if self.user_role != "admin":
            print("⚠️ Permission denied: only admin can update members")
            return False
        return self._repo.update(email, new_member)
