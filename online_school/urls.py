from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from online_school import views

app_name = 'online_school'

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('courses/', views.CoursesPageView.as_view(), name='courses'),
    path('lessons/', views.LessonsPageView.as_view(), name='lessons'),
    path('teachers/', views.TeachersPageView.as_view(), name='teachers'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
