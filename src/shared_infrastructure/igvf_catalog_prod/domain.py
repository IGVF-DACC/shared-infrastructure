from constructs import Construct

from aws_cdk.aws_certificatemanager import Certificate
from aws_cdk.aws_route53 import HostedZone

from typing import Any


class Domain(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.name = 'catalogkg.igvf.org'
        self.certificate = Certificate.from_certificate_arn(
            self,
            'DomainCertificate',
            'arn:aws:acm:us-west-2:636503752262:certificate/623d26db-c86c-4341-b7cd-b5c9f92b2ffb',
        )
        self.east1_certificate = Certificate.from_certificate_arn(
            self,
            'East1Certificate',
            'arn:aws:acm:us-east-1:636503752262:certificate/b8fcae0e-ef8a-40a8-9dfb-1ab977d97505',
        )
        self.zone = HostedZone.from_lookup(
            self,
            'DomainZone',
            domain_name=self.name,
        )
