# Dialek REST API
-----
This is the rest api for the Dialek team's software solution.
-----
## Set up for local environment
-----
### Requirements
This Django project runs using Python 2.7.11

Install the requirements as follows:
```shell
cd to this directory
pip install -r requirements.txt
```

### Running the REST service locally
Run the service as follows
```shell
python manage.py runserver 0.0.0.0:8000
```

Any changes made locally will cause the site to rebuild automagically.

The different rest endpoints can be accessed as follows:

#### Endpoints

 ```python
 GET /rest_api/get_languages
```
Returns list of languages:
 ```python
 [
    "german",
    "italian",
    "spanish",
    "french",
    "english"
]
```
-----
 ```python
 GET /rest_api/choose_language/<language>
```
Returns a key value pairs of DoB and Gender in the chosen language:
 ```python
 {
    "gender": "genero",
    "date_of_birth": "fecha de nacimiento"
}
```
-----
 ```python
 GET /reat_api/get_patient_data/<YYYY-MM-DD>/<male | female>
```

Returns records for patient with this date of birth and gender:
```python
{
    "gender": "male",
    "first_name": "John",
    "date_of_birth": "1990-01-01",
    "surname": "Doe",
    "patient_id": 1
}
```
-----
```python
 GET /rest_api/question/1/
```

Returns data for question 1
```python
{
    "question": "¿Cómo ayuda?",
    "question_id": 1
}
```
-----
```python
 POST /rest_api/question/<question_id>/
```
Post text in native language for translation to english and adding to the doctor's file
```shell
curl -X POST -H "Content-Type: application/json" -d '{
    "text": "hola, mundo"
}' "http://localhost:8000/rest_api/question/2/"
```

Returns
```python
{
    "question": "¿Cómo ayuda?",
    "question_id": 1
}
```
-----
```python
 GET /rest_api/get_report/
```
Gets doctor's report.
```python
{
    "nhs_number": "01234567",
    "first_name": "Sabina",
    "date_of_birth": "1990-01-01",
    "surname": "Socoli",
    "questions": [
        {
            "answer": "This is my answer to question 1",
            "question": "What's wrong?"
        },
        {
            "answer": "This is my answer to question 2",
            "question": "When did this headache start?"
        }
    ]
}
```

