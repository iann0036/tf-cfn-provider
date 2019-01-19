# Terraform::OVH::PubliccloudUser

__DEPRECATED__ use `Terraform::OVH::CloudUser` instead.
Creates a user in a public cloud project.

## Properties

`ProjectId` - (Required) The id of the public cloud project. If omitted, the `OVH_PROJECT_ID` environment variable is used.

`Description` - A description associated with the user.


## Return Values

### Fn::GetAtt

`ProjectId` - See Properties above.

`Description` - See Properties above.

`Username` - the username generated for the user. This username can be used with.

`Password` - (Sensitive) the password generated for the user. The password can.

`Status` - the status of the user. should be normally set to 'ok'.

`CreationDate` - the date the user was created.

`OpenstackRc` - a convenient map representing an openstack_rc file.

## See Also

* [ovh_publiccloud_user](https://www.terraform.io/docs/providers/ovh/r/publiccloud_user.html) in the _Terraform Provider Documentation_