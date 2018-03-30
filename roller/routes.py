from flask import render_template, flash, request, url_for
from roller import app
from roller.forms import rollForm
import lotwrollengine

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def roller():
    form = rollForm()
    if form.validate_on_submit():
        dice = form.numberDice.data
        results = lotwrollengine.roll(dice)
        for result in results:
            flash(result)
    return render_template('roll.html', form=form)
