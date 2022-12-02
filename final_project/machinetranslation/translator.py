import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']

authenticator = IAMAuthenticator('agdmm9bCE4yz047efGDuWB-LtxKkngRl3VhTdmXCDPp9')

language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/f80d248b-8b4d-4632-a985-c65dec9b8c6d')

def english_to_french(englishText):
    translation = language_translator.translate(text=englishText,model_id='en-fr').get_result()
    frenchText=translation['translations'][0]['translation']
    return frenchText

def french_to_english(frenchText):
    translation = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    englishText=translation['translations'][0]['translation']
    return englishText

