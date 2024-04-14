from flask import Flask, render_template, request
from web_scrapping import get_content_from
from summarization import summarize_text
from translator import translate_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def summarize():
    url = request.form.get("url")
    target_language = request.form.get("language")
    content = get_content_from(url)
    summary = summarize_text(content)
    print("Summary:", summary)  # Debugging print statement
    if summary:  # Check if summary is not empty
        translated_summary = translate_text(summary, target_lang=target_language)
        return render_template('result.html', summary=translated_summary)
    else:
        return "Failed to summarize the text."



if __name__ == '__main__':
    app.run(debug=True)
