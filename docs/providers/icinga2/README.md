# Icinga2 Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/icinga2**. The below arguments may be included as the key/value or JSON properties in the secret:

* ``api_url`` - (Required) The root API URL of an Icinga2 server.

* ``api_user`` - (Required) The API username to use to
  authenticate to the Icinga2 server.

* ``api_password`` - (Required) The password to use to
  authenticate to the Icinga2 server.

* ``insecure_skip_tls_verify`` - (optional) Defaults to false. If set to true,
  verification of the Icinga2 server's SSL certificate is disabled. This is a security
  risk and should be avoided.


## Supported Resources

* [Terraform::Icinga2::Checkcommand](Checkcommand.md)
* [Terraform::Icinga2::Host](Host.md)
* [Terraform::Icinga2::Hostgroup](Hostgroup.md)
* [Terraform::Icinga2::Notification](Notification.md)
* [Terraform::Icinga2::Service](Service.md)
* [Terraform::Icinga2::User](User.md)