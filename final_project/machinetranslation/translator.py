"""  translate text between english and french """
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#from dotenv import load_dotenv
#load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']

apikey='agdmm9bCE4yz047efGDuWB-LtxKkngRl3VhTdmXCDPp9'
url='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/f80d248b-8b4d-4632-a985-c65dec9b8c6d'

# Language translator instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(url)

#English To French translator function
def english_to_french(english_text):
    """ Return french text of the english text passed as argument """
    translation=language_translator.translate(text=english_text, model_id = 'en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

# French To English translator function
def french_to_english(french_text):
    """ Return english text of the french text passed as argument """
    translation = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translation']
    return english_text
