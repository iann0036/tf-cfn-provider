# Terraform::TencentCloud::Lb

Provides a Load Balancer resource.

## Properties

`Type` - (Required)  The network type of the LB, valid choices: "OPEN", "INTERNAL".

`Forward` - (Optional) The type of the LB, valid choices: "CLASSIC", "APPLICATION".

`Name` - (Optional) The name of the LB.

`VpcId` - (Optional) The VPC ID of the LB, unspecified or 0 stands for CVM basic network.

`ProjectId` - (Optional) The project id of the LB, unspecified or 0 stands for default project.


## Return Values

### Fn::GetAtt

`Status` - The status of the LB.

## See Also

* [tencentcloud_lb](https://www.terraform.io/docs/providers/tencentcloud/r/lb.html) in the _Terraform Provider Documentation_