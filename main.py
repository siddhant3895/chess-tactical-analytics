import os
from src.parser import parse_pgn_metadata
from src.analyzer import calculate_bot_win_rates
from src.visualizer import plot_bot_win_rates

def run_pipeline():
    """
    Main orchestrator that manages the end-to-end data flow
    from raw file ingestion to metric matrix generation and visualization.
    """
    print("[START] Launching Chess Tactical Analytics Pipeline...")
    
    # Define relative pathing to the raw telemetry data
    raw_data_path = os.path.join("data", "raw", "sample.pgn")
    
    # Trigger Layer 1: Data Ingestion and Tag Extraction
    print("\n--- Execution Stage 1: Data Parsing ---")
    game_dataframe = parse_pgn_metadata(raw_data_path)
    
    if game_dataframe.empty:
        print("[FAIL] Pipeline broke: Core DataFrame generation returned empty matrix.")
        return
        
    # Trigger Layer 2: Metric Computation and Grouping
    print("\n--- Execution Stage 2: Metric Computation ---")
    performance_metrics = calculate_bot_win_rates(game_dataframe)
    
    if performance_metrics.empty:
        print("[WARNING] Analytics matrix empty. Skipping visualization stage.")
        return

    # Trigger Layer 3: Performance Graphics Export
    print("\n--- Execution Stage 3: Data Visualization ---")
    output_asset = plot_bot_win_rates(performance_metrics)
    
    print("\n[SUCCESS] Full pipeline execution sequence completed cleanly.")

if __name__ == "__main__":
    run_pipeline()
