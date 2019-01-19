# Terraform::AWS::IamGroupPolicy

Provides an IAM policy attached to a group.

## Properties

`Policy` - (Required) The policy document. This is a JSON formatted string. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).

`Name` - (Optional) The name of the policy. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Group` - (Required) The IAM group to attach to the policy.


## Return Values

### Fn::GetAtt

`Id` - The group policy ID.

`Group` - The group to which this policy applies.

`Name` - The name of the policy.

`Policy` - The policy document attached to the group.

## See Also

* [aws_iam_group_policy](https://www.terraform.io/docs/providers/aws/r/iam_group_policy.html) in the _Terraform Provider Documentation_