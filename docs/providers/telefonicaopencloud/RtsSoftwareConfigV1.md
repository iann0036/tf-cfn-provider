# Terraform::TelefonicaOpenCloud::RtsSoftwareConfigV1

Provides an RTS software config resource.

# Example Usage

 ```hcl
variable "config_name" {}
 
resource "telefonicaopencloud_rts_software_config_v1" "myconfig" {
  name = "${var.config_name}"
}
 ```

# Argument Reference

The following arguments are supported:

* `name` - (Required) The name of the software configuration.

* `group` - (Optional) The namespace that groups this software configuration by when it is delivered to a server.

* `inputs` - (Optional) A list of software configuration inputs.

* `outputs` - (Optional) A list of software configuration outputs.

* `config` - (Optional) The software configuration code.

* `options` - (Optional) The software configuration options.


# Attributes Reference

In addition to all arguments above, the following attributes are exported:

* `id` - The id of the software config.
 
# Import

Software Config can be imported using the `config id`, e.g.
```
 $ terraform import telefonicaopencloud_rts_software_config_v1 4779ab1c-7c1a-44b1-a02e-93dfc361b32d
```

## Properties

TBC

## See Also

* [telefonicaopencloud_rts_software_config_v1](https://www.terraform.io/docs/providers/telefonicaopencloud/r/rts_software_config_v1.html) in the _Terraform Provider Documentation_