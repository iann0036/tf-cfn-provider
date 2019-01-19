# Terraform::AWS::IamAccountPasswordPolicy

-> **Note:** There is only a single policy allowed per AWS account. An existing policy will be lost when using this resource as an effect of this limitation.

Manages Password Policy for the AWS Account.
See more about [Account Password Policy](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)
in the official AWS docs.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`ExpirePasswords` - Indicates whether passwords in the account expire.

## See Also

* [aws_iam_account_password_policy](https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy.html) in the _Terraform Provider Documentation_