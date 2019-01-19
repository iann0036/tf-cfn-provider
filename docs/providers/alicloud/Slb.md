# Terraform::Alicloud::Slb

Provides an Application Load Balancer resource.

-> **NOTE:** Resource `alicloud_slb` has deprecated 'listener' filed from terraform-alicloud-provider [version 1.3.0](https://github.com/alibaba/terraform-provider/releases/tag/V1.3.0) . You can create new listeners for Load Balancer by resource `alicloud_slb_listener`.
If you have had several listeners in one load balancer, you can import them via the specified listener ID. In the `alicloud_slb_listener`, listener ID is consist of load balancer ID and frontend port, and its format is `<load balancer ID>:<frontend port>`, like "lb-hr2fwnf32t:8080".

-> **NOTE:** At present, to avoid some unnecessary regulation confusion, SLB can not support alicloud international account to create "paybybandwidth" instance.

-> **NOTE:** The supported specifications vary by region. Currently not all regions support guaranteed-performance instances.
For more details about guaranteed-performance instance, see [Guaranteed-performance instances](https://www.alibabacloud.com/help/doc-detail/27657.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the load balancer.

`Name` - The name of the load balancer.

`Internet` - The internet of the load balancer.

`InternetChargeType` - The internet_charge_type of the load balancer.

`Bandwidth` - The bandwidth of the load balancer.

`VswitchId` - The VSwitch ID of the load balancer. Only available on SLB launched in a VPC.

`Address` - The IP address of the load balancer.

`Specification` - The specification of the Server Load Balancer instance.

## See Also

* [alicloud_slb](https://www.terraform.io/docs/providers/alicloud/r/slb.html) in the _Terraform Provider Documentation_