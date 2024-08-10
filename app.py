from flask import Flask, render_template, request
import nltk
from newspaper import Article

app = Flask(__name__)

nltk.download('punkt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_article', methods=['POST'])
def get_article():
    url = request.form['url']
    article = Article(url)
    
    try:
        article.download()
        article.parse()
        article.nlp()

        title = article.title
        authors = ', '.join(article.authors)
        summary = article.summary

        return render_template('index.html', title=title, authors=authors, summary=summary)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
