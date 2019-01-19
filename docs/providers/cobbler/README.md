# Cobbler Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cobbler**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) The username to the Cobbler service.

* `password` - (Required) The password to the Cobbler service.

* `url` - (Required) The url to the Cobbler service.

* `insecure` - (Optional) Ignore SSL certificate warnings and errors.

* `cacert_file` - (Optional) The path or contents of an SSL CA certificate.
  This can also be specified with the `COBBLER_CACERT_FILE` shell environment
  variable.


## Supported Resources

* [Terraform::Cobbler::Distro](Distro.md)
* [Terraform::Cobbler::KickstartFile](KickstartFile.md)
* [Terraform::Cobbler::Profile](Profile.md)
* [Terraform::Cobbler::Repo](Repo.md)
* [Terraform::Cobbler::Snippet](Snippet.md)
* [Terraform::Cobbler::System](System.md)