from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_languages$',
        views.GetListOfLanguages.as_view(),
        name='get_languages'),
    url(r'^choose_language/(?P<language>\w+)/$',
        views.GetDobAndGender.as_view(),
        name='get_dob_and_gender'),
    url(r'^get_patient_data/(?P<dob>\d{4}-\d{2}-\d{2})/(?P<gender>\w+)/$',
        views.GetPatientData.as_view(),
        name='get_patient_data'),
    url(r'^question/1/$',
        views.GetFirstQuestion.as_view(),
        name='get_first_question'),
    url(r'^question/(?P<question_id>\d+)/$',
        views.Question.as_view(),
        name='question'),
    url(r'^get_report$',
        views.GetReport.as_view(),
        name='get_report')
]
