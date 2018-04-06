import json
from channels import Group
from channels.sessions import channel_session, enforce_ordering
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.security.websockets import allowed_hosts_only
from urllib.parse import parse_qs
from channels.generic import BaseConsumer
from channels.generic.websockets import WebsocketConsumer
from channels.generic.websockets import WebsocketDemultiplexer, JsonWebsocketConsumer

# Connected to websocket.connect
# @channel_session
@channel_session_user_from_http
def ws_connect(message, room_name):
    # Accept connection
    message.reply_channel.send({"accept": True})
    Group("chat-%s" % message.user.username[0] if message.user.username else 'guest').add(message.reply_channel)

# Connected to websocket.receive
# @channel_session
@allowed_hosts_only
@channel_session_user
def ws_message(message, room_name):
    Group("chat-%s" % message.user.username[0] if message.user.username else 'guest').send({
        "text": message['text'],
    })

# Connected to websocket.disconnect
# @channel_session
@channel_session_user
def ws_disconnect(message, room_name):
    Group("chat-%s" % message.user.username[0] if message.user.username else 'guest').discard(message.reply_channel)