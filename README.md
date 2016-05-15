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

 ```python
 GET /get_patient_data/<YYYY-MM-DD>/<male | female>
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

