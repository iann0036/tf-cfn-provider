# Terraform::AWS::ApiGatewayVpcLink

Provides an API Gateway VPC Link.

## Properties

`Name` - (Required) The name used to label and identify the VPC link.

`Description` - (Optional) The description of the VPC link.

`TargetArns` - (Required, ForceNew) The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.


## Return Values

### Fn::GetAtt

`Id` - The identifier of the VpcLink.

## See Also

* [aws_api_gateway_vpc_link](https://www.terraform.io/docs/providers/aws/r/api_gateway_vpc_link.html) in the _Terraform Provider Documentation_