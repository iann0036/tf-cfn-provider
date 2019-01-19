# Terraform::TencentCloud::Lb

Provides a Load Balancer resource.

## Properties

`Type` - (Required) (Int) The network type of the LB, 2 for public network and 1 for private network.

`Forward` - (Optional) (Int) The type of the LB, 0 for classic and 1 for application.

`Name` - (Optional) The name of the LB.

`VpcId` - (Optional) The VPC ID of the LB, unspecified or 0 stands for CVM basic network.

`ProjectId` - (Optional) The project id of the LB, unspecified or 0 stands for default project.


## Return Values

### Fn::GetAtt

`Status` - The status of the LB.

## See Also

* [tencentcloud_lb](https://www.terraform.io/docs/providers/tencentcloud/r/lb.html) in the _Terraform Provider Documentation_