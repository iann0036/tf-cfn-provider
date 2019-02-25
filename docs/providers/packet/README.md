# Packet Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/packet** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `auth_token` - (Required) This is your Packet API Auth token.


## Supported Resources

* [Terraform::Packet::BgpSession](BgpSession.md)
* [Terraform::Packet::Device](Device.md)
* [Terraform::Packet::IpAttachment](IpAttachment.md)
* [Terraform::Packet::Organization](Organization.md)
* [Terraform::Packet::ProjectSshKey](ProjectSshKey.md)
* [Terraform::Packet::Project](Project.md)
* [Terraform::Packet::ReservedIpBlock](ReservedIpBlock.md)
* [Terraform::Packet::SpotMarketRequest](SpotMarketRequest.md)
* [Terraform::Packet::SshKey](SshKey.md)
* [Terraform::Packet::Vlan](Vlan.md)
* [Terraform::Packet::VolumeAttachment](VolumeAttachment.md)
* [Terraform::Packet::Volume](Volume.md)