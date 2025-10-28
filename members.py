class Members():
    def __init__(
        self,
        full_name: str="",
        email: str="",
        phone: int= 1,
        address: str="",
        skills: str="",
        interests: str="",
        subscription_status: str="",
    ):
        self.full_name=full_name
        self.email=email
        self.phone=phone
        self.address=address
        self.skills=skills
        self.interests=interests
        self.subscription_status=subscription_status
    def display_html_row(self):
        return f"<tr><td>{self.full_name}</td><td>{self.email}</td><td>{self.phone}</td>" \
               f"<td>{self.address}</td><td>{self.skills}</td><td>{self.interests}</td>" \
               f"<td>{self.subscription_status}</td></tr>"