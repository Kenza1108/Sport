from fastapi import APIRouter, HTTPException
from managers.sportclub_facade import SportClubFacade

router = APIRouter()

# ----------------- Initialize Facade -----------------
club = SportClubFacade(user_role="admin")  

# ----------------- Members API -----------------
@router.get("/members")
def get_members():
    return [m.to_dict() for m in club.get_members()]

@router.post("/members")
def add_member(member: dict):
    club.add_member(member)
    return {"message": "✅ Member added successfully!"}

@router.delete("/members/{email}")
def delete_member(email: str):
    if not club.delete_member(email):
        raise HTTPException(status_code=404, detail="Member not found")
    return {"message": "Member deleted"}

# ----------------- Events API -----------------
@router.get("/events")
def get_events():
    return [e.to_dict() for e in club.get_events()]

@router.post("/events")
def add_event(event: dict):
    if club.events_repo.real_repo.find_event_by_name(event.get("event_name")):
        raise HTTPException(status_code=400, detail="Event already exists")
    club.add_event(event)
    return {"message": "✅ Event added successfully!"}

@router.delete("/events/{event_name}")
def delete_event(event_name: str):
    if not club.delete_event(event_name):
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted"}

# ----------------- Subscriptions API -----------------
@router.get("/subscriptions")
def get_subscriptions():
    return [s.to_dict() for s in club.get_subscriptions()]

@router.post("/subscriptions")
def add_subscription(sub: dict):
    club.add_subscription(sub)
    return {"message": "✅ Subscription added successfully!"}

@router.delete("/subscriptions/{sub_id}")
def delete_subscription(sub_id: str):
    if not club.delete_subscription(sub_id):
        raise HTTPException(status_code=404, detail="Subscription not found")
    return {"message": "Subscription deleted"}
