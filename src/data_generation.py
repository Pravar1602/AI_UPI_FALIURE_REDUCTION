import pandas as pd
import numpy as np
import random
import os

def generate_synthetic_data():
    # Create the data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    apps = ['SBI YONO', 'GPay', 'PhonePe', 'Paytm', 'CRED']
    issues = [
        'Failed transactions and money deducted', 
        'App freezes during payment', 
        'Slow refunds and poor support',
        'UPI server delay error',
        'Transaction failed due to bank server down'
    ]
    
    print("Generating synthetic reviews...")
    # Generate 10,500 reviews
    reviews_data = []
    for i in range(10500):
        reviews_data.append({
            'review_id': i,
            'app_name': random.choice(apps),
            'review_text': random.choice(issues),
            'rating': random.randint(1, 3)
        })
    df_reviews = pd.DataFrame(reviews_data)
    
    # Save to CSV
    df_reviews.to_csv('data/raw_reviews.csv', index=False)
    print(" Saved data/raw_reviews.csv")
    
    print("Generating synthetic transaction logs...")
    # Generate transaction logs for AI prediction (Features: Time, Network, Bank, etc.)
    tx_data = []
    for i in range(5000):
        tx_data.append({
            'transaction_id': i,
            'bank_name': random.choice(['HDFC', 'SBI', 'ICICI', 'Axis']),
            'hour_of_day': random.randint(0, 23),
            'network_latency_ms': random.randint(20, 500),
            'previous_failures_24h': random.randint(0, 5),
            'is_peak_hour': 1 if random.randint(0, 23) in [10,11,12,18,19,20,21] else 0,
            'server_delay_occurred': random.choices([0, 1], weights=[0.7, 0.3])[0] # 30% delay rate
        })
    df_tx = pd.DataFrame(tx_data)
    
    # Save to CSV
    df_tx.to_csv('data/transaction_logs.csv', index=False)
    print(" Saved data/transaction_logs.csv")
    
    print("\n Data generation complete: 10,500 reviews and 5,000 transaction logs.")

if __name__ == "__main__":
    generate_synthetic_data()