# Terraform::Alicloud::EipAssociation

Provides an Alicloud EIP Association resource for associating Elastic IP to ECS Instance, SLB Instance or Nat Gateway.

~> **NOTE:** `alicloud_eip_association` is useful in scenarios where EIPs are either
 pre-existing or distributed to customers or users and therefore cannot be changed.

~> **NOTE:** From version 1.7.1, the resource support to associate EIP to SLB Instance or Nat Gateway.

~> **NOTE:** One EIP can only be associated with ECS or SLB instance which in the VPC.

## Properties

TBC

## Return Values

### Fn::GetAtt

`AllocationId` - As above.

`InstanceId` - As above.

## See Also

* [alicloud_eip_association](https://www.terraform.io/docs/providers/alicloud/r/eip_association.html) in the _Terraform Provider Documentation_