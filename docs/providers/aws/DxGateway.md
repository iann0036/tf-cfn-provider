# Terraform::AWS::DxGateway

Provides a Direct Connect Gateway.

## Properties

`Name` - (Required) The name of the connection.

`AmazonSideAsn` - (Required) The ASN to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294.


## Return Values

### Fn::GetAtt

`Id` - The ID of the gateway.

## See Also

* [aws_dx_gateway](https://www.terraform.io/docs/providers/aws/r/dx_gateway.html) in the _Terraform Provider Documentation_