# Terraform::AWS::WafWebAcl

Provides a WAF Web ACL Resource

## Properties

`DefaultAction` - (Required) Configuration block with action that you want AWS WAF to take when a request doesn't match the criteria in any of the rules that are associated with the web ACL. Detailed below.

`MetricName` - (Required) The name or description for the Amazon CloudWatch metric of this web ACL.

`Name` - (Required) The name or description of the web ACL.

`Rules` - (Required) Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.

`LoggingConfiguration` - (Optional) Configuration block to enable WAF logging. Detailed below.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF WebACL.

## See Also

* [aws_waf_web_acl](https://www.terraform.io/docs/providers/aws/r/waf_web_acl.html) in the _Terraform Provider Documentation_