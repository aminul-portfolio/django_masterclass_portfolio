from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def home(request):
    return render(request, 'core/home.html')

def topic_page(request, template_name, page_name):
    comments = Comment.objects.filter(page_name=page_name).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.page_name = page_name
            comment.save()
            return redirect(request.path)
    else:
        form = CommentForm()

    return render(request, template_name, {
        'form': form,
        'comments': comments,
    })



def css(request):
    return render(request, '02_CSS/css.html')

def bootstrap(request):
    return render(request, '03_BOOTSTRAP/bootstrap.html')

def python_basic(request):
    return render(request, '04_PYTHON_BASIC/python_basic.html')

def python_advanced(request):
    return render(request, '05_PYTHON_ADVANCED/python_advanced.html')

def introduction_to_django(request):
    return render(request, '06_Introduction_to_Django/introduction_to_django.html')

def introduction_to_django_2(request):
    return render(request, '06_Introduction_to_Django/2nd.html')

def django_views_routing_urls(request):
    return render(request, '07_Django_Views_Routing_URLs/django_views_routing_urls.html')

def django_and_templates(request):
    return render(request, '08_Django_and_Templates/django_and_templates.html')

def django_models_databases(request):
    return render(request, '09_Django_Models_Databases/django_models_databases.html')

def django_admin_portal(request):
    return render(request, '10_Django_Admin_Portal/django_admin_portal.html')

def django_forms(request):
    return render(request, '11_Django_Forms/django_forms.html')

def django_class_based_views(request):
    return render(request, '12_Django_Class_Based_Views/django_class_based_views.html')