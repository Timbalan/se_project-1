from transformers import pipeline

pipe = pipeline(model="sberbank-ai/rugpt3large_based_on_gpt2")

print(pipe("джедаи")[0]['generated_text'])