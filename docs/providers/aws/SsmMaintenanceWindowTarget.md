# Terraform::AWS::SsmMaintenanceWindowTarget

Provides an SSM Maintenance Window Target resource

## Properties

`WindowId` - (Required) The Id of the maintenance window to register the target with.

`ResourceType` - (Required) The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.

`Targets` - (Required) The targets (either instances or tags). Instances are specified using Key=instanceids,Values=instanceid1,instanceid2. Tags are specified using Key=tag name,Values=tag value.

`OwnerInformation` - (Optional) User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.


## Return Values

### Fn::GetAtt

`Id` - The ID of the maintenance window target.

## See Also

* [aws_ssm_maintenance_window_target](https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_target.html) in the _Terraform Provider Documentation_