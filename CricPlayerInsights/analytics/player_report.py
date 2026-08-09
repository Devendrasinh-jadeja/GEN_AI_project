from analytics.dangerous_bowlers import get_dangerous_bowlers
from analytics.favourite_bowlers import get_favourite_bowlers
from analytics.venue_intelligence import get_best_venues
from analytics.phase_analysis import get_phase_analysis


def _get_batting_profile(player_df, player):

    runs = int(player_df["runs"].sum())
    balls = len(player_df)
    boundaries = int((player_df["runs"] >= 4).sum())
    dots = int((player_df["runs"] == 0).sum())

    outs = int(
        player_df["player_dismissed"].fillna("")
        .eq(player)
        .sum()
    )

    average = round(runs / outs, 2) if outs > 0 else 0
    boundary_percentage = round((boundaries / balls) * 100, 2) if balls > 0 else 0
    dot_ball_percentage = round((dots / balls) * 100, 2) if balls > 0 else 0

    dismissal_breakdown = (
        player_df[
            player_df["player_dismissed"].fillna("") == player
        ]
        .groupby("dismissal_kind")
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
        .reset_index(drop=True)
    )

    top_teams = (
        player_df
        .groupby("bowling_team")
        .agg(
            runs=("runs", "sum"),
            balls=("runs", "count"),
            matches=("match_id", "nunique")
        )
        .reset_index()
    )

    top_teams["strike_rate"] = round(
        (top_teams["runs"] / top_teams["balls"]) * 100,
        2
    )

    top_teams = (
        top_teams[top_teams["balls"] >= 50]
        .sort_values(["runs", "strike_rate"], ascending=[False, False])
        .reset_index(drop=True)
    )

    return {
        "average": average,
        "boundary_percentage": boundary_percentage,
        "dot_ball_percentage": dot_ball_percentage,
        "dismissal_breakdown": dismissal_breakdown,
        "top_teams": top_teams
    }


def generate_player_report(df, player):

    player_df = df[
        df["batter"] == player
    ]

    runs = int(
        player_df["runs"].sum()
    )

    balls = len(player_df)

    sr = round(
        (runs / balls) * 100,
        2
    )

    matches = player_df[
        "match_id"
    ].nunique()

    dangerous = get_dangerous_bowlers(
        df,
        player
    )

    favourite = get_favourite_bowlers(
        df,
        player
    )

    venues = get_best_venues(
        df,
        player
    )

    phases = get_phase_analysis(
        df,
        player
    )

    profile = _get_batting_profile(
        player_df,
        player
    )

    return {
        "player": player,
        "runs": runs,
        "matches": matches,
        "strike_rate": sr,
        "average": profile["average"],
        "boundary_percentage": profile["boundary_percentage"],
        "dot_ball_percentage": profile["dot_ball_percentage"],
        "dismissal_breakdown": profile["dismissal_breakdown"],
        "top_teams": profile["top_teams"],
        "dangerous": dangerous,
        "favourite": favourite,
        "venues": venues,
        "phases": phases
    }