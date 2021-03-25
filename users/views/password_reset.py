from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#models
from users.models import User

#For Email
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from users.utils import token_generator
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.conf import settings



class ForgotPasswordAPIView(APIView):
    '''
    This is the Forgot Password API. The user has to enter the email address.
    If the user exists, an email with a unique link is mailed to the email address
    given by the user. 
    '''
    def post(self,request,*args,**kwargs):
        email = request.data.get('email')
        if email:
            user = User.objects.filter(email__iexact=email)
            if user.exists():
                #Sending the email for Password reset
                    #Path to view
                        # --relative url for verification
                        # --encode uid
                        # --Generating the token and sending the email to the user.

                user = user.first()
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                print(token_generator.make_token(user))
                # NOTE_ : Here in the link I have used https for the localhost.
                # It's because gmail stooped allowing the emails starting with http.
                # To overcome that I have used https. You need to change the https to http
                # while using in the browser or postman.
                link = 'https://localhost:8000' + reverse('activate_email', kwargs={
                                'uidb64': uidb64, 'token': token_generator.make_token(user)})
                
                email_to = str(user.email)

                email_subject = "Reset your Password"
                
                email_body = "Hi "+ str(user.name).upper() + ",<br>You have requested to reset your password."\
                                " Please click the below link to reset your password."\
                                "<br>Please click " + link + " to reset your password.<br>"\
                                "If you haven't requested to reset password, please ignore the message." \
                                
                
                email_from = settings.DEFAULT_FROM_EMAIL
                email = EmailMessage(
                    email_subject,
                    email_body,
                    email_from,
                    [email_to],
                
                )

                email.content_subtype = "html"
                email.send(fail_silently=False)
                #The password_change_request field is to check if the user is
                #using the same link even after password changed with the link.
                user.password_change_request = True
                user.save()
                return Response({'message': 'Password reset link has been sent to your email. Please check your email. The link is only valid for 30mins'})
            else:
                return Response({'error':'User doesn\'t exist with this email.'},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error':'Please enter the email.'},status=status.HTTP_400_BAD_REQUEST)



class EmailVerificationAPIView(APIView):
    '''
    The link sent to the email should be executed as a post request with password as 
    the data in the body.And this checks if the token is valid and changes the password 
    if it is a valid link and isn't expired. 
    '''
    def post(self, request, uidb64, token):
        new_password = request.POST.get("password")
        
        id_ = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.filter(pk=id_)
        
        if not user.exists():
            return Response({'error':'User not found.'},status=status.HTTP_404_NOT_FOUND)

        user = user.first()
        if token_generator.check_token(user, token):
            if new_password:
                user.set_password(new_password)
                user.password_change_request = False
                user.save()
                return Response({'message' : 'Your password has been changed successfully.'},status=status.HTTP_200_OK)
            else:
                return Response({'error':'Please enter the password.'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message' : 'Sorry! The link has been expired or wrong link.',},status=status.HTTP_200_OK)
            

        
        