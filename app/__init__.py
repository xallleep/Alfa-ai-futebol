from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurações para Render
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-render')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///predictions.db').replace('postgres://', 'postgresql://')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()
        
        # Configuração do scheduler apenas no processo principal
        if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
            scheduler = BackgroundScheduler()
            from .scraper import daily_scrape_and_analyze
            scheduler.add_job(
                func=daily_scrape_and_analyze,
                trigger="cron",
                hour=8,
                minute=0,
                timezone="UTC"
            )
            scheduler.start()
            atexit.register(lambda: scheduler.shutdown())
    
    return app