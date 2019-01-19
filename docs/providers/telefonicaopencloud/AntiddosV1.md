# Terraform::TelefonicaOpenCloud::AntiddosV1

Anti-DDoS monitors the service traffic from the Internet to ECSs, ELB instances, and BMSs to detect attack traffic in real time. It then cleans attack traffic according to user-configured defense policies so that services run as normal.

## Properties

`EnableL7` - (Required) Specifies whether to enable L7 defense.

`TrafficPosId` - (Required) The position ID of traffic. The value ranges from 1 to 9.

`HttpRequestPosId` - (Required) The position ID of number of HTTP requests. The value ranges from 1 to 15.

`CleaningAccessPosId` - (Required)The position ID of access limit during cleaning. The value ranges from 1 to 8.

`AppTypeId` - (Required) The application type ID.

`FloatingIpId` - (Required) The ID corresponding to the Elastic IP Address (EIP) of a user.


## See Also

* [telefonicaopencloud_antiddos_v1](https://www.terraform.io/docs/providers/telefonicaopencloud/r/antiddos_v1.html) in the _Terraform Provider Documentation_