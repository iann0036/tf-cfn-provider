# Terraform::AWS::Route53Zone

Manages a Route53 Hosted Zone.

## Properties

`Name` - (Required) This is the name of the hosted zone.

`Comment` - (Optional) A comment for the hosted zone. Defaults to 'Managed by Terraform'.

`DelegationSetId` - (Optional) The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `Vpc` and `VpcId` as delegation sets can only be used for public zones.

`ForceDestroy` - (Optional) Whether to destroy all records (possibly managed outside of Terraform) in the zone when destroying the zone.

`Tags` - (Optional) A mapping of tags to assign to the zone.

`Vpc` - (Optional) Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with `DelegationSetId`, `VpcId`, and `VpcRegion` in this resource and any [`Terraform::AWS::Route53ZoneAssociation` resource](/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.

`VpcId` - (Optional, **DEPRECATED**) Use `Vpc` instead. The VPC to associate with a private hosted zone. Specifying `VpcId` will create a private hosted zone. Conflicts with `DelegationSetId` as delegation sets can only be used for public zones and `Vpc`.

`VpcRegion` - (Optional, **DEPRECATED**) Use `Vpc` instead. The VPC's region. Defaults to the region of the AWS provider.


## Return Values

### Fn::GetAtt

`ZoneId` - The Hosted Zone ID. This can be referenced by zone records.

`NameServers` - A list of name servers in associated (or default) delegation set.

## See Also

* [aws_route53_zone](https://www.terraform.io/docs/providers/aws/r/route53_zone.html) in the _Terraform Provider Documentation_