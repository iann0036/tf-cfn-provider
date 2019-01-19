# Spotinst Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/spotinst**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) A Personal API Access Token issued by Spotinst.
* `account` - (Optional) A valid Spotinst account ID.


## Supported Resources

* [Terraform::Spotinst::ElastigroupAwsBeanstalk](ElastigroupAwsBeanstalk.md)
* [Terraform::Spotinst::ElastigroupAws](ElastigroupAws.md)
* [Terraform::Spotinst::ElastigroupAzure](ElastigroupAzure.md)
* [Terraform::Spotinst::ElastigroupGcp](ElastigroupGcp.md)
* [Terraform::Spotinst::ElastigroupGke](ElastigroupGke.md)
* [Terraform::Spotinst::OceanAws](OceanAws.md)
* [Terraform::Spotinst::Subscription](Subscription.md)