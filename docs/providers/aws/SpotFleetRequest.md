# Terraform::AWS::SpotFleetRequest

Provides an EC2 Spot Fleet Request resource. This allows a fleet of Spot
instances to be requested on the Spot market.

## Properties

`IamFleetRole` - (Required) Grants the Spot fleet permission to terminate Spot instances on your behalf when you cancel its Spot fleet request using CancelSpotFleetRequests or when the Spot fleet request expires, if you set terminateInstancesWithExpiration.

`ReplaceUnhealthyInstances` - (Optional) Indicates whether Spot fleet should replace unhealthy instances. Default `false`.

`LaunchSpecification` - Used to define the launch configuration of the spot-fleet request. Can be specified multiple times to define different bids across different markets and instance types.

`SpotPrice` - (Optional; Default: On-demand price) The maximum bid price per unit hour.

`WaitForFulfillment` - (Optional; Default: false) If set, Terraform will wait for the Spot Request to be fulfilled, and will throw an error if the timeout of 10m is reached.

`TargetCapacity` - The number of units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O.

`AllocationStrategy` - Indicates how to allocate the target capacity across the Spot pools specified by the Spot fleet request. The default is `lowestPrice`.

`InstancePoolsToUseCount` - (Optional; Default: 1) The number of Spot pools across which to allocate your target Spot capacity. Valid only when `AllocationStrategy` is set to `lowestPrice`. Spot Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.

`ExcessCapacityTerminationPolicy` - Indicates whether running Spot instances should be terminated if the target capacity of the Spot fleet request is decreased below the current size of the Spot fleet.

`TerminateInstancesWithExpiration` - Indicates whether running Spot instances should be terminated when the Spot fleet request expires.

`InstanceInterruptionBehaviour` - (Optional) Indicates whether a Spot instance stops or terminates when it is interrupted. Default is `terminate`.

`FleetType` - (Optional) The type of fleet request. Indicates whether the Spot Fleet only requests the target capacity or also attempts to maintain it. Default is `maintain`.

`ValidUntil` - (Optional) The end date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. Defaults to 24 hours.

`ValidFrom` - (Optional) The start date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Spot fleet request ID.

`SpotRequestState` - The state of the Spot fleet request.

## See Also

* [aws_spot_fleet_request](https://www.terraform.io/docs/providers/aws/r/spot_fleet_request.html) in the _Terraform Provider Documentation_