# Terraform::AWS::WafregionalIpset

Provides a WAF Regional IPSet Resource for use with Application Load Balancer.

## Properties

`Name` - (Required) The name or description of the IPSet.

`IpSetDescriptor` - (Optional) One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR notation) from which web requests originate.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF IPSet.

`Arn` - The ARN of the WAF IPSet.

## See Also

* [aws_wafregional_ipset](https://www.terraform.io/docs/providers/aws/r/wafregional_ipset.html) in the _Terraform Provider Documentation_