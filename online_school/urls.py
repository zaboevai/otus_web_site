from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

import online_school.views_api
from online_school import views

app_name = 'online_school'

urlpatterns = [
    path('', views.IndexPageView.as_view()),
    path('courses/', views.CoursesListView.as_view(), name='courses'),
    path('lessons/', views.LessonsListView.as_view(), name='lessons'),
    path('teachers/', views.TeachersListView.as_view(), name='teachers'),
    path('contacts/', views.ContactsListView.as_view(), name='contacts'),

    path('register/', views.registration, name='register'),
    path('login/', views.LoginAuthView.as_view(), name='login'),
    path('logout/', views.LogoutAuthView.as_view(), name='logout'),
    path('accounts/profile/', views.ProfileAuthView.as_view(), name='index'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),


    path('api/auth/', online_school.views_api.AuthApiView.as_view()),
    path('api/login/', online_school.views_api.LoginApiView.as_view()),
    path('api/courses/', online_school.views_api.CourseListApiView.as_view()),
    path('api/courses/<int:pk>/', online_school.views_api.CourseListDetailApiView.as_view()),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
