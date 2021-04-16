from django.shortcuts import render
import pandas as pd
from pathlib import Path
from .models import PredResults
from django.http import JsonResponse

BASE_DIR = Path(__file__).resolve().parent.parent
def predict(request):
    return render(request,'predict/predict.html')

def predict_chances(request):
    
    if request.method=="POST":
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))
        
        model=pd.read_pickle(f'{BASE_DIR}\\new_model.pickle')
        result=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        classification = result[0]
        obj=PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
                                   petal_width=petal_width, classification=classification)
        obj.save()
        return JsonResponse({'result': classification, 'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width},
                            safe=False)

def view_result(request):
    data = {"dataset": PredResults.objects.all()}
    return render(request, "predict/results.html", data)