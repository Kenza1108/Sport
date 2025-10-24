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