from flask import Flask, send_file
from flask_cors import CORS
from wordcloud import WordCloud
import io

app = Flask(__name__)
CORS(app)

@app.route("/wordcloud-image")
def wordcloud_image():
    word_counts = {
        "Python": 50, "React": 30, "Flask": 20,
        "JavaScript": 40, "HTML": 25, "CSS": 35
    }

    wc = WordCloud(width=800, height=400, background_color="white")
    wc.generate_from_frequencies(word_counts)

    img_io = io.BytesIO()
    wc.to_image().save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
