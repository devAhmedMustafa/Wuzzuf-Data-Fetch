from django.shortcuts import render
from .functions import write_csv, fetch_data
from django.http import JsonResponse, HttpResponse, Http404
from django.conf import settings
import os
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
@xframe_options_exempt
def app(request):

    return render(request, 'index.html')

@xframe_options_exempt
def fetch_request(request):

    category = request.GET.get('category')

    job_details = fetch_data(category)
    write_csv(job_details)

    data = {
    
    }

    return JsonResponse(data)

@xframe_options_exempt
def download(request):

    file_path = os.path.join(settings.MEDIA_ROOT, 'files/wuzzuf.csv')
    if os.path.exists(file_path):
        print('true')
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename="wuzzuf.csv"'
            return response
        
    raise Http404
