import datetime
import errno
import os
import sys
import logging
import tempfile
from argparse import ArgumentParser

from flask import Flask, request, abort, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.models import (
    UnknownEvent
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    LocationMessageContent,
    StickerMessageContent,
    ImageMessageContent,
    VideoMessageContent,
    AudioMessageContent,
    FileMessageContent,
    UserSource,
    RoomSource,
    GroupSource,
    FollowEvent,
    UnfollowEvent,
    JoinEvent,
    LeaveEvent,
    PostbackEvent,
    BeaconEvent,
    MemberJoinedEvent,
    MemberLeftEvent,
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    MessagingApiBlob,
    ReplyMessageRequest,
    PushMessageRequest,
    MulticastRequest,
    BroadcastRequest,
    TextMessage,
    ApiException,
    LocationMessage,
    StickerMessage,
    ImageMessage,
    TemplateMessage,
    FlexMessage,
    Emoji,
    QuickReply,
    QuickReplyItem,
    ConfirmTemplate,
    ButtonsTemplate,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    FlexBubble,
    FlexImage,
    FlexBox,
    FlexText,
    FlexIcon,
    FlexButton,
    FlexSeparator,
    FlexContainer,
    MessageAction,
    URIAction,
    PostbackAction,
    DatetimePickerAction,
    CameraAction,
    CameraRollAction,
    LocationAction,
    ErrorResponse
)

from linebot.v3.insight import (
    ApiClient as InsightClient,
    Insight
)


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app.logger.setLevel(logging.INFO)
handler = WebhookHandler('6784e25383ee39debbddd38dbcd7ab1f')
Xeberlhyn = MessagingApi(ApiClient(Configuration("2Qch8cY6wIMUpoDKqxoe7vhUjCKTX07Ccn+Vn5hk8A1SqMu7TcvY0ablo0DDuEnaoASRcMTNFQu3buoi7MGmrbwRFEKJdzQPHgu/i1QhxqDuJy/MaCSK0sSKqnxEUOsrb5PFZPzw0FhCweL/vmfb0QdB04t89/1O/w1cDnyilFU=")))
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
chanels = Xeberlhyn.get_bot_info()
BotMID = chanels.user_id
Creator = 'u7b53d142b0b84803853f8841e48cba82'




def sendMessage(to, teks):
    return Xeberlhyn.reply_message(to, TextSendMessage(text=teks))

def sendImage(to, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, ImageSendMessage(url, url))

def sendAudio(to, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, AudioSendMessage(url, 60000))

def sendVideo(to, url):
    app.logger.info("url=" + url)
    preview = "https://i.ibb.co/wrJNNGL/20220219-100319.jpg"
    return Xeberlhyn.reply_message(to, VideoSendMessage(url, preview))

def sendTextImageURL(to, teks, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, [TextSendMessage(text=teks), ImageSendMessage(url, url)])

def sendTextAudioURL(to, teks, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, [TextSendMessage(text=teks), AudioSendMessage(url, 60000)])

def sendTextVideoURL(to, teks, url):
    app.logger.info("url=" + url)
    preview = "https://i.ibb.co/wrJNNGL/20220219-100319.jpg"
    return Xeberlhyn.reply_message(to, [TextSendMessage(text=teks), VideoSendMessage(url, preview)])

def sendFlexVideoURL(to, data, url):
    app.logger.info("url=" + url)
    preview = "https://i.ibb.co/wrJNNGL/20220219-100319.jpg"
    return Xeberlhyn.reply_message(to, [FlexSendMessage(alt_text="©VTEAM-OFFICIAL", contents=data), VideoSendMessage(url, preview)])

def sendFlexAudioURL(to, data, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, [FlexSendMessage(alt_text="©VTEAM-OFFICIAL", contents=data), VideoSendMessage(url, 60000)])

def sendFlexImageURL(to, data, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, [FlexSendMessage(alt_text="©VTEAM-OFFICIAL", contents=data), VideoSendMessage(url, url)])

def sendDowbleMessage(to, txt1, txt2):
    return Xeberlhyn.reply_message(to, [TextSendMessage(text=txt1), TextSendMessage(text=txt2)])



def make_static_tmp_dir():
    try:
        os.makedirs(static_tmp_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(static_tmp_path):
            pass
        else:
            raise


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except ApiException as e:
        app.logger.warn("Got exception from LINE Messaging API: %s\n" % e.body)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_text_message(event):
    tks = str(event.message.text)
    VinsenT = tks.lower()
    sender = event.source.user_id
    msg_id = event.message.id
    to = event.reply_token
    room = event.source.group_id
    if VinsenT == '!my profile':
        profile = Xeberlhyn.get_profile(sender)
        url = profile.picture_url
        c_ = "╭───「 Costumer service」"
        c_ += "\n│⊧≽ Nama : " + profile.display_name
        c_ += "\n│⊧≽ Status : " + str(profile.status_message)
        c_ += "\n│⊧≽ Mid : " + sender
        c_ += "\n│╭───「 message」"
        c_ += "\n││• hello dear, ini data profile mu"
        c_ += "\n│╰──────────────"
        c_ += "\n╰───「 By: ©VinsenTEAM 」"
        sendTextImageURL(to, str(c_), str(url))


@handler.add(MemberLeftEvent)
def handle_member_left(event):
    app.logger.info("Got memberLeft event")


@handler.add(UnknownEvent)
def handle_unknown_left(event):
    app.logger.info(f"unknown event {event}")

@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()
    make_static_tmp_dir()
    app.run(debug=options.debug, port=options.port)
