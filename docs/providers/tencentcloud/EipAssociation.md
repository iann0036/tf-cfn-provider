# Terraform::TencentCloud::EipAssociation

Provides an eip resource associated with other resource like CVM or ENI.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The association id.

`EipId` - The id of the EIP.

`InstanceId` - The instance id of the EIP bound with.

`NetworkInterfaceId` - The network interface id.

`PrivateIp` - (Optional) The IP belongs to the `network_interface_id`.

## See Also

* [tencentcloud_eip_association](https://www.terraform.io/docs/providers/tencentcloud/r/eip_association.html) in the _Terraform Provider Documentation_