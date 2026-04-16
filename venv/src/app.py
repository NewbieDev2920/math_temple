from flask import Flask, render_template
import json
import random
import datetime
import os

app = Flask(__name__)

# Daily selection state
daily_cache = {
    "date": None,
    "selection": {}
}

class Question:
    def __init__(self, question, answer, type, image=None):
        self.question = question
        self.answer = answer
        self.type = type
        self.image = image

    @classmethod
    def from_dict(cls, d, type_str):
        return cls(d.get('question', ''), d.get('answer', ''), type_str, d.get('image', None))

class Quote:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    @classmethod
    def from_dict(cls, d):
        return cls(d.get('quote', ''), d.get('author', ''))

def load_json_data(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'data', filename)
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_daily_selection():
    global daily_cache
    current_date = datetime.date.today()
    
    # If the date has changed, randomly select new items (uniform distribution over the banks)
    if daily_cache['date'] != current_date:
        defs_data = load_json_data('definitions.json')
        theos_data = load_json_data('theorems.json')
        proofs_data = load_json_data('proofs.json')
        comps_data = load_json_data('computations.json')
        quotes_data = load_json_data('quotes.json')

        definition = random.choice(defs_data) if defs_data else {"question": "No definitions found.", "answer": ""}
        theorem = random.choice(theos_data) if theos_data else {"question": "No theorems found.", "answer": ""}
        proof = random.choice(proofs_data) if proofs_data else {"question": "No proofs found.", "answer": ""}
        computation = random.choice(comps_data) if comps_data else {"question": "No computations found.", "answer": ""}
        quote_item = random.choice(quotes_data) if quotes_data else {"quote": "No quotes found.", "author": ""}

        daily_cache['date'] = current_date
        daily_cache['selection'] = {
            'definition': Question.from_dict(definition, "Definition"),
            'theorem': Question.from_dict(theorem, "Theorem"),
            'proof': Question.from_dict(proof, "Proof"),
            'computation': Question.from_dict(computation, "Computation"),
            'quote': Quote.from_dict(quote_item)
        }

    return daily_cache['selection']

@app.route('/')
def index():
    selection = get_daily_selection()
    return render_template('index.html', selection=selection)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
