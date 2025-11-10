# Intent-Classification-Chatbot
A machine learning chatbot built with scikit-learn &amp; NLTK that classifies 27 customer intents with 98.7% accuracy.
# 🤖 AI Customer Support Bot

A machine learning-powered chatbot trained on 20,000+ real-world utterances to handle 27 customer intents with 98.7% accuracy.

![Demo GIF of the chatbot in action] ## Overview

This project is a complete NLP pipeline for building a practical, high-accuracy customer support bot. The model is built from scratch using `scikit-learn` and `NLTK` and is capable of classifying user text into 27 distinct intents, such as `track_order`, `reset_password`, and `contact_human_agent`.

## Features
* **Model:** Logistic Regression trained on 20,000+ utterances.
* **Accuracy:** **98.7%** on the held-out test set.
* **Intents Handled:** 27 (e.g., `cancel_order`, `payment_issue`, `delivery_options`).
* **Tech Stack:** Python, scikit-learn, NLTK, pandas.

## How It Works

### 1. Data Preprocessing
The text data (`cleaned_chatbot_data.csv`) is cleaned and normalized using a custom `preprocess_text` function which:
* Converts text to lowercase.
* Removes punctuation and non-alphabetic characters.
* Tokenizes the text.
* Removes stop words.
* Lemmatizes each token to its root form.

### 2. Model Training
1.  **Vectorization:** The cleaned text is converted into a numerical matrix using `TfidfVectorizer`.
2.  **Training:** A `LogisticRegression` model is trained on these vectors.
3.  **Evaluation:** The model achieves 98.7% accuracy on a 20/80 test/train split.

## How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download NLTK data:**
    ```python
    # Run this in a Python shell
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

5.  **(Add your instructions for getting the data and training the model here)**
    * Example: "Download the dataset from [Kaggle Link]. Place it in the folder and run `python train_model.py` to generate the `.pkl` files."

6.  **Run the chat:**
    ```bash
    python chat.py
    ```
