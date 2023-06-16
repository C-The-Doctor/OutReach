# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACb986d66f2b3399dc110943b64ae4b1dc"
auth_token = "13dc38f559a62ac1b08a53c24617768e"

# Your Twilio Credentials
# Ensure There Stored In .Env
# Initiate A Connection To Your Twilio Api
client = Client(account_sid, auth_token)


# Provider Details Conf
Provider = "+13203498237"


def Broadcast_Voice_Notification(Trigger , Account):

    call = client.calls.create(
                        twiml= Trigger ,
                        to= Account,
                        from_= Provider
                    )

    return call.sid


def Broadcast_Sms_Notification(Trigger , Account):

    call = client.messages.create(
                        body=Trigger,
                        from_=Provider,
                        to=Account
                    )

    return call.sid
