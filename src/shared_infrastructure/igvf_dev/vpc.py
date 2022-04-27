from constructs import Construct

from aws_cdk.aws_ec2 import Vpc


class DemoVpc(Construct):

    def __init__(self, scope, construct_id, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        self.vpc = Vpc.from_lookup(
            self,
            'DemoVpc',
            vpc_id='vpc-0b5e3b97317057133'
        )