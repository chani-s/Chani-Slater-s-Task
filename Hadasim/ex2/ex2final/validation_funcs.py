from datetime import datetime
from data_base import exec, retrieval


# Function to check if there are missing arguments
def check_missing_arguments(data, required_fields):
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    return True, "OK"


# Function to check the validation of the ID (according to the Israeli rules)
def check_personal_id(id_number):
    id_number = id_number.rjust(9, '0')
    checksum = sum((int(digit) * ((i % 2) + 1) if i % 2 == 0 else int(digit)) for i, digit in enumerate(id_number))
    if not checksum % 10 == 0 or len(id_number) > 9 or not id_number.isdigit():
        return False, "Invalid ID number"
    else:
        return True, "OK"


# Function to check the validation of dates parameters
def check_date_format(dates, date_format='%Y-%m-%d'):
    try:
        for date in dates:
            if datetime.strptime(date, date_format) > datetime.now():
                return False, "Invalid date - After current date"
    except ValueError:
        return False, f"Date parameter should be in format YYYY-MM-DD"

    return True, "OK"

# Function to check the validation of the add client request's parameters

def personal_validation(data, required_fields):
    is_missing = check_missing_arguments(data, required_fields)
    if not is_missing[0]:
        return False, is_missing[1]

    valid_id = check_personal_id(data['id'])
    if not valid_id[0]:
        return False, valid_id[1]

    primary_key_sql = "SELECT id FROM basic_details WHERE id = ?"
    if exec(primary_key_sql, [data['id']]):
        return False, "ID already exists"

    valid_date = check_date_format([data['birth_date']])
    if not valid_date[0]:
        return False, valid_date[1]

    else:
        return True, "OK"


# Function to check the validation of the add vaccination request's parameters
def covid_validation(data, required_fields):
    # Check missing values:
    is_missing = check_missing_arguments(data, required_fields)
    if not is_missing[0]:
        return False, is_missing[1]

    # Check the number of vaccinations for this ID:
    user_vaccinations = retrieval(data['id'], "covid_details")
    if len(user_vaccinations) > 3:
        return False, "The maximum number of vaccinations is 4!"

    # Check validation of ID number (According to Israel rules):
    valid_id = check_personal_id(data['id'])
    if not valid_id[0]:
        return False, valid_id[1]

    # Check if User exist in the basic_details data base:
    sql_query = "SELECT id FROM basic_details WHERE id = ?"
    if not exec(sql_query, [data['id']]):
        return False, "User ID does not exist in system!"

    primary_key_sql = """SELECT id, vaccination_date FROM covid_details WHERE id = ? 
                        AND vaccination_date = ?"""
    if exec(primary_key_sql, [data['id'], data['vaccination_date']]):
        return False, "Vaccination already exists"

    # Check dates formatting:
    vaccination = data['vaccination_date']
    positive = data['positive_date']
    recovery = data['recovery_date']
    valid_dates = check_date_format([vaccination, positive, recovery])
    if not valid_dates[0]:
        return False, valid_dates[1]

    # Check validation of dates:
    d_format = "%Y-%m-%d"
    if datetime.strptime(positive, d_format) > datetime.strptime(recovery, d_format):
        return False, "Recovery date before positive date"

    else:
        return True, "OK"


# Function to check the validation of GET parameters
def input_check(result, user_id):
    if not check_personal_id(user_id)[0]:
        return False, check_personal_id(user_id)[1]
    if not result:
        return False, 'User ID not exist'
    else:
        return True, 'OK'
