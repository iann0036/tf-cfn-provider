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

* [Terraform::DigitalOcean::Certificate](docs/providers/digitalocean/Certificate.md)
* [Terraform::DigitalOcean::Domain](docs/providers/digitalocean/Domain.md)
* [Terraform::DigitalOcean::DropletSnapshot](docs/providers/digitalocean/DropletSnapshot.md)
* [Terraform::DigitalOcean::Droplet](docs/providers/digitalocean/Droplet.md)
* [Terraform::DigitalOcean::Firewall](docs/providers/digitalocean/Firewall.md)
* [Terraform::DigitalOcean::FloatingIpAssignment](docs/providers/digitalocean/FloatingIpAssignment.md)
* [Terraform::DigitalOcean::FloatingIp](docs/providers/digitalocean/FloatingIp.md)
* [Terraform::DigitalOcean::KubernetesCluster](docs/providers/digitalocean/KubernetesCluster.md)
* [Terraform::DigitalOcean::KubernetesNodePool](docs/providers/digitalocean/KubernetesNodePool.md)
* [Terraform::DigitalOcean::Loadbalancer](docs/providers/digitalocean/Loadbalancer.md)
* [Terraform::DigitalOcean::Record](docs/providers/digitalocean/Record.md)
* [Terraform::DigitalOcean::SpacesBucket](docs/providers/digitalocean/SpacesBucket.md)
* [Terraform::DigitalOcean::SshKey](docs/providers/digitalocean/SshKey.md)
* [Terraform::DigitalOcean::Tag](docs/providers/digitalocean/Tag.md)
* [Terraform::DigitalOcean::VolumeAttachment](docs/providers/digitalocean/VolumeAttachment.md)
* [Terraform::DigitalOcean::VolumeSnapshot](docs/providers/digitalocean/VolumeSnapshot.md)
* [Terraform::DigitalOcean::Volume](docs/providers/digitalocean/Volume.md)