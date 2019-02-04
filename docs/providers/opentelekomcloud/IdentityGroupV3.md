# Terraform::OpenTelekomCloud::IdentityGroupV3

Manages a User Group resource within OpentelekomCloud IAM service.

Note: You _must_ have admin privileges in your OpentelekomCloud cloud to use
this resource.

Note: Please authentication on domain level via configuration
provider as following example:

```hcl
provider "opentelekomcloud" {
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

`Name` - (Required) The name of the group.The length is less than or equal
to 64 bytes.

`Description` - (Optional) A description of the group.

`DomainId` - (Optional) The domain this group belongs to.

`Region` - (Optional) The region in which to obtain the V3 Keystone client.
If omitted, the `Region` argument of the provider is used. Changing this
creates a new User Group.


## Return Values

### Fn::GetAtt

`DomainId` - See Properties above.

## See Also

* [opentelekomcloud_identity_group_v3](https://www.terraform.io/docs/providers/opentelekomcloud/r/identity_group_v3.html) in the _Terraform Provider Documentation_