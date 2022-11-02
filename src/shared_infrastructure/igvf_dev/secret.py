from constructs import Construct

from aws_cdk.aws_secretsmanager import Secret

from typing import Any


class DockerHubCredentials(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'DockerSecret',
            'arn:aws:secretsmanager:us-west-2:109189702753:secret:docker-hub-credentials-EStRH5',
        )


class PortalCredentials(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.indexing_service_key = Secret.from_secret_complete_arn(
            self,
            'IndexingServiceKey',
            'arn:aws:secretsmanager:us-west-2:109189702753:secret:indexing-service-portal-key-BdNl8x',
        )
