# Terraform::OPC::ComputeOrchestratedInstance

The `Terraform::OPC::ComputeOrchestratedInstance` resource creates and manages an orchestration containing a number of
instances in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Properties

`Name` - (Required) The name of the orchestration.

`DesiredState` - (Required) The desired state of the orchestration. Permitted values are:.

### DesiredState Properties

`Instance` - (Required) The information pertaining to creating an instance through the orchestration API.

`Description` - (Optional) The description of the orchestration.


## See Also

* [opc_compute_orchestrated_instance](https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance.html) in the _Terraform Provider Documentation_