from django.urls import path
from django.urls.conf import include

#import Views
from users.views.authentication import SignUpAPIView,LoginAPIView
from users.views.teacher import AddStudentsAPIView,GetStudentsAPIView
from users.views.superAdmin import AddUsersAPIView, GetUsersAPIView
from users.views.student import GetStudentProfileAPIView
from users.views.password_reset import ForgotPasswordAPIView, EmailVerificationAPIView

urlpatterns = [
    path('sign-up/',SignUpAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    
    #Add and Get Students by Teacher
    path('add-students/',AddStudentsAPIView.as_view()),
    path('get-students/',GetStudentsAPIView.as_view()),

    #Add and get users by admin
    path('add-users/',AddUsersAPIView.as_view()),
    path('get-all-users/',GetUsersAPIView.as_view()),

    #Get student profile
    path('get-student-profile/',GetStudentProfileAPIView.as_view()),

    #Password Reset
    path('forgot-password/', ForgotPasswordAPIView.as_view()),
    path('activate_email/<uidb64>/<token>', EmailVerificationAPIView.as_view(), name = "activate_email"),

]
