# Terraform::AWS::IamUserPolicy

Provides an IAM policy attached to a user.

## Properties

`Policy` - (Required) The policy document. This is a JSON formatted string. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).

`Name` - (Optional) The name of the policy. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`User` - (Required) IAM user to which to attach this policy.


## Return Values

### Fn::GetAtt

`Id` - The user policy ID, in the form of `user_name:user_policy_name`.

`Name` - The name of the policy (always set).

## See Also

* [aws_iam_user_policy](https://www.terraform.io/docs/providers/aws/r/iam_user_policy.html) in the _Terraform Provider Documentation_