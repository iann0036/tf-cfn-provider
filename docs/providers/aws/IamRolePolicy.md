# Terraform::AWS::IamRolePolicy

Provides an IAM role policy.

## Properties

`Name` - (Optional) The name of the role policy. If omitted, Terraform will
assign a random, unique name.

`NamePrefix` - (Optional) Creates a unique name beginning with the specified
prefix. Conflicts with `Name`.

`Policy` - (Required) The policy document. This is a JSON formatted string. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).

`Role` - (Required) The IAM role to attach to the policy.


## Return Values

### Fn::GetAtt

`Id` - The role policy ID, in the form of `role_name:role_policy_name`.

`Name` - The name of the policy.

`Policy` - The policy document attached to the role.

`Role` - The name of the role associated with the policy.

## See Also

* [aws_iam_role_policy](https://www.terraform.io/docs/providers/aws/r/iam_role_policy.html) in the _Terraform Provider Documentation_