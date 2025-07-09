from flask import render_template
from app import db
from app.models import Prediction
from datetime import datetime

def init_routes(app):
    @app.route('/')
    def index():
        today = datetime.now().date()
        predictions = Prediction.query.filter(
            Prediction.match_date >= today
        ).order_by(
            Prediction.match_date.asc()
        ).limit(10).all()
        
        return render_template('index.html', predictions=predictions)