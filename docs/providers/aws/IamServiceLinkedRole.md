# Terraform::AWS::IamServiceLinkedRole

Provides an [IAM service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html).

## Properties

`AwsServiceName` - (Required, Forces new resource) The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).

`CustomSuffix` - (Optional, forces new resource) Additional string appended to the role name. Not all AWS services support custom suffixes.

`Description` - (Optional) The description of the role.


## Return Values

### Fn::GetAtt

`CreateDate` - The creation date of the IAM role.

`Name` - The name of the role.

`Arn` - The Amazon Resource Name (ARN) specifying the role.

`Path` - The path of the role.

`Id` - The Amazon Resource Name (ARN) of the role.

`UniqueId` - The stable and unique string identifying the role.

## See Also

* [aws_iam_service_linked_role](https://www.terraform.io/docs/providers/aws/r/iam_service_linked_role.html) in the _Terraform Provider Documentation_