# Terraform::NSXT::LbHttpsMonitor

Provides a resource to configure lb https monitor on NSX-T manager

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - ID of the lb_https_monitor.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`IsSecure` - This flag is set to true when all the ciphers and protocols are secure. It is set to false when one of the ciphers or protocols is insecure.

## See Also

* [nsxt_lb_https_monitor](https://www.terraform.io/docs/providers/nsxt/r/lb_https_monitor.html) in the _Terraform Provider Documentation_