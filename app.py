from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__)

# Initialize summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    max_length = data.get('max_length', 150)
    min_length = data.get('min_length', 30)
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Handle long texts by splitting into chunks if necessary
    max_words = 1024
    if len(text.split()) > max_words:
        return jsonify({'error': f'Text too long. Please provide a shorter text (max {max_words} words).'}), 400
    
    try:
        # Generate summary
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return jsonify({'summary': summary[0]['summary_text']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 