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
        return (
            f"<tr>"
            f"<td>{self.id_number}</td>"
            f"<td>{self.amount}</td>"
            f"<td>{self.date}</td>"
            f"<td>{self.status}</td>"
            f"</tr>"
        )

    def process_payment(self):
        print(f"Processing payment of {self.amount} for subscription {self.id_number}")
        self.status = "paid"


# --- Subclass 1: Donation ---
class Donation(Subscription):
    def __init__(self, id_number, amount, date, donor_name):
        super().__init__(id_number, amount, date, "donation")
        self.donor_name = donor_name

    def to_dict(self):
        data = super().to_dict()
        data["donor_name"] = self.donor_name
        return data

    def display_html_row(self):
        return (
            f"<tr>"
            f"<td>{self.id_number}</td>"
            f"<td>{self.amount}</td>"
            f"<td>{self.date}</td>"
            f"<td>{self.status}</td>"
            f"<td>{self.donor_name}</td>"
            f"</tr>"
        )

    def process_payment(self):
        print(f"Processing donation of {self.amount} from {self.donor_name}")
        self.status = "donated"


# --- Subclass 2: Monthly Subscription ---
class MonthlySubscription(Subscription):
    def __init__(self, id_number, amount, date, month):
        super().__init__(id_number, amount, date, "monthly")
        self.month = month

    def to_dict(self):
        data = super().to_dict()
        data["month"] = self.month
        return data

    def display_html_row(self):
        return (
            f"<tr>"
            f"<td>{self.id_number}</td>"
            f"<td>{self.amount}</td>"
            f"<td>{self.date}</td>"
            f"<td>{self.status}</td>"
            f"<td>{self.month}</td>"
            f"</tr>"
        )


# --- Subclass 3: Annual Subscription ---
class AnnualSubscription(Subscription):
    def __init__(self, id_number, amount, date, year):
        super().__init__(id_number, amount, date, "annual")
        self.year = year

    def to_dict(self):
        data = super().to_dict()
        data["year"] = self.year
        return data

    def display_html_row(self):
        return (
            f"<tr>"
            f"<td>{self.id_number}</td>"
            f"<td>{self.amount}</td>"
            f"<td>{self.date}</td>"
            f"<td>{self.status}</td>"
            f"<td>{self.year}</td>"
            f"</tr>"
        )
