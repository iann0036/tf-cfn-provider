# Terraform::AWS::WafregionalWebAclAssociation

Provides a resource to create an association between a WAF Regional WebACL and Application Load Balancer.

-> **Note:** An Application Load Balancer can only be associated with one WAF Regional WebACL.

## Properties

`WebAclId` - (Required) The ID of the WAF Regional WebACL to create an association.

`ResourceArn` - (Required) Application Load Balancer ARN to associate with.


## Return Values

### Fn::GetAtt

`Id` - The ID of the association.

## See Also

* [aws_wafregional_web_acl_association](https://www.terraform.io/docs/providers/aws/r/wafregional_web_acl_association.html) in the _Terraform Provider Documentation_