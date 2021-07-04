from django.test import TestCase
import json
import urllib.request

# Create your tests here.
def dictionary(request):
    if request.POST:
        url = 'https://api.dictionaryapi.dev/api/v2/entries/' +  request.POST['lang'] + '/' + request.POST['search_query']
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        j = len(result[0]['meanings'])
        if len(result[0]['meanings'])==1:

            if (request.POST['lang'] != 'en_US' and 'en_UK'):
                context = {
                'word': result[0]['word'], 
                'f_definitions': [],
                'partOfSpeech': result[0]['meanings'][0]['partOfSpeech'],
                }

            else: 
                context = {
                'word': result[0]['word'], 
                'f_definitions': [],
                'partOfSpeech': result[0]['meanings'][0]['partOfSpeech'],
                'audio': result[0]['phonetics'][0]['audio'],
                }

            for i in range(0, len(result[0]['meanings'][0]['definitions'])):
                context['f_definitions'].append(result[0]['meanings'][0]['definitions'][i]['definition']) 


        elif len(result[0]['meanings'])==2:

            if (request.POST['lang'] != 'en_US' and 'en_UK'):
                context={
                    'word': result[0]['word'],
                    'f_definitions': [], 
                    's_definitions': [],
                    'partOfSpeech': result[0]['meanings'][0]['partOfSpeech'],
                    'partOfSpeech1': result[0]['meanings'][1]['partOfSpeech'],
                }
            
            else:
                context = {
                'word': result[0]['word'],
                'f_definitions': [], 
                's_definitions': [],
                'partOfSpeech': result[0]['meanings'][0]['partOfSpeech'],
                'audio': result[0]['phonetics'][0]['audio'],
                'text': result[0]['phonetics'][0]['text'],
                'partOfSpeech1': result[0]['meanings'][1]['partOfSpeech'],
                }


            for i in range(0, len(result[0]['meanings'][0]['definitions'])):
                context['f_definitions'].append(result[0]['meanings'][0]['definitions'][i]['definition']) 
            for i in range(0, len(result[0]['meanings'][1]['definitions'])):
                context['s_definitions'].append(result[0]['meanings'][1]['definitions'][i]['definition'])


        elif len(result[0]['meanings'])==3:

            if (request.POST['lang'] != 'en_US' and 'en_UK'):
                context = {
                'word': result[0]['word'],
                'f_definitions': [], 
                's_definitions': [],
                't_definitions': [],
                'definition': result[0]['meanings'][0]['definitions'][0]['definition'], 
                'partOfSpeech': result[0]['meanings'][0]['partOfSpeech'],
                'partOfSpeech1': result[0]['meanings'][1]['partOfSpeech'],
                'partOfSpeech2': result[0]['meanings'][2]['partOfSpeech'],
                }
            
            else:
                context = {
                'word': result[0]['word'],
                'f_definitions': [], 
                's_definitions': [],
                't_definitions': [],
                'definition': result[0]['meanings'][0]['definitions'][0]['definition'], 
                'partOfSpeech': result[0]['meanings'][0]['partOfSpeech'],
                'audio': result[0]['phonetics'][0]['audio'],
                'text': result[0]['phonetics'][0]['text'],
                'partOfSpeech1': result[0]['meanings'][1]['partOfSpeech'],
                'partOfSpeech2': result[0]['meanings'][2]['partOfSpeech'],
                }

            for i in range(0, len(result[0]['meanings'][0]['definitions'])):
                context['f_definitions'].append(result[0]['meanings'][0]['definitions'][i]['definition']) 
            for i in range(0, len(result[0]['meanings'][1]['definitions'])):
                context['s_definitions'].append(result[0]['meanings'][1]['definitions'][i]['definition'])
            for i in range(0, len(result[0]['meanings'][2]['definitions'])):
                context['t_definitions'].append(result[0]['meanings'][2]['definitions'][i]['definition'])

        

        else:
        
            if (request.POST['lang'] != 'en_US' and 'en_UK'):
                context = {
                'word': result[0]['word'], 
                'definition': result[0]['meanings'][0]['definitions'][0]['definition'], 
                'partOfSpeech': result[0]['meanings'][0]['partOfSpeech'],
                }

            else:
                context = {
                'word': result[0]['word'], 
                'definition': result[0]['meanings'][0]['definitions'][0]['definition'], 
                'partOfSpeech': result[0]['meanings'][0]['partOfSpeech'],
                'audio': result[0]['phonetics'][0]['audio'],
                'text': result[0]['phonetics'][0]['text'],
                }
        return(context)