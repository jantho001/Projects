import http.client, urllib
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "aqv51a55c4axu3rpysnxvqpxp9bri8",
    "user": "ursx4wqb3ttgxp7jch8batv8nfpwxo",
    "message": "TS is playing!",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()