# Movie-data-EDA-and-Visualization

A Python project that explores and visualizes a movie dataset to show trends, relationships, and insights using data cleaning, EDA (exploratory data analysis), and visualizations.

This repository includes modular Python code and a Jupyter notebook to demonstrate a clear, reproducible analysis workflow.

---

###  Project Overview

This project analyzes a dataset of movies to answer questions like:

- What movies have the highest gross revenue?
- How do budget, votes, and gross revenue relate to each other?
- What patterns can we see in the data through visualizations?

The code is organized into reusable modules for loading, cleaning, analyzing, and visualizing data, and the Jupyter notebook presents the results in a narrative style.

---

### Repository Structure

```
Movie-data-EDA-and-Visualization-/
├── data/
│   └── movies.csv          # Movie dataset
├── src/                    # Python modules
│   ├── __init__.py
│   ├── load_data.py        # Loads the dataset
│   ├── clean_data.py       # Cleans and preprocesses the data
│   ├── eda.py              # Summary and exploration functions
│   ├── visualization.py    # Plotting functions
│   └── analysis.py         # Correlation & analysis logic
├── notebooks/
│   └── exploration.ipynb      # Jupyter notebook demonstrating EDA
├── run.py                  # Script to run the full analysis
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

###  Tools and Libraries

- **numpy** for numerical operations
- **pandas** for data manipulation
- **matplotlib** and **seaborn** for visualization

---

### How to install the required libraries
```bash
pip install -r requirements.txt
```

---

### How to Run

From the Command Line or Terminal, run the full analysis pipeline (load, clean, analyze, visualize):

```bash
python run.py
```

### Using Jupyter Notebook

1. Activate your Python environment.
2. Start Jupyter Notebook.
3. Open `notebooks/analysis.ipynb`
4. Run all cells — the notebook includes charts, tables, and explanations.