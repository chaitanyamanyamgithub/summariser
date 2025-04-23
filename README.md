# AI Text Summarizer

A modern web application that uses AI to summarize text. Built with Python (Flask) and a responsive frontend.

## Features

- **AI-Powered Summarization**: Utilizes Hugging Face's advanced transformer models to create concise summaries
- **Modern UI**: Clean and responsive design with animations and intuitive controls
- **Real-time Processing**: Asynchronous processing with loading indicators for better user experience
- **Copy to Clipboard**: One-click copy functionality for the generated summary
- **Error Handling**: Comprehensive error handling for a smooth user experience

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone this repository or download the code
2. Navigate to the project directory

```bash
cd summariser
```

3. Install the required Python packages

```bash
pip install -r requirements.txt
```

This will install all necessary dependencies including Flask and the transformer models.

## Running the Application

Start the application by running:

```bash
python app.py
```

The server will start, and you can access the application at [http://localhost:5000](http://localhost:5000) in your web browser.

## How to Use

1. Visit the application in your web browser
2. Paste the text you want to summarize in the input area
3. Click the "Summarize" button
4. Wait for the AI to process your text (a loading indicator will be displayed)
5. View the generated summary on the right side
6. Use the "Copy" button to copy the summary to your clipboard
7. Use the "Clear" button to start over

## Technical Details

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (with Bootstrap 5)
- **AI Model**: facebook/bart-large-cnn from Hugging Face Transformers
- **Styling**: Custom CSS with responsive design

## Limitations

- The current implementation has a text limit of 1024 words for summarization
- Processing time depends on the length of the input text and server resources

## License

This project is open source and available under the MIT License. 