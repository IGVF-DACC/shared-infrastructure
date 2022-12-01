from constructs import Construct

from aws_cdk.aws_certificatemanager import Certificate
from aws_cdk.aws_route53 import HostedZone

from typing import Any


class Domain(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.name = 'sandbox.igvf.org'
        self.certificate = Certificate.from_certificate_arn(
            self,
            'DomainCertificate',
            'arn:aws:acm:us-west-2:920073238245:certificate/42fc15e0-50ad-43c3-815b-cd2419ac67c2',
        )
        self.zone = HostedZone.from_lookup(
            self,
            'DomainZone',
            domain_name=self.name,
        )
