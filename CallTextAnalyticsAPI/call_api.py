import os , json
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

key = "<your subscription key >"
endpoint = "< endpoint of your text analytics cog service"

def authenticateClient():
    credentials = CognitiveServicesCredentials(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credentials=credentials)
    return text_analytics_client

def sentiment():
    
    client = authenticateClient()

    try:
        documents = [
            {"id": "1", "language": "en", "text": "I had the best day of my life."},
            {"id": "2", "language": "en",
                "text": "This was a waste of my time. The speaker put me to sleep."},
            {"id": "3", "language": "es", "text": "No tengo dinero ni nada que dar..."},
            {"id": "4", "language": "it",
                "text": "L'hotel veneziano era meraviglioso. È un bellissimo pezzo di architettura."}
        ]

        response = client.sentiment(documents=documents)
        for document in response.documents:
            print("Document Id: ", document.id, ", Sentiment Score: ",
                  "{:.2f}".format(document.score))

    except Exception as err:
        print("Encountered exception. {}".format(err))


sentiment()

