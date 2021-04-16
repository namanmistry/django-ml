
from django.urls import path
from .views import predict,predict_chances,view_result

app_name = "predict"
urlpatterns = [
    path('', predict,name='predict'),
    path('predict/', predict_chances,name='submit_prediction'),
    path('results/', view_result,name='results'),
]