# Terraform::AWS::GameliftFleet

Provides a Gamelift Fleet resource.

## Properties

`BuildId` - (Required) ID of the Gamelift Build to be deployed on the fleet.

`Ec2InstanceType` - (Required) Name of an EC2 instance type. e.g. `t2.micro`.

`Name` - (Required) The name of the fleet.

`Description` - (Optional) Human-readable description of the fleet.

`Ec2InboundPermission` - (Optional) Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.

`MetricGroups` - (Optional) List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.

`NewGameSessionProtectionPolicy` - (Optional) Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.

`ResourceCreationLimitPolicy` - (Optional) Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.

`RuntimeConfiguration` - (Optional) Instructions for launching server processes on each instance in the fleet. See below.


## Return Values

### Fn::GetAtt

`Id` - Fleet ID.

`Arn` - Fleet ARN.

`OperatingSystem` - Operating system of the fleet's computing resources.

## See Also

* [aws_gamelift_fleet](https://www.terraform.io/docs/providers/aws/r/gamelift_fleet.html) in the _Terraform Provider Documentation_