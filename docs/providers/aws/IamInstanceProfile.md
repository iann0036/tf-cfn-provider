# Terraform::AWS::IamInstanceProfile

Provides an IAM instance profile.

~> **NOTE:** Either `Role` or `Roles` (**deprecated**) must be specified.

## Properties

`Name` - (Optional, Forces new resource) The profile's name. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Path` - (Optional, default "/") Path in which to create the profile.

`Roles` - (**Deprecated**)
A list of role names to include in the profile.  The current default is 1.  If you see an error message similar to `Cannot exceed quota for InstanceSessionsPerInstanceProfile: 1`, then you must contact AWS support and ask for a limit increase.
WARNING: This is deprecated since [version 0.9.3 (April 12, 2017)](https://github.com/hashicorp/terraform/blob/master/CHANGELOG.md#093-april-12-2017), as >= 2 roles are not possible. See [issue #11575](https://github.com/hashicorp/terraform/issues/11575).

`Role` - (Optional) The role name to include in the profile.


## See Also

* [aws_iam_instance_profile](https://www.terraform.io/docs/providers/aws/r/iam_instance_profile.html) in the _Terraform Provider Documentation_