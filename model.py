from transformers import T5ForConditionalGeneration, T5Tokenizer

def generate_summary(input_text, min_length=30, max_length=150, num_beams=4, early_stopping=True):
    # initialize the model architecture and weights
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    # initialize the model tokenizer
    tokenizer = T5Tokenizer.from_pretrained("t5-base")

    # encode the text into tensor of integers using the appropriate tokenizer
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # generate the summarization output
    output = model.generate(inputs,
                             min_length=min_length,
                             max_length=max_length,
                             num_beams=num_beams,
                             early_stopping=early_stopping)
    
    # decode the generated output
    summary = tokenizer.decode(output[0], skip_special_tokens=True)
    return summary

# Example usage:
input_text = "Your input text goes here."
summary = generate_summary(input_text)
print(summary)
