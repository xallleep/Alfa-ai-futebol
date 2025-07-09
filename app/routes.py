from flask import Blueprint, render_template
from datetime import datetime
from app.models import Prediction

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    today = datetime.utcnow().date()
    predictions = Prediction.query.filter(
        Prediction.match_date >= today
    ).order_by(
        Prediction.match_date.asc()
    ).limit(10).all()
    
    return render_template('index.html', predictions=predictions)