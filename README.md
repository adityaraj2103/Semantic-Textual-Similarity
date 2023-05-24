# PDF Sentence Comparison

This Flask application allows you to compare sentences provided by the user with the sentences extracted from a PDF file. It uses the SentenceTransformer library to compute similarity scores between the sentences and displays the results in a dictionary format.
The model used in this project is **'multi-qa-mpnet-base-dot-v1'**. It is a sentence-transformers model: It maps sentences & paragraphs to a 768 dimensional dense vector space and was designed for semantic search. It has been trained on 215M (question, answer) pairs from diverse sources. 

## Installation

1. Clone the repository:
```
git clone https://github.com/your_username/your_repository.git
```

2. Install the required dependencies:
```
pip install -U sentence-transformers
pip install flask
pip install pyPDF2
```

## Usage

1. Run the Flask application:
```python app.py```

2. Access the application in your web browser:
http://localhost:5000/


3. Upload a PDF file and enter a list of sentences to compare.

4. Click the "Submit" button.

5. The application will extract sentences from the PDF file, compare them with the provided sentences, and display the results in a dictionary format.

## Directory Structure

The project directory should have the following structure:

├── app.py
├── templates
│ ├── index.html
│ └── result.html
├── simple.py
└── README.md


- `app.py`: The Flask application file that handles the web routes and form submission.
- `templates`: Directory containing HTML templates for the application.
  - `index.html`: The main page template with a form to upload the PDF file and enter sentences.
  - `result.html`: The template to display the comparison results in a dictionary format.
- `simple.py`: A Python module containing the `compare` function for sentence comparison.
- `README.md`: This file, providing instructions and information about the application.

## Dependencies

- Flask: A micro web framework for Python.
- PyPDF2: A library for extracting text and metadata from PDF files.
- SentenceTransformer: A library for encoding and comparing sentences.

## References

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- PyPDF2: [https://github.com/mstamy2/PyPDF2](https://github.com/mstamy2/PyPDF2)
- SentenceTransformer: [https://www.sbert.net/](https://www.sbert.net/)

