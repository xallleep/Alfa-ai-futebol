from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    
    with app.app_context():
        from . import routes
        from .models import Prediction
        
        # Criar tabelas se não existirem
        db.create_all()
        
        # Agendar tarefa diária
        scheduler = BackgroundScheduler()
        from .scraper import daily_scrape_and_analyze
        scheduler.add_job(func=daily_scrape_and_analyze, trigger="cron", hour=8, minute=0)
        scheduler.start()
        
        # Desligar o agendador quando o aplicativo for encerrado
        atexit.register(lambda: scheduler.shutdown())
    
    return app