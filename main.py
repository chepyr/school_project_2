import os

from forms.getPoints import GetPointsForm
from flask import Flask, render_template_string, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JHDBOsdhc98dbHBASJwxkOaw89d3bq2'


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/shortest_path', methods=['GET', 'POST'])
def shortest_path():
    form = GetPointsForm()
    if form.is_submitted():
        points = form.points.data
        return render_template("shortest_path_get.html")
    else:
        return render_template('for_tests.html', form=form)





if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
