from constructs import Construct

from aws_cdk.aws_certificatemanager import Certificate
from aws_cdk.aws_route53 import HostedZone

from typing import Any


class DemoDomain(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.name = 'demo.igvf.org'
        self.certificate = Certificate.from_certificate_arn(
            self,
            'DomainCertificate',
            'arn:aws:acm:us-west-2:109189702753:certificate/6bee1171-2028-43eb-aab8-d992da3c60df'
        )
        self.east1_certificate = Certificate.from_certificate_arn(
            self,
            'East1Certificate',
            'arn:aws:acm:us-east-1:109189702753:certificate/1db73b67-1246-4e2a-9e32-cc4cea331fb1'
        )
        self.zone = HostedZone.from_lookup(
            self,
            'DomainZone',
            domain_name=self.name,
        )
