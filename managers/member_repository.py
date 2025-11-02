from models.members import Member

class MemberRepository:
    def __init__(self):
        self.members = []

    def add_member(self, full_name, email, phone, address, skills, interests, subscription_status):
        new_member = Member(full_name, email, phone, address, skills, interests, subscription_status)
        self.members.append(new_member)
        print(f"✅ Member '{full_name}' added successfully.")

    def get_all_members(self):
        return self.members
