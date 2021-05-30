def register_blueprints(app):
    from app.server import home

    app.register_blueprint(home)