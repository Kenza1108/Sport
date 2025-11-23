# controllers/sportclub_controller.py
from fastapi import APIRouter, HTTPException
from models.members import Member
from models.events import Event
from models.subscription import Subscription
from managers.member_repository import MemberRepository
from managers.EventManager import EventRepository
from managers.FinanceManager import SubscriptionRepository
from models.FileStorage import FileStorage
from factories.event_factory import EventFactory

router = APIRouter()

# ----------------- Singleton Controller -----------------
class SportClubController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SportClubController, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Repositories
        self.members_repo = MemberRepository()
        self.events_repo = EventRepository()
        self.subs_repo = SubscriptionRepository()

        # File storages
        self.members_storage = FileStorage("data/members.csv")
        self.events_storage = FileStorage("data/events.csv")
        self.subs_storage = FileStorage("data/subscriptions.csv")

    # ----------------- Load & Save Data -----------------
    def load_data(self):
        # Members
        for row in self.members_storage.load_dict_list():
            self.members_repo.add_member(Member(**row))
        # Events
        for row in self.events_storage.load_dict_list():
            self.events_repo.add_event(Event(**row))
        # Subscriptions
        for row in self.subs_storage.load_dict_list():
            self.subs_repo.add_subscription(Subscription(**row))

    def save_data(self):
        # Members
        self.members_storage.save_dict_list(
            [m.to_dict() for m in self.members_repo.get_all_members()],
            fieldnames=Member.fields()
        )
        # Events
        self.events_storage.save_dict_list(
            [e.to_dict() for e in self.events_repo.get_all_events()],
            fieldnames=Event.fields()
        )
        # Subscriptions
        self.subs_storage.save_dict_list(
            [s.to_dict() for s in self.subs_repo.get_all_subscriptions()],
            fieldnames=Subscription.fields()
        )
        print("✅ All data saved successfully.")

# ----------------- Initialize Singleton Controller -----------------
club = SportClubController()
club.load_data()

# ----------------- Members API -----------------
@router.get("/members")
def get_members():
    return [m.to_dict() for m in club.members_repo.get_all_members()]

@router.post("/members")
def add_member(member: dict):
    new_member = Member(**member)
    club.members_repo.add_member(new_member)
    club.save_data()
    return {"message": "✅ Member added successfully!"}

@router.delete("/members/{email}")
def delete_member(email: str):
    success = club.members_repo.remove_member(email)
    if not success:
        raise HTTPException(status_code=404, detail="Member not found")
    club.save_data()
    return {"message": "Member deleted"}

# ----------------- Events API -----------------
@router.get("/events")
def get_events():
    return [e.to_dict() for e in club.events_repo.get_all_events()]

@router.post("/events")
def add_event(event: dict):
    if club.events_repo.find_event_by_name(event.get("event_name")):
        raise HTTPException(status_code=400, detail="Event already exists")
    # Use Factory to create event
    new_event = EventFactory.create_event(event.get("event_type"), **event)
    club.events_repo.add_event(new_event)
    club.save_data()
    return {"message": "✅ Event added successfully!"}

@router.delete("/events/{event_name}")
def delete_event(event_name: str):
    success = club.events_repo.remove_event(event_name)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    club.save_data()
    return {"message": "Event deleted"}

# ----------------- Subscriptions API -----------------
@router.get("/subscriptions")
def get_subscriptions():
    return [s.to_dict() for s in club.subs_repo.get_all_subscriptions()]

@router.post("/subscriptions")
def add_subscription(sub: dict):
    new_sub = Subscription(**sub)
    club.subs_repo.add_subscription(new_sub)
    club.save_data()
    return {"message": "✅ Subscription added successfully!"}

@router.delete("/subscriptions/{sub_id}")
def delete_subscription(sub_id: str):
    success = club.subs_repo.remove_subscription(sub_id)
    if not success:
        raise HTTPException(status_code=404, detail="Subscription not found")
    club.save_data()
    return {"message": "Subscription deleted"}
