from django.shortcuts import render,  HttpResponse, redirect
from django.contrib.auth.models import User # authentication models
from django.contrib.auth.decorators import login_required   # authentication decorator

# for importing Excel files
from .forms import UploadFileForm
from .models import UploadedFile
import openpyxl

def index(request):
    html = """
        <html>
            <h2>Our Super page!!! </h2>
            <br>
            <p> If you see this, you super rock!</p>
        </html>
    """
    # return HttpResponse(html)

    return render(request, 'app/index.html')

def test(request):
    return render(request, 'app/test.html')

def create_user(request):
    user = User.objects.create_user('batman', 'batman@heroes.com','batipassword')

    user.first_name = "Bruce"
    user.last_name = "Wayne"
    user.save()

def handle_uploaded_file(file):
    """ Takes care of the file that was uploaded"""
    # Save file to the model (optional)
    uploaded_file = UploadedFile(file=file)
    uploaded_file.save()

    # Process the file
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    return data

def upload_file(request):
    """ Uploads user files."""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = handle_uploaded_file(file)
            # Process data or pass to template context
            return render(request, 'app/upload_success.html', {'data': data})
    else:
        form = UploadFileForm()
    return render(request, 'app/upload.html', {'form': form})