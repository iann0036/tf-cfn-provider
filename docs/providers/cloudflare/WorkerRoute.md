# Terraform::Cloudflare::WorkerRoute

Provides a Cloudflare worker route resource. A route will also require a `Terraform::Cloudflare::WorkerScript`.

## Properties

`Zone` - (Required) The zone to add the route to.

`Pattern` - (Required) The [route pattern](https://developers.cloudflare.com/workers/api/route-matching/).


## Return Values

### Fn::GetAtt

`ZoneId` - The zone id of the route.

## See Also

* [cloudflare_worker_route](https://www.terraform.io/docs/providers/cloudflare/r/worker_route.html) in the _Terraform Provider Documentation_