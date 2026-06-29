import pandas as pd

def calculate_bot_win_rates(df):
    """
    Processes the match DataFrame to calculate win, loss, 
    and draw percentages against individual bot profiles.
    """
    if df.empty:
        print("[WARNING] Analytical engine received an empty matrix.")
        return pd.DataFrame()

    print("[INFO] Computing aggregate win rates against bot opponents...")
    
    # Define your profile anchor for identity mapping
    user_handle = "siddhant3895"
    
    # Dynamically isolate who the bot opponent is for each row
    df['Bot_Opponent'] = df.apply(
        lambda r: r['Black'] if r['White'] == user_handle else r['White'], 
        axis=1
    )
    
    # Calculate categorical match outcomes from the perspective of the user
    def evaluate_outcome(row):
        if row['Result'] == '1-0':
            return 'Win' if row['White'] == user_handle else 'Loss'
        elif row['Result'] == '0-1':
            return 'Win' if row['Black'] == user_handle else 'Loss'
        elif row['Result'] == '1/2-1/2':
            return 'Draw'
        return 'Unknown'
        
    df['Outcome'] = df.apply(evaluate_outcome, axis=1)
    
    # Generate cross-tabulation matrix showing normalized percentage distributions
    performance_matrix = pd.crosstab(
        df['Bot_Opponent'], 
        df['Outcome'], 
        normalize='index'
    ) * 100
    
    print("\n[SUCCESS] Statistical Performance Matrix Derived:")
    print(performance_matrix.round(2))
    return performance_matrix

if __name__ == "__main__":
    print("[SUCCESS] Core analyzer engine compiled successfully.")
    
    # Local integration testing template using dummy match arrays
    mock_pipeline_data = [
        {"White": "siddhant3895", "Black": "Martin", "Result": "1-0"},
        {"White": "Nelson", "Black": "siddhant3895", "Result": "1-0"},
        {"White": "siddhant3895", "Black": "Martin", "Result": "1/2-1/2"}
    ]
    calculate_bot_win_rates(pd.DataFrame(mock_pipeline_data))
