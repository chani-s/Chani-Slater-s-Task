from flask import Flask, request, jsonify

from data_base import create_table, insert_basic_data, insert_covid_data, retrieval, non_vaccination_sum
from validation_funcs import personal_validation, covid_validation, input_check

app = Flask(__name__)

# Function to get details of the client with the given ID
@app.route('/api/get_details/<user_id>', methods=['GET'])
def get_personal_details(user_id):
    result = retrieval(user_id, "basic_details")
    if not input_check(result, user_id)[0]:
        return jsonify({'Error': input_check(result, user_id)[1]}), 400
    return jsonify(result)


# Function to get vaccinations details of the client with the given ID
@app.route('/api/get_vaccinations/<user_id>', methods=['GET'])
def get_vaccinations_details(user_id):
    result = retrieval(user_id, "covid_details")
    if not input_check(result, user_id)[0]:
        return jsonify({'Error': input_check(result, user_id)[1]}), 400
    return jsonify(result)


# Function to get the number of the non vaccinated clients
@app.route('/api/get_non_vaccinated_number', methods=['GET'])
def get_non_vaccinated_number():
    non_vaccinated_number = non_vaccination_sum()
    return jsonify({'Number of non vaccinated': non_vaccinated_number})


# Function to add basic personal details of clients
@app.route('/api/add_personal_details', methods=['POST'])
def add_personal_details():
    data = request.get_json()
    create_table()
    validate = personal_validation(data, ('id', 'first_name', 'last_name', 'city', 'street', 'birth_date', 'phone', 'mobile'))
    if validate[0]:
        first_name = data['first_name']
        last_name = data['last_name']
        text = f'Added {first_name} {last_name}!'
        try:
            insert_basic_data(data['id'], first_name, last_name, data['city'],
                                data['street'], data['birth_date'],
                                data['phone'], data['mobile'])
            return jsonify({'Successful!': text})
        except Exception as e:
            print("Error:", e)
            return jsonify({'Error': str(e)}), 400
    else:
        return jsonify({'Error': validate[1]}), 400


# Function to add vaccinations details of clients
@app.route('/api/add_covid_details', methods=['POST'])
def add_covid_details():
    data = request.get_json()
    create_table()
    validate = covid_validation(data, ('id', 'vaccination_date',
                                       'vaccination_factory', 'positive_date', 'recovery_date'))
    if validate[0]:
        try:
            insert_covid_data(data['id'], data['vaccination_date'], data['vaccination_factory'],
                              data['positive_date'], data['recovery_date'])
            text = f'added vaccination for {data["id"]}!'
            return jsonify({'Successful': text})
        except Exception as e:
            print("Error:", e)
            return jsonify({'Error': str(e)}), 400
    else:
        return jsonify({'Error': validate[1]}), 400


if __name__ == '__main__':
    app.run(debug=True)
