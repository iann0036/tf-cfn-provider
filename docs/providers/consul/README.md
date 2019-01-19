# Consul Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/consul**. The below arguments may be included as the key/value or JSON properties in the secret:

* `address` - (Optional) The HTTP(S) API address of the agent to use. Defaults to "127.0.0.1:8500".
* `scheme` - (Optional) The URL scheme of the agent to use ("http" or "https"). Defaults to "http".
* `http_auth` - (Optional) HTTP Basic Authentication credentials to be used when communicating with Consul, in the format of either `user` or `user:pass`. This may also be specified using the `CONSUL_HTTP_AUTH` environment variable.
* `datacenter` - (Optional) The datacenter to use. Defaults to that of the agent.
* `token` - (Optional) The ACL token to use by default when making requests to the agent. Can also be specified with `CONSUL_HTTP_TOKEN` or `CONSUL_TOKEN` as an environment variable.
* `ca_file` - (Optional) A path to a PEM-encoded certificate authority used to verify the remote agent's certificate.
* `cert_file` - (Optional) A path to a PEM-encoded certificate provided to the remote agent; requires use of `key_file`.
* `key_file`- (Optional) A path to a PEM-encoded private key, required if `cert_file` is specified.
* `insecure_https`- (Optional) Boolean value to disable SSL certificate verification; setting this value to true is not recommended for production use. Only use this with scheme set to "https".


## Supported Resources

* [Terraform::Consul::AgentService](docs/providers/consul/AgentService.md)
* [Terraform::Consul::CatalogEntry](docs/providers/consul/CatalogEntry.md)
* [Terraform::Consul::Intention](docs/providers/consul/Intention.md)
* [Terraform::Consul::KeyPrefix](docs/providers/consul/KeyPrefix.md)
* [Terraform::Consul::Keys](docs/providers/consul/Keys.md)
* [Terraform::Consul::Node](docs/providers/consul/Node.md)
* [Terraform::Consul::PreparedQuery](docs/providers/consul/PreparedQuery.md)
* [Terraform::Consul::Service](docs/providers/consul/Service.md)