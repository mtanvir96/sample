from flask import Flask, Response
import requests

app = Flask(__name__)

CONTENT_TYPE = str('text/plain; version=0.0.4; charset=utf-8')

URLS = [
    'https://httpstat.us/200',
    'https://httpstat.us/503'
]

RESPONSE_HEADER1 = 'sample_external_url_up'
RESPONSE_HEADER2 = 'sample_external_url_response_ms'

@app.route('/metric', methods=['GET'])
def get_stats():

    result = []
    for url in URLS:
        response = requests.get(url)
        responseTime = response.elapsed.microseconds / 1000
        if response.status_code == 200:
            output1 = RESPONSE_HEADER1 + '{url="' + url + '"} = 1'
            output2 = RESPONSE_HEADER2 + '{url="' + url + '"} = ' + str(responseTime)
        elif response.status_code == 503:
            output1 = RESPONSE_HEADER1 + '{url="' + url + '"} = 0'
            output2 = RESPONSE_HEADER2 + '{url="' + url + '"} = ' + str(responseTime)
        else:
            # Not preocessing any other response
            continue    

        result.append(output1)
        result.append(output2)

    output = "\n".join(result)

    return Response(output, mimetype=CONTENT_TYPE) 

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')