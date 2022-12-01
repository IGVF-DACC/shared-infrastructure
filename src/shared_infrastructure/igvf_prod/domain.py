from constructs import Construct

from aws_cdk.aws_certificatemanager import Certificate
from aws_cdk.aws_route53 import HostedZone

from typing import Any


class Domain(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.name = 'data.igvf.org'
        self.certificate = Certificate.from_certificate_arn(
            self,
            'DomainCertificate',
            'arn:aws:acm:us-west-2:035226225042:certificate/50d2a523-674b-4172-be69-b570471cd9f9',
        )
        self.zone = HostedZone.from_lookup(
            self,
            'DomainZone',
            domain_name=self.name,
        )
