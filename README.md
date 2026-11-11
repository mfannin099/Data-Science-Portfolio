
# **Python:**

---

## Personal Finance Hub: Spending, Budgeting & Stock Research
A personal finance toolkit that started as three separate apps (a Streamlit credit card dashboard, a Dash budgeting tool, and a Shiny stock tool) and that I consolidated into one **Shiny for Python** app, the Finance Hub. Everything lives in a single `uv`-managed Python project with tests.

- **Home:** Upload a credit card CSV once (or use synthetic sample data) and review the merchant categories. Category corrections are remembered per merchant and applied across the whole app.
- **Spending:** Filters, Venmo splits, and breakdowns by category, merchant, weekday, and time of day. It also covers needs vs. wants and flags money-saving opportunities such as recurring charges, frequent small purchases, large one-off purchases, and new merchants.
- **Budget:** Enter income as net or gross and build a plan using the 50/30/20 rule or Zero-Based and Pay Yourself First suggestions, with editable allocations. It compares the budget to actual spending over the last 30 days of the statement and exports to CSV or PDF.
- **Stocks:** Compare up to 5 tickers (growth of $1,000 and fundamentals) using Yahoo Finance data, with a moving-average forecast and an XGBoost forecast that includes a scorecard. The ML model uses customizable SMA/EMA trend features.

Statement and budget data stays in the session and nothing is saved between runs, which was a deliberate privacy choice for financial data. This project is for educational use and is not financial advice.

**Tools:** Python, Shiny for Python, Streamlit, Dash, XGBoost, pandas, Yahoo Finance, pytest, uv

<!-- Add a screenshot here, e.g. ![](/images/finance_hub.png) -->

[Link to code](https://github.com/mfannin099/PersonalFinanceApplications)

---

## Life Tracker: Full-Stack Fitness Logging App
A full-stack app for logging personal fitness data: daily weight entries and workout entries (lift split, secondary muscle group, and optional cardio details). It exposes full create, read, update, and delete REST endpoints from a **FastAPI** backend, with interactive API docs at `/docs`, and a **React + TypeScript** frontend built with Vite.

Data is stored in **Supabase** (hosted Postgres) in `weights` and `workouts` tables, accessed from the backend with the `supabase-py` client. Validation happens server-side:
- Dates are accepted as `m-d-yyyy` or `mm-dd-yyyy` and normalized to `mm-dd-yyyy`.
- Weight must be non-negative with at most one decimal place.
- Workouts require a valid lift split. Cardio fields are cleared when no cardio was done, and when it was, a cardio type plus either distance or duration is required.

The app is deployed on **Vercel**, with the React build served as static assets and the API running as a Python serverless function.

**Tools:** Python, FastAPI, React, TypeScript, Vite, Supabase (Postgres), Vercel, uv

<!-- Add a screenshot here, e.g. ![](/images/life_tracker.png) -->

[Link to code](https://github.com/mfannin099/life_tracker_app)

---

## 18 Birdies Golf Analysis: Statistics, Simulation & FastAPI
A personal project that started with my own golf data and grew into a deployed model. I exported my rounds from the 18Birdies app as JSON, then parsed and cleaned them in pandas. From there I explored my 9-hole scores, fit a regression line, and looked for outliers.

To go beyond simple descriptive stats, I used PyMC to apply Bayesian statistics to the scores. I also wrote a simulator (`golf_sim.py`) to generate golf scores, and used that simulated data to train a DecisionTreeClassifier that predicts a handicap. The model is served through a FastAPI endpoint that accepts hole yardage, par, and a player's score.

**Tools:** Python, pandas, Jupyter, PyMC, scikit-learn, FastAPI, uv

<!-- Add a screenshot here, e.g. ![](/images/golf_regression.png) -->

[Link to code](https://github.com/mfannin099/18_birdies_project)

---

## Book Recommendation Engine: Flask App & Automated Weekly Picks
A Flask app that recommends what to read next based on books you've already read. Books can be entered by hand or uploaded as a CSV, XLSX, or TXT list, and the app returns 10 recommendations. An optional genre field can steer the results.

**How it works:**
1. Each book's description is pulled from Open Library, with Wikipedia and then Apple's iTunes Search API as fallbacks. The fallbacks raised description coverage from about 36% to about 70% on a test library.
2. Descriptions are combined into a taste profile using TF-IDF.
3. The app searches Open Library for similar unread books and ranks the candidates by similarity. Weak matches are dropped rather than used to pad the list.

I also built a weekly automation: a GitHub Actions job reads my reading-log Google Sheet and, every Saturday, commits two fresh recommendation CSVs to a separate `results` branch. Because the ranking is based on word overlap, it can't match synonyms, which is a known limitation I documented in the README.

**Tools:** Python, Flask, pandas, scikit-learn, thefuzz, requests, pytest, uv, GitHub Actions

[Link to code](https://github.com/mfannin099/bookRecommendation)

---

# **Side Projects & Learning:**

## ad_hoc: Small Projects and Experiments
A running repo of smaller projects I build to learn new tools. Current folders include:

- **finances_streamlit_tracker:** a personal finance tracker built with Streamlit
- **flask101:** Flask fundamentals
- **google_books_api:** working with the Google Books API
- **hugging_face_test:** experiments with Hugging Face models
- **stats_powerlifting:** statistical analysis of powerlifting data
- **gfl_schedule:** a schedule project
- **OOP_practice:** object-oriented programming practice

[Link to code](https://github.com/mfannin099/ad_hoc)
