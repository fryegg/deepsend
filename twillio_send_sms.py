from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid =
# Your Auth Token from twilio.com/console
auth_token  =

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+821039288568", 
    from_="+18032239287",
    body="고현서씨 롤하세요")

print(message.sid)
