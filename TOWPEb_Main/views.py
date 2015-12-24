from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})
    elif request.method == 'POST':
        try:
            email = request.POST['inputEmail']
            name = request.POST['inputSubject']
            message = request.POST['message']
            send_mail('An email from ' + name, message, email,
                      ['carlosalejandro@towpeb.com', 'info@towpeb.com', 'rolandocruz@towpeb.com',
                       'jorgevaldes@towpeb.com'], fail_silently=False)
            return render(request, 'index.html', {'OK': True})
        except KeyError:
            return render(request, 'index.html', {'Fail': True})
