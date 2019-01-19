# Terraform::TencentCloud::EipAssociation

Provides an eip resource associated with other resource like CVM or ENI.

## Properties

`EipId` - (Required) The eip's id.

`InstanceId` - (Optional) The instance id going to bind with the EIP. This field is conflict with `NetworkInterfaceId` and `PrivateIp` fields.

`NetworkInterfaceId` - (Optional) Indicates the network interface id like `eni-xxxxxx`. This field is conflict with `InstanceId`.

`PrivateIp` - (Optional) Indicates an IP belongs to the `NetworkInterfaceId`. This field is conflict with `InstanceId`.


## Return Values

### Fn::GetAtt

`Id` - The association id.

`EipId` - The id of the EIP.

`InstanceId` - The instance id of the EIP bound with.

`NetworkInterfaceId` - The network interface id.

`PrivateIp` - (Optional) The IP belongs to the `NetworkInterfaceId`.

## See Also

* [tencentcloud_eip_association](https://www.terraform.io/docs/providers/tencentcloud/r/eip_association.html) in the _Terraform Provider Documentation_