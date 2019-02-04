# Terraform::Alicloud::Slb

Provides an Application Load Balancer resource.

-> **NOTE:** Resource `Terraform::Alicloud::Slb` has deprecated 'listener' filed from terraform-alicloud-provider [version 1.3.0](https://github.com/alibaba/terraform-provider/releases/tag/V1.3.0) . You can create new listeners for Load Balancer by resource `alicloudSlbListener`.
If you have had several listeners in one load balancer, you can import them via the specified listener ID. In the `Terraform::Alicloud::SlbListener`, listener ID is consist of load balancer ID and frontend port, and its format is `<load balancer ID>:<frontend port>`, like "lb-hr2fwnf32t:8080".

-> **NOTE:** At present, to avoid some unnecessary regulation confusion, SLB can not support alicloud international account to create "paybybandwidth" instance.

-> **NOTE:** The supported specifications vary by region. Currently not all regions support guaranteed-performance instances.
For more details about guaranteed-performance instance, see [Guaranteed-performance instances](https://www.alibabacloud.com/help/doc-detail/27657.htm).

## Properties

`Name` - (Optional) The name of the SLB. This name must be unique within your AliCloud account, can have a maximum of 80 characters,
must contain only alphanumeric characters or hyphens, such as "-","/",".","_", and must not begin or end with a hyphen. If not specified,
Terraform will autogenerate a name beginning with `tf-lb`.

`Internet` - (Optional, Forces New Resource) If true, the SLB addressType will be internet, false will be intranet, Default is false. If load balancer launched in VPC, this value must be "false".

`InternetChargeType` - (Optional, Forces New Resource) Valid
values are `PayByBandwidth`, `PayByTraffic`. If this value is "PayByBandwidth", then argument "internet" must be "true". Default is "PayByTraffic". If load balancer launched in VPC, this value must be "PayByTraffic".
Before version 1.10.1, the valid values are "paybybandwidth" and "paybytraffic".

`Bandwidth` - (Optional) Valid
value is between 1 and 1000, If argument "internet_charge_type" is "paybytraffic", then this value will be ignore.

`Listener` - (Deprecated) The field has been deprecated from terraform-alicloud-provider [version 1.3.0](https://github.com/alibaba/terraform-provider/releases/tag/V1.3.0), and use resource `Terraform::Alicloud::SlbListener` to replace.

`VswitchId` - (Required for a VPC SLB, Forces New Resource) The VSwitch ID to launch in.

`Specification` - (Optional) The specification of the Server Load Balancer instance. Default to empty string indicating it is "Shared-Performance" instance.
Launching "[Performance-guaranteed](https://www.alibabacloud.com/help/doc-detail/27657.htm)" instance, it is must be specified and it valid values are: "slb.s1.small", "slb.s2.small", "slb.s2.medium",
"slb.s3.small", "slb.s3.medium" and "slb.s3.large".

`Tags` - (Optional) A mapping of tags to assign to the resource. The `Tags` can have a maximum of 10 tag for every load balancer instance.


## Return Values

### Fn::GetAtt

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