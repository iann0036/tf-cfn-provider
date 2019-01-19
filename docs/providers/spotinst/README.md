# Spotinst Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/spotinst**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) A Personal API Access Token issued by Spotinst.
* `account` - (Optional) A valid Spotinst account ID.


## Supported Resources

* [Terraform::Spotinst::ElastigroupAwsBeanstalk](docs/providers/spotinst/ElastigroupAwsBeanstalk.md)
* [Terraform::Spotinst::ElastigroupAws](docs/providers/spotinst/ElastigroupAws.md)
* [Terraform::Spotinst::ElastigroupAzure](docs/providers/spotinst/ElastigroupAzure.md)
* [Terraform::Spotinst::ElastigroupGcp](docs/providers/spotinst/ElastigroupGcp.md)
* [Terraform::Spotinst::ElastigroupGke](docs/providers/spotinst/ElastigroupGke.md)
* [Terraform::Spotinst::OceanAws](docs/providers/spotinst/OceanAws.md)
* [Terraform::Spotinst::Subscription](docs/providers/spotinst/Subscription.md)