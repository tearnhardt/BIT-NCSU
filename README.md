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
6. Navigate to the Storage Bucket now and click on the .json file that should now be in it. This will open in a new webpage. Save that document to a specific place on your computer. 

## Python
1. If your computer does not have Python on it, download the latest version for your computer. 
   *Pay attention to where you save the program files because this will be importatn for the Virtual Environment portion.*    
2. Test the IDLE of the Python Version you downloaded to make sure it opens up.  

## Virtual Environment  
1. Open up Windows Command Prompt. You should be in your ```C:\Users\[USER_NAME]``` drectory. Remembering where you saved your Python program files, navigate in to it using this code, changing the [PATH_TO_PYTHON_FOLDER] to the actual location you saved it in:  
```
cd [PATH_TO_PYTHON_FOLDER]  
```
2. Create a virtual environment in a easy to find location on your computer. Do so by typing this code into Command Prompt where [NAME] is any name you choose the virtual environment to go by:  
```
Python -m virtualenv [NAME]
[NAME]/Scripts/activate
[NAME]/Scipts/pip.exe install google-cloud-speech  
```  
*You now also just installed the Google Cloud Speech-to-text API so that you can use it in python later.*  
3. Exit Command Prompt now. You have finished setting up the virtual environment.   

## Audacity  
1. Now you will need to download the free software [Audacity](https://www.audacityteam.org/) to edit the .wav files so that they can be used. *Google Cloud Speech-to-text is particular with the type of audio files it will allow.*  
2. After installing Audacity, open an audio file in it and select the left sidebar section next to the audio waves (as shown in the image below) that has the name of the audio file. There should be some drop down options, choose the one that says Stereo to Mono. Then double click the upper audio wave portion so that it's selected. Then go to File, select Export, and within those options select Export Selected Audio and save the audio to another place on your computer.![Audacity](https://www.audacityteam.org/wp-content/uploads/2017/12/Audacity-220-Windows-normal.png)  
3. Do this for each audio file needed to transcribe and then upload them to your Bucket on the Google Cloud Storage. Depending on the size of the files this can take a long time. Once they are fully uploaded, they are ready to be transcribed.  

## Python Script  
1. Copy the Python script from this repository and paste it into a Python script on your computer. Save that file in a memorable location under the name Transcript.py.  
2. For each audio file you wish to transcribe you will have to change two lines of this Python script.  
```python
sys.stdout = open('[FILE_NAME].txt','wt') 

transcript('gs://[BUCKET_NAME]/[AUDIO_FILE].wav')
```  
*By changing the first portion you choose what to name the actual text file containing the transcript. The second portion is directing where to find the file on the Google Cloud Storage.*  
## Google Application Credentials  
1. Locate the .json file saved earlier in the Google Cloud Section.  
2. Open Command Prompt and type: 
```
set GOOGLE_APPLICATION_CREDENTIALS=[PATH]
```
*Where [PATH] is the path to the location of the .json file.*  



