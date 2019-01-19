# Terraform::Grafana::Organization

The organization resource allows Grafana organizations and their membership to
be created and managed.

## Properties

`Name` - (Required) The display name for the Grafana organization created.

`AdminUser` - (Optional) The login name of the configured [default admin user](http://docs.grafana.org/installation/configuration/#admin-user) for the Grafana installation. If unset, this value defaults to `admin`, the Grafana default. Grafana adds the default admin user to all organizations automatically upon creation, and this parameter keeps Terraform from removing it from organizations.

`CreateUsers` - (Optional) Whether or not to create Grafana users specified in the organization's membership if they don't already exist in Grafana. If unspecified, this parameter defaults to `true`, creating placeholder users with the `Name`, `login`, and `email` set to the email of the user, and a random password. Setting this option to `false` will cause an error to be thrown for any users that do not already exist in Grafana.

`Admins` - (Optional) A list of email addresses corresponding to users who should be given `admin` access to the organization. Note: users specified here must already exist in Grafana unless 'create_users' is set to true.

`Editors` - (Optional) A list of email addresses corresponding to users who should be given `editor` access to the organization. Note: users specified here must already exist in Grafana unless 'create_users' is set to true.

`Viewers` - (Optional) A list of email addresses corresponding to users who should be given `viewer` access to the organization. Note: users specified here must already exist in Grafana unless 'create_users' is set to true.


## Return Values

### Fn::GetAtt

`OrgId` - The organization id assigned to this organization by Grafana.

## See Also

* [grafana_organization](https://www.terraform.io/docs/providers/grafana/r/organization.html) in the _Terraform Provider Documentation_