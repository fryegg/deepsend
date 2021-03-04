from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC793162969c5d0acb7987a4138327d542"
# Your Auth Token from twilio.com/console
auth_token  = "65f727562a78d3f1e998006349f8f33b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+821039288568", 
    from_="+18032239287",
    body="고현서씨 롤하세요")

print(message.sid)