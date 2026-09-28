import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def analyze_reviews():
    df = pd.read_csv('data/raw_reviews.csv')
    
    # Simple NLP: Extract top keywords using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
    X = vectorizer.fit_transform(df['review_text'])
    
    print("--- Top Issues Identified from 10,000+ Reviews ---")
    print("Top Keywords:", vectorizer.get_feature_names_out())
    
    # Categorize issues
    def categorize(text):
        if 'failed' in text.lower() or 'deducted' in text.lower():
            return 'Failed Transactions'
        elif 'freeze' in text.lower():
            return 'App Freezes'
        elif 'refund' in text.lower():
            return 'Slow Refunds'
        return 'Other'
        
    df['issue_category'] = df['review_text'].apply(categorize)
    print("\n--- Issue Breakdown ---")
    print(df['issue_category'].value_counts())
    print("\n--- Complaints by App ---")
    print(df.groupby(['app_name', 'issue_category']).size().unstack().fillna(0))

if __name__ == "__main__":
    analyze_reviews()