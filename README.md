# Important points to be done before executing the Project

__Step 1 :__ First create  a virtual environment and install all the packages
in requirements.txt using, 
```bash
pip install -r requirements.txt
```

__Step 2 :__ Connect a new PostgreSQL DB which is available on your local computer to this django project by changing the values of DATABASES variable in the settings file.

__Step 3 :__ Email credentials should be provided in the settings file. You have to give the email in the __EMAIL_HOST_USER__ and __DEFAULT_FROM_EMAIL__. You also have to generate the GOOGLE_APP_PASSWORD. You can get it from here
https://myaccount.google.com/security . You need to complete the 
2-step verification under the __Signing in to Google__ section. Then the app 
passwords section will be availble under the same section and generate one and use that password in __EMAIL_HOST_PASSWORD__.

__Finally,__ the project runs smoothly as per the requirements mentioned in the task.


# API Documentation

__Q1. User Sign Up/Forgot Password APIs__
__User SignUp__
link : http://localhost:8000/users/sign-up/
request-method : POST 
Sample Form-data :
{
    'email'         : 'xxx@gmail.com',
    'password'      : 'xxxx',
    'name'          : 'xxxx',
    'father_name'   : 'xxxx',
    'date_of_birth' : 'DD-MM-YYYY',
    'gender'        : 'male/female',
    'role'          : 'SUPER_ADMIN/TEACHER/STUDENT'
}

__Forgot Password__
__STEP 1:__ 
link : http://localhost:8000/users/forgot-password/
request-method : POST

Sample Form-data :
{
    'email'         : 'xxx@gmail.com',
}

__After this API request, an email with a unique link is sent to the email provided in the request and if the user doesn't exist with the email, error message is shown__

__STEP 2:__
Send a POST request to the link which is sent in the email.
Sample Form-data : :
{
    'password' : 'new_password'
}

__Q2. Uses JWT Authentication__
This project uses the JWT authentication.
link: http://localhost:8000/users/login/
request-method : POST
Sample Form-data :
{
    'email'    : 'xxxx@gmail.com',
    'password' : 'xxxx'
}

__NOTE:__ You will receive a token and the message that the user is logged in successfully.


__Q3. Must define 3 user levels; 1. Super-dmin, 2.Teacher, 3. Student(Use internal Django Groups to achieve the same)__
This project satisfies all these rules.


__Q4. Teacher must be able to add/list the students.__
The Token received when the teacher is logged in through Q2.(above), paste it in the request headers like :
{ 
    'Authorization' : 'jwt __Received token__'
}

__To create the Students__
link : http://localhost:8000/users/add-students/
request-type : POST
Sample Form-data :
{
    'email'         : 'xxx@gmail.com',
    'password'      : 'xxxx',
    'name'          : 'xxxx',
    'father_name'   : 'xxxx',
    'date_of_birth' : 'DD-MM-YYYY',
    'gender'        : 'male/female'
}

__To list the Students__
link : http://localhost:8000/users/get-students/
request-method : GET

You get all the students data.

__Q5. Admin must be able to add/list every user in the database__
The Token received when the teacher is logged in through Q2.(above), paste it in the request headers like :
{ 
    'Authorization' : 'jwt __Received token__'
}

__To create any User__
link : http://localhost:8000/users/add-users/
request-method : POST
Sample Form-data :
{
    'email'         : 'xxx@gmail.com',
    'password'      : 'xxxx',
    'name'          : 'xxxx',
    'father_name'   : 'xxxx',
    'date_of_birth' : 'DD-MM-YYYY',
    'gender'        : 'male/female',
    'role'          : 'SUPER_ADMIN/TEACHER/STUDENT'
}

__To list all types of Users__
link : http://localhost:8000/users/get-all-users/
request-method : GET

You get all the users data.


__Q6. Students must be able to see his information only__

The Token received when the teacher is logged in through Q2.(above), paste it in the request headers like :
{ 
    'Authorization' : 'jwt __Received_token_when_logged_in__'
}
link : http://localhost:8000/users/get-student-profile/
request_method : GET

You the logged in student profile only.

__Q7. Code should be commented for clarity__
The code is nicely written with proper comments.
