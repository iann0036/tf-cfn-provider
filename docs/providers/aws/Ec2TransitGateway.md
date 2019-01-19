# Terraform::AWS::Ec2TransitGateway

Manages an EC2 Transit Gateway.

## Properties

`AmazonSideAsn` - (Optional) Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is `64512` to `65534` for 16-bit ASNs and `4200000000` to `4294967294` for 32-bit ASNs. Default value: `64512`.

`AutoAcceptSharedAttachments` - (Optional) Whether resource attachment requests are automatically accepted. Valid values: `disable`, `enable`. Default value: `disable`.

`DefaultRouteTableAssociation` - (Optional) Whether resource attachments are automatically associated with the default association route table. Valid values: `disable`, `enable`. Default value: `enable`.

`DefaultRouteTablePropagation` - (Optional) Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: `disable`, `enable`. Default value: `enable`.

`Description` - (Optional) Description of the EC2 Transit Gateway.

`DnsSupport` - (Optional) Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.

`Tags` - (Optional) Key-value tags for the EC2 Transit Gateway.

`VpnEcmpSupport` - (Optional) Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.


## See Also

* [aws_ec2_transit_gateway](https://www.terraform.io/docs/providers/aws/r/ec2_transit_gateway.html) in the _Terraform Provider Documentation_