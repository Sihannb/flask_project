class Marque:
    def __init__(self, nom, vues=0, likes=0):
        self.nom = nom
        self.vues = vues or 0    # ← si None, remplace par 0
        self.likes = likes or 0  # ← si None, remplace par 0

    @property
    def taux(self):
        return (self.likes / self.vues * 100) if self.vues > 0 else 0

    def to_dict(self):
        return {
            "nom": self.nom,
            "vues": self.vues,
            "score": self.likes,
            "taux": self.taux
        }