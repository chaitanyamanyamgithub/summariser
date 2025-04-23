from flask import Flask, render_template, request, jsonify
import re
import os

# Get the absolute path to the template and static folders
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'app', 'templates')
static_dir = os.path.join(base_dir, 'app', 'static')

# Initialize Flask app with absolute paths
app = Flask(__name__, 
            template_folder=template_dir,
            static_folder=static_dir)

def simple_summarize(text, max_length=150, min_length=30):
    # Split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Calculate the number of sentences to include based on max_length
    num_sentences = max(min(len(sentences) // 3, max_length // 20), min_length // 20)
    
    # Take first sentence as it's often important (introduction)
    summary = [sentences[0]]
    
    # Add more sentences from the middle and end
    if len(sentences) > 2:
        middle_sentences = sentences[1:min(num_sentences, len(sentences)-1)]
        summary.extend(middle_sentences)
    
    # Return joined summary
    return " ".join(summary)

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
        # Generate summary using simple algorithm
        summary = simple_summarize(text, max_length, min_length)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Add route to check if server is running
@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    # Print debug information
    print(f"Template directory: {template_dir}")
    print(f"Static directory: {static_dir}")
    print(f"Template exists: {os.path.exists(os.path.join(template_dir, 'index.html'))}")
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 