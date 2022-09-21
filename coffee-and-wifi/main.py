from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, InputRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[InputRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[URL(message="Invalid URL")])
    open_time = StringField('Opening Time (e.g. 8AM)', validators=[DataRequired()])
    close_time = StringField('Closing Time (e.g. 5:30PM)', validators=[DataRequired()])
    cafe_rating = SelectField('Cafe Rating', choices=[('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')], validators=[DataRequired()])
    wifi_rating = SelectField('WIFI Rating', choices=[('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')], validators=[DataRequired()])
    power_rating = SelectField('Power Socket Availability Rating', choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        data_row = [form.cafe.data, form.location.data, form.open_time.data, form.close_time.data, form.cafe_rating.data, form.wifi_rating.data, form.power_rating.data]
        print(data_row)
        with open('cafe-data.csv', 'a', encoding='UTF-8', newline='') as data:
            write_obj = csv.writer(data)
            write_obj.writerow(data_row)
            data.close()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', 'r', encoding="utf-8", newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
