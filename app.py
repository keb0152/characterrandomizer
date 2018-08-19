from flask import Flask, request
from flask import render_template
from flask_bootstrap import Bootstrap
from theapp import models


app = Flask(__name__)
bootstrap = Bootstrap(app)
CharacterMaker = models.characterMaker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/defaults', methods=['GET','POST'])
def defaultValues():
    if request.method == 'POST':
        values = {'sex': None,
                  'age': None,
                  'gender': None,
                  'race': None}
        doSex = request.values.get('doSex')
        doAge = request.values.get('doAge')
        doGender = request.values.get('doGender')
        doRace = request.values.get('doRace')
        if doSex:
            values['sex'] = CharacterMaker.sexuality()
        if doAge:
            values['age'] = CharacterMaker.age()
        if doGender:
            values['gender'] = CharacterMaker.gender()
        if doRace:
            values['race'] = CharacterMaker.race()
        return render_template('useDefaults.html', age = values['age'], sex = values['sex'],
                                                   gender = values['gender'], race = values['race'])
    else:
        return render_template('useDefaults.html')

@app.route('/notDefaults', methods=['GET','POST'])
def noDefaultValues():
    return render_template('dontUseDefaults.html')


if __name__ == '__main__':
    app.run()