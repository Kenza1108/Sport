from interfaces.subscription_interface import SubscriptionInterface

# --- Base Class ---
class Subscription(SubscriptionInterface):
    def __init__(self, id_number, amount, date, status):
        self.id_number = id_number
        self.amount = amount
        self.date = date
        self.status = status
        
    def to_dict(self):
        return {
            "id_number": self.id_number,
            "amount": self.amount,
            "date": self.date,
            "status": self.status
        }
    
    def display_html_row(self):
        return f"<tr><td>{self.id_number}</td><td>{self.amount}</td><td>{self.date}</td><td>{self.status}</td></tr>"

    def process_payment(self):
        print(f"Processing payment of {self.amount} for subscription {self.id_number}")
        self.status = "paid"

# --- Subclasses ---
class Donation(Subscription):
    def __init__(self, id_number, amount, date, donor_name):
        super().__init__(id_number, amount, date, "donation")
        self.donor_name = donor_name

    def display_html_row(self):
        return super().display_html_row()[:-5] + f"<td>{self.donor_name}</td></tr>"

    def process_payment(self):
        print(f"Processing donation of {self.amount} from {self.donor_name}")
        self.status = "donated"

class MonthlySubscription(Subscription):
    def __init__(self, id_number, amount, date, month):
        super().__init__(id_number, amount, date, "monthly")
        self.month = month

    def display_html_row(self):
        return super().display_html_row()[:-5] + f"<td>{self.month}</td></tr>"

class AnnualSubscription(Subscription):
    def __init__(self, id_number, amount, date, year):
        super().__init__(id_number, amount, date, "annual")
        self.year = year

    def display_html_row(self):
        return super().display_html_row()[:-5] + f"<td>{self.year}</td></tr>"
