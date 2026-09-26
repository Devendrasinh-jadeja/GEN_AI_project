# GEN_AI_project

A full-stack cricket intelligence platform built with Flask for analyzing player performance, simulating match situations, comparing players, and exploring team statistics using structured cricket data.

This project combines data analytics, predictive modeling, and AI-ready tooling to provide a rich cricket dashboard for analysts, fans, and developers. It includes a web application with multiple analysis pages and downloadable reports.

## Project overview

The application reads structured ball-by-ball cricket data from `data/processed/ball_by_ball_clean.csv` and provides:

- player batting and bowling intelligence
- recent form and consistency analysis
- season-wise comparisons
- head-to-head and matchup analysis
- opponent and kryptonite insights
- pressure and clutch evaluation
- predictive performance recommendations
- match impact and super over simulation
- team and venue analysis
- squad optimization
- leaderboard summaries and CSV report export

The project is designed to be both a practical sports analytics dashboard and a foundation for further GenAI-powered cricket insights.

## Key features

### Player analysis
- Individual batter and bowler reports
- Role eligibility checks for batters, bowlers, and all-rounders
- Recent form tracking and milestone monitoring
- Consistency scoring and innings-level breakdowns
- Advanced intelligence summaries for player performance evaluation

### Comparison and matchup tools
- Compare two players side by side
- Player vs team and bowler vs team analysis
- Head-to-head matchup evaluation
- Opponent intelligence and weakness analysis

### Prediction and simulation
- Player performance prediction based on venue and opponent context
- Match impact simulator for chase scenarios
- Super Over simulation
- Venue-specific insights and pitch behavior analysis
- Squad builder for selecting optimal team combinations

### Reporting and dashboards
- Top batters, bowlers, strike rates, and economy leaders
- Team analytics and season comparisons
- Dismissal pattern analysis
- Overall match statistics and venue statistics
- Report generation and CSV export for selected players or comparisons

### AI-ready foundation
- LangChain / LangGraph-ready architecture for future AI workflows
- Suitable for integrating LLM-based analysis, storytelling, and interactive insight generation

## LangGraph and its use in this project

LangGraph is a graph-based orchestration framework from the LangChain ecosystem used to build stateful AI workflows. Instead of a single monolithic prompt, LangGraph allows you to define a workflow as a set of connected steps or nodes, where each node can do a specific job such as:

- receive a user question
- decide which tool or dataset to use
- run a calculation or analytics function
- combine results from multiple modules
- generate a final natural-language explanation

In this project, LangGraph can be used to build an AI-powered cricket analyst that works like this:

1. User asks: "Compare Rohit Sharma and Virat Kohli in the last 3 seasons."
2. The LangGraph workflow identifies the required analysis path:
   - player comparison
   - season stats
   - recent form
   - head-to-head context
3. Relevant analytics functions from the `analytics/` package are executed.
4. Results are combined into a single structured output.
5. A language model converts these results into a clean, human-readable insight summary.

This is especially useful for projects where the system needs to combine multiple tools, reason step by step, and respond dynamically rather than using a fixed response template.

For this repository, the current implementation is primarily a deterministic cricket analytics dashboard. The LangGraph concept is a future enhancement that can help transform the project into an intelligent assistant that can:

- answer sports-related queries in natural language
- decide which analytics module to call automatically
- chain together multiple analyses in one conversation
- generate summary narratives based on the data
- support more conversational and agent-style cricket insights

## Repository structure

```text
GEN_AI_project/
├── analytics/                    # Core analytics and scoring modules
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
│   ├── phase_analysis.py
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
│   └── venue_intelligence.py
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
│   ├── matchup.html
│   ├── leaderboards.html
│   ├── teams.html
│   ├── statistics.html
│   ├── simulator.html
│   ├── squad_builder.html
│   ├── venue_lab.html
│   └── ...
├── app.py                       # Flask application entry point
├── requirements.txt            # Python package dependencies
├── README.md
├── test_all_features.py
├── test_features.py
├── test_leaderboards.py
├── ok
├── tempCodeRunnerFile.py
└── .vscode/
```

## Tech stack

- Python
- Flask
- Pandas
- NumPy
- Matplotlib
- Plotly
- scikit-learn
- LangChain / LangGraph

## Data source

The main dataset used by the application is:

```text
data/processed/ball_by_ball_clean.csv
```

This file contains ball-by-ball cricket event data used for scoring, filtering, comparison, and prediction logic.

## Installation

1. Clone the repository

```bash
git clone https://github.com/Devendrasinh-jadeja/GEN_AI_project.git
cd GEN_AI_project
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the project

Start the Flask app with:

```bash
python app.py
```

Then open the application in the browser:

```text
http://127.0.0.1:5000/
```

## Main application pages

The dashboard provides multiple pages or sections for analysis, including:

- home player dashboard
- player comparison page
- matchup analysis
- player prediction
- match simulator
- clutch and pressure analysis
- recent form and insights
- leaderboards
- team statistics
- season comparison
- dismissal analysis
- statistics overview
- super over analysis
- moneyball ROI engine
- opponent intelligence
- venue lab
- squad builder

## Example use cases

- Compare a batter and bowler across multiple metrics
- Identify recent form and consistency changes over time
- Predict a player’s likely output in a given venue and match context
- Simulate a chase or pressure scenario with remaining overs
- Explore which players are strongest in clutch moments
- Evaluate team balance and optimize a Dream XI squad
- Generate downloadable player reports for presentations and analysis
- Use a LangGraph-style workflow to chain analytics tools and answer questions in natural language

## Notes

- The application is structured around cricket analytics and data exploration workflows.
- Several modules rely on clean, consistent input data for accurate results.
- The project is ready for future GenAI enhancements, including natural-language summaries and AI-assisted analytical explanations.
- LangGraph is presented as a future integration path that can connect analytics modules into a conversational reasoning system.

## License

This project currently does not include a license file. If you plan to share or distribute it publicly, it is recommended to add an open-source license such as MIT or Apache 2.0.

## Author

Built for cricket analytics and AI-enhanced sports intelligence experimentation.
