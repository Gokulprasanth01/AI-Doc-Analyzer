from transformers import BartTokenizer, BartForConditionalGeneration

# Load pre-trained model and tokenizer
tokenizer_bart = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model_bart = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

def summarize_text(text):
    inputs = tokenizer_bart.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model_bart.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer_bart.decode(summary_ids[0], skip_special_tokens=True)
    return summary
