import os
import requests
import urllib.parse

from flask import Flask, request

app = Flask(__name__)


########
# Ping #
########

@app.route('/ping/', methods=['GET','POST'])
@app.route('/ping', methods=['GET','POST'])
def ping():

    # get url
    url = os.environ.get('URL', None)
    
    # check url
    if url is None:
        return 'No url', 404
    
    # get content
    content = request.full_path
    
    # check no content
    if '?' not in content:
        return 'No content', 404
    content = content[content.index('?')+1:].strip()
    if content == '':
        return 'Empty content', 404
    
    # decode content
    content = urllib.parse.unquote(content)
    
    # do request
    r = requests.post(url, json={"content":content})
    
    # return same response
    return r.content, r.status_code, r.headers.items()

###################
# Invalid request #
###################

app.config['TRAP_HTTP_EXCEPTIONS'] = True


@app.errorhandler(Exception)
def invalid(e):
    return f'Invalid request: {repr(e)}', 404


########
# Main #
########

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
