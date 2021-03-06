# Terraform::Cloudflare::WorkerScript

Provides a Cloudflare worker script resource. In order for a script to be active, you'll also need to setup a `Terraform::Cloudflare::WorkerRoute`.

## Properties

`Zone` - (Required for single-script accounts) The zone for the script.

`Name` - (Required for multi-script accounts) The name for the script.

`Content` - (Required) The script content.


## Return Values

### Fn::GetAtt

`ZoneId` - The zone id of the script (only for non-multi-script resources).

## See Also

* [cloudflare_worker_script](https://www.terraform.io/docs/providers/cloudflare/r/worker_script.html) in the _Terraform Provider Documentation_