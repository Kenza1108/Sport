# managers/sportclub_facade.py

from managers.member_repository import MemberRepository
from managers.EventManager import EventRepository
from managers.FinanceManager import SubscriptionRepository

from proxies.member_proxy import MemberRepositoryProxy
from proxies.event_proxy import EventRepositoryProxy
from proxies.subscription_proxy import SubscriptionRepositoryProxy

from models.FileStorage import FileStorage
from models.members import Member
from models.events import Event
from models.subscription import Subscription

class SportClubFacade:
    _instance = None

    def __new__(cls, user_role="user"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, user_role="user"):
        # --- Repositories réels ---
        real_members_repo = MemberRepository()
        real_events_repo = EventRepository()
        real_subs_repo = SubscriptionRepository()

        # --- Proxies avec rôle utilisateur ---
        self.members_repo = MemberRepositoryProxy(real_members_repo, user_role)
        self.events_repo = EventRepositoryProxy(real_events_repo, user_role)
        self.subs_repo = SubscriptionRepositoryProxy(real_subs_repo, user_role)

        # --- Stockage CSV ---
        self.members_storage = FileStorage("data/members.csv")
        self.events_storage = FileStorage("data/events.csv")
        self.subs_storage = FileStorage("data/subscriptions.csv")

        self.load_all_data()

    # --- Chargement & Sauvegarde ---
    def load_all_data(self):
        for row in self.members_storage.load_dict_list():
            self.members_repo.add(Member(**row))
        for row in self.events_storage.load_dict_list():
            self.events_repo.add(Event(**row))
        for row in self.subs_storage.load_dict_list():
            self.subs_repo.add(Subscription(**row))

    def save_all_data(self):
        self.members_storage.save_dict_list(
            [m.to_dict() for m in self.members_repo.get_all()],
            fieldnames=Member.fields()
        )
        self.events_storage.save_dict_list(
            [e.to_dict() for e in self.events_repo.get_all()],
            fieldnames=Event.fields()
        )
        self.subs_storage.save_dict_list(
            [s.to_dict() for s in self.subs_repo.get_all()],
            fieldnames=Subscription.fields()
        )
        print("✅ All data saved successfully.")

    # --- Members ---
    def add_member(self, member_data: dict):
        full_name = f"{member_data.get('first_name', '')} {member_data.get('last_name', '')}".strip()
        data = {
            "full_name": full_name,
            "email": member_data.get("email", ""),
            "phone": member_data.get("phone", ""),
            "address": member_data.get("address", ""),
            "skills": member_data.get("skills", ""),
            "interests": member_data.get("interests", ""),
            "subscription_status": member_data.get("subscription_status", "")
        }
        member = Member(**data)
        self.members_repo.add(member)
        self.save_all_data()

    def get_members(self):
        return self.members_repo.get_all()

    def delete_member(self, email):
        # استخدم دالة delete من Proxy
        success = self.members_repo.delete(email)
        if success:
            self.save_all_data()
            return True
        return False

    # --- Events ---
    def add_event(self, event_data: dict):
        event = Event(**event_data)
        self.events_repo.add(event)
        self.save_all_data()

    def get_events(self):
        return self.events_repo.get_all()

    def delete_event(self, event_name):
        success = self.events_repo.delete(event_name)
        if success:
            self.save_all_data()
            return True
        return False

    # --- Subscriptions ---
    def add_subscription(self, sub_data: dict):
        sub = Subscription(**sub_data)
        self.subs_repo.add(sub)
        self.save_all_data()

    def get_subscriptions(self):
        return self.subs_repo.get_all()

    def delete_subscription(self, sub_id):
        success = self.subs_repo.delete(sub_id)
        if success:
            self.save_all_data()
            return True
        return False
