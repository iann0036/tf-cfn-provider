# Terraform::AWS::WafIpset

Provides a WAF IPSet Resource

## Properties

`Name` - (Required) The name or description of the IPSet.

`IpSetDescriptors` - (Optional) One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR format) from which web requests originate.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF IPSet.

`Arn` - The ARN of the WAF IPSet.

## See Also

* [aws_waf_ipset](https://www.terraform.io/docs/providers/aws/r/waf_ipset.html) in the _Terraform Provider Documentation_