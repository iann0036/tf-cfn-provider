# Terraform::AWS::IamRole

Provides an IAM role.

## Properties

`Name` - (Optional, Forces new resource) The name of the role. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`AssumeRolePolicy` - (Required) The policy that grants an entity permission to assume the role.

`ForceDetachPolicies` - (Optional) Specifies to force detaching any policies the role has before destroying it. Defaults to `false`.

`Path` - (Optional) The path to the role. See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.

`Description` - (Optional) The description of the role.

`MaxSessionDuration` - (Optional) The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.

`PermissionsBoundary` - (Optional) The ARN of the policy that is used to set the permissions boundary for the role.

`Tags` - Key-value mapping of tags for the IAM role.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) specifying the role.

`CreateDate` - The creation date of the IAM role.

`Description` - The description of the role.

`Id` - The name of the role.

`Name` - The name of the role.

`UniqueId` - The stable and unique string identifying the role.

## See Also

* [aws_iam_role](https://www.terraform.io/docs/providers/aws/r/iam_role.html) in the _Terraform Provider Documentation_