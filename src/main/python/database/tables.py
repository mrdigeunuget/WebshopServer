from sqlalchemy import Table, Column, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship, backref
from database.db_model import DBModel


class Gebruikers(DBModel):

    __tablename__ = "gebruikers"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    voornaam = Column(VARCHAR(40), nullable=False)
    achternaam = Column(VARCHAR(40), nullable=False)
    email = Column(VARCHAR(40), nullable=False)
    straatnaam = Column(VARCHAR(40), nullable=False)
    huisnummer = Column(VARCHAR(10), nullable=False)
    postcode = Column(VARCHAR(10), nullable=False)

    def to_dict(self, full=True):
        return dict(
            id = self.id,
            voornaam = self.voornaam,
            email = self.email,
            straatnaam = self.straatnaam,
            huisnummer = self.huisnummer,
            postcode = self.postcode
        )

class Product(DBModel):

    __tablename__ = "product"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    naam = Column(VARCHAR(40), nullable=False)
    categorie = Column(VARCHAR(40), nullable=False)
    maat = Column(VARCHAR(5), nullable=False, index=True)
    kleur = Column(VARCHAR(15), nullable=False, index=True)
    prijs = Column(Integer, nullable=False)
    voorraad = Column(Integer, nullable=False)

    def to_dict(self, full=True):
        return dict(
            id = self.id,
            naam = self.naam,
            categorie = self.categorie,
            maat = self.maat,
            kleur = self.kleur,
            prijs = self.prijs,
            voorraad = self.voorraad
        )

class Winkelwagen(DBModel):

    __tablename__ = "winkelwagen"

    winkelwagen_id = Column(Integer, autoincrement=True, primary_key=True)
    gebruikers_id = Column(Integer, nullable=False, index=True)
    product_id = Column(ForeignKey(Product.id), nullable=False)
    hoeveelheid = Column(Integer, nullable=False)
    starttijd = Column(VARCHAR(20))

    def to_dict(self, full=True):
        return dict(
            winkelwagen_id = self.winkelwagen_id,
            gebruikers_id = self.gebruikers_id,
            product_id = self.product_id,
            hoeveelheid = self.hoeveelheid,
            starttijd = self.starttijd
        )


class Bestellingen(DBModel):

    __tablename__ = "bestellingen"

    id = Column(Integer, nullable=False, primary_key=True)
    gebruikers_id = Column(ForeignKey(Gebruikers.id), nullable=False)
    prijs = Column(Integer, nullable=False)
    aantal_artikelen = Column(Integer)
    datum = Column(VARCHAR(30))

    def to_dict(self, full=True):
        return dict(
            id=self.id,
            gebruikers_id=self.gebruikers_id,
            prijs=self.prijs,
            aantal_artikelen=self.aantal_artikelen,
            datum=self.datum
        )


class BestellingItems(DBModel):

    __tablename__ = "bestelling_items"

    bestellingItem_id = Column(Integer, autoincrement=True, primary_key=True)
    bestelling_id = Column(ForeignKey(Bestellingen.id), nullable=False)
    product_id = Column(ForeignKey(Product.id), nullable=False)
    hoeveelheid = Column(Integer, nullable=False)

    def to_dict(self, full=True):
        return dict(
            bestellingItem_id=self.bestellingItem_id,
            bestelling_id=self.bestelling_id,
            product_id=self.product_id,
            hoeveelheid=self.hoeveelheid
        )


class Kleur(DBModel):

    __tablename__ = "kleur"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    kleur = Column(ForeignKey(Product.kleur), nullable=False)

    def to_dict(self, full=True):
        return dict(
            id=self.id,
            kleur=self.kleur,
        )


class Maat(DBModel):

    __tablename__ = "Maat"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    maat = Column(ForeignKey(Product.maat), nullable=False)

    def to_dict(self, full=True):
        return dict(
            id=self.id,
            maat=self.maat,
        )



class Favoriet(DBModel):

    __tablename__ = "favoriet"

    id = Column(Integer, autoincrement=True, primary_key=True)
    product_id = Column(ForeignKey(Product.id), nullable=False)
    gebruikers_id = Column(Integer, nullable=False)

    def to_dict(self, full=True):
        return dict(
            id=self.id,
            product_id=self.product_id,
            gebruikers_id=self.gebruikers_id,

        )


