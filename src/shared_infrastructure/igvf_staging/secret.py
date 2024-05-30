from constructs import Construct

from aws_cdk.aws_secretsmanager import Secret

from typing import Any


class DockerHubCredentials(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'DockerSecret',
            'arn:aws:secretsmanager:us-west-2:920073238245:secret:docker-hub-credentials-BODcWa',
        )


class PortalCredentials(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.indexing_service_key = Secret.from_secret_complete_arn(
            self,
            'IndexingServiceKey',
            'arn:aws:secretsmanager:us-west-2:920073238245:secret:indexing-service-portal-key-VNaZJw',
        )


class UploadFilesUserAccessKeys(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'AccessKeyAndSecretAccessKey',
            'arn:aws:secretsmanager:us-west-2:920073238245:secret:upload-igvf-files-user-access-key-secret-zoV8fQ',
        )


class UploadRestrictedFilesUserAccessKeys(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'AccessKeyAndSecretAccessKey',
            'arn:aws:secretsmanager:us-west-2:920073238245:secret:upload-igvf-restricted-files-user-access-key-secret-O5b9A6',
        )
