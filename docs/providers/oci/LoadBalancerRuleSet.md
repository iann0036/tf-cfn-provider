# Terraform::OCI::LoadBalancerRuleSet

This resource provides the Rule Set resource in Oracle Cloud Infrastructure Load Balancer service.

Creates a new rule set associated with the specified load balancer.

## Properties

`Items` - (Required) (Updatable)
* `Action` - (Required) (Updatable) The action can be one of these values: `ADD_HTTP_REQUEST_HEADER`, `ADD_HTTP_RESPONSE_HEADER`, `EXTEND_HTTP_REQUEST_HEADER_VALUE`, `EXTEND_HTTP_RESPONSE_HEADER_VALUE`, `REMOVE_HTTP_REQUEST_HEADER`, `REMOVE_HTTP_RESPONSE_HEADER`
* `Header` - (Required) (Updatable) A header name that conforms to RFC 7230.  Example: `example_header_name`
* `Prefix` - (Applicable when action=EXTEND_HTTP_REQUEST_HEADER_VALUE | EXTEND_HTTP_RESPONSE_HEADER_VALUE) (Updatable) A string to prepend to the header value. The resulting header value must still conform to RFC 7230.  Example: `example_prefix_value`
* `Suffix` - (Applicable when action=EXTEND_HTTP_REQUEST_HEADER_VALUE | EXTEND_HTTP_RESPONSE_HEADER_VALUE) (Updatable) A string to append to the header value. The resulting header value must still conform to RFC 7230.  Example: `example_suffix_value`
* `Value` - (Required when action=ADD_HTTP_REQUEST_HEADER | ADD_HTTP_RESPONSE_HEADER) (Updatable) A header value that conforms to RFC 7230.  Example: `example_value`.

`Action` - (Required) (Updatable) The action can be one of these values: `ADD_HTTP_REQUEST_HEADER`, `ADD_HTTP_RESPONSE_HEADER`, `EXTEND_HTTP_REQUEST_HEADER_VALUE`, `EXTEND_HTTP_RESPONSE_HEADER_VALUE`, `REMOVE_HTTP_REQUEST_HEADER`, `REMOVE_HTTP_RESPONSE_HEADER`
* `Header` - (Required) (Updatable) A header name that conforms to RFC 7230.  Example: `example_header_name`
* `Prefix` - (Applicable when action=EXTEND_HTTP_REQUEST_HEADER_VALUE | EXTEND_HTTP_RESPONSE_HEADER_VALUE) (Updatable) A string to prepend to the header value. The resulting header value must still conform to RFC 7230.  Example: `example_prefix_value`
* `Suffix` - (Applicable when action=EXTEND_HTTP_REQUEST_HEADER_VALUE | EXTEND_HTTP_RESPONSE_HEADER_VALUE) (Updatable) A string to append to the header value. The resulting header value must still conform to RFC 7230.  Example: `example_suffix_value`
* `Value` - (Required when action=ADD_HTTP_REQUEST_HEADER | ADD_HTTP_RESPONSE_HEADER) (Updatable) A header value that conforms to RFC 7230.  Example: `example_value`.

`Header` - (Required) (Updatable) A header name that conforms to RFC 7230.  Example: `example_header_name`
* `Prefix` - (Applicable when action=EXTEND_HTTP_REQUEST_HEADER_VALUE | EXTEND_HTTP_RESPONSE_HEADER_VALUE) (Updatable) A string to prepend to the header value. The resulting header value must still conform to RFC 7230.  Example: `example_prefix_value`
* `Suffix` - (Applicable when action=EXTEND_HTTP_REQUEST_HEADER_VALUE | EXTEND_HTTP_RESPONSE_HEADER_VALUE) (Updatable) A string to append to the header value. The resulting header value must still conform to RFC 7230.  Example: `example_suffix_value`
* `Value` - (Required when action=ADD_HTTP_REQUEST_HEADER | ADD_HTTP_RESPONSE_HEADER) (Updatable) A header value that conforms to RFC 7230.  Example: `example_value`.

`Prefix` - (Applicable when action=EXTEND_HTTP_REQUEST_HEADER_VALUE | EXTEND_HTTP_RESPONSE_HEADER_VALUE) (Updatable) A string to prepend to the header value. The resulting header value must still conform to RFC 7230.  Example: `example_prefix_value`
* `Suffix` - (Applicable when action=EXTEND_HTTP_REQUEST_HEADER_VALUE | EXTEND_HTTP_RESPONSE_HEADER_VALUE) (Updatable) A string to append to the header value. The resulting header value must still conform to RFC 7230.  Example: `example_suffix_value`
* `Value` - (Required when action=ADD_HTTP_REQUEST_HEADER | ADD_HTTP_RESPONSE_HEADER) (Updatable) A header value that conforms to RFC 7230.  Example: `example_value`.

`Suffix` - (Applicable when action=EXTEND_HTTP_REQUEST_HEADER_VALUE | EXTEND_HTTP_RESPONSE_HEADER_VALUE) (Updatable) A string to append to the header value. The resulting header value must still conform to RFC 7230.  Example: `example_suffix_value`
* `Value` - (Required when action=ADD_HTTP_REQUEST_HEADER | ADD_HTTP_RESPONSE_HEADER) (Updatable) A header value that conforms to RFC 7230.  Example: `example_value`.

`Value` - (Required when action=ADD_HTTP_REQUEST_HEADER | ADD_HTTP_RESPONSE_HEADER) (Updatable) A header value that conforms to RFC 7230.  Example: `example_value`.

`LoadBalancerId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the specified load balancer.

`Name` - (Required) The name for this set of rules. It must be unique and it cannot be changed. Avoid entering confidential information.  Example: `example_rule_set`.


## Return Values

### Fn::GetAtt

`Action` - The action can be one of these values: `ADD_HTTP_REQUEST_HEADER`, `ADD_HTTP_RESPONSE_HEADER`, `EXTEND_HTTP_REQUEST_HEADER_VALUE`, `EXTEND_HTTP_RESPONSE_HEADER_VALUE`, `REMOVE_HTTP_REQUEST_HEADER`, `REMOVE_HTTP_RESPONSE_HEADER`.

`Header` - A header name that conforms to RFC 7230.  Example: `example_header_name`.

`Prefix` - A string to prepend to the header value. The resulting header value must still conform to RFC 7230.  Example: `example_prefix_value`.

`Suffix` - A string to append to the header value. The resulting header value must still conform to RFC 7230.  Example: `example_suffix_value`.

`Value` - A header value that conforms to RFC 7230.  Example: `example_value`.

`Name` - The name for this set of rules. It must be unique and it cannot be changed. Avoid entering confidential information.  Example: `example_rule_set`.

## See Also

* [oci_load_balancer_rule_set](https://www.terraform.io/docs/providers/oci/r/load_balancer_rule_set.html) in the _Terraform Provider Documentation_