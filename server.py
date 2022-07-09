from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'my secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def survey():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['user_location']
    session['language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def result():
    return render_template('results.html', user_name=session['name'], user_location=session['location'], user_language=session['language'] ,user_comment=session['comment'])

if __name__ == '__main__':
    app.run(debug=True)