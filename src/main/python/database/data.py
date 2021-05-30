from datetime import datetime, date
import click

from database.db_model import DBModel
from database.tables import Gebruikers, Product, Winkelwagen, Bestellingen, BestellingItems, Maat, Kleur, Favoriet



def gebruikers_data(app):
    click.echo("Adding gebruikers")
    app.session.add(
        Gebruikers(
            voornaam="Jan",
            achternaam="Janssen",
            email="Janjanssen@gmail.com",
            straatnaam="Mudaheerd",
            huisnummer="73",
            postcode="9737XB",
        )
    )
    app.session.add(
        Gebruikers(
            voornaam="Henk",
            achternaam="Henksen",
            email="Henkhenksen@gmail.com",
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
            naam="Spijkerbroek",
            categorie="Mannen",
            maat="s",
            kleur="blauw",
            prijs="10",
            voorraad="3",
        )
    )
    app.session.add(
        Product(
            naam="T-Shirt",
            categorie="Mannen",
            maat="m",
            kleur="grijs",
            prijs="10",
            voorraad="5",
        )
    )
    app.session.flush()
    app.session.commit()

def bestellingen_data(app):
    click.echo("Adding bestellingen")
    app.session.add(
        Bestellingen(
            id="1",
            gebruikers_id="1",
            prijs="20",
            aantal_artikelen="2",
            datum="maandag",
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
            maat="s",
        )
    )
    app.session.add(
        Maat(
            maat="m",
        )
    )
    app.session.flush()
    app.session.commit()

def kleur_data(app):
    click.echo("Adding kleuren")
    app.session.add(
        Kleur(
            kleur="blauw",
        )
    )
    app.session.add(
        Kleur(
            kleur="grijs",
        )
    )
    app.session.flush()
    app.session.commit()

def favoriet_data(app):
    click.echo("Adding kleuren")
    app.session.add(
        Favoriet(
            gebruiker_id="1",
            product_id='1',
        )
    )
    app.session.flush()
    app.session.commit()

def setup_db(app, cache):
    try:
        if (app.session.query(Gebruikers).first() is not None):
            print('done')
            return
    except:
          print('nieuwe data')
          # drop all databases and clear cache
          DBModel.metadata.drop_all(bind=app.engine)
          cache.clear()

          # create a new database and add new data
          DBModel.metadata.create_all(bind=app.engine)

          gebruikers_data(app)
          product_data(app)
          bestellingen_data(app)
          bestellingItem_data(app)
          maat_data(app)
          kleur_data(app)
          favoriet_data(app)
