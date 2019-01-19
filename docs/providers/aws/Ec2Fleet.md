# Terraform::AWS::Ec2Fleet

Provides a resource to manage EC2 Fleets.

## Properties

`LaunchTemplateConfig` - (Required) Nested argument containing EC2 Launch Template configurations. Defined below.

`TargetCapacitySpecification` - (Required) Nested argument containing target capacity configurations. Defined below.

`ExcessCapacityTerminationPolicy` - (Optional) Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.

`OnDemandOptions` - (Optional) Nested argument containing On-Demand configurations. Defined below.

`ReplaceUnhealthyInstances` - (Optional) Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.

`SpotOptions` - (Optional) Nested argument containing Spot configurations. Defined below.

`Tags` - (Optional) Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.

`TerminateInstances` - (Optional) Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.

`TerminateInstancesWithExpiration` - (Optional) Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.

`Type` - (Optional) The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.


## See Also

* [aws_ec2_fleet](https://www.terraform.io/docs/providers/aws/r/ec2_fleet.html) in the _Terraform Provider Documentation_