# RabbitMQ Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/rabbitmq**. The below arguments may be included as the key/value or JSON properties in the secret:

* `endpoint` - (Required) The HTTP URL of the management plugin on the
  RabbitMQ server. The RabbitMQ management plugin *must* be enabled in order
  to use this provder. _Note_: This is not the IP address or hostname of the
  RabbitMQ server that you would use to access RabbitMQ directly.
* `username` - (Required) Username to use to authenticate with the server.
* `password` - (Optional) Password for the given user.
* `insecure` - (Optional) Trust self-signed certificates.
* `cacert_file` - (Optional) The path to a custom CA / intermediate certificate.


## Supported Resources

* [Terraform::RabbitMQ::Binding](docs/providers/rabbitmq/Binding.md)
* [Terraform::RabbitMQ::Exchange](docs/providers/rabbitmq/Exchange.md)
* [Terraform::RabbitMQ::Permissions](docs/providers/rabbitmq/Permissions.md)
* [Terraform::RabbitMQ::Policy](docs/providers/rabbitmq/Policy.md)
* [Terraform::RabbitMQ::Queue](docs/providers/rabbitmq/Queue.md)
* [Terraform::RabbitMQ::User](docs/providers/rabbitmq/User.md)
* [Terraform::RabbitMQ::Vhost](docs/providers/rabbitmq/Vhost.md)