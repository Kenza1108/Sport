import csv
from models.members import Member
from models.events import Event
from models.subscription import Subscription
from managers.member_repository import MemberRepository
from managers.EventManager import EventRepository
from managers.FinanceManager import SubscriptionRepository
from models.FileStorage import FileStorage

class SportClub:
    def __init__(self, members_file, events_file, subscriptions_file):
        self.members = MemberRepository()
        self.events = EventRepository()
        self.subscriptions = SubscriptionRepository()
        self.members_storage = FileStorage(members_file)
        self.events_storage = FileStorage(events_file)
        self.subscriptions_storage = FileStorage(subscriptions_file)

    # --- Load data from CSV files ---
    def load_data(self):
        # Load Members
        for row in self.members_storage.load_dict_list():
            self.members.add_member(
                full_name=row['full_name'],
                email=row['email'],
                phone=int(row['phone']),
                address=row['address'],
                skills=row['skills'],
                interests=row['interests'],
                subscription_status=row['subscription_status'],
            )
        
        # Load Events
        for row in self.events_storage.load_dict_list():
            self.events.add_event(
                event_name=row['event_name'],
                description=row['description'],
                event_date=row['event_date'],
                organizer=row['organizer'],
                participants=row['participants'],
            )
        
        # Load Subscriptions
        for row in self.subscriptions_storage.load_dict_list():
            self.subscriptions.add_subscription(
                id_number=row['id_number'],
                amount=float(row['amount']),
                date=row['date'],
                status=row['status'],
            )

    # --- Save data to CSV files ---
    def save_data(self):
        # Save Members
        members_list = [m.to_dict() for m in self.members.get_all_members()]
        self.members_storage.save_dict_list(members_list, fieldnames=[
            "full_name", "email", "phone", "address", "skills", "interests", "subscription_status"
        ])
        
        # Save Events
        events_list = [e.to_dict() for e in self.events.get_all_events()]
        self.events_storage.save_dict_list(events_list, fieldnames=[
            "event_name", "description", "event_date", "organizer", "participants"
        ])
        
        # Save Subscriptions
        subscriptions_list = [s.to_dict() for s in self.subscriptions.get_all_subscriptions()]
        self.subscriptions_storage.save_dict_list(subscriptions_list, fieldnames=[
            "id_number", "amount", "date", "status"
        ])
        
        print("✅ All data saved successfully.")

    # --- Generate HTML with headers ---
    def generate_html(self):
        html = ["<html><head><meta charset='utf-8'></head><body>"]
        html.append("<h1>🏆 Sport Club</h1>")

        # Members
        members = self.members.get_all_members()
        if members:
            html.append("<h2>Members</h2><table border='1'>")
            headers = members[0].to_dict().keys()
            html.append("<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>")
            for m in members:
                html.append(m.display_html_row())
            html.append("</table>")

        # Events
        events = self.events.get_all_events()
        if events:
            html.append("<h2>Events</h2><table border='1'>")
            headers = events[0].to_dict().keys()
            html.append("<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>")
            for e in events:
                html.append(e.display_html_row())
            html.append("</table>")

        # Subscriptions
        subs = self.subscriptions.get_all_subscriptions()
        if subs:
            html.append("<h2>Subscriptions</h2><table border='1'>")
            headers = subs[0].to_dict().keys()
            html.append("<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>")
            for s in subs:
                html.append(s.display_html_row())
            html.append("</table>")

        html.append("</body></html>")
        return "\n".join(html)

    # --- Save HTML page ---
    def save_html(self, output_file="Sport.html"):
        html_content = self.generate_html()
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✅ HTML file generated: {output_file}")

# --- Main execution ---
if __name__ == "__main__":
    club = SportClub("members.csv", "events.csv", "subscriptions.csv")

    # Example: Add a new member
    club.members.add_member(
        full_name="Ali Ahmed",
        email="ali@example.com",
        phone=123456789,
        address="Algiers, Algeria",
        skills="Tennis, Swimming",
        interests="Fitness, Running",
        subscription_status="paid"
    )

    # Load existing CSV data
    club.load_data()

    # Generate HTML file
    club.save_html()

    # Save updated CSV data
    club.save_data()
