# models/members.py
from interfaces.member_interface import MemberInterface

class Member(MemberInterface):
    """Classe représentant un membre de l'association."""

    def __init__(
        self,
        full_name: str,
        email: str,
        phone: str,
        address: str,
        skills: str,
        interests: str,
        subscription_status: str,
    ):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        self.skills = skills
        self.interests = interests
        self.subscription_status = subscription_status

    # --- Méthodes implémentées de l'interface ---
    def to_dict(self) -> dict:
        """Retourne un dictionnaire représentant le membre."""
        return {
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "skills": self.skills,
            "interests": self.interests,
            "subscription_status": self.subscription_status
        }

    def display_html_row(self) -> str:
        """Retourne une ligne HTML représentant le membre."""
        return (
            f"<tr>"
            f"<td>{self.full_name}</td>"
            f"<td>{self.email}</td>"
            f"<td>{self.phone}</td>"
            f"<td>{self.address}</td>"
            f"<td>{self.skills}</td>"
            f"<td>{self.interests}</td>"
            f"<td>{self.subscription_status}</td>"
            f"</tr>"
        )

    def register_member(self):
        """Affiche un message de confirmation lors de l'inscription."""
        print(f"✅ Membre '{self.full_name}' enregistré avec succès.")
