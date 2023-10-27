from constructs import Construct

from aws_cdk.aws_ec2 import Vpc

from typing import Any


class DemoNetwork(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.vpc = Vpc.from_lookup(
            self,
            'DemoVpc',
            vpc_id='vpc-04c01400456f63ed9'
        )
