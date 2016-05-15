from rest_framework.views import APIView
from rest_framework.response import Response
from algos import snippets, translation_algos
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

class GetListOfLanguages(APIView):
    def get(self, request):
        languages = snippets.get_list_of_languages()
        return Response(languages)


class GetDobAndGender(APIView):
    def get(self, request, language):
        dob_phrase = snippets.get_dob_in_language(language)
        gender = snippets.get_gender_in_language(language)
        data = {
        "date_of_birth": dob_phrase,
        "gender": gender
        }
        print data
        return Response(data)


class GetPatientData(APIView):
    def get(self, request, dob, gender):
        data = snippets.get_patient_data(dob, gender)
        return Response(data)

class GetFirstQuestion(APIView):
    def get(self, request):
        phrase = translation_algos.translate_en_to_es('How can I help you?')
        data = {
            "question_id": 1,
            "question": phrase,
            "surname": "Socoli",
            "first_name": "Sabina",
            "nhs_number": "01234567",
            "date_of_birth": "1990-01-01"
        }
        return Response(data)

    @csrf_exempt
    def post(self, request):
        data = request.data
        parsed_response = request.data['text']
        translated_response = translation_algos.translate_es_to_en(parsed_response)
        snippets.persist_question_to_file(1, translated_response)
        next_question = snippets.get_next_question(1, translated_response)
        next_question['question'] = translation_algos.translate_en_to_es(next_question['question'])
        return Response(next_question)
        

class Question(APIView):
    @csrf_exempt
    def post(self, request, question_id):
        data = request.data
        parsed_response = request.data['text']
        translated_response = translation_algos.translate_es_to_en(parsed_response)
        snippets.persist_question_to_file(question_id, translated_response)
        next_question = snippets.get_next_question(question_id, translated_response)
        next_question['question'] = translation_algos.translate_en_to_es(next_question['question'])
        return Response(next_question)

class GetReport(APIView):
    def get(self, request):
        report = snippets.get_report()
        return Response(report)
