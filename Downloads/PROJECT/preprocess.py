import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

#Loading the dataset
file_path = 'Dataset(20000).csv'
try:
    df = pd.read_csv(file_path)
except Exception as e:
    print(f"Error loading file: {e}")
    print("Please make sure the file is in the same directory  and the name is correct.")
    
#Data Inspection
print("---First five row of your data----")
print(df.head())
print("----Column Names----")
print(df.columns)        

#Download NLTK(Natural Language ToolKit)
# print("\nDownloading NLTK resources (one time setup)...")
# nltk.download('punkt_tab')  #For tokenizing words
# nltk.download('stopwords')  #For removing stop  words
# nltk.download('wordnet')   #For lemmatization
# print("NLTK resources downloaded.")

#Define your  Preprocessing Function
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    #Lowercasing  Step1
    text = text.lower()
    
    #Removing non-alphabetic characters Step2
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    
    #Tokenization (split into words)  Step3
    tokens = word_tokenize(text)
    
    #Stop_word removal and lemmatization
    cleaned_tokens = []
    for token in tokens:
        if token not in stop_words:
            cleaned_tokens.append(lemmatizer.lemmatize(token))
     
    return " ".join(cleaned_tokens)        

# --- 5. Apply Preprocessing to Your DataFrame ---
print("\nApplying preprocessing to all 20,000 utterances...")
df['cleaned_utterance'] = df['utterance'].apply(preprocess_text)
print("Preprocessing complete.")

# --- 6. Check Your Results ---
print("\n--- DataFrame with new 'cleaned_utterance' column: ---")
print(df.head())

# --- 7. Save Your Cleaned Data ---
cleaned_file_path = 'cleaned_chatbot_data.csv'
df.to_csv(cleaned_file_path, index=False)
print(f"\nSuccessfully saved cleaned data to: {cleaned_file_path}")

# Loading the cleaned data
df = pd.read_csv("cleaned_chatbot_data.csv")

#Handling potential empty rows from preprocessing
df = df.dropna(subset=['cleaned_utterance','intent'])

# -----Define your features X and Y -----
# # X is the input
# # Y is the output
X = df['cleaned_utterance']
y=df['intent']

# Splitting data into train and test data
#Using 80% and 20% method
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42, stratify=y)
print(f"Training with {len(X_train)} samples, testing with {len(X_test)} samples.")

#Create and fit the TF_IDF Vectorizer
vectorizer = TfidfVectorizer()

#Learn the vocab and transform the vectors
X_train_vectors = vectorizer.fit_transform(X_train)

#Only transform X_test using the already fitted vectorizer
X_test_vectors = vectorizer.transform(X_test)

print("\nText Successfully vectorized")
print(f"Vocabulary size: {len(vectorizer.get_feature_names_out())}")


#TRAIN THE MODEL----------------------
print("Training the Logistic Regression model...")
model = LogisticRegression(max_iter=1000) # max_iter for convergence
model.fit(X_train_vectors, y_train)
print("Model training complete.")

# --- 6. Evaluate the Model ---
predictions = model.predict(X_test_vectors)
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy on Test Data: {accuracy * 100:.2f}%")


#Compiling the trained model into a pickle file
with open('chatbot_model.pkl', 'wb') as f_model:
    pickle.dump(model, f_model)

with open('tfidf_vectorizer.pkl', 'wb') as f_vec:
    pickle.dump(vectorizer, f_vec)

print("\nModel and Vectorizer saved to 'chatbot_model.pkl' and 'tfidf_vectorizer.pkl'")