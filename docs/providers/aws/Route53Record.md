# Terraform::AWS::Route53Record

Provides a Route53 record resource.

## Properties

`ZoneId` - (Required) The ID of the hosted zone to contain this record.

`Name` - (Required) The name of the record.

`Type` - (Required) The record type. Valid values are `A`, `AAAA`, `CAA`, `CNAME`, `MX`, `NAPTR`, `NS`, `PTR`, `SOA`, `SPF`, `SRV` and `TXT`.

`Ttl` - (Required for non-alias records) The TTL of the record.

`Records` - (Required for non-alias records) A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the Terraform configuration string (e.g. `"first255characters\"\"morecharacters"`).

`SetIdentifier` - (Optional) Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.

`HealthCheckId` - (Optional) The health check the record should be associated with.

`Alias` - (Optional) An alias block. Conflicts with `Ttl` & `Records`. Alias record documented below.

`FailoverRoutingPolicy` - (Optional) A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.

`GeolocationRoutingPolicy` - (Optional) A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.

`LatencyRoutingPolicy` - (Optional) A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.

`WeightedRoutingPolicy` - (Optional) A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.

`MultivalueAnswerRoutingPolicy` - (Optional) Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.

`AllowOverwrite` - (Optional) Allow creation of this record in Terraform to overwrite an existing record, if any. This does not prevent other resources within Terraform or manual Route53 changes from overwriting this record. `true` by default.

`Name` - (Required) DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.

`ZoneId` - (Required) Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](/docs/providers/aws/r/elb.html#zone_id) for example.

`EvaluateTargetHealth` - (Required) Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).

`Type` - (Required) `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets.

`Continent` - A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `Continent` or `Country` must be specified.

`Country` - A two-character country code or `*` to indicate a default resource record set.

`Subdivision` - (Optional) A subdivision code for a country.

`Region` - (Required) An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency.

`Weight` - (Required) A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.


## Return Values

### Fn::GetAtt

`Name` - The name of the record.

`Fqdn` - [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `Name`.

## See Also

* [aws_route53_record](https://www.terraform.io/docs/providers/aws/r/route53_record.html) in the _Terraform Provider Documentation_