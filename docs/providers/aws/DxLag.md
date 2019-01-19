# Terraform::AWS::DxLag

Provides a Direct Connect LAG.

## Properties

`Name` - (Required) The name of the LAG.

`ConnectionsBandwidth` - (Required) The bandwidth of the individual physical connections bundled by the LAG. Available values: 1Gbps, 10Gbps. Case sensitive.

`Location` - (Required) The AWS Direct Connect location in which the LAG should be allocated. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.

`NumberOfConnections` - (**Deprecated**) The number of physical connections initially provisioned and bundled by the LAG. Use `Terraform::AWS::DxConnection` and `awsDxConnectionAssociation` resources instead. Default connections will be removed as part of LAG creation automatically in future versions.

`ForceDestroy` - (Optional, Default:false) A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are *not* recoverable.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the LAG.

`Arn` - The ARN of the LAG.

## See Also

* [aws_dx_lag](https://www.terraform.io/docs/providers/aws/r/dx_lag.html) in the _Terraform Provider Documentation_