# Terraform::HuaweiCloud::IdentityGroupMembershipV3

Manages a User Group Membership resource within HuaweiCloud IAM service.

Note: You _must_ have admin privileges in your HuaweiCloud cloud to use
this resource.

Note: Please authentication on domain level via configuration
provider as following example:

```hcl
provider "huaweicloud" {
  user_name   = "<username>"
  password    = "<password>"
  domain_name = "<domain name>"
  auth_url    = "https://iam.eu-de.otc.t-systems.com/v3"
  region      = "eu-de"
  insecure    = "true"
}
```
Donot configuration either ```tenant_name``` nor ```tenant_id```.

## Properties

`Group` - (Required) The group ID of this membership.

`Users` - (Required) A List of user IDs to associate to the group.


## Return Values

### Fn::GetAtt

`Group` - See Properties above.

`Users` - See Properties above.

## See Also

* [huaweicloud_identity_group_membership_v3](https://www.terraform.io/docs/providers/huaweicloud/r/identity_group_membership_v3.html) in the _Terraform Provider Documentation_