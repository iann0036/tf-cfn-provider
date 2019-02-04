# Terraform::HuaweiCloud::IdentityProjectV3

Manages a Project resource within HuaweiCloud Identity And Access 
Management service.

Note: You _must_ have security admin privileges in your HuaweiCloud 
cloud to use this resource. please refer to [User Management Model](
https://docs.otc.t-systems.com/en-us/usermanual/iam/iam_01_0034.html)

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

`Name` - (Required) The name of the project. it must start with
ID of an existing region_ and be less than or equal to 64 characters.
Example: eu-de_project1.

`Description` - (Optional) A description of the project.

`DomainId` - (Optional) The domain this project belongs to. Changing this
creates a new Project.

`ParentId` - (Optional) The parent of this project. Changing this creates
a new Project.

`Region` - (Optional) The region in which to obtain the IAM client.
If omitted, the `Region` argument of the provider is used. Changing this
creates a new Project.


## Return Values

### Fn::GetAtt

`DomainId` - See Properties above.

`ParentId` - See Properties above.

## See Also

* [huaweicloud_identity_project_v3](https://www.terraform.io/docs/providers/huaweicloud/r/identity_project_v3.html) in the _Terraform Provider Documentation_