# Terraform::NSXT::LbServerSslProfile

Provides a resource to configure lb server ssl profile on NSX-T manager

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - ID of the lb server ssl profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`IsSecure` - This flag is set to true when all the ciphers and protocols are secure. It is set to false when one of the ciphers or protocols is insecure.

## See Also

* [nsxt_lb_server_ssl_profile](https://www.terraform.io/docs/providers/nsxt/r/lb_server_ssl_profile.html) in the _Terraform Provider Documentation_