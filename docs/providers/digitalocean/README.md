# DigitalOcean Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/digitalocean**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) This is the DO API token. This can also be specified
  with the `DIGITALOCEAN_TOKEN` shell environment variable.
* `spaces_access_id` - (Optional) The access key ID used for Spaces API
  operations (Defaults to the value of the `SPACES_ACCESS_KEY_ID` environment
  variable).
* `spaces_secret_key` - (Optional) The secret access key used for Spaces API
  operations (Defaults to the value of the `SPACES_SECRET_ACCESS_KEY`
  environment variable).
* `api_endpoint` - (Optional) This can be used to override the base URL for
  DigitalOcean API requests (Defaults to the value of the `DIGITALOCEAN_API_URL`
  environment variable or `https://api.digitalocean.com if unset).

## Supported Resources

* [Terraform::DigitalOcean::Certificate](Certificate.md)
* [Terraform::DigitalOcean::Domain](Domain.md)
* [Terraform::DigitalOcean::DropletSnapshot](DropletSnapshot.md)
* [Terraform::DigitalOcean::Droplet](Droplet.md)
* [Terraform::DigitalOcean::Firewall](Firewall.md)
* [Terraform::DigitalOcean::FloatingIpAssignment](FloatingIpAssignment.md)
* [Terraform::DigitalOcean::FloatingIp](FloatingIp.md)
* [Terraform::DigitalOcean::KubernetesCluster](KubernetesCluster.md)
* [Terraform::DigitalOcean::KubernetesNodePool](KubernetesNodePool.md)
* [Terraform::DigitalOcean::Loadbalancer](Loadbalancer.md)
* [Terraform::DigitalOcean::Record](Record.md)
* [Terraform::DigitalOcean::SpacesBucket](SpacesBucket.md)
* [Terraform::DigitalOcean::SshKey](SshKey.md)
* [Terraform::DigitalOcean::Tag](Tag.md)
* [Terraform::DigitalOcean::VolumeAttachment](VolumeAttachment.md)
* [Terraform::DigitalOcean::VolumeSnapshot](VolumeSnapshot.md)
* [Terraform::DigitalOcean::Volume](Volume.md)