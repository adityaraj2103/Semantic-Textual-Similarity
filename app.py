from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import PyPDF2
from simple import compare
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(filename)
        sentences = request.form['sentences']
        queries = re.split(r'(?<=[.!?])\s+', sentences)
        sentences_list = []
        with open(filename, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            text = ''
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                temp = page.extract_text()
                page_sentences = re.split(r'(?<=[.!?])\s+', temp)
                sentences_list.extend(page_sentences)
        text = {}
        for query in queries:
            text[query] = []
            for i in range(0, len(sentences_list)):
                score = compare(query, sentences_list[i])
                if score >= 0.8:
                    text[query].append(sentences_list[i])
        return render_template('result.html', dictionary=text)
    
    else: 
        return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
