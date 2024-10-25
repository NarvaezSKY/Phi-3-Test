# main.py

from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Define the path to the model directory
model_directory = "/app/models/Phi-3-mini-4k-instruct"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_directory)
print("Tokenizer loaded.")

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(model_directory)
print("Model loaded.")

# Function to generate response
def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=512, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'No prompt provided.'}), 400
    response = generate_response(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)