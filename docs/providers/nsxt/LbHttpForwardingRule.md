# Terraform::NSXT::LbHttpForwardingRule

Provides a resource to configure lb http forwarding rule on NSX-T manager. This rule will be executed when HTTP request message is forwarded by load balancer.

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb rule.

`MatchStrategy` - (Required) Strategy to define how load balancer rule is considered a match when multiple match conditions are specified in one rule. If set to ALL, then load balancer rule is considered a match only if all the conditions match. If set to ANY, then load balancer rule is considered a match if any one of the conditions match.

`BodyCondition` - (Optional) Set of match conditions used to match http request body:
* `Value` - (Required) The value to look for in the body.
* `MatchType` - (Required) Defines how value field is used to match the body of HTTP requests. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Value` - (Required) The value to look for in the body.
* `MatchType` - (Required) Defines how value field is used to match the body of HTTP requests. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`MatchType` - (Required) Defines how value field is used to match the body of HTTP requests. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`HeaderCondition` - (Optional) Set of match conditions used to match http request header:
* `Name` - (Required) The name of HTTP header to match.
* `Value` - (Required) The value of HTTP header to match.
* `MatchType` - (Required) Defines how value field is used to match the header value of HTTP requests. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX. Header name field does not support match types.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Name` - (Required) The name of HTTP header to match.
* `Value` - (Required) The value of HTTP header to match.
* `MatchType` - (Required) Defines how value field is used to match the header value of HTTP requests. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX. Header name field does not support match types.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Value` - (Required) The value of HTTP header to match.
* `MatchType` - (Required) Defines how value field is used to match the header value of HTTP requests. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX. Header name field does not support match types.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`MatchType` - (Required) Defines how value field is used to match the header value of HTTP requests. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX. Header name field does not support match types.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`CookieCondition` - (Optional) Set of match conditions used to match http request cookie:
* `Name` - (Required) The name of cookie to match.
* `Value` - (Required) The value of cookie to match.
* `MatchType` - (Required) Defines how value field is used to match the cookie. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Name` - (Required) The name of cookie to match.
* `Value` - (Required) The value of cookie to match.
* `MatchType` - (Required) Defines how value field is used to match the cookie. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Value` - (Required) The value of cookie to match.
* `MatchType` - (Required) Defines how value field is used to match the cookie. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`MatchType` - (Required) Defines how value field is used to match the cookie. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`MethodCondition` - (Optional) Set of match conditions used to match http request method:
* `Method` - (Required) One of GET, HEAD, POST, PUT, OPTIONS.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Method` - (Required) One of GET, HEAD, POST, PUT, OPTIONS.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`VersionCondition` - (Optional) Match condition used to match http version of the request:
* `Version` - (Required) One of HTTP_VERSION_1_0, HTTP_VERSION_1_1.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Version` - (Required) One of HTTP_VERSION_1_0, HTTP_VERSION_1_1.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`IpCondition` - (Optional) Set of match conditions used to match IP header values of HTTP request:
* `SourceAddress` - (Required) The value source IP address to match.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`SourceAddress` - (Required) The value source IP address to match.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`UriCondition` - (Optional) Set of match conditions used to match http request URI:
* `Uri` - (Required) The value of URI to match.
* `MatchType` - (Required) Defines how value field is used to match the URI. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Uri` - (Required) The value of URI to match.
* `MatchType` - (Required) Defines how value field is used to match the URI. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`MatchType` - (Required) Defines how value field is used to match the URI. Accepted values are STARTS_WITH, ENDS_WITH, CONTAINS, EQUALS, REGEX.
* `CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`CaseSensitive` - (Optional) If true, case is significant in the match. Default is true.
* `Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`Inverse` - (Optional) A flag to indicate whether reverse the match result of this condition. Default is false.

`HttpRejectAction` - (At least one action is required) Set of http reject actions to be executed when load balancer rule matches:
* `ReplyStatus` - (Required) The HTTP reply status.
* `ReplyMessage` - (Required) The HTTP reply message.

`ReplyStatus` - (Required) The HTTP reply status.
* `ReplyMessage` - (Required) The HTTP reply message.

`ReplyMessage` - (Required) The HTTP reply message.

`HttpRedirectAction` - (At least one action is required) Set of http redirect actions to be executed when load balancer rule matches:
* `RedirectStatus` - (Required) The HTTP reply status.
* `RedirectUrl` - (Required) The URL to redirect to.

`RedirectStatus` - (Required) The HTTP reply status.
* `RedirectUrl` - (Required) The URL to redirect to.

`RedirectUrl` - (Required) The URL to redirect to.

`SelectPoolAction` - (At least one action is required) Set of pool selection actions to be executed when load balancer rule matches:
* `PoolId` - (Required) The loadbalancer pool the request will be forwarded to.

`PoolId` - (Required) The loadbalancer pool the request will be forwarded to.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb rule.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_http_forwarding_rule](https://www.terraform.io/docs/providers/nsxt/r/lb_http_forwarding_rule.html) in the _Terraform Provider Documentation_