# Terraform::AWS::IamRolePolicy

Provides an IAM role policy.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The role policy ID, in the form of `role_name:role_policy_name`.

`Name` - The name of the policy.

`Policy` - The policy document attached to the role.

`Role` - The name of the role associated with the policy.

## See Also

* [aws_iam_role_policy](https://www.terraform.io/docs/providers/aws/r/iam_role_policy.html) in the _Terraform Provider Documentation_