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
    def display_info(self):
        return (
            f"{self.id_number} | {self.amoun} | {self.date} | {self.status} | "
    )

        