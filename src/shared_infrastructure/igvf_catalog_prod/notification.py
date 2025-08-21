from constructs import Construct

from aws_cdk.aws_chatbot import SlackChannelConfiguration

from aws_cdk.aws_sns import Topic

from typing import Any


class Notification(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.encode_dcc_chatbot = SlackChannelConfiguration.from_slack_channel_configuration_arn(
            self,
            'CatalogChatbot',
            'arn:aws:chatbot::636503752262:chat-configuration/slack-channel/slack-catalog',
        )
        self.alarm_notification_topic = Topic.from_topic_arn(
            self,
            'AlarmNotificationTopic',
            topic_arn='arn:aws:sns:us-west-2:636503752262:IGVFProdCatalogSlack'
        )
