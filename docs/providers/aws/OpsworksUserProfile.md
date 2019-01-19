# Terraform::AWS::OpsworksUserProfile

Provides an OpsWorks User Profile resource.

## Properties

`UserArn` - (Required) The user's IAM ARN.

`AllowSelfManagement` - (Optional) Whether users can specify their own SSH public key through the My Settings page.

`SshUsername` - (Required) The ssh username, with witch this user wants to log in.

`SshPublicKey` - (Optional) The users public key.


## Return Values

### Fn::GetAtt

`Id` - Same value as `UserArn`.

## See Also

* [aws_opsworks_user_profile](https://www.terraform.io/docs/providers/aws/r/opsworks_user_profile.html) in the _Terraform Provider Documentation_