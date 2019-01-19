# Chef Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/chef**. The below arguments may be included as the key/value or JSON properties in the secret:

* `server_url` - (Required) The HTTP(S) API URL of the Chef server to use. If
  the target Chef server supports organizations, use the full URL of the
  organization you wish to configure. May be provided instead via the
  ``CHEF_SERVER_URL`` environment variable.
* `client_name` - (Required) The name of the client account to use when making
  requests. This must have been already configured on the Chef server.
  May be provided instead via the ``CHEF_CLIENT_NAME`` environment variable.
* `key_material` - (Required) The PEM-formatted private key contents belonging to
  the configured client. This is issued by the server when a new client object
  is created. May be provided via the
  ``CHEF_KEY_MATERIAL`` environment variable.
* `allow_unverified_ssl` - (Optional) Boolean indicating whether to make
  requests to a Chef server whose SSL certicate cannot be verified. Defaults
  to ``false``.


## Supported Resources

* [Terraform::Chef::DataBagItem](docs/providers/chef/DataBagItem.md)
* [Terraform::Chef::DataBag](docs/providers/chef/DataBag.md)
* [Terraform::Chef::Environment](docs/providers/chef/Environment.md)
* [Terraform::Chef::Node](docs/providers/chef/Node.md)
* [Terraform::Chef::Role](docs/providers/chef/Role.md)