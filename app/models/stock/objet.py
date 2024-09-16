from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from app.database import Base


class Objet(Base):
    __tablename__ = "objet"

    # Identifiant unique de l'objet
    codobj = Column(Integer, primary_key=True, index=True)

    # Nom ou description de l'objet
    libobj = Column(String(50), nullable=True)

    # Taille de l'objet
    tailleobj = Column(String(50), nullable=True)

    # Prix unitaire de l'objet
    puobj = Column(Numeric(precision=10, scale=4), default=0.0000)

    # Poids de l'objet
    poidsobj = Column(Numeric(precision=10, scale=4), default=0.0000)

    # Disponibilité de l'objet
    indispobj = Column(Integer, default=0)

    # Divers attributs spécifiques à l'objet
    o_imp = Column(Integer, default=0)
    o_aff = Column(Integer, default=0)
    o_cartp = Column(Integer, default=0)
    points = Column(Integer, default=0)
    o_ordre_aff = Column(Integer, default=0)

    # Relation avec la table ObjetCond (assurez-vous que ObjetCond est défini ailleurs)
    condit = relationship("ObjetCond", back_populates='objets')

    def __repr__(self):
        return f"<Objet(codobj={self.codobj}, libobj={self.libobj}, tailleobj={self.tailleobj}, puobj={self.puobj}, poidsobj={self.poidsobj})>"
