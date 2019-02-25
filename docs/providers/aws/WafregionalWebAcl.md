# Terraform::AWS::WafregionalWebAcl

Provides a WAF Regional Web ACL Resource for use with Application Load Balancer.

## Properties

`DefaultAction` - (Required) The action that you want AWS WAF Regional to take when a request doesn't match the criteria in any of the rules that are associated with the web ACL.

`MetricName` - (Required) The name or description for the Amazon CloudWatch metric of this web ACL.

`Name` - (Required) The name or description of the web ACL.

`LoggingConfiguration` - (Optional) Configuration block to enable WAF logging. Detailed below.

`Rule` - (Optional) Set of configuration blocks containing rules for the web ACL. Detailed below.


## Return Values

### Fn::GetAtt

`Arn` - Amazon Resource Name (ARN) of the WAF Regional WebACL.

`Id` - The ID of the WAF Regional WebACL.

## See Also

* [aws_wafregional_web_acl](https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl.html) in the _Terraform Provider Documentation_