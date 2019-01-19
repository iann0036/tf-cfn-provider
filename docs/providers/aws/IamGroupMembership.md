# Terraform::AWS::IamGroupMembership

~> **WARNING:** Multiple aws_iam_group_membership resources with the same group name will produce inconsistent behavior!

Provides a top level resource to manage IAM Group membership for IAM Users. For
more information on managing IAM Groups or IAM Users, see [IAM Groups][1] or
[IAM Users][2]

~> **Note:** `Terraform::AWS::IamGroupMembership` will conflict with itself if used more than once with the same group. To non-exclusively manage the users in a group, see the
[`Terraform::AWS::IamUserGroupMembership` resource][3].

## Properties

`Name` - (Required) The name to identify the Group Membership.

`Users` - (Required) A list of IAM User names to associate with the Group.


## Return Values

### Fn::GetAtt

`Name` - The name to identify the Group Membership.

`Users` - list of IAM User names.

## See Also

* [aws_iam_group_membership](https://www.terraform.io/docs/providers/aws/r/iam_group_membership.html) in the _Terraform Provider Documentation_