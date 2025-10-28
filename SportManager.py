import csv
from members import Members
from events import Events
from subscription import Subscription

class SportClub:
    def __init__(self, sport_file):
        self.sport_file = sport_file
        self.data = {
            "Members": [],
            "Events": [],
            "Subscriptions": [],
        }

    # Méthode pour lire le CSV et créer les objets
    def load_data(self):
        with open(self.sport_file, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter="\t")

            for row in reader:
                event = Events(
                    event_name=row['event_name'],
                    description=row['description'],
                    event_date=row['event_date'],
                    organizer=row['organizer'],
                    participants=row['participants'],
                )

                member = Members(
                    full_name=row['full_name'],
                    email=row['email'],
                    phone=int(row['phone']),
                    address=row['address'],
                    skills=row['skills'],
                    interests=row['interests'],
                    subscription_status=row['subscription_status'],
                )

                subscription = Subscription(
                    id_number=row['id_number'],
                    amount=float(row['amount']),
                    date=row['date'],
                    status=row['status'],
                )

                self.data["Events"].append(event)
                self.data["Members"].append(member)
                self.data["Subscriptions"].append(subscription)

    # Méthode pour générer le HTML
    def generate_html(self):
        html = ['<html><head><meta charset="utf-8"></head><body>']
        html.append("<center><h1>Sport Club</h1></center>")

        # --- Members Section ---
        html.append("<h2>Members</h2>")
        html.append("<table border='2' cellspacing='0' cellpadding='5'>")
        html.append(
            "<tr><th>Full Name</th><th>Email</th><th>Phone</th>"
            "<th>Address</th><th>Skills</th><th>Interests</th>"
            "<th>Subscription Status</th></tr>"
        )
        for m in self.data["Members"]:
            html.append(f"<tr><td>{m.full_name}</td><td>{m.email}</td>"
                        f"<td>{m.phone}</td><td>{m.address}</td>"
                        f"<td>{m.skills}</td><td>{m.interests}</td>"
                        f"<td>{m.subscription_status}</td></tr>")
        html.append("</table>")

        # --- Events Section ---
        html.append("<h2>Events</h2>")
        html.append("<table border='2' cellspacing='0' cellpadding='5'>")
        html.append(
            "<tr><th>Event Name</th><th>Description</th><th>Event Date</th>"
            "<th>Organizer</th><th>Participants</th></tr>"
        )
        for e in self.data["Events"]:
            html.append(f"<tr><td>{e.event_name}</td><td>{e.description}</td>"
                        f"<td>{e.event_date}</td><td>{e.organizer}</td>"
                        f"<td>{e.participants}</td></tr>")
        html.append("</table>")

        # --- Subscriptions Section ---
        html.append("<h2>Subscriptions</h2>")
        html.append("<table border='2' cellspacing='0' cellpadding='5'>")
        html.append("<tr><th>ID Number</th><th>Amount</th><th>Date</th><th>Status</th></tr>")
        for s in self.data["Subscriptions"]:
            html.append(f"<tr><td>{s.id_number}</td><td>{s.amount}</td>"
                        f"<td>{s.date}</td><td>{s.status}</td></tr>")
        html.append("</table>")
        html.append("</body></html>")

        return "\n".join(html)

    #  Méthode pour sauvegarder le HTML
    def save_html(self, output_file="Sport.html"):
        html_content = self.generate_html()
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✅ HTML file generated: {output_file}")


if __name__ == "__main__":
    club = SportClub("Sport.csv")
    club.load_data()
    club.save_html()
