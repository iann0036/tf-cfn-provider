# Terraform::AWS::IamUser

Provides an IAM user.

## Properties

`Name` - (Required) The user's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. User names are not distinguished by case. For example, you cannot create users named both "TESTUSER" and "testuser".

`Path` - (Optional, default "/") Path in which to create the user.

`PermissionsBoundary` - (Optional) The ARN of the policy that is used to set the permissions boundary for the user.

`ForceDestroy` - (Optional, default false) When destroying this user, destroy even if it has non-Terraform-managed IAM access keys, login profile or MFA devices. Without `ForceDestroy` a user with non-Terraform-managed access keys and login profile will fail to be destroyed.

`Tags` - Key-value mapping of tags for the IAM user.


## Return Values

### Fn::GetAtt

`Arn` - The ARN assigned by AWS for this user.

`Name` - The user's name.

`UniqueId` - The [unique ID][1] assigned by AWS.

## See Also

* [aws_iam_user](https://www.terraform.io/docs/providers/aws/r/iam_user.html) in the _Terraform Provider Documentation_