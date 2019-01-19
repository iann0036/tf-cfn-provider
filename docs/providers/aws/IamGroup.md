# Terraform::AWS::IamGroup

Provides an IAM group.

## Properties

`Name` - (Required) The group's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins".

`Path` - (Optional, default "/") Path in which to create the group.


## Return Values

### Fn::GetAtt

`Id` - The group's ID.

`Arn` - The ARN assigned by AWS for this group.

`Name` - The group's name.

`Path` - The path of the group in IAM.

`UniqueId` - The [unique ID][1] assigned by AWS.

## See Also

* [aws_iam_group](https://www.terraform.io/docs/providers/aws/r/iam_group.html) in the _Terraform Provider Documentation_