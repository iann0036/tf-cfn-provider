# Terraform::Vault::AwsAuthBackendRole

Manages an AWS auth backend role in a Vault server. Roles constrain the
instances or principals that can perform the login operation against the
backend. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/aws.html) for more
information.

## Properties

`Role` - (Required) The name of the role.

`AuthType` - (Optional) The auth type permitted for this role. Valid choices
are `ec2` and `iam`. Defaults to `iam`.

`BoundAmiIds` - (Optional) If set, defines a constraint on the EC2 instances
that can perform the login operation that they should be using the AMI ID
specified by this field. `AuthType` must be set to `ec2` or
`InferredEntityType` must be set to `ec2_instance` to use this constraint.

`BoundAccountIds` - (Optional) If set, defines a constraint on the EC2
instances that can perform the login operation that they should be using the
account ID specified by this field. `AuthType` must be set to `ec2` or
`InferredEntityType` must be set to `ec2_instance` to use this constraint.

`BoundRegions` - (Optional) If set, defines a constraint on the EC2 instances
that can perform the login operation that the region in their identity
document must match the one specified by this field. `AuthType` must be set
to `ec2` or `InferredEntityType` must be set to `ec2_instance` to use this
constraint.

`BoundVpcIds` - (Optional) If set, defines a constraint on the EC2 instances
that can perform the login operation that they be associated with the VPC ID
that matches the value specified by this field. `AuthType` must be set to
`ec2` or `InferredEntityType` must be set to `ec2_instance` to use this
constraint.

`BoundSubnetIds` - (Optional) If set, defines a constraint on the EC2
instances that can perform the login operation that they be associated with
the subnet ID that matches the value specified by this field. `AuthType`
must be set to `ec2` or `InferredEntityType` must be set to `ec2_instance`
to use this constraint.

`BoundIamRoleArns` - (Optional) If set, defines a constraint on the EC2
instances that can perform the login operation that they must match the IAM
role ARN specified by this field. `AuthType` must be set to `ec2` or
`InferredEntityType` must be set to `ec2_instance` to use this constraint.

`BoundIamInstanceProfileArns` - (Optional) If set, defines a constraint on
the EC2 instances that can perform the login operation that they must be
associated with an IAM instance profile ARN which has a prefix that matches
the value specified by this field. The value is prefix-matched as though it
were a glob ending in `*`. `AuthType` must be set to `ec2` or
`InferredEntityType` must be set to `ec2_instance` to use this constraint.

`RoleTag` - (Optional) If set, enable role tags for this role. The value set
for this field should be the key of the tag on the EC2 instance. `AuthType`
must be set to `ec2` or `InferredEntityType` must be set to `ec2_instance`
to use this constraint.

`BoundIamPrincipalArns` - (Optional) If set, defines the IAM principal that
must be authenticated when `AuthType` is set to `iam`. Wildcards are
supported at the end of the ARN.

`InferredEntityType` - (Optional) If set, instructs Vault to turn on
inferencing. The only valid value is `ec2_instance`, which instructs Vault to
infer that the role comes from an EC2 instance in an IAM instance profile.
This only applies when `AuthType` is set to `iam`.

`InferredAwsRegion` - (Optional) When `InferredEntityType` is set, this
is the region to search for the inferred entities. Required if
`InferredEntityType` is set. This only applies when `AuthType` is set to
`iam`.

`ResolveAwsUniqueIds` - (Optional) If set to `true`, the
`BoundIamPrincipalArns` are resolved to [AWS Unique
IDs](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-unique-ids)
for the bound principal ARN. This field is ignored when a
`bound_iam_principal_arn` ends in a wildcard. Resolving to unique IDs more
closely mimics the behavior of AWS services in that if an IAM user or role is
deleted and a new one is recreated with the same name, those new users or
roles won't get access to roles in Vault that were permissioned to the prior
principals of the same name. Defaults to `true`. Once set to `true`, this
cannot be changed to `false`--the role must be deleted and recreated, with
the value set to `true`.

`Ttl` - (Optional) The TTL period of tokens issued using this role, provided
as a number of seconds.

`MaxTtl` - (Optional) The maximum allowed lifetime of tokens issued using
this role, provided as a number of seconds.

`Period` - (Optional) If set, indicates that the token generated using this
role should never expire. The token should be renewed within the duration
specified by this value. At each renewal, the token's TTL will be set to the
value of this field. The maximum allowed lifetime of token issued using this
role. Specified as a number of seconds.

`Policies` - (Optional) An array of strings specifying the policies to be set
on tokens issued using this role.

`AllowInstanceMigration` - (Optional) If set to `true`, allows migration of
the underlying instance where the client resides.

`DisallowReauthentication` - (Optional) IF set to `true`, only allows a
single token to be granted per instance ID. This can only be set when
`AuthType` is set to `ec2`.


## See Also

* [vault_aws_auth_backend_role](https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role.html) in the _Terraform Provider Documentation_