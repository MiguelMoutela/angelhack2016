import os
import datetime
import json

import pandas as pd

DOB_dict = {
    "english": "date of birth",
    "spanish": "fecha de nacimiento",
    "italian": "data de nascimento",
    "french": "date de naissance",
    "german": "Geburtsdatum"
}

gender_dict = {
    "english": "gender",
    "spanish": "genero",
    "italian": "genere",
    "french": "sexe",
    "german": "Geschlecht"
}

questions = {
    1: "How can I help you?",
    2: "When has started this head ache?",
    3: "Hours, Days, Months?",
    4: "Was it developed suddenly or over time?'",
    5: "Has it been instant?",
    6: "Around or a specific place?",
    7: "Has the pain changed since it started?",
    8: "Can you describe the type of pain?",
    9: "The pain moves?",
    10: "What, makes the pain better?",
    11: "What, makes the pain worse?",
    12: "Out of ten, how would you rate the pain? ten is being the worst",
    13: "Have you had this pain before?",
    14: "Do you have a skin rash? Yes or No",
    15: "Have you had any nausea? Yes or No",
    16: "Have you vomited? Yes or No",
    17: "Have you had a fever? Yes or No",
    18: "Do you have any pain in your neck? Yes or No",
    19: "Have you experienced any memory loss? Yes or No",
    20: "Have you had any problems moving your arms or legs? Yes or No",
    21: "Have you experienced any loss of feeling in your arms or legs? Yes or No",
    22: "Have you ever had any convulsions? Yes or No"
}

__here__ = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(__here__, '..', '..', 'patient_data')

def get_dob_in_language(language):
    return DOB_dict[language]

def get_gender_in_language(language):
    return gender_dict[language]

def get_list_of_languages():
    return [key for key in DOB_dict]

def get_patient_data(dob, gender):
    data_df = pd.read_csv(os.path.join(DATA_DIR, 'patient_data.csv'))
    str_to_datetime = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d')
    dob_dt = str_to_datetime(dob)
    gender = gender
    data_df['date_of_birth'] = data_df['date_of_birth'].map(str_to_datetime)
    data_df = data_df[data_df['date_of_birth'] == dob_dt]
    data_df = data_df[data_df['gender'] == gender]
    patient = data_df.iloc[0].to_dict()
    patient['date_of_birth'] = datetime.datetime.strftime(patient['date_of_birth'], '%Y-%m-%d')
    return patient

def persist_question_to_file(question_id, parsed_response):
    question_id = int(question_id)
    report_path = os.path.join(DATA_DIR, 'report.json')
    with open(report_path) as json_file:
        data = json.load(json_file)

    if not data.has_key('first_name'):
        data['first_name'] = 'Sabina'
        data['surname'] = 'Socoli'
        data['date_of_birth'] = '1990-01-01'
        data['nhs_number'] = '01234567'
        data['questions'] = []

    question = questions[question_id]
    data['questions'].append({'question': question, 'answer': parsed_response})

    with open(report_path, 'w') as json_file:
        json.dump(data, json_file)


def get_next_question(question_id, parsed_response):
    question_id = int(question_id)
    time_list = ['minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year']
    
    if question_id == 2:
        check_response_for_time = any(word in parsed_response for word in time_list)
        if check_response_for_time:
            new_question_id = 4
        else:
            new_question_id = 3
    else:
        new_question_id = question_id + 1

    next_question = {
    "question_id": new_question_id,
    "question": questions[new_question_id]
    }
    return next_question


def get_report():
    report_path = os.path.join(DATA_DIR, 'report.json')
    with open(report_path) as json_file:
        data = json.load(json_file)

    return data


