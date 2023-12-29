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

channel_secret = os.getenv('6784e25383ee39debbddd38dbcd7ab1f', None)
channel_access_token = os.getenv('2Qch8cY6wIMUpoDKqxoe7vhUjCKTX07Ccn+Vn5hk8A1SqMu7TcvY0ablo0DDuEnaoASRcMTNFQu3buoi7MGmrbwRFEKJdzQPHgu/i1QhxqDuJy/MaCSK0sSKqnxEUOsrb5PFZPzw0FhCweL/vmfb0QdB04t89/1O/w1cDnyilFU=', None)
if channel_secret is None or channel_access_token is None:
    print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
    sys.exit(1)

handler = WebhookHandler(channel_secret)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
configuration = Configuration(access_token=channel_access_token)




def make_static_tmp_dir():
    try:
        os.makedirs(static_tmp_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(static_tmp_path):
            pass
        else:
            raise

@handler.add(MessageEvent, message=TextMessageContent)
def handle_text_message(event):
    Xeberlhyn = MessagingApi(ApiClient(configuration))
    tks = str(event.message.text)
    VinsenT = tks.lower()
    sender = event.source.user_id
    msg_id = event.message.id
    to = event.reply_token
    room = event.source.group_id
    if VinsenT == 'ping':
        profile = Xeberlhyn.get_profile(sender)
        c_ = "╭───「 Costumer service」"
        c_ += "\n│⊧≽ Nama : " + profile.display_name
        c_ += "\n│⊧≽ Status : " + str(profile.status_message)
        c_ += "\n│⊧≽ Mid : " + sender
        c_ += "\n│╭───「 message」"
        c_ += "\n││• hello dear, ini data profile mu"
        c_ += "\n│╰──────────────"
        c_ += "\n╰───「 By: ©VinsenTEAM 」"
        Xeberlhyn.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[TextMessage(text=str(c_))]
                    )
                )


#______________________________________________________________
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        print("\n")
    except InvalidSignatureError:
        abort(400)
    return 'OK'
if __name__ == "__main__":
    arg_parser = ArgumentParser(usage='Usage: python ' + __file__ + ' [--port <port>] [--help]')
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()
    make_static_tmp_dir()
    app.run(debug=options.debug, port=options.port)
