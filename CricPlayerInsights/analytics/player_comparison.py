import pandas as pd


def compare_players(df, player1, player2):
    """Compare two batters or two bowlers side-by-side."""

    # =============================
    # BATTER COMPARISON
    # =============================

    p1_batter_df = df[df["batter"] == player1]
    p2_batter_df = df[df["batter"] == player2]

    batter_comparison = {
        player1: {
            "runs": int(p1_batter_df["runs"].sum()),
            "balls": len(p1_batter_df),
            "matches": p1_batter_df["match_id"].nunique(),
            "avg_sr": round(
                (p1_batter_df["runs"].sum() / len(p1_batter_df)) * 100, 2
            ) if len(p1_batter_df) > 0 else 0,
        },
        player2: {
            "runs": int(p2_batter_df["runs"].sum()),
            "balls": len(p2_batter_df),
            "matches": p2_batter_df["match_id"].nunique(),
            "avg_sr": round(
                (p2_batter_df["runs"].sum() / len(p2_batter_df)) * 100, 2
            ) if len(p2_batter_df) > 0 else 0,
        },
    }

    # =============================
    # BOWLER COMPARISON
    # =============================

    p1_bowler_df = df[df["bowler"] == player1]
    p2_bowler_df = df[df["bowler"] == player2]

    bowler_comparison = {
        player1: {
            "wickets": int(p1_bowler_df["wicket"].sum()),
            "overs": round(len(p1_bowler_df) / 6, 1),
            "economy": round(
                p1_bowler_df["total_runs"].sum() / (len(p1_bowler_df) / 6), 2
            ) if len(p1_bowler_df) > 0 else 0,
            "matches": p1_bowler_df["match_id"].nunique(),
        },
        player2: {
            "wickets": int(p2_bowler_df["wicket"].sum()),
            "overs": round(len(p2_bowler_df) / 6, 1),
            "economy": round(
                p2_bowler_df["total_runs"].sum() / (len(p2_bowler_df) / 6), 2
            ) if len(p2_bowler_df) > 0 else 0,
            "matches": p2_bowler_df["match_id"].nunique(),
        },
    }

    return {
        "batter_comparison": batter_comparison,
        "bowler_comparison": bowler_comparison,
    }
