from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd

# Load the trained model
model = load_model('sql_injection_detection_model.h5')

# Load the tokenizer (assuming you have saved it during training)
tokenizer = load_tokenizer('tokenizer.pickle')

# Function to preprocess input data
def preprocess_input(sql_payloads, tokenizer):
    max_sequence_length =  # Set the max sequence length based on your training
    sequences = tokenizer.texts_to_sequences(sql_payloads)
    padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')
    return padded_sequences

# Function to predict SQL injection for a list of payloads
def predict_top_sql_injections(sql_payloads, model, tokenizer, top_n=3):
    # Preprocess input
    input_sequences = preprocess_input(sql_payloads, tokenizer)

    # Make predictions for all input sequences
    probabilities = model.predict(input_sequences)

    # Get the top N predictions and their corresponding labels
    top_predictions = []
    for prob_list in probabilities:
        sorted_indices = sorted(range(len(prob_list)), key=lambda k: prob_list[k], reverse=True)[:top_n]
        labels = ["Potential SQL injection" if idx == 1 else "Safe input" for idx in sorted_indices]
        top_predictions.append(list(zip(labels, prob_list[sorted_indices])))

    return top_predictions

# Example usage
sql_payloads = [
    "SELECT * FROM users",
    "1 or sleep(5)#",
    "INSERT INTO users VALUES (1, 'John Doe')"
]

top_predictions = predict_top_sql_injections(sql_payloads, model, tokenizer, top_n=3)

for i, sql_payload in enumerate(sql_payloads):
    print(f"SQL Payload {i+1}: {sql_payload}")
    print(f"Top Predictions: {top_predictions[i]}\n")
