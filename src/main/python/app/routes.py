def register_blueprints(app):
    from app.server import home
    from app.login import login

    app.register_blueprint(home)
    app.register_blueprint(login)