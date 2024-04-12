from flask import Flask, render_template, request
from web_scrapping import get_content_from
from summarization import summarize_text

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "POST":
        url = request.form.get("url")
    return render_template("index.html")

@app.route('/', methods=['POST'])
def summarize():
    content = get_content_from(url)
    summary = summarize_text(content)
    print("Summary:", summary)  # Debugging print statement
    if summary:  # Check if summary is not empty
        return render_template('result.html', summary=summary)
    else:
        return "Failed to summarize the text."



if __name__ == '__main__':
    app.run(debug=True)
