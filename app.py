from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form.get('input_url')
        if url:
            match = re.search(r'suno\.com\/song\/([a-f0-9-]+)', url)
            if match:
                song_id = match.group(1)
                result = f"https://cdn1.suno.ai/{song_id}.mp3"
            else:
                result = "Invalid URL"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
