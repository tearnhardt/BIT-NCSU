# BIT NCSU Speech-to-text Transcripts 
Methods and code that harness the Google Cloud Speech-to-text API to produce audio transcripts of lectures with punctuation. 

## Google Cloud
1. Set up a [Google Cloud Account](https://cloud.google.com/) selecting to start a free trial. 
   *Note: this will require access to a credit card in order for Google to confirm your account. Only $1 will be charged and it will be  refunded within a month of signing up. This free trial will credit your account with $300 to use on the console.*
2. Once the account is set up, go and create a New Project.  
3. After creating a new Project, go to the left sidebar and scroll to the Storage option. Click on it and choose to make a bucket storage.   
   *The Bucket is where you will eventually upload your files to, but don't do that yet.*
4. Navigate to the Google Cloud Console Terminal and type:  
```
gcloud iam service-accounts keys create [FILE_NAME].json --iam-account [NAME]@[PROJECT_ID].iamgserviceaccount.com
```
   *Where [NAME] is the username you chose for your account and [PROJECT_ID] is the ID of the project you're working on. [FILE_NAME] is any name you choose.*  
5. In the Console Terminal type:  
```
gsutil cp '[FILE_NAME].json' 'gs://[BUCKET_NAME]'
```  
   *This is saving the .json file to the storage bucket you made earlier.*
6. Navigate to the Storage Bucket now and click on the .json file that should now be in it. This will open in a new webpage. SAve that document to a specific place on your computer. 

## Python
1. If your computer does not have Python on it, download the latest version for your computer. 
   *Pay attention to where you save the program files because this will be importatn for the Virtual Environment portion.*  
2. Test the IDLE of the Python Version you downloaded to make sure it opens up.  

## Virtual Environment  
1. Open up Windows Command Prompt. You should be in your ```C:\Users\[USER_NAME]``` drectory. Remembering where you saved your Python program files, navigate in to it using this code:  
```
cd [PATH_TO_PYTHON_FOLDER]  
```
2. Create a virtual environment in a easy to find location on your computer. Do so by 


