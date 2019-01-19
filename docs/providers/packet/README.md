# Packet Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/packet**. The below arguments may be included as the key/value or JSON properties in the secret:

* `auth_token` - (Required) This is your Packet API Auth token.


## Supported Resources

* [Terraform::Packet::Device](docs/providers/packet/Device.md)
* [Terraform::Packet::IpAttachment](docs/providers/packet/IpAttachment.md)
* [Terraform::Packet::Organization](docs/providers/packet/Organization.md)
* [Terraform::Packet::Project](docs/providers/packet/Project.md)
* [Terraform::Packet::ReservedIpBlock](docs/providers/packet/ReservedIpBlock.md)
* [Terraform::Packet::SpotMarketRequest](docs/providers/packet/SpotMarketRequest.md)
* [Terraform::Packet::SshKey](docs/providers/packet/SshKey.md)
* [Terraform::Packet::Vlan](docs/providers/packet/Vlan.md)
* [Terraform::Packet::VolumeAttachment](docs/providers/packet/VolumeAttachment.md)
* [Terraform::Packet::Volume](docs/providers/packet/Volume.md)