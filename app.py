from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode
from werkzeug.datastructures import MultiDict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    urls = []
    if request.method == 'POST':
        raw_urls = request.form.get('urls', '').splitlines()
        for url in raw_urls:
            img = qrcode.make(url)
            buffered = BytesIO()
            img.save(buffered)
            img_str = b64encode(buffered.getvalue()).decode("utf-8")
            urls.append({'url': url, 'qr': img_str})
    return render_template('index.html', urls=urls)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8881, debug=True)
