# Terraform::AWS::OpsworksPermission

Provides an OpsWorks permission resource.

## Properties

`AllowSsh` - (Optional) Whether the user is allowed to use SSH to communicate with the instance.

`AllowSudo` - (Optional) Whether the user is allowed to use sudo to elevate privileges.

`UserArn` - (Required) The user's IAM ARN to set permissions for.

`Level` - (Optional) The users permission level. Mus be one of `deny`, `show`, `deploy`, `manage`, `iam_only`.

`StackId` - (Required) The stack to set the permissions for.


## Return Values

### Fn::GetAtt

`Id` - The computed id of the permission. Please note that this is only used internally to identify the permission. This value is not used in aws.

## See Also

* [aws_opsworks_permission](https://www.terraform.io/docs/providers/aws/r/opsworks_permission.html) in the _Terraform Provider Documentation_