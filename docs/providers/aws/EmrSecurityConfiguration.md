# Terraform::AWS::EmrSecurityConfiguration

Provides a resource to manage AWS EMR Security Configurations

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the EMR Security Configuration (Same as the `name`).

`Name` - The Name of the EMR Security Configuration.

`Configuration` - The JSON formatted Security Configuration.

`CreationDate` - Date the Security Configuration was created.

## See Also

* [aws_emr_security_configuration](https://www.terraform.io/docs/providers/aws/r/emr_security_configuration.html) in the _Terraform Provider Documentation_