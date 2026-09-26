# GEN_AI_project

A Flask-based cricket analytics and player intelligence dashboard for exploring player performance, forecasting outcomes, comparing players, and evaluating match strategies using structured cricket data.

This project turns raw ball-by-ball cricket data into actionable insights for batters, bowlers, teams, and match scenarios. It includes a full web application with multiple analytical modules and downloadable reports.

## Overview

The application reads cricket event data from the `data/processed/ball_by_ball_clean.csv` dataset and provides:

- Player-centric intelligence dashboards
- Team and season comparisons
- Performance prediction and match impact simulation
- Head-to-head and opponent analysis
- Clutch and pressure evaluation
- Booking value and ROI insights using moneyball logic
- Squad optimization and venue analysis
- Leaderboards and statistical summaries
- Exportable player and comparison reports

## Features

### Player insights
- Individual player analysis for batting and bowling performance
- Role eligibility checks for batters, bowlers, and all-rounders
- Recent form and consistency monitoring
- Milestone and innings-level breakdowns
- Advanced player intelligence summaries

### Comparison and matchup analysis
- Compare two players across key metrics
- Batter vs team and bowler vs team analysis
- Head-to-head player matchups
- Opponent intelligence and kryptonite analysis

### Prediction and simulation
- Player performance prediction
- Match impact simulator for pressure scenarios
- Super Over showdown simulation
- Venue-based performance insights
- Squad optimizer for Dream XI style team building

### Reporting and analytics
- Leaderboards for top batters, bowlers, strike rates, and economies
- Team stats and bowling performance summaries
- Dismissal analysis and wicket patterns
- Season-by-season comparison
- Overall statistics and venue trends
- CSV report export

## Project structure

```text
GEN_AI_project/
├── analytics/                 # Core analytical functions and scoring logic
│   ├── advanced_intelligence.py
│   ├── bowler_intelligence.py
│   ├── charts.py
│   ├── clutch.py
│   ├── dismissal_analysis.py
│   ├── head_to_head.py
│   ├── kryptonite.py
│   ├── leaderboards.py
│   ├── moneyball.py
│   ├── opponent_intelligence.py
│   ├── player_comparison.py
│   ├── player_form.py
│   ├── player_report.py
│   ├── predictor.py
│   ├── report_generator.py
│   ├── season_comparison.py
│   ├── simulator.py
│   ├── squad_optimizer.py
│   ├── statistics.py
│   ├── super_over.py
│   ├── team_stats.py
│   ├── venue_lab.py
│   └── ...
├── data/
│   ├── processed/
│   └── raw_json/
├── static/
│   ├── css/
│   └── js/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── compare.html
│   ├── predict.html
│   ├── simulator.html
│   ├── matchup.html
│   ├── leaderboards.html
│   ├── teams.html
│   ├── statistics.html
│   └── ...
├── app.py                     # Flask application entrypoint
├── requirements.txt
├── test_all_features.py
├── test_features.py
├── test_leaderboards.py
├── README.md
└── ...
```

## Tech stack

- Python
- Flask
- Pandas
- NumPy
- Matplotlib
- Plotly
- scikit-learn

## Dataset

The project expects a cleaned cricket event dataset at:

```text
data/processed/ball_by_ball_clean.csv
```

If the dataset is missing or not generated, ensure the processed CSV is available before starting the app.

## Installation

1. Clone the repository

```bash
git clone https://github.com/Devendrasinh-jadeja/GEN_AI_project.git
cd GEN_AI_project
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate it

- On macOS/Linux:

```bash
source .venv/bin/activate
```

- On Windows:

```bash
.venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the app

Start the Flask application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## Example use cases

- Analyze a batter's recent form and consistency
- Compare two players across batting and bowling metrics
- Predict a player's expected performance in a venue or scenario
- Simulate a match pressure situation with remaining overs and target runs
- Build a squad based on player impact and role balance
- Explore team and season trends across cricket seasons

## Notes

- The app is designed as a data-driven sports intelligence dashboard and is best suited for cricket analytics exploration.
- Several modules are built around a single processed cricket dataset, so consistent data quality is important for reliable outputs.
- UI templates provide interactive analysis pages for the different modules in the project.

## License

This project does not currently include a license file. If you plan to distribute or reuse it publicly, consider adding an appropriate open-source license.

## Author

Developed for cricket analytics and AI-driven sports intelligence experimentation.
