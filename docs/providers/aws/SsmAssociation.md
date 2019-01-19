# Terraform::AWS::SsmAssociation

Associates an SSM Document to an instance or EC2 tag.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Name` - The name of the SSM document to apply.

`InstanceIds` - The instance id that the SSM document was applied to.

`Parameters` - Additional parameters passed to the SSM document.

## See Also

* [aws_ssm_association](https://www.terraform.io/docs/providers/aws/r/ssm_association.html) in the _Terraform Provider Documentation_