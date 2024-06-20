from constructs import Construct

from typing import Any


class CodeStarConnection(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.arn = (
            'arn:aws:codestar-connections:'
            'us-west-2:109189702753:'
            'connection/d65802e7-37d9-4be6-bc86-f94b2104b5ff'
        )
