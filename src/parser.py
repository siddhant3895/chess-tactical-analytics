import chess.pgn
import pandas as pd
import os

def parse_pgn_metadata(file_path):
    """
    Ingests a raw local PGN file, loops through all matches,
    and extracts metadata headers into a structured pandas DataFrame.
    """
    if not os.path.exists(file_path):
        print(f"[ERROR] Target file not found at: {file_path}")
        return pd.DataFrame()

    print(f"[INFO] Initializing data stream from: {file_path}")
    extracted_games = []
    
    with open(file_path, "r", encoding="utf-8") as pgn_file:
        while True:
            # Read games sequentially from the file stream
            game = chess.pgn.read_game(pgn_file)
            if game is None:
                break  # Reached the end of the PGN file
                
            headers = game.headers
            
            # Map out key telemetry tags
            match_metrics = {
                "Event": headers.get("Event", "Unknown"),
                "Site": headers.get("Site", "Chess.com"),
                "Date": headers.get("Date", "Unknown"),
                "White": headers.get("White", "Unknown"),
                "Black": headers.get("Black", "Unknown"),
                "Result": headers.get("Result", "*"),
                "WhiteElo": headers.get("WhiteElo", "0"),
                "BlackElo": headers.get("BlackElo", "0"),
                "Termination": headers.get("Termination", "Unknown")
            }
            extracted_games.append(match_metrics)
            
    # Convert the list of structured dictionaries directly into a DataFrame
    df = pd.DataFrame(extracted_games)
    print(f"[SUCCESS] Extracted {len(df)} matches into standard matrix format.")
    return df

if __name__ == "__main__":
    print("[SUCCESS] Core parser engine compiled successfully.")
    # Execution entry point for local pipeline testing
    # sample_df = parse_pgn_metadata("data/raw/bot_matches.pgn")
