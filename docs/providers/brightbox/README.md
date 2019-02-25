# Brightbox Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/brightbox** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `apiclient` - (optional) This is the Brightbox client id for an
account.

* `apisecret` - (optional) This is the Brightbox client secret. This can
also be specified with the `BRIGHTBOX_CLIENT_SECRET` shell environment
variable.

* `username` - (optional) This is the Brightbox user logon. This can
also be specified with the `BRIGHTBOX_USER_NAME` shell environment
variable.

* `password` - (optional) This is the Brightbox user logon password. This
can also be specified with the `BRIGHTBOX_PASSWORD` shell environment
variable.

* `account` - (optional) This is the Brightbox account you wish to
operate upon.

* `apiurl` - (Optional) Use this to override the default endpoint URL
constructed for the region. It's typically used to connect to custom
Brightbox endpoints.

~> **NOTE:** At least one of `username` or `apiclient` must be specified.


## Supported Resources

* [Terraform::Brightbox::Cloudip](Cloudip.md)
* [Terraform::Brightbox::Container](Container.md)
* [Terraform::Brightbox::DatabaseServer](DatabaseServer.md)
* [Terraform::Brightbox::FirewallPolicy](FirewallPolicy.md)
* [Terraform::Brightbox::FirewallRule](FirewallRule.md)
* [Terraform::Brightbox::LoadBalancer](LoadBalancer.md)
* [Terraform::Brightbox::ServerGroup](ServerGroup.md)
* [Terraform::Brightbox::Server](Server.md)