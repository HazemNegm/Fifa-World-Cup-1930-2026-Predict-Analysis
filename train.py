import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from utils.data_loader import load_data

# Load data
matches, teams, editions = load_data()

# Basic feature engineering for match prediction
def prepare_match_data(matches):
    matches = matches.copy()
    matches['goal_diff'] = matches['score1'] - matches['score2']
    matches['winner'] = np.where(matches['goal_diff'] > 0, matches['team1'], 
                                np.where(matches['goal_diff'] < 0, matches['team2'], 'Draw'))
    # Simple features
    matches['rank_diff'] = np.random.randint(-50, 50, len(matches))  # Placeholder, in real would use historical ranks
    matches['is_knockout'] = matches['stage'].str.contains('Final|Semi|Quarter', na=False).astype(int)
    return matches

data = prepare_match_data(matches)

# For demo, simple model
X = data[['rank_diff', 'is_knockout']].fillna(0)
y = (data['goal_diff'] > 0).astype(int)  # 1 if team1 wins

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'models/match_predictor.pkl')

print("Model trained. Accuracy:", accuracy_score(y_test, model.predict(X_test)))
