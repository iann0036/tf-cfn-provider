# Terraform::Spotinst::Mrscaler

Provides a Spotinst AWS MrScaler resource.

## Properties

`Name` - (Required) The MrScaler name.

`Description` - (Optional) The MrScaler description.

`Region` - (Required) The MrScaler region.

`Strategy` - (Required) The MrScaler strategy. Allowed values are `new` `clone` and `wrap`.

`ClusterId` - (Optional) The MrScaler cluster id.

`ExposeClusterId` - (Optional) Allow the `ClusterId` to set a Terraform output variable.


## Return Values

### Fn::GetAtt

`Id` - The scaler ID.

## See Also

* [spotinst_mrscaler](https://www.terraform.io/docs/providers/spotinst/r/mrscaler.html) in the _Terraform Provider Documentation_