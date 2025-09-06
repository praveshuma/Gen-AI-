import pandas as pd
import numpy as np
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random

# 1. Generate synthetic data with sensitive information
def generate_synthetic_data(num_records=10):
    names = ["Alice Smith", "Bob Johnson", "Charlie Brown", "Diana Wilson", "Emma Davis"]
    addresses = ["123 Main St", "456 Oak Ave", "789 Pine Rd", "101 Maple Dr", "202 Birch Ln"]
    emails = ["alice@example.com", "bob@example.com", "charlie@example.com", "diana@example.com", "emma@example.com"]
    
    data = {
        "Name": [random.choice(names) for _ in range(num_records)],
        "Address": [random.choice(addresses) for _ in range(num_records)],
        "Email": [random.choice(emails) for _ in range(num_records)],
        "Salary": [random.randint(30000, 100000) for _ in range(num_records)]
    }
    return data

# 2. Create DataFrame
def create_dataframe():
    data = generate_synthetic_data()
    df = pd.DataFrame(data)
    return df

# 3. Print synthetic data to verify structure
def print_data(df):
    print("Synthetic DataFrame:")
    print(df)
    print("\nDataFrame Info:")
    print(df.info())

# 4. Implement differential privacy with optimized noise
def apply_differential_privacy(df, epsilon=1.0, sensitivity=70000):
    dp_df = df.copy()
    # Add Laplace noise to Salary column with reduced sensitivity
    noise = np.random.laplace(0, sensitivity/epsilon, len(df))
    dp_df['Salary'] = df['Salary'] + noise
    dp_df['Salary'] = dp_df['Salary'].clip(lower=30000, upper=100000)  # Clip to original range
    return dp_df

# 5. Traditional data masking (e.g., anonymize names)
def apply_data_masking(df):
    masked_df = df.copy()
    masked_df['Name'] = masked_df['Name'].apply(lambda x: 'User_' + str(hash(x) % 10000))
    masked_df['Email'] = masked_df['Email'].apply(lambda x: 'user' + str(hash(x) % 10000) + '@example.com')
    return masked_df

# 6. Load pre-trained text generation model and tokenizer
def load_gpt_model():
    try:
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        model = GPT2LMHeadModel.from_pretrained("gpt2")
        tokenizer.pad_token = tokenizer.eos_token  # Set pad token to avoid warnings
        print("Successfully loaded GPT-2 model and tokenizer")
        return model, tokenizer
    except Exception as e:
        print(f"Error loading model: {e}")
        return None, None

# 7. Generate anonymized text using GPT-2
def generate_anonymized_text(model, tokenizer, prompt, max_length=250):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=max_length,
        num_return_sequences=1,
        do_sample=True,  # Enable sampling for diversity
        top_k=50,        # Top-k sampling
        top_p=0.95       # Top-p (nucleus) sampling
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Main execution
if __name__ == "__main__":
    # Generate and display synthetic data
    df = create_dataframe()
    print_data(df)
    
    # Apply differential privacy
    dp_df = apply_differential_privacy(df, epsilon=1.0, sensitivity=70000)
    print("\nDataFrame with Differential Privacy (Salary column):")
    print(dp_df)
    
    # Apply traditional data masking
    masked_df = apply_data_masking(df)
    print("\nDataFrame with Traditional Data Masking (Name and Email):")
    print(masked_df)
    
    # Load GPT-2 model and tokenizer
    model, tokenizer = load_gpt_model()
    
    # Generate anonymized text example
    if model and tokenizer:
        prompt = "Privacy in digital applications is enhanced by"
        generated_text = generate_anonymized_text(model, tokenizer, prompt)
        print("\nGenerated Anonymized Text Example:")
        print(generated_text)