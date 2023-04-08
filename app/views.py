from django.shortcuts import render
from .functions import write_csv, fetch_data
from django.http import JsonResponse, HttpResponse, Http404
from django.conf import settings
import os

# Create your views here.

def app(request):

    return render(request, 'index.html')

def fetch_request(request):

    category = request.GET.get('category')

    job_details = fetch_data(category)
    write_csv(job_details)

    data = {
    
    }

    return JsonResponse(data)

def download(request):

    file_path = os.path.join(settings.MEDIA_ROOT, 'files/wuzzuf.csv')
    if os.path.exists(file_path):
        print('true')
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename="wuzzuf.csv"'
            return response
        
    raise Http404
