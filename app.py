from flask import Flask, render_template

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static/dist',
    template_folder='templates',
)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 5500,debug=True)