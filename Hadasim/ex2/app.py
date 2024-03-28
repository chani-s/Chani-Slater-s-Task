from flask import Flask, render_template, request
import data_base

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('basic.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    last_name = request.form['last_name']
    id = request.form['id']
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    address = f"{street}, {city}, {state}"
    b_date = request.form['dob']
    phone = request.form['phone']
    data_base.insert_basic_data(id, name, last_name, address, b_date, phone)
    return f'Hello, {name} {last_name}.\nYour details added to repository!'


@app.route('/covid')
def covid():
    render_template('vaccination_details.html')


@app.route('/covid/submission', methods=['POST'])
def covid_details():
    id = request.form['id']
    vaccination_date = request.form['v_date']
    vaccination_factory = request.form['v_factory']
    positive_date = request.form['p_date']
    data_base.insert_vaccination_data(id, vaccination_date, vaccination_factory, positive_date)
    name = data_base.my_execute("select first_name from basic_details where id = basic_details.id")
    return f'Hello, {name}.\nYour details added to repository!'


if __name__ == '__main__':
    app.run(debug=True)
