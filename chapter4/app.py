from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/mypage')
def mypage():
   return 'This is my Page!'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)