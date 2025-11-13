# managers/member_repository.py
from models.members import Member

class MemberRepository:
    def __init__(self):
        # Initialize the members list
        self.members = []

    def add_member(self, member: Member):
        """Add a new member only if not already exists"""
        if any(m.email == member.email for m in self.members):
            print(f"⚠️ Member '{member.full_name}' already exists.")
            return
        self.members.append(member)
        print(f"✅ Member '{member.full_name}' added successfully.")

    def get_all_members(self):
        """Return all members"""
        return self.members

    def find_member_by_email(self, email: str):
        """Find a member by email"""
        for m in self.members:
            if m.email == email:
                return m
        return None

    def remove_member(self, email: str):
        """Remove a member by email"""
        member = self.find_member_by_email(email)
        if member:
            self.members.remove(member)
            print(f"🗑️ Member '{email}' removed.")
            return True
        return False
