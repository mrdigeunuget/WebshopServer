from sqlalchemy import Table, Column, Integer, ForeignKey, VARCHAR, Float
from sqlalchemy.orm import relationship, backref
from database.db_model import DBModel


class Gebruikers(DBModel):

    __tablename__ = "gebruikers"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    voornaam = Column(VARCHAR(40), nullable=False)
    achternaam = Column(VARCHAR(40), nullable=False)
    email = Column(VARCHAR(40), nullable=False)
    wachtwoord = Column(VARCHAR(513), nullable=False)
    straatnaam = Column(VARCHAR(40), nullable=False)
    huisnummer = Column(VARCHAR(10), nullable=False)
    postcode = Column(VARCHAR(10), nullable=False)
    admin = Column(Integer, nullable=False, default=2)

    def to_dict(self, full=False):
        if (full):
            return dict(
                id=self.id,
                admin=self.admin,
            )
        else:
            return dict(
                id=self.id,
                voornaam=self.voornaam,
                achternaam=self.achternaam,
                email=self.email,
                straatnaam=self.straatnaam,
                wachtwoord=self.wachtwoord,
                huisnummer=self.huisnummer,
                postcode=self.postcode,
                admin=self.admin
            )

class Kleur(DBModel):

    __tablename__ = "kleur"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    kleur = Column(VARCHAR(20), nullable=False, index=True)

    def to_dict(self, full=True):
        return dict(
            id=self.id,
            kleur=self.kleur,
        )


class Maat(DBModel):

    __tablename__ = "Maat"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    maat = Column(VARCHAR(10), nullable=False, index=True)

    def to_dict(self, full=True):
        return dict(
            id=self.id,
            maat=self.maat,
        )

class Categorie(DBModel):

    __tablename__ = "categorie"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    categorie = Column(VARCHAR(25), nullable=False, unique=True)

    def to_dict(self, full=True):
        return dict(
            id=self.id,
            categorie=self.categorie,
        )

class Product(DBModel):

    __tablename__ = "product"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    naam = Column(VARCHAR(40), nullable=False)
    categorie = Column(ForeignKey(Categorie.categorie), nullable=False)
    subcategorie = Column(VARCHAR(40), nullable=True)
    maat = Column(ForeignKey(Maat.maat), nullable=False)
    kleur = Column(ForeignKey(Kleur.kleur), nullable=False)
    prijs = Column(Float, nullable=False)
    voorraad = Column(Integer, nullable=False)
    body = Column(VARCHAR(100), nullable=False)
    imagePath = Column(VARCHAR(50), nullable=False)
    manufacturer = Column(VARCHAR(50), nullable=False)
    model = Column(VARCHAR(15), nullable=False)

    def to_dict(self, full=True):
        return dict(
            id = self.id,
            naam = self.naam,
            categorie = self.categorie,
            subcategorie = self.subcategorie,
            maat = self.maat,
            kleur = self.kleur,
            prijs = self.prijs,
            voorraad = self.voorraad,
            body = self.body,
            imagePath = self.imagePath,
            manufacturer = self.manufacturer,
            model = self.model,
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

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    gebruikers_id = Column(ForeignKey(Gebruikers.id), nullable=False)
    prijs = Column(Float)
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
            bestelling_id=self.bestelling_id,
            product_id=self.product_id,
            hoeveelheid=self.hoeveelheid
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


