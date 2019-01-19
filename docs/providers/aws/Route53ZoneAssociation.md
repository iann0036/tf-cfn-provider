# Terraform::AWS::Route53ZoneAssociation

Manages a Route53 Hosted Zone VPC association. VPC associations can only be made on private zones.

~> **NOTE:** Unless explicit association ordering is required (e.g. a separate cross-account association authorization), usage of this resource is not recommended. Use the `vpc` configuration blocks available within the [`aws_route53_zone` resource](/docs/providers/aws/r/route53_zone.html) instead.

~> **NOTE:** Terraform provides both this standalone Zone VPC Association resource and exclusive VPC associations defined in-line in the [`aws_route53_zone` resource](/docs/providers/aws/r/route53_zone.html) via `vpc` configuration blocks. At this time, you cannot use those in-line VPC associations in conjunction with this resource and the same zone ID otherwise it will cause a perpetual difference in plan output. You can optionally use the generic Terraform resource [lifecycle configuration block](/docs/configuration/resources.html#lifecycle) with `ignore_changes` in the `aws_route53_zone` resource to manage additional associations via this resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The calculated unique identifier for the association.

`ZoneId` - The ID of the hosted zone for the association.

`VpcId` - The ID of the VPC for the association.

`VpcRegion` - The region in which the VPC identified by `vpc_id` was created.

## See Also

* [aws_route53_zone_association](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) in the _Terraform Provider Documentation_