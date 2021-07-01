from datetime import datetime, date
import click

from database.db_model import DBModel
from database.tables import Gebruikers, Product, Winkelwagen, Bestellingen, BestellingItems, Maat, Kleur, Favoriet, Categorie



def gebruikers_data(app):
    click.echo("Adding gebruikers")
    app.session.add(
        Gebruikers(
            voornaam="Jan",
            achternaam="Janssen",
            email="Janjanssen@gmail.com",
            wachtwoord="Wachtwoord",
            straatnaam="Mudaheerd",
            huisnummer="73",
            postcode="9737XB",
        )
    )
    app.session.add(
        Gebruikers(
            voornaam="Test",
            achternaam="Admin",
            email="admin@gmail.com",
            wachtwoord="admin",
            straatnaam="Mudaheerd",
            huisnummer="73",
            postcode="9737XB",
            admin = 1,
        )
    )
    app.session.add(
        Gebruikers(
            voornaam="Henk",
            achternaam="Henksen",
            email="Henkhenksen@gmail.com",
            wachtwoord="wachtwoord",
            straatnaam="Framaheerd",
            huisnummer="4",
            postcode="9737NL",
        )
    )
    app.session.flush()
    app.session.commit()

def product_data(app):
    click.echo("Adding producten")
    app.session.add(
        Product(
            naam="T-Shirt basic",
            categorie="Men",
            subcategorie="Shirts",
            maat="S",
            kleur="Red",
            prijs="19.95",
            voorraad="4",
            imagePath="assets/images/men_t-shirt_basic.png",
            body="Dit is een basic t-shirt voor heren",
            manufacturer="company name",
            model= "Tx17",
        )
    )
    app.session.add(
        Product(
            naam="T-Shirt print",
            categorie="Men",
            subcategorie="Shirts",
            maat="L",
            kleur="White",
            prijs="19.95",
            voorraad="4",
            imagePath="assets/images/men_t-shirt_print.png",
            body="Dit is een print t-shirt voor heren",
            manufacturer="company name",
            model="Tx17",
        )
    )
    app.session.add(
        Product(
            naam="T-Shirt basic",
            categorie="Woman",
            subcategorie="Shirts",
            maat="M",
            kleur="Grey",
            prijs="19.95",
            voorraad="3",
            imagePath="assets/images/woman_t-shirt_basic.png",
            body="Dit is een blauwe basic t-shirt voor dames",
            manufacturer="company name",
            model="Tx17",
        )
    )
    app.session.add(
        Product(
            naam="T-Shirt basic",
            categorie="Kids",
            subcategorie="Shirts",
            maat="S",
            kleur="Green",
            prijs="15.95",
            voorraad="0",
            imagePath="assets/images/men_t-shirt_basic.png",
            body="Dit is een basic t-shirt voor kinderen",
            manufacturer="company name",
            model="Tx17",
        )
    )
    app.session.add(
        Product(
            naam="T-Shirt basic",
            categorie="Men",
            subcategorie="Shirts",
            maat="S",
            kleur="White",
            prijs="19.95",
            voorraad="4",
            imagePath="assets/images/men_t-shirt_basic.png",
            body="Dit is een witte basic t-shirt maat s voor heren",
            manufacturer="company name",
            model="Tx17",
        )
    )
    app.session.add(
        Product(
            naam="T-Shirt basic",
            categorie="Men",
            subcategorie="Shirts",
            maat="M",
            kleur="White",
            prijs="19.95",
            voorraad="4",
            imagePath="assets/images/men_t-shirt_basic.png",
            body="Dit is een witte basic t-shirt maat m voor heren",
            manufacturer="company name",
            model="Tx17",
        )
    )
    app.session.add(
        Product(
            naam="Sweater basic",
            categorie="Men",
            subcategorie="Sweaters",
            maat="S",
            kleur="Grey",
            prijs="29.95",
            voorraad="10",
            imagePath="assets/images/men_sweater_basic.png",
            body="Dit is een grijze basic sweater maat S voor heren",
            manufacturer="company name",
            model="Tx17",
        )
    )
    app.session.add(
        Product(
            naam="Sweater basic",
            categorie="Men",
            subcategorie="Sweaters",
            maat="L",
            kleur="Red",
            prijs="34.95",
            voorraad="7",
            imagePath="assets/images/men_sweater_basic.png",
            body="Dit is een rode basic sweater maat L voor heren",
            manufacturer="company name",
            model="Tx17",
        )
    )
    app.session.add(
        Product(
            naam="basic dress",
            categorie="Woman",
            subcategorie="Dresses",
            maat="S",
            kleur="Blue",
            prijs="24.95",
            voorraad="4",
            imagePath="assets/images/woman_dress_basic.png",
            body="Dit is een blauwe basic dress maat S voor vrouwen",
            manufacturer="company name",
            model="Tx17",
        )
    )
    app.session.add(
        Product(
            naam="basic dress",
            categorie="Woman",
            subcategorie="Dresses",
            maat="M",
            kleur="Green",
            prijs="24.95",
            voorraad="4",
            imagePath="assets/images/woman_dress_basic.png",
            body="Dit is een groene basic dress maat M voor vrouwen",
            manufacturer="company name",
            model="Tx17",
        )
    )


    app.session.flush()
    app.session.commit()

def bestellingen_data(app):
    click.echo("Adding bestellingen")
    app.session.add(
        Bestellingen(
            gebruikers_id="1",
            prijs="20",
            aantal_artikelen="2",
            datum="maandag",
        )
    )
    app.session.add(
        Bestellingen(
            gebruikers_id="3",
        )
    )
    app.session.flush()
    app.session.commit()

def bestellingItem_data(app):
    click.echo("Adding bestellingItems")
    app.session.add(
        BestellingItems(
            bestelling_id="1",
            product_id="1",
            hoeveelheid="1",
        )
    )
    app.session.add(
        BestellingItems(
            bestelling_id="1",
            product_id="2",
            hoeveelheid="1",
        )
    )
    app.session.flush()
    app.session.commit()

def maat_data(app):
    click.echo("Adding maten")
    app.session.add(
        Maat(
            maat="S",
        )
    )
    app.session.add(
        Maat(
            maat="M",
        )
    )
    app.session.add(
        Maat(
            maat="L",
        )
    )
    app.session.add(
        Maat(
            maat="XL",
        )
    )
    app.session.flush()
    app.session.commit()

def kleur_data(app):
    click.echo("Adding kleuren")
    app.session.add(
        Kleur(
            kleur="Blue",
        )
    )
    app.session.add(
        Kleur(
            kleur="White",
        )
    )
    app.session.add(
        Kleur(
            kleur="Grey",
        )
    )
    app.session.add(
        Kleur(
            kleur="Red",
        )
    )
    app.session.add(
        Kleur(
            kleur="Green",
        )
    )
    app.session.add(
        Kleur(
            kleur="Yellow",
        )
    )
    app.session.flush()
    app.session.commit()

def categorie_data(app):
    click.echo("Adding categorie")
    app.session.add(
        Categorie(
            categorie="Men",
        )
    )
    app.session.add(
        Categorie(
            categorie="Kids",
        )
    )
    app.session.add(
        Categorie(
            categorie="Woman",
        )
    )
    app.session.flush()
    app.session.commit()


def favoriet_data(app):
    click.echo("Adding kleuren")
    app.session.add(
        Favoriet(
            gebruikers_id="1",
            product_id='1',
        )
    )
    app.session.flush()
    app.session.commit()

def setup_db(app, cache):
    # try:
    #     if (app.session.query(Gebruikers).first() is not None):
    #         print('done')
    #         return
    # except:
    print('nieuwe data')
    # drop all databases and clear cache
    DBModel.metadata.drop_all(bind=app.engine)

    cache.clear()

    # create a new database and add new data
    DBModel.metadata.create_all(bind=app.engine)

    gebruikers_data(app)
    kleur_data(app)
    maat_data(app)
    categorie_data(app)
    product_data(app)
    bestellingen_data(app)
    bestellingItem_data(app)
    favoriet_data(app)
