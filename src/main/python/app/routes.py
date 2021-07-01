def register_blueprints(app):
    from app.server import home
    from app.login import login
    from app.bestellen import bestellen

    app.register_blueprint(home)
    app.register_blueprint(login)
    app.register_blueprint(bestellen)