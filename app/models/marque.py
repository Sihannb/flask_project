class Marque:
    __tablename__ = "marques"

    def __init__(self, nom, vues=0, likes=0, id=None):
        self.id = id
        self.nom = nom
        self.vues = vues or 0
        self.likes = likes or 0

    @property
    def taux(self):
        vues = self.vues or 0
        likes = self.likes or 0
        return (likes / vues * 100) if vues > 0 else 0

    def to_dict(self):
        return {
    "nom": self.nom,
    "vues": self.vues,
    "score": self.likes,
    "taux": self.taux
}

# 🔹 Convertir un dict Supabase → objet Marque
    @staticmethod
    def from_dict(data: dict):
        return Marque(
    id=data.get("id"),
    nom=data.get("nom"),
    vues=data.get("vues", 0),
    likes=data.get("likes", 0)
)