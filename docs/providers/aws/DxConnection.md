# Terraform::AWS::DxConnection

Provides a Connection of Direct Connect.

## Properties

`Name` - (Required) The name of the connection.

`Bandwidth` - (Required) The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.

`Location` - (Required) The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the connection.

`Arn` - The ARN of the connection.

`JumboFrameCapable` - Boolean value representing if jumbo frames have been enabled for this connection.

## See Also

* [aws_dx_connection](https://www.terraform.io/docs/providers/aws/r/dx_connection.html) in the _Terraform Provider Documentation_