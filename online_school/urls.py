from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from online_school import views

app_name = 'online_school'

urlpatterns = [
    path('', views.IndexPageView.as_view()),
    path('courses/', views.CoursesListView.as_view(), name='courses'),
    path('lessons/', views.LessonsListView.as_view(), name='lessons'),
    path('teachers/', views.TeachersListView.as_view(), name='teachers'),

    path('api/auth/', views.AuthApiView.as_view()),
    path('api/login/', views.LoginApiView.as_view()),

    path('api/courses/', views.CourseListApiView.as_view()),
    path('api/courses/<int:pk>/', views.CourseListDetailApiView.as_view()),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
