from flask import Flask, request, redirect

app = Flask(__name__)

# A simple in-memory dictionary to store short -> long URLs
url_mapping = {}

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.json
    long_url = data.get('url')
    short_id = str(len(url_mapping) + 1)
    url_mapping[short_id] = long_url
    return {'short_url': f'http://localhost:5000/{short_id}'}, 201

@app.route('/<short_id>')
def redirect_url(short_id):
    long_url = url_mapping.get(short_id)
    if long_url:
        return redirect(long_url)
    return {'error': 'URL not found'}, 404

if __name__ == '__main__':
    app.run(debug=True)
