from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from algos import snippets, translation_algos

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
        phrase = translation_algos.translate_en_to_es('How Can I Help?')
        data = {
            "question_id": 1,
            "question": phrase,
        }
        return Response(data)

class Question(APIView):
    def post(self, request, question_id):

        audio_file = request.FILES['file']
        # parse audio file
        # translate parsed response
        # add parsed response to report
        # snippets.get_next_question(question_id, parsed_response)
        # translate next question
        # return next_question

class GetReport(APIView):
    def get(self, request):
        report = snippets.get_report()
        return Response(report)
