from constructs import Construct

from typing import Any


class CodeStarConnection(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.arn = (
            'arn:aws:codeconnections:'
            'us-west-2:636503752262:'
            'connection/fe8ba008-c9f7-4076-83bb-2c57ba0ecd45'
        )