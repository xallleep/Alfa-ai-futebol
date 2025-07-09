from datetime import datetime
from app.models import Prediction

def analyze_match(match_data):
    stats = match_data['stats']
    
    # Lógica de análise mantida conforme seu original
    home_goals = min(3, int(len([x for x in stats['home_form'] if x == 'W']) * 0.6))
    away_goals = min(2, int(len([x for x in stats['away_form'] if x == 'W']) * 0.4))
    
    return Prediction(
        league=match_data['league'],
        home_team=match_data['home_team'],
        away_team=match_data['away_team'],
        predicted_score=f"{home_goals}-{away_goals}",
        corners_prediction=f"{int(stats['avg_corners']['total'])}+ cantos",
        yellow_cards_prediction=f"{int(stats['avg_cards']['home_yellow'] + stats['avg_cards']['away_yellow'])}+ amarelos",
        red_cards_prediction="0-2 vermelhos",
        confidence=70,
        match_date=match_data['match_date']
    )