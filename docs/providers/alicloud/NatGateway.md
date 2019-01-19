# Terraform::Alicloud::NatGateway

Provides a resource to create a VPC NAT Gateway.


~> **NOTE:** Resource bandwidth packages will not be supported since 00:00 on November 4, 2017, and public IP can be replaced be elastic IPs.
If a Nat Gateway has already bought some bandwidth packages, it can not bind elastic IP and you have to submit the [work order](https://selfservice.console.aliyun.com/ticket/createIndex) to solve.
If you want to add public IP, you can use resource 'alicloud_eip_association' to bind several elastic IPs for one Nat Gateway.

~> **NOTE:** From version 1.7.1, this resource has deprecated bandwidth packages.
But, in order to manage stock bandwidth packages, version 1.13.0 re-support configuring 'bandwidth_packages'.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the nat gateway.

`Name` - The name of the nat gateway.

`Description` - The description of the nat gateway.

`Spec` - It has been deprecated from provider version 1.7.1.

`Specification` - The specification of the nat gateway.

`VpcId` - The VPC ID for the nat gateway.

`BandwidthPackageIds` - A list ID of the bandwidth packages, and split them with commas.

`SnatTableIds` - The nat gateway will auto create a snap and forward item, the `snat_table_ids` is the created one.

`ForwardTableIds` - The nat gateway will auto create a snap and forward item, the `forward_table_ids` is the created one.

## See Also

* [alicloud_nat_gateway](https://www.terraform.io/docs/providers/alicloud/r/nat_gateway.html) in the _Terraform Provider Documentation_