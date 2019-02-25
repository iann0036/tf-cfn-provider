# Terraform::Spotinst::MultaiListener

Provides a Spotinst Multai Listener.

## Properties

`BalancerId` - (Required) The ID of the balancer.

`Protocol` - (Required) The protocol to allow connections to the load balancer.

`Port` - (Required) The port on which the load balancer is listening.

`TlsConfig` - (Optional) Describes the TLSConfig configuration.

`MinVersion` - (Required) MinVersion contains the minimum SSL/TLS version that is acceptable (1.0 is the minimum).

`MaxVersion` - (Required) MaxVersion contains the maximum SSL/TLS version that is acceptable.
*.

`Tags` - (Optional) A list of key:value paired tags.

`Key` - (Required) The tag's key.

`Value` - (Required) The tag's value.


## See Also

* [spotinst_multai_listener](https://www.terraform.io/docs/providers/spotinst/r/multai_listener.html) in the _Terraform Provider Documentation_