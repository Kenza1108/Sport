class Events():
    def __init__(
        self,
        event_name: str="",
        description: str="",
        event_date: str="",
        organizer: str="",
        participants: str="",
    ):
        self.event_name=event_name
        self.description=description
        self.event_date=event_date
        self.organizer=organizer
        self.participants=participants
    def display_info(self):
        return (
            f"{self.event_name} | {self.description} | {self.event_date} | "
            f"{self.organizer} | {self.participants}"
    )

        