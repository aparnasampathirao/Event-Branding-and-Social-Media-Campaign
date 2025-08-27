# engagement_tracker.py

import pandas as pd

def analyze_campaign_performance(file_path):
    """
    Analyze social media campaign performance based on engagement data.
    
    Args:
        file_path (str): Path to the CSV file containing campaign data.
    
    CSV file format (example):
    Date,Likes,Shares,Reach
    2025-01-01,120,30,1400
    2025-01-02,200,45,1600
    2025-01-03,150,40,1350
    2025-01-04,180,50,1700
    """
    
    # Load engagement data
    data = pd.read_csv(file_path)
    
    # Calculate averages
    avg_likes = data['Likes'].mean()
    avg_shares = data['Shares'].mean()
    avg_reach = data['Reach'].mean()
    
    # Calculate growth percentage (baseline reach = 1000 for comparison)
    baseline_reach = 1000
    growth_percent = ((avg_reach - baseline_reach) / baseline_reach) * 100
    
    # Display results
    print("📊 Campaign Performance Report")
    print(f"✅ Average Likes: {avg_likes:.2f}")
    print(f"✅ Average Shares: {avg_shares:.2f}")
    print(f"✅ Average Reach: {avg_reach:.2f}")
    print(f"📈 Growth in Reach: {growth_percent:.2f}%")

if __name__ == "__main__":
    # Run analysis on your engagement data file
    analyze_campaign_performance("metrics/engagement_report.csv")
