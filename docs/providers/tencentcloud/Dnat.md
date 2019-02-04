# Terraform::TencentCloud::Dnat

Provides a port mapping/forwarding of destination network address port translation (DNAT/DNAPT) resource.

## Properties

`NatId` - (Required, Forces new resource) The ID for the NAT Gateway.

`VpcId` - (Required, Forces new resource) The VPC ID for the NAT Gateway.

`Protocol` - (Required, Forces new resource) The ip protocol, valid value is tcp|udp.

`ElasticIp` - (Required, Forces new resource) The elastic IP of NAT gateway association, must a [Elastic IP](eip.html).

`ElasticPort` - (Required, Forces new resource) The external port, valid value is 1~65535.

`PrivateIp` - (Required, Forces new resource) The internal ip, must a private ip (VPC IP).


## See Also

* [tencentcloud_dnat](https://www.terraform.io/docs/providers/tencentcloud/r/dnat.html) in the _Terraform Provider Documentation_