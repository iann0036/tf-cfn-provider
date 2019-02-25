# Terraform::Cloudflare::LoadBalancer

Provides a Cloudflare Load Balancer resource. This sits in front of a number of defined pools of origins and provides various options for geographically-aware load balancing. Note that the load balancing feature must be enabled in your Clouflare account before you can use this resource.

## Properties

`Zone` - (Required) The zone to add the load balancer to.

`Name` - (Required) The DNS name (FQDN, including the zone) to associate with the load balancer.

`FallbackPoolId` - (Required) The pool ID to use when all other pools are detected as unhealthy.

`DefaultPoolIds` - (Required) A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.

`Description` - (Optional) Free text description.

`Ttl` - (Optional) Time to live (TTL) of this load balancer's DNS `Name`. Conflicts with `Proxied` - this cannot be set for proxied load balancers. Default is `30`.

`SteeringPolicy` - (Optional) Determine which method the load balancer uses to determine the fastest route to your origin. Valid values  are: "off", "geo", "dynamic_latency" or "". Default is "".

`Proxied` - (Optional) Whether the hostname gets Cloudflare's origin protection. Defaults to `false`.

`RegionPools` - (Optional) A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.

`PopPools` - (Optional) A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.

`SessionAffinity` - (Optional) Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.

`Region` - (Required) A region code which must be in the list defined [here](https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions). Multiple entries should not be specified with the same region.

`PoolIds` - (Required) A list of pool IDs in failover priority to use in the given region.

`Pop` - (Required) A 3-letter code for the Point-of-Presence. Allowed values can be found in the list of datacenters on the [status page](https://www.cloudflarestatus.com/). Multiple entries should not be specified with the same PoP.

`PoolIds` - (Required) A list of pool IDs in failover priority to use for traffic reaching the given PoP.


## Return Values

### Fn::GetAtt

`Id` - Unique identifier in the API for the load balancer.

`ZoneId` - ID associated with the specified `Zone`.

`CreatedOn` - The RFC3339 timestamp of when the load balancer was created.

`ModifiedOn` - The RFC3339 timestamp of when the load balancer was last modified.

## See Also

* [cloudflare_load_balancer](https://www.terraform.io/docs/providers/cloudflare/r/load_balancer.html) in the _Terraform Provider Documentation_