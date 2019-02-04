# Terraform::AWS::AmiLaunchPermission

Adds launch permission to Amazon Machine Image (AMI) from another AWS account.

## Properties

`ImageId` - (required) A region-unique name for the AMI.

`AccountId` - (required) An AWS Account ID to add launch permissions.


## Return Values

### Fn::GetAtt

`Id` - A combination of "`ImageId`-`AccountId`".

## See Also

* [aws_ami_launch_permission](https://www.terraform.io/docs/providers/aws/r/ami_launch_permission.html) in the _Terraform Provider Documentation_