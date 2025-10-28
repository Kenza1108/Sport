class Subscription():
    def __init__(
        self,
        id_number: int= 1,
        amount: float= 0,
        date: str="",
        status: str="",
    ):
        self.id_number=id_number
        self.amount=amount
        self.date=date
        self.status=status
    def display_html_row(self):
        return f"<tr><td>{self.id_number}</td><td>{self.amount}</td><td>{self.date}</td>" \
               f"<td>{self.status}</td></tr>"

        