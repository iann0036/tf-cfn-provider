# Terraform::AWS::Ec2CapacityReservation

Provides an EC2 Capacity Reservation. This allows you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration.

## Properties

`AvailabilityZone` - (Required) The Availability Zone in which to create the Capacity Reservation.

`EbsOptimized` - (Optional) Indicates whether the Capacity Reservation supports EBS-optimized instances.

`EndDate` - (Optional) The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`).

`EndDateType` - (Optional) Indicates the way in which the Capacity Reservation ends. Specify either `unlimited` or `limited`.

`EphemeralStorage` - (Optional) Indicates whether the Capacity Reservation supports instances with temporary, block-level storage.

`InstanceCount` - (Required) The number of instances for which to reserve capacity.

`InstanceMatchCriteria` - (Optional) Indicates the type of instance launches that the Capacity Reservation accepts. Specify either `open` or `targeted`.

`InstancePlatform` - (Required) The type of operating system for which to reserve capacity. Valid options are `Linux/UNIX`, `Red Hat Enterprise Linux`, `SUSE Linux`, `Windows`, `Windows with SQL Server`, `Windows with SQL Server Enterprise`, `Windows with SQL Server Standard` or `Windows with SQL Server Web`.

`InstanceType` - (Required) The instance type for which to reserve capacity.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Tenancy` - (Optional) Indicates the tenancy of the Capacity Reservation. Specify either `default` or `dedicated`.


## Return Values

### Fn::GetAtt

`Id` - The Capacity Reservation ID.

## See Also

* [aws_ec2_capacity_reservation](https://www.terraform.io/docs/providers/aws/r/ec2_capacity_reservation.html) in the _Terraform Provider Documentation_