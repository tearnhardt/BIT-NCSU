#Transcript Code:
    #The only parts needed to change for each use on a Transcript is the [FILE_NAME] and'gs://[BUCKET_NAME]/[AUDIO_FILE].wav'


#Libraries to import. The speech_v1p1beta1 is the beta version that allows for punctuation. 
import sys
from google.cloud import speech
from google.cloud import speech_v1p1beta1 as speech


#Defining a function so that running this code on different files is easier. 
def transcript(uri):
    client = speech.SpeechClient()
    operation = client.long_running_recognize(
        audio=speech.types.RecognitionAudio(
            uri=uri,
        ),
    config=speech.types.RecognitionConfig(
        encoding='LINEAR16',
        language_code='en-US',
        enable_automatic_punctuation=True
        ),
    )
    op_result = operation.result()

    for result in op_result.results:
        for alternative in result.alternatives:
            print(alternative.transcript)  


            
#Changeable Parts
sys.stdout = open('[FILE_NAME].txt','wt') 

transcript('gs://[BUCKET_NAME]/[AUDIO_FILE].wav')

