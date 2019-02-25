# Terraform::AWS::RamResourceAssociation

Manages a Resource Access Manager (RAM) Resource Association.

~> *NOTE:* Certain AWS resources (e.g. EC2 Subnets) can only be shared in an AWS account that is a member of an AWS Organizations organization with organization-wide Resource Access Manager functionality enabled. See the [Resource Access Manager User Guide](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) and AWS service specific documentation for additional information.

## Properties

`ResourceArn` - (Required) Amazon Resource Name (ARN) of the resource to associate with the RAM Resource Share.

`ResourceShareArn` - (Required) Amazon Resource Name (ARN) of the RAM Resource Share.


## Return Values

### Fn::GetAtt

`Id` - The Amazon Resource Name (ARN) of the resource share.

## See Also

* [aws_ram_resource_association](https://www.terraform.io/docs/providers/aws/r/ram_resource_association.html) in the _Terraform Provider Documentation_