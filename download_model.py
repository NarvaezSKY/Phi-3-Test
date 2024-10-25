from transformers import AutoTokenizer, AutoModelForCausalLM
import os

def download_model(model_name, save_directory):
    print(f"Downloading model '{model_name}'...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    os.makedirs(save_directory, exist_ok=True)
    tokenizer.save_pretrained(save_directory)
    model.save_pretrained(save_directory)
    print(f"Model saved to '{save_directory}'.")

if __name__ == "__main__":
    MODEL_NAME = "Microsoft/Phi-3-mini-4k-instruct"
    SAVE_DIRECTORY = "./models/Phi-3-mini-4k-instruct"
    download_model(MODEL_NAME, SAVE_DIRECTORY)
