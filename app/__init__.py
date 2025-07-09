import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurações
    app.config.from_pyfile('config.py')
    
    # Inicializa extensões
    db.init_app(app)
    
    # Registra blueprints/rotas
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    # Configura o scheduler apenas no processo principal
    if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        scheduler = BackgroundScheduler()
        from app.scraper import daily_scrape_and_analyze
        scheduler.add_job(
            func=daily_scrape_and_analyze,
            trigger="cron",
            hour=8,
            minute=0,
            timezone="UTC"
        )
        scheduler.start()
    
    return app