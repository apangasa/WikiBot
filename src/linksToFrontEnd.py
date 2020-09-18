from flask import Flask, request
import urllib.parse
from flask_cors import CORS

start_title = "2013–14 Western Kentucky Hilltoppers basketball team"
end_title = "Helicobacter heilmannii sensu lato"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def start_and_end():
    start_link = urllib.parse.quote(start_title)
    end_link = urllib.parse.quote(end_title)

    URL = 'https://en.wikipedia.org/wiki/'
    data = {'start_link': URL + start_link,
            'end_link': URL + end_link}
    return data, 200
