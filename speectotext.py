import requests
import time
baseUrl = "https://api-labs.symbl.ai/v1/conversations/{conversationId}/messages"
# Generated using Submit text end point
from get import conversationId


url = baseUrl.format(conversationId=conversationId)

# set your access token here. See https://docs.symbl.ai/docs/developer-tools/authentication
access_token = ""
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

params = {
    'verbose': True,  # <Optional, boolean| Gives you word level timestamps of each sentence.>
    'sentiment': True  # <Optional, boolean| Give you sentiment analysis on each message.>
}

responses = {
    401: 'Unauthorized. Please generate a new access token.',
    404: 'The conversation and/or it\'s metadata you asked could not be found, please check the input provided',
    500: 'Something went wrong! Please contact support@symbl.ai'
}

response = requests.request("GET", url, headers=headers)

if response.status_code == 200:
    # Successful API execution
    # messages is a list of id, text, from, startTime, endTime, conversationId, words, phrases, sentiment
    print("messages => " + str(response.json()['messages']))
elif response.status_code in responses.keys():
    print(responses[response.status_code])  # Expected error occurred
else:
    print("Unexpected error occurred. Please contact support@symbl.ai" + ", Debug Message => " + str(response.text))

exit()