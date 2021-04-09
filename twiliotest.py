from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC8c43dcb7c3476ff212bd92de120ae6ae'
auth_token = 'fdfd9eb1be27efd6e51422497f49b5ff'
client = Client(account_sid, auth_token)

client.api.account.messages.create(to="+4917671227950",from_="+12542390909",body="Jetzt kannst du dich anmelden!")