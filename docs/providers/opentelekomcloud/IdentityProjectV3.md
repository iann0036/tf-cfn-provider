# Terraform::OpenTelekomCloud::IdentityProjectV3

Manages a Project resource within OpentelekomCloud Identity And Access 
Management service.

Note: You _must_ have security admin privileges in your OpentelekomCloud 
cloud to use this resource. please refer to [User Management Model](
https://docs.otc.t-systems.com/en-us/usermanual/iam/iam_01_0034.html)

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

* [opentelekomcloud_identity_project_v3](https://www.terraform.io/docs/providers/opentelekomcloud/r/identity_project_v3.html) in the _Terraform Provider Documentation_