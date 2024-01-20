from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import re

# Load the trained model
model = load_model('sql_injection_detection_model.h5')

# Load the tokenizer (assuming you have saved it during training)
tokenizer = load_tokenizer('tokenizer.pickle')

# Function to preprocess input data
def preprocess_input(user_input, tokenizer):
    # Tokenize and pad sequences
    max_sequence_length =  # Set the max sequence length based on your training
    sequence = tokenizer.texts_to_sequences([user_input])
    padded_sequence = pad_sequences(sequence, maxlen=max_sequence_length, padding='post')
    return padded_sequence

# Function to predict SQL injection
def predict_sql_injection(user_input, model, tokenizer):
    # Preprocess input
    input_sequence = preprocess_input(user_input, tokenizer)

    # Make a prediction
    probability = model.predict(input_sequence)[0, 0]

    # Set a threshold (e.g., 0.5)
    threshold = 0.5

    # Classify based on the threshold
    if probability > threshold:
        return "Potential SQL injection detected"
    else:
        return "Input processed successfully"

# Example usage
new_data = pd.Series(["SELECT * FROM users", "1 or sleep(5)#", "INSERT INTO users VALUES (1, 'John Doe')"])

for user_input in new_data:
    result = predict_sql_injection(user_input, model, tokenizer)
    print(f"User Input: {user_input} - Result: {result}")
