
import sys
from google.cloud import speech
from google.cloud import speech_v1p1beta1 as speech



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


sys.stdout = open('lecture14las.txt','wt')

transcript('gs://bit_ncsu_transcripts/Lecture 14 LAS.wav')
