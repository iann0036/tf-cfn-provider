# Spotinst Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/spotinst** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Required) A Personal API Access Token issued by Spotinst.
* `account` - (Optional) A valid Spotinst account ID.


## Supported Resources

* [Terraform::Spotinst::ElastigroupAwsBeanstalk](ElastigroupAwsBeanstalk.md)
* [Terraform::Spotinst::ElastigroupAws](ElastigroupAws.md)
* [Terraform::Spotinst::ElastigroupAzure](ElastigroupAzure.md)
* [Terraform::Spotinst::ElastigroupGcp](ElastigroupGcp.md)
* [Terraform::Spotinst::ElastigroupGke](ElastigroupGke.md)
* [Terraform::Spotinst::Mrscaler](Mrscaler.md)
* [Terraform::Spotinst::MultaiBalancer](MultaiBalancer.md)
* [Terraform::Spotinst::MultaiDeployment](MultaiDeployment.md)
* [Terraform::Spotinst::MultaiListener](MultaiListener.md)
* [Terraform::Spotinst::MultaiRoutingRule](MultaiRoutingRule.md)
* [Terraform::Spotinst::MultaiTargetSet](MultaiTargetSet.md)
* [Terraform::Spotinst::MultaiTarget](MultaiTarget.md)
* [Terraform::Spotinst::OceanAws](OceanAws.md)
* [Terraform::Spotinst::Subscription](Subscription.md)