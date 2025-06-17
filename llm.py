from langchain.llms import HuggingFacePipeline
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

def load_llm():
    model_id = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    text_gen = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_new_tokens=200)
    return HuggingFacePipeline(pipeline=text_gen)

