from constructs import Construct

from aws_cdk.aws_certificatemanager import Certificate
from aws_cdk.aws_route53 import HostedZone

from typing import Any


class Domain(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.name = 'staging.igvf.org'
        self.certificate = Certificate.from_certificate_arn(
            self,
            'DomainCertificate',
            'arn:aws:acm:us-west-2:920073238245:certificate/bee17e48-fc7e-4623-b675-b588c1df32ab',
        )
        self.zone = HostedZone.from_lookup(
            self,
            'DomainZone',
            domain_name=self.name,
        )
