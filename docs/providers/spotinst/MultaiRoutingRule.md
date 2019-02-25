# Terraform::Spotinst::MultaiRoutingRule

Provides a Spotinst Multai Routing Rule.

## Properties

`BalancerId` - (Required) The ID of the balancer.

`ListenerId` - (Required) The ID of the listener.

`Route` - (Required) Route defines a simple language for matching HTTP requests and route the traffic accordingly. Route provides series of matchers that follow the syntax: Path matcher: — Path("/foo/bar") // trie-based PathRegexp(“/foo/.*”) // regexp-based Method matcher: — Method(“GET”) // trie-based MethodRegexp(“POST|PUT”) // regexp based Header matcher: — Header(“Content-Type”, “application/json”) // trie-based HeaderRegexp(“Content-Type”, “application/.*”) // regexp based Matchers can be combined using && operator: — Method(“POST”) && Path("/v1").

`Strategy` - (Optional) Balancing strategy. Valid values: `ROUNDROBIN`, `RANDOM`, `LEASTCONN`, `IPHASH`.

`Tags` - (Optional) A list of key:value paired tags.

`Key` - (Required) The tag's key.

`Value` - (Required) The tag's value.


## See Also

* [spotinst_multai_routing_rule](https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule.html) in the _Terraform Provider Documentation_