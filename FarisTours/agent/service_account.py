from oauth2client.service_account import ServiceAccountCredentials
from django.http import JsonResponse
# The scope for the OAuth2 request.
SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

# The location of the key file with the key data.
KEY_FILEPATH = 'static/api/analytics_key.json'

# Defines a method to get an access token from the ServiceAccount object.
from django.views.decorators.csrf import csrf_exempt

def get_access_token(request):
    token = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILEPATH, SCOPE).get_access_token().access_token
    return JsonResponse({
                'token':token
            })


