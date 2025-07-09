from datetime import datetime
from app import db

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    league = db.Column(db.String(100), nullable=False)
    home_team = db.Column(db.String(100), nullable=False)
    away_team = db.Column(db.String(100), nullable=False)
    predicted_score = db.Column(db.String(20), nullable=False)
    corners_prediction = db.Column(db.String(50), nullable=False)
    yellow_cards_prediction = db.Column(db.String(50), nullable=False)
    red_cards_prediction = db.Column(db.String(50), nullable=False)
    confidence = db.Column(db.Integer, nullable=False)
    analysis_date = db.Column(db.DateTime, default=datetime.utcnow)
    match_date = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return f'<Prediction {self.home_team} vs {self.away_team}>'