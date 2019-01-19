# Terraform::AWS::Route53Zone

Manages a Route53 Hosted Zone.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`ZoneId` - The Hosted Zone ID. This can be referenced by zone records.

`NameServers` - A list of name servers in associated (or default) delegation set.

## See Also

* [aws_route53_zone](https://www.terraform.io/docs/providers/aws/r/route53_zone.html) in the _Terraform Provider Documentation_