from models.members import Member
from interfaces.repository_interface import RepositoryInterface

class MemberRepository(RepositoryInterface):
    def __init__(self):
        self.members = []

    # ---------------------------------------------
    # CREATE
    # ---------------------------------------------
    def add(self, member: Member):
        if any(m.email == member.email for m in self.members):
            print(f"⚠️ Member '{member.full_name}' already exists.")
            return False
        self.members.append(member)
        print(f"✅ Member '{member.full_name}' added successfully.")
        return True

    # ---------------------------------------------
    # READ
    # ---------------------------------------------
    def get_all(self):
        return self.members

    def find_by_email(self, email: str):
        for m in self.members:
            if m.email == email:
                return m
        return None

    # Alias لتوافق مع الـ Proxy/Facade
    find_member_by_email = find_by_email

    # ---------------------------------------------
    # UPDATE
    # ---------------------------------------------
    def update(self, email: str, new_member: Member):
        for i, m in enumerate(self.members):
            if m.email == email:
                self.members[i] = new_member
                print(f"🔄 Member '{email}' updated.")
                return True
        print(f"⚠️ Member '{email}' not found for update.")
        return False

    # ---------------------------------------------
    # DELETE
    # ---------------------------------------------
    def delete(self, email: str):
        for m in self.members:
            if m.email == email:
                self.members.remove(m)
                print(f"🗑️ Member '{email}' removed.")
                return True
        print(f"⚠️ Member '{email}' not found for deletion.")
        return False
