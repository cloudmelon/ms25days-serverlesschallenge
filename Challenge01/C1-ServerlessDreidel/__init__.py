import logging
import azure.functions as func
import random


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    dreidel = ['נ (Nun)', 'ג (Gimmel)', 'ה (Hay)', 'ש (Shin)', 'ש (Shin)']

    dreidel_item = random.choice(dreidel)

    return func.HttpResponse(
            f"Congrats ! You get {dreidel_item} !", 
            status_code=200
    )
