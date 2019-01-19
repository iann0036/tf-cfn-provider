# Terraform::AWS::Cloud9EnvironmentEc2

Provides a Cloud9 EC2 Development Environment.

## Properties

`Name` - (Required) The name of the environment.

`InstanceType` - (Required) The type of instance to connect to the environment, e.g. `t2.micro`.

`AutomaticStopTimeMinutes` - (Optional) The number of minutes until the running instance is shut down after the environment has last been used.

`Description` - (Optional) The description of the environment.

`OwnerArn` - (Optional) The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to the environment's creator.

`SubnetId` - (Optional) The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.


## Return Values

### Fn::GetAtt

`Id` - The ID of the environment.

`Arn` - The ARN of the environment.

`Type` - The type of the environment (e.g. `ssh` or `ec2`).

## See Also

* [aws_cloud9_environment_ec2](https://www.terraform.io/docs/providers/aws/r/cloud9_environment_ec2.html) in the _Terraform Provider Documentation_