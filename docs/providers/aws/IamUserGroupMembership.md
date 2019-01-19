# Terraform::AWS::IamUserGroupMembership

Provides a resource for adding an [IAM User][2] to [IAM Groups][1]. This
resource can be used multiple times with the same user for non-overlapping
groups.

To exclusively manage the users in a group, see the
[`aws_iam_group_membership` resource][3].

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`User` - The name of the IAM User.

`Groups` - The list of IAM Groups.

## See Also

* [aws_iam_user_group_membership](https://www.terraform.io/docs/providers/aws/r/iam_user_group_membership.html) in the _Terraform Provider Documentation_