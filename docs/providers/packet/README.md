# Packet Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/packet**. The below arguments may be included as the key/value or JSON properties in the secret:

* `auth_token` - (Required) This is your Packet API Auth token.


## Supported Resources

* [Terraform::Packet::Device](Device.md)
* [Terraform::Packet::IpAttachment](IpAttachment.md)
* [Terraform::Packet::Organization](Organization.md)
* [Terraform::Packet::Project](Project.md)
* [Terraform::Packet::ReservedIpBlock](ReservedIpBlock.md)
* [Terraform::Packet::SpotMarketRequest](SpotMarketRequest.md)
* [Terraform::Packet::SshKey](SshKey.md)
* [Terraform::Packet::Vlan](Vlan.md)
* [Terraform::Packet::VolumeAttachment](VolumeAttachment.md)
* [Terraform::Packet::Volume](Volume.md)