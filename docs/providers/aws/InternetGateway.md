# Terraform::AWS::InternetGateway

Provides a resource to create a VPC Internet Gateway.

## Properties

`VpcId` - (Required) The VPC ID to create in.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Internet Gateway.

`OwnerId` - The ID of the AWS account that owns the internet gateway.

## See Also

* [aws_internet_gateway](https://www.terraform.io/docs/providers/aws/r/internet_gateway.html) in the _Terraform Provider Documentation_