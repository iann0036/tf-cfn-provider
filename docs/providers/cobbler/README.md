# Cobbler Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cobbler**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) The username to the Cobbler service. This can
  also be specified with the `COBBLER_USERNAME` shell environment variable.

* `password` - (Required) The password to the Cobbler service. This can
  also be specified with the `COBBLER_PASSWORD` shell environment variable.

* `url` - (Required) The url to the Cobbler service. This can
  also be specified with the `COBBLER_URL` shell environment variable.

* `insecure` - (Optional) Ignore SSL certificate warnings and errors. This
  can also be specified with the `COBBLER_INSECURE` shell environment variable.

* `cacert_file` - (Optional) The path or contents of an SSL CA certificate.
  This can also be specified with the `COBBLER_CACERT_FILE` shell environment
  variable.


## Supported Resources

* [Terraform::Cobbler::Distro](docs/providers/cobbler/Distro.md)
* [Terraform::Cobbler::KickstartFile](docs/providers/cobbler/KickstartFile.md)
* [Terraform::Cobbler::Profile](docs/providers/cobbler/Profile.md)
* [Terraform::Cobbler::Repo](docs/providers/cobbler/Repo.md)
* [Terraform::Cobbler::Snippet](docs/providers/cobbler/Snippet.md)
* [Terraform::Cobbler::System](docs/providers/cobbler/System.md)