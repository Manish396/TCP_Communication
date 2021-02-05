from flask import Flask
app = Flask(__name__)
app.config.from_object('config.Config')
@app.route('/')
def hello_world():
    return 'hello, World!'
def start_ngrok():
    from pyngrok import ngrok
    url = ngrok.connect(5000)
    print("Tunnel url:", url)
if app.config['START_NGROK']:
    start_ngrok()
if __name__ == '__main__':
    app.run()
    