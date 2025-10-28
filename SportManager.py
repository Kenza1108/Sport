import csv
from members import Members
from events import Events
from subscription import Subscription

class SportClub:
    def __init__(self, sport_file):
        self.sport_file = sport_file
        self.sport_file = sport_file
        self.members = []          
        self.events = []           
        self.subscriptions = [] 
        

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

                self.events.append(event)
                self.members.append(member)
                self.subscriptions.append(subscription)

    # Méthode pour générer le HTML
    def generate_html(self):
        html = ["<html><head><meta charset='utf-8'></head><body>"]
        html.append("<h1>Sport Club</h1>")

        html.append("<h2>Members</h2><table border='1'>")
        for m in self.members:
            html.append(m.display_html_row())
        html.append("</table>")

        html.append("<h2>Events</h2><table border='1'>")
        for e in self.events:
            html.append(e.display_html_row())
        html.append("</table>")

        html.append("<h2>Subscriptions</h2><table border='1'>")
        for s in self.subscriptions:
            html.append(s.display_html_row())
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
