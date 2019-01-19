# Terraform::AWS::IamUserGroupMembership

Provides a resource for adding an [IAM User][2] to [IAM Groups][1]. This
resource can be used multiple times with the same user for non-overlapping
groups.

To exclusively manage the users in a group, see the
[`Terraform::AWS::IamGroupMembership` resource][3].

## Properties

`User` - (Required) The name of the [IAM User][2] to add to groups.

`Groups` - (Required) A list of [IAM Groups][1] to add the user to.


## Return Values

### Fn::GetAtt

`User` - The name of the IAM User.

`Groups` - The list of IAM Groups.

## See Also

* [aws_iam_user_group_membership](https://www.terraform.io/docs/providers/aws/r/iam_user_group_membership.html) in the _Terraform Provider Documentation_