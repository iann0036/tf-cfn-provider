# Terraform::AWS::IamPolicyAttachment

Attaches a Managed IAM Policy to user(s), role(s), and/or group(s)

!> **WARNING:** The aws_iam_policy_attachment resource creates **exclusive** attachments of IAM policies. Across the entire AWS account, all of the users/roles/groups to which a single policy is attached must be declared by a single aws_iam_policy_attachment resource. This means that even any users/roles/groups that have the attached policy via any other mechanism (including other Terraform resources) will have that attached policy revoked by this resource. Consider `Terraform::AWS::IamRolePolicyAttachment`, `awsIamUserPolicyAttachment`, or `awsIamGroupPolicyAttachment` instead. These resources do not enforce exclusive attachment of an IAM policy.

~> **NOTE:** The usage of this resource conflicts with the `Terraform::AWS::IamGroupPolicyAttachment`, `awsIamRolePolicyAttachment`, and `awsIamUserPolicyAttachment` resources and will permanently show a difference if both are defined.

## Properties


## Return Values

### Fn::GetAtt

`Id` - The policy's ID.

`Name` - The name of the attachment.

## See Also

* [aws_iam_policy_attachment](https://www.terraform.io/docs/providers/aws/r/iam_policy_attachment.html) in the _Terraform Provider Documentation_