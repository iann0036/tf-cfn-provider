# TencentCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/tencentcloud** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `secret_id` - (Optional) This is the TencentCloud access key.

* `secret_key` - (Optional) This is the TencentCloud secret key.

* `region` - (Required) This is the TencentCloud region.
  The default input value is ap-guangzhou.



## Supported Resources

* [Terraform::TencentCloud::AlbServerAttachment](AlbServerAttachment.md)
* [Terraform::TencentCloud::CbsSnapshot](CbsSnapshot.md)
* [Terraform::TencentCloud::CbsStorage](CbsStorage.md)
* [Terraform::TencentCloud::ContainerClusterInstance](ContainerClusterInstance.md)
* [Terraform::TencentCloud::ContainerCluster](ContainerCluster.md)
* [Terraform::TencentCloud::Dnat](Dnat.md)
* [Terraform::TencentCloud::EipAssociation](EipAssociation.md)
* [Terraform::TencentCloud::Eip](Eip.md)
* [Terraform::TencentCloud::Instance](Instance.md)
* [Terraform::TencentCloud::KeyPair](KeyPair.md)
* [Terraform::TencentCloud::Lb](Lb.md)
* [Terraform::TencentCloud::NatGateway](NatGateway.md)
* [Terraform::TencentCloud::RouteEntry](RouteEntry.md)
* [Terraform::TencentCloud::RouteTable](RouteTable.md)
* [Terraform::TencentCloud::SecurityGroupRule](SecurityGroupRule.md)
* [Terraform::TencentCloud::SecurityGroup](SecurityGroup.md)
* [Terraform::TencentCloud::Subnet](Subnet.md)
* [Terraform::TencentCloud::Vpc](Vpc.md)