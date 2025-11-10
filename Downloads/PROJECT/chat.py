import pickle
import random
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# ====================================================================
#  BOT RESPONSE DICTIONARY
#  Copy and paste this into your 'chat.py' file
# ====================================================================

responses = {
    # --- Order Management ---
    "cancel_order": [
        "I can help with that. To cancel your order, I'll need your order number.",
        "To request a cancellation, please provide your order number and the reason."
    ],
    "change_order": [
        "To make changes to an existing order, please contact our support team directly. Would you like me to connect you?",
        "Order modifications are possible within 2 hours of placing it. What is your order number?"
    ],
    "place_order": [
        "You can place an order by browsing our products, adding items to your cart, and proceeding to checkout.",
        "Ready to order? Just add the items you want to your cart and click 'Checkout'!"
    ],
    "track_order": [
        "I can track your order for you. What is your order number?",
        "To get your order status, please enter your order number or tracking number."
    ],

    # --- Shipping & Delivery ---
    "change_shipping_address": [
        "You can change your shipping address in your 'Account Settings' under 'Addresses'.",
        "If the order has not yet shipped, I can help update the address. What is your order number?"
    ],
    "set_up_shipping_address": [
        "To add a new shipping address, please go to your 'Account Profile' > 'Addresses' > 'Add New'.",
        "You can set up your default shipping address in your account settings."
    ],
    "delivery_options": [
        "We offer Standard, Express, and Next-Day shipping. You can see the options and costs at checkout.",
        "Shipping options vary by location. Please enter your address at checkout to see what's available."
    ],
    "delivery_period": [
        "Standard shipping typically takes 3-5 business days. Express shipping is 1-2 business days.",
        "Your estimated delivery date is provided in your order confirmation email."
    ],

    # --- Payments & Refunds ---
    "check_cancellation_fee": [
        "There is no fee for cancelling an order before it has shipped.",
        "We do not charge a cancellation fee, but please note that custom orders may be an exception."
    ],
    "check_payment_methods": [
        "We accept all major credit cards (Visa, MasterCard, Amex), PayPal, and Google Pay.",
        "You can find a full list of our accepted payment methods on our checkout page."
    ],
    "payment_issue": [
        "I'm sorry to hear you're having payment trouble. Could you please tell me the error message you're seeing?",
        "If your payment was declined, please double-check your card details or try a different payment method."
    ],
    "check_refund_policy": [
        "We offer a 30-day money-back guarantee on most items. You can read our full refund policy on our website.",
        "Our policy is a full refund for items returned within 30 days in their original condition."
    ],
    "get_refund": [
        "To request a refund for a completed order, please visit your order history and select 'Request Refund'.",
        "I can help start a refund request. What is your order number?"
    ],
    "track_refund": [
        "Refunds are typically processed within 5-7 business days after we receive your returned item.",
        "You can check the status of your refund in your account's 'Order History' page."
    ],

    # --- Invoices ---
    "check_invoices": [
        "You can view all your past invoices in your account dashboard under 'My Invoices'.",
        "To see your invoices, log in to your account and go to 'Order History'."
    ],
    "get_invoice": [
        "I can send you a copy of your invoice. Which order number is it for?",
        "A copy of your invoice was sent to your email. I can also resend it if you provide the order number."
    ],

    # --- Account Management ---
    "create_account": [
        "You can create an account by clicking the 'Sign Up' button on our homepage. It's free!",
        "To register, just click 'Create Account' and fill in your email and a new password."
    ],
    "delete_account": [
        "To delete your account, please go to 'Settings' > 'Privacy' > 'Delete Account'. Please note this is permanent.",
        "I can submit a request to delete your account. Are you sure you wish to proceed?"
    ],
    "edit_account": [
        "You can edit your account details, like your name and phone number, in your 'Account Settings' page.",
        "To update your profile, log in and visit your 'Account Dashboard'."
    ],
    "recover_password": [
        "No problem! You can reset your password by clicking the 'Forgot Password' link on the login page.",
        "To recover your password, please go to the login page and click 'I forgot my password'."
    ],
    "registration_problems": [
        "I'm sorry you're having trouble. Could you tell me what error you are seeing while trying to register?",
        "If you can't register, please ensure your email isn't already in use and that your password meets the requirements."
    ],
    "switch_account": [
        "To switch accounts, please 'Log Out' of your current session and then 'Log In' with your other account.",
        "You can sign out and sign back in with a different account at any time."
    ],

    # --- Support & Feedback ---
    "complaint": [
        "I am very sorry to hear that. Please tell me what happened so I can document it and help you.",
        "I understand you'd like to file a complaint. I am here to listen and will forward your feedback to the right team."
    ],
    "contact_customer_service": [
        "You can contact our customer service team by phone at 1-800-555-1234 or by email at support@example.com.",
        "Our support team is available 24/7. Would you like me to connect you?"
    ],
    "contact_human_agent": [
        "I understand. Let me connect you to a human agent who can better assist you.",
        "One moment please, I am transferring you to a live support agent."
    ],
    "review": [
        "We'd love to hear your feedback! You can leave a review on any product page or on our 'Testimonials' page.",
        "Thank you for your feedback! You can leave a review for your product by visiting your 'Order History'."
    ],

    # --- Other ---
    "newsletter_subscription": [
        "You can subscribe to our newsletter by entering your email at the bottom of our homepage.",
        "To get updates on sales and new products, just sign up for our newsletter!"
    ],

    # --- Fallback (Default) ---
    "fallback": [
        "I'm sorry, I don't quite understand that. Can you please rephrase?",
        "My apologies, I'm not trained to handle that specific request.",
        "I don't have the answer for that. Would you like to speak to a human agent?"
    ]
}

# --- 2. LOAD YOUR SAVED MODEL AND VECTORIZER ---
with open('chatbot_model.pkl', 'rb') as f_model:
    model = pickle.load(f_model)

with open('tfidf_vectorizer.pkl', 'rb') as f_vec:
    vectorizer = pickle.load(f_vec)

# --- 3. COPY YOUR PREPROCESSING FUNCTION ---
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # 1. Lowercasing
    text = text.lower()
    # 2. Remove non-alphabetic characters
    text = re.sub(r'[^a-zA-Z\s]', '', text, flags=re.I|re.A)
    # 3. Tokenization
    tokens = word_tokenize(text)
    # 4. Stop-word removal and Lemmatization
    cleaned_tokens = []
    for token in tokens:
        if token not in stop_words:
            cleaned_tokens.append(lemmatizer.lemmatize(token))
    # 5. Join tokens back into a single string
    return " ".join(cleaned_tokens)

# --- 4. CREATE FUNCTIONS TO GET PREDICTION AND RESPONSE ---
def get_prediction(text):
    # Preprocess the user's text
    cleaned_text = preprocess_text(text)
    
    # Vectorize the cleaned text
    text_vector = vectorizer.transform([cleaned_text])
    
    # Get the model's prediction
    prediction = model.predict(text_vector)
    
    return prediction[0] # The prediction is an array, get the first item

def get_bot_response(intent):
    if intent in responses:
        # Pick a random response from the list
        return random.choice(responses[intent])
    else:
        # Use the fallback if the intent isn't in our map
        return random.choice(responses["fallback"])

# --- 5. CREATE THE CHAT LOOP ---
print("Bot is ready! Type 'quit' to exit.")
while True:
    # Get user input
    user_input = input("You: ")
    
    if user_input.lower() == 'quit':
        print("Bot: Goodbye!")
        break
        
    # Get the predicted intent
    intent = get_prediction(user_input)
    
    # Get the bot's response
    response = get_bot_response(intent)
    
    print(f"Bot: {response}")