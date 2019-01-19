# Terraform::AWS::IamServiceLinkedRole

Provides an [IAM service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Amazon Resource Name (ARN) of the role.

`Arn` - The Amazon Resource Name (ARN) specifying the role.

`CreateDate` - The creation date of the IAM role.

`Name` - The name of the role.

`Path` - The path of the role.

`UniqueId` - The stable and unique string identifying the role.

## See Also

* [aws_iam_service_linked_role](https://www.terraform.io/docs/providers/aws/r/iam_service_linked_role.html) in the _Terraform Provider Documentation_