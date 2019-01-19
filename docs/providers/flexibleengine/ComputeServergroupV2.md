# Terraform::FlexibleEngine::ComputeServergroupV2

Manages a V2 Server Group resource within FlexibleEngine.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Compute client. If omitted, the `Region` argument of the provider is used. Changing this creates a new server group.

`Name` - (Required) A unique name for the server group. Changing this creates a new server group.

`Policies` - (Required) The set of policies for the server group. Only two two policies are available right now, and both are mutually exclusive. See the Policies section for more information. Changing this creates a new server group.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Policies` - See Properties above.

`Members` - The instances that are part of this server group.

## See Also

* [flexibleengine_compute_servergroup_v2](https://www.terraform.io/docs/providers/flexibleengine/r/compute_servergroup_v2.html) in the _Terraform Provider Documentation_