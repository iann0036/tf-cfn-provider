# Terraform::BIGIP::LtmDatagroup

`Terraform::BIGIP::LtmDatagroup` Manages internal (in-line) datagroup configuration

Resource should be named with their "full path". The full path is the combination of the partition + name of the resource, for example /Common/my-datagroup.

## Properties

`Name` - (Required if `Record` defined), sets the value of the record's `Name` attribute, must be of type defined in `Type` attribute.

`Type` - (Required) datagroup type (applies to the `Name` field of the record), supports: `string`, `ip` or `integer`.

`Record` - (Optional) a set of `Name` and `Data` attributes, name must be of type specified by the `Type` attributed (`string`, `ip` and `integer`), data is optional and can take any value, multiple `Record` sets can be specified as needed.

`Data` - (Optional if `Record` defined), sets the value of the record's `Data` attribute, specifying a value here will create a record in the form of `name := data`.


## See Also

* [bigip_ltm_datagroup](https://www.terraform.io/docs/providers/bigip/r/ltm_datagroup.html) in the _Terraform Provider Documentation_