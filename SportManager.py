import csv
from members import Members
from events import Events
from subscription import Subscription

def csv_to_objects(sport_file):
    data={"Members": [],
          "Events":[],
          "Subscriptions":[],
          }
    with open(sport_file,encoding='utf-8') as f:
        reader=csv.DictReader(f, delimiter="\t")       

        for row in reader:
            events= Events(
                event_name=row['event_name'],
                description=row['description'],
                event_date=row['event_date'],
                organizer=row['organizer'],
                participants=row['participants'],
            )
            members= Members(
                full_name=row['full_name'],
                email=row['email'],
                phone=int(row['phone']),
                address=row['address'],
                skills=row['skills'],
                interests=row['interests'],
                subscription_status=row['subscription_status'],
            )
           
            subscriptions=Subscription(
                    id_number=row['id_number'],
                    amount=float(row['amount']),
                    date=row['date'],
                    status=row['status'], 
            )
            data["Members"].append(members)
            data["Events"].append(events)
            data["Subscriptions"].append(subscriptions)

    return data

def to_html_page(data):
    html=['<html><head><meta charset="utf-8"></head><body>']
    html.append("<center><h1>Sport Clube</h1></center>")
    html.append(f"<h2>Members</h2>")
    html.append("<table border='2' cellspacing='0' cellpadding='5'>")
    html.append("<tr><th>full_name</th><th>email</th><th>phone</th><th>address</th>"
    "<th>skills</th><th>interests</th><th>subscription_status</th></tr>")
    for member in data["Members"]:
        html.append("<tr>")
        html.append(f"<td>{member.full_name}</td>")
        html.append(f"<td>{member.email}</td>")
        html.append(f"<td>{member.phone}</td>")
        html.append(f"<td>{member.address}</td>")
        html.append(f"<td>{member.skills}</td>")
        html.append(f"<td>{member.interests}</td>")
        html.append(f"<td>{member.subscription_status}</td>") 
        html.append("</tr>")
    html.append("</table>")
    
    html.append(f"<h2>Events</h2>")
    html.append("<table border='2' cellspacing='0' cellpadding='5'>")
    html.append("<tr><th>event_name</th><th>description</th><th>event_date</th><th>organizer</th>"
    "<th>participants</th></tr>")
    for event in data["Events"]:
        html.append("<tr>")
        html.append(f"<td>{event.event_name}</td>")
        html.append(f"<td>{event.description}</td>")
        html.append(f"<td>{event.event_date}</td>")
        html.append(f"<td>{event.organizer}</td>")
        html.append(f"<td>{event.participants}</td>")
        html.append("</tr>")
    html.append("</table>")
    html.append(f"<h2>Subscriptions</h2>")
    html.append("<table border='2' cellspacing='0' cellpadding='5'>")
    html.append("<tr><th>id_number</th><th>amount</th><th>date</th><th>status</th></tr>")
    
    for subscription in data['Subscriptions']:  
        html.append("<tr>")  
        html.append(f"<td>{subscription.id_number}</td>")
        html.append(f"<td>{subscription.amount}</td>")
        html.append(f"<td>{subscription.date}</td>")
        html.append(f"<td>{subscription.status}</td>")
        html.append("</tr>")
    html.append("</table>")
    html.append("</body></html>")
    return"\n".join(html)


if __name__ == "__main__":
    sport_file="Sport.csv"
    result = csv_to_objects(sport_file)
    html_content=to_html_page(result)
    with open("Sport.html","w",encoding="utf-8") as f:
        f.write(html_content)
    print("✅ HTML file generated: Sport.html")
