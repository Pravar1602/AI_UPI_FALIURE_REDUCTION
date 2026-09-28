import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_delay_model():
    df = pd.read_csv('data/transaction_logs.csv')
    
    # Features and Target
    X = df[['hour_of_day', 'network_latency_ms', 'previous_failures_24h', 'is_peak_hour']]
    y = df['server_delay_occurred']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train AI Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    # Simulate Real-time Prediction & Backup Suggestion
    print("\n--- Real-time Prediction & Backup Suggestion ---")
    # Scenario: Peak hour, high latency, previous failures
    live_tx = pd.DataFrame([{
        'hour_of_day': 19, 
        'network_latency_ms': 450, 
        'previous_failures_24h': 2, 
        'is_peak_hour': 1
    }])
    
    delay_prob = model.predict_proba(live_tx)[0][1]
    print(f"Predicted Probability of Server Delay: {delay_prob * 100:.2f}%")
    
    if delay_prob > 0.70:
        print(" ALERT: High chance of failure! Suggested Action: Initiate backup payment option (e.g., UPI Lite or alternate bank route).")
    else:
        print("Safe to proceed with standard UPI transaction.")

if __name__ == "__main__":
    train_delay_model()