# Terraform::AWS::IamPolicy

Provides an IAM policy.

## Properties

`Description` - (Optional, Forces new resource) Description of the IAM policy.

`Name` - (Optional, Forces new resource) The name of the policy. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Path` - (Optional, default "/") Path in which to create the policy.
See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.

`Policy` - (Required) The policy document. This is a JSON formatted string. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).


## Return Values

### Fn::GetAtt

`Id` - The policy's ID.

`Arn` - The ARN assigned by AWS to this policy.

`Description` - The description of the policy.

`Name` - The name of the policy.

`Path` - The path of the policy in IAM.

`Policy` - The policy document.

## See Also

* [aws_iam_policy](https://www.terraform.io/docs/providers/aws/r/iam_policy.html) in the _Terraform Provider Documentation_