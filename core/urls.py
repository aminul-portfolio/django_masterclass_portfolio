from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # 🧾 HTML Topics
    path('html/', lambda r: views.topic_page(r, '01_HTML/html.html', 'html'), name='html'),
    path('css/', lambda r: views.topic_page(r, '02_CSS/css.html', 'css'), name='css'),
    path('bootstrap/', lambda r: views.topic_page(r, '03_BOOTSTRAP/bootstrap.html', 'bootstrap'), name='bootstrap'),
    path('python_basic/', lambda r: views.topic_page(r, '04_PYTHON_BASIC/python_basic.html', 'python_basic'), name='python_basic'),
    path('di-tu-fun/',lambda r: views.topic_page(r, '04_PYTHON_BASIC/di_tu_fun.html', 'di_tu_fun'),name='di_tu_fun'),
    path('python_advanced/', lambda r: views.topic_page(r, '05_PYTHON_ADVANCED/python_advanced.html', 'python_advanced'), name='python_advanced'),
    path( 'error-handling/', lambda r: views.topic_page(r, '05_PYTHON_ADVANCED/error_handling_examples.html', 'error_handling_examples'), name='error_handling_examples'),


    # 🚀 Django Intro Series
    path('introduction_to_django/', lambda r: views.topic_page(r, '06_Introduction_to_Django/introduction_to_django.html', 'introduction_to_django'), name='introduction_to_django'),
    path('introduction_to_django_2/', lambda r: views.topic_page(r, '06_Introduction_to_Django/2nd.html', 'introduction_to_django_2'), name='introduction_to_django_2'),

    # 🔁 Views & Routing
    path('django_views_routing_urls/', lambda r: views.topic_page(r, '07_Django_Views_Routing_URLs/django_views_routing_urls.html', 'django_views_routing_urls'), name='django_views_routing_urls'),

    # 🧩 Templates & Backend
    path('django_and_templates/', lambda r: views.topic_page(r, '08_Django_and_Templates/django_and_templates.html', 'django_and_templates'), name='django_and_templates'),
    path('django_models_databases/', lambda r: views.topic_page(r, '09_Django_Models_Databases/django_models_databases.html', 'django_models_databases'), name='django_models_databases'),
    path('django_admin_portal/', lambda r: views.topic_page(r, '10_Django_Admin_Portal/django_admin_portal.html', 'django_admin_portal'), name='django_admin_portal'),
    path('django_forms/', lambda r: views.topic_page(r, '11_Django_Forms/django_forms.html', 'django_forms'), name='django_forms'),
    path('django_class_based_views/', lambda r: views.topic_page(r, '12_Django_Class_Based_Views/django_class_based_views.html', 'django_class_based_views'), name='django_class_based_views'),
]
