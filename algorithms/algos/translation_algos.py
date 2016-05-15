import requests


URL = 'http://language-translation-nodejs-jaggs6-1942.eu-gb.mybluemix.net/api/translate'

def translate_es_to_en(query_text):
    data = {
        'model_id': 'es-en',
        'text': query_text,
    }
    res = requests.post(URL, data)
    try:
        assert res.status_code == 200
    except AssertionError:
        print "Well that didn't work..."
    try:
        data = res.json()
    except ValueError:
        print "Well that didn't work..."
    translation = data['translations'][0]['translation']
    return translation

def translate_en_to_es(query_text):
    data = {
        'model_id': 'en-es',
        'text': query_text,
    }
    res = requests.post(URL, data)
    try:
        assert res.status_code == 200
    except AssertionError:
        print "Well that didn't work..."
    try:
        data = res.json()
    except ValueError:
        print "Well that didn't work..."
    translation = data['translations'][0]['translation']
    return translation
