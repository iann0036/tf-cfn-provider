# Triton Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/triton**. The below arguments may be included as the key/value or JSON properties in the secret:

* `account` - (Required) This is the name of the Triton account. It can also be
provided via the `SDC_ACCOUNT` or `TRITON_ACCOUNT` environment variables.
* `user` - (Optional) This is the username to interact with the triton API. It
can be provided via the `SDC_USER` or `TRITON_USER` environment variables.
* `key_material` - (Optional) This is the private key of an SSH key associated
with the Triton account to be used. If this is not set, the private key corresponding
to the fingerprint in `key_id` must be available via an SSH Agent. It can be provided
via the `SDC_KEY_MATERIAL` or `TRITON_KEY_MATERIAL` environment variables.
* `key_id` - (Required) This is the fingerprint of the public key matching the key
specified in `key_path`. It can be obtained via the command `ssh-keygen -l -E md5 -f /path/to/key`.
It can be provided via the `SDC_KEY_ID` or `TRITON_KEY_ID` environment variables.
* `url` - (Optional) This is the URL to the Triton API endpoint. It is required
if using a private installation of Triton. The default is to use the Joyent public
cloud us-west-1 endpoint. Valid public cloud endpoints include: `us-east-1`, `us-east-2`,
`us-east-3`, `us-sw-1`, `us-west-1`, `eu-ams-1`. It can be provided
via the `SDC_URL` or `TRITON_URL` environment variables.
* `insecure_skip_tls_verify` (Optional - defaults to false) This allows skipping
TLS verification of the Triton endpoint. It is useful when connecting to a temporary
Triton installation such as Cloud-On-A-Laptop which does not generally use a certificate
signed by a trusted root CA.


## Supported Resources

* [Terraform::Triton::Fabric](docs/providers/triton/Fabric.md)
* [Terraform::Triton::FirewallRule](docs/providers/triton/FirewallRule.md)
* [Terraform::Triton::InstanceTemplate](docs/providers/triton/InstanceTemplate.md)
* [Terraform::Triton::Key](docs/providers/triton/Key.md)
* [Terraform::Triton::Machine](docs/providers/triton/Machine.md)
* [Terraform::Triton::ServiceGroup](docs/providers/triton/ServiceGroup.md)
* [Terraform::Triton::Snapshot](docs/providers/triton/Snapshot.md)
* [Terraform::Triton::Vlan](docs/providers/triton/Vlan.md)