# Terraform::AWS::OrganizationsPolicy

Provides a resource to manage an [AWS Organizations policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html).

## Properties

`Content` - (Required) The policy content to add to the new policy. For example, if you create a [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the [Service Control Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html).

`Name` - (Required) The friendly name to assign to the policy.

`Description` - (Optional) A description to assign to the policy.

`Type` - (Optional) The type of policy to create. Currently, the only valid value is `SERVICE_CONTROL_POLICY` (SCP).


## See Also

* [aws_organizations_policy](https://www.terraform.io/docs/providers/aws/r/organizations_policy.html) in the _Terraform Provider Documentation_