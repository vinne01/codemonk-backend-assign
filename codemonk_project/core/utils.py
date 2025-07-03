import re

def tokenize_text(text):
    return re.findall(r'\w+', text.lower())

def split_paragraphs(text):
    return [p.strip() for p in text.strip().split("\n\n") if p.strip()]
