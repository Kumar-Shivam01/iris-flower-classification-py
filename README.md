# Iris Flower Classification

A beginner-friendly machine learning web application that predicts an Iris flower species from four measurements.

## What this project does

The user enters these measurements in centimetres:

- sepal length
- sepal width
- petal length
- petal width

The application predicts one of three flower species:

- Setosa
- Versicolor
- Virginica

## Technologies used

- **Python** — programming language
- **scikit-learn** — trains the machine learning model
- **Streamlit** — creates the web page
- **Decision Tree Classifier** — the prediction algorithm

## How the machine learning works

1. The app loads the Iris dataset, which contains 150 labelled flower examples.
2. It uses 80% of those examples to train a Decision Tree model.
3. When a visitor enters new measurements, the trained model compares them with patterns it learned from the dataset.
4. The app displays the predicted species and confidence level.

## Run the project on your computer

### 1. Install Python

Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/).

### 2. Open a terminal in this project folder

### 3. Install the required libraries

```powershell
python -m pip install -r requirements.txt
```

### 4. Start the application

```powershell
python -m streamlit run app.py
```

Your browser should open automatically. If it does not, open the local address shown in the terminal, usually `http://localhost:8501`.

## Upload to GitHub

Run these commands from the project folder after you have created the files:

```powershell
git init
git branch -M main
git remote add origin https://github.com/Kumar-Shivam01/iris-flower-classification-py.git
git add .
git commit -m "Create Iris flower classification app"
git push -u origin main
```

If GitHub asks you to sign in, follow the browser instructions. A password may not work; GitHub normally uses a browser sign-in or a personal access token.

## Deploy with Streamlit Community Cloud

1. Visit [share.streamlit.io](https://share.streamlit.io/) and sign in with GitHub.
2. Choose **Create app**.
3. Select the repository `Kumar-Shivam01/iris-flower-classification-py`.
4. Keep the main file as `app.py`.
5. Click **Deploy**.

Streamlit installs the libraries listed in `requirements.txt` and gives you a public website link.
