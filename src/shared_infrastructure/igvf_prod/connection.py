from constructs import Construct

from typing import Any


class CodeStarConnection(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.arn = (
            'arn:aws:codestar-connections:'
            'us-west-2:035226225042:'
            'connection/9f7b2d32-8c73-486a-b6b1-6a3a381e5d05'
        )
