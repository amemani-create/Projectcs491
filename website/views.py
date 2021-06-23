from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_subject = request.POST['user_subject']
        user_message = request.POST['user_message']

        #send email to cokedama for contact form
        send_mail(
            user_subject, #subject
            user_message + '\n\nFrom, ' + user_name, #message
            user_email, #from email
            ['cokedama100@gmail.com', user_email], #to email
        )

        return render(request, 'contact.html', {'user_name': user_name})
    else:
        return render(request, 'contact.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})

def portfolio_single(request):
    return render(request, 'portfolio-single.html', {})

def service(request):
    return render(request, 'service.html', {})