# Terraform::AWS::CloudhsmV2Hsm

Creates an HSM module in Amazon CloudHSM v2 cluster.

## Properties

`ClusterId` - (Required) The ID of Cloud HSM v2 cluster to which HSM will be added.

`SubnetId` - (Optional) The ID of subnet in which HSM module will be located.

`AvailabilityZone` - (Optional) The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.

`IpAddress` - (Optional) The IP address of HSM module. Must be within the CIDR of selected subnet.


## Return Values

### Fn::GetAtt

`HsmId` - The id of the HSM module.

`HsmState` - The state of the HSM module.

`HsmEniId` - The id of the ENI interface allocated for HSM module.

## See Also

* [aws_cloudhsm_v2_hsm](https://www.terraform.io/docs/providers/aws/r/cloudhsm_v2_hsm.html) in the _Terraform Provider Documentation_