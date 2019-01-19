# Terraform::NSXT::LbHttpRequestRewriteRule

Provides a resource to configure lb http request rewrite rule on NSX-T manager. This rule will be executed when HTTP request message is received by load balancer.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - ID of the lb rule.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_http_request_rewrite_rule](https://www.terraform.io/docs/providers/nsxt/r/lb_http_request_rewrite_rule.html) in the _Terraform Provider Documentation_