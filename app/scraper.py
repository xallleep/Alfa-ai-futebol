from datetime import datetime, timedelta
from app import db
from app.models import Prediction

def daily_scrape_and_analyze():
    # Simulação de dados raspados - substitua por sua lógica real de scraping
    mock_matches = [
        {
            'league': 'Premier League',
            'home_team': 'Chelsea',
            'away_team': 'Liverpool',
            'match_date': datetime.utcnow() + timedelta(days=1),
            'stats': {
                'home_form': ['W', 'W', 'L', 'D', 'W'],
                'away_form': ['W', 'D', 'W', 'L', 'W'],
                'avg_corners': {'home': 5.2, 'away': 4.8, 'total': 10.0},
                'avg_cards': {'home_yellow': 1.8, 'away_yellow': 2.1, 'home_red': 0.1, 'away_red': 0.05}
            }
        }
    ]
    
    # Limpa previsões antigas
    Prediction.query.delete()
    
    # Cria novas previsões
    for match in mock_matches:
        prediction = analyze_match(match)
        db.session.add(prediction)
    
    db.session.commit()

def analyze_match(match_data):
    stats = match_data['stats']
    
    # Lógica de análise melhorada
    home_attack = len([x for x in stats['home_form'][:5] if x in ['W', 'D']]) / 5
    away_attack = len([x for x in stats['away_form'][:5] if x in ['W', 'D']]) / 5
    
    home_defense = len([x for x in stats['home_form'][:5] if x in ['L', 'D']]) / 5
    away_defense = len([x for x in stats['away_form'][:5] if x in ['L', 'D']]) / 5
    
    # Cálculo de gols mais sofisticado
    home_goals = max(0, min(3, round((home_attack * 1.5) + (away_defense * 0.8))))
    away_goals = max(0, min(2, round((away_attack * 1.2) + (home_defense * 0.6))))
    
    # Cálculo de confiança
    confidence = int(60 + (home_attack + away_attack) * 20)
    
    return Prediction(
        league=match_data['league'],
        home_team=match_data['home_team'],
        away_team=match_data['away_team'],
        predicted_score=f"{home_goals}-{away_goals}",
        corners_prediction=f"{int(stats['avg_corners']['total'])} cantos",
        yellow_cards_prediction=f"{int(stats['avg_cards']['home_yellow'] + stats['avg_cards']['away_yellow'])} amarelos",
        red_cards_prediction="0-2 vermelhos",
        confidence=min(95, confidence),
        match_date=match_data['match_date']
    )