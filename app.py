from flask import*

app=Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')

if __name__=='__main__':
    app.run(debug=True)

