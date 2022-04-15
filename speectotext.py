import requests
import time
baseUrl = "https://api-labs.symbl.ai/v1/conversations/{conversationId}/messages"
# Generated using Submit text end point
from get import conversationId


url = baseUrl.format(conversationId=conversationId)

# set your access token here. See https://docs.symbl.ai/docs/developer-tools/authentication
access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFVUTRNemhDUVVWQk1rTkJNemszUTBNMlFVVTRRekkyUmpWQ056VTJRelUxUTBVeE5EZzFNUSJ9.eyJodHRwczovL3BsYXRmb3JtLnN5bWJsLmFpL3VzZXJJZCI6IjUxMzkyMTYzMDMzOTA3MjAiLCJpc3MiOiJodHRwczovL2RpcmVjdC1wbGF0Zm9ybS5hdXRoMC5jb20vIiwic3ViIjoicGNSUEtRWlNONXZwWkxhNUF2ZFJrTEI1a2MwY1FWeGJAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vcGxhdGZvcm0ucmFtbWVyLmFpIiwiaWF0IjoxNjQ5OTg5ODQ1LCJleHAiOjE2NTAwNzYyNDUsImF6cCI6InBjUlBLUVpTTjV2cFpMYTVBdmRSa0xCNWtjMGNRVnhiIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.orVkReKwlHC9Jpi_NPZsG_XugPJ4a9qfuh3n4i0kQREXqofX8k5YmxlEtVQiX959irTcgJwINd_POwAa8ITHqBas_0oS2e5chCkm6XnNNvsGYkaBRDWWVDk_7n9vN5WnLJApVs4Mm40XuSYfF5VUJqqVfX-kPkSH-Ar_oLvJF4Z6HBBy80heAWKnkXWUVgBKGd9dSLYoGBTgsqJ0PkWrPDHebvZzRIKSG5m4Z5z-tPYqa2311FSpbC7s36pCKjuNTSyhF-4aQ6C7ad4-N9zuFw3iUHE8BQPIRjeVkH_b6KaVsn0hwyYgyxbNsz9FYGd9YZ7_yC2EJeEh14fpXhTjlg'
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
