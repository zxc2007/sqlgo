"""
# SQLGO License - Version 1.1

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
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
