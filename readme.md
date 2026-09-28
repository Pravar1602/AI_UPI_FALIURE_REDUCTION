# AI-Powered UPI Payment Failure Reduction 

##  Overview
This project aims to reduce UPI payment failures by analyzing 10,000+ user reviews from top Indian banking/payment apps (SBI YONO, GPay, PhonePe, Paytm, CRED) and deploying an AI model to predict bank server delays.

##  Tech Stack
- **Languages:** Python, SQL
- **Libraries:** Pandas, Scikit-Learn, NumPy
- **Concepts:** NLP (TF-IDF), Random Forest Classification, Feature Engineering

##  Key Features
1. **Review Analysis (NLP):** Identifies key issues like failed transactions, app freezes, and slow refunds.
2. **Predictive AI:** Analyzes transaction logs (network latency, peak hours, previous failures) to predict server delays.
3. **Backup Suggestion:** If delay probability > 70%, the system triggers a backup payment option.

##  How to Run Locally
1. Clone this repository:
   `git clone https://github.com/Pravar1602/ai-upi-failure-reduction.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Generate synthetic data:
   `python src/data_generation.py`
4. Run NLP Analysis:
   `python src/nlp_analysis.py`
5. Train AI Model and test prediction:
   `python src/delay_prediction.py`

## Business Impact
- Targeted **20% drop** in failed transactions.
- Targeted **30% reduction** in payment complaints.
- See the full [Feature Rollout Plan](docs/feature_rollout_plan.md).
