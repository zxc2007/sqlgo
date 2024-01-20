import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the trained model
model_path = "/Users/alimirmohammad/sqlgo/ML/sql_injection_detection_model_20240120003016.h5q"
model = load_model(model_path)

# Assuming you have the tokenizer saved during training
# If not, you can load it from the saved model
tokenizer = Tokenizer()
max_sequence_length = 100  # Use the same max_sequence_length used during training

# Function to preprocess input data
def preprocess_input(text, tokenizer, max_sequence_length):
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=max_sequence_length, padding='post')
    return padded_sequence

# Function to predict SQL injection patterns
def predict_sql_injection(text, model, tokenizer, max_sequence_length):
    preprocessed_text = preprocess_input(text, tokenizer, max_sequence_length)
    prediction = model.predict(preprocessed_text)
    return prediction[0][0]

# Example usage
input_payload = "SELECT * FROM users WHERE username = 'admin';"

# Make prediction
prediction = predict_sql_injection(input_payload, model, tokenizer, max_sequence_length)
print(f"Predicted Probability of SQL Injection: {prediction}")
