from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from website.models import Project, Tree


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

        # send email to cokedama for contact form
        send_mail(
            user_subject,  # subject
            user_message + '\n\nFrom, ' + user_name,  # message
            user_email,  # from email
            ['cokedama100@gmail.com', user_email],  # to email
        )

        return render(request, 'contact.html', {'user_name': user_name})
    else:
        return render(request, 'contact.html', {})


def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})


def portfolio_single(request, id, slug):
    project = get_object_or_404(Project, slug=slug, id=id)
    return render(request, 'portfolio-single.html', {'project': project})


def tree_profile(request):
    trees = Tree.objects.all()
    return render(request, 'tree_profile.html', {'trees': trees})


def tree_single(request, id, slug):
    tree = get_object_or_404(Tree, slug=slug, id=id)
    return render(request, 'tree-single.html', {'tree': tree})


def consult(request):
    return render(request, 'consult.html', {})
