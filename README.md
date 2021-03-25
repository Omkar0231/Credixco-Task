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
