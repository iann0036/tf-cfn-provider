# Terraform::Cloudflare::ZoneSettingsOverride

Provides a resource which customizes Cloudflare zone settings. Note that after destroying this resource Zone Settings will be reset to their initial values.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The zone ID.

`InitialSettings` - Settings present in the zone at the time the resource is created. This will be used to restore the original settings when this resource is destroyed. Shares the same schema as the `settings` attribute (Above).

`IntialSettingsReadAt` - Time when this resource was created and the `initial_settings` were set.

`ReadonlySettings` - Which of the current `settings` are not able to be set by the user. Which settings these are is determined by plan level and user permissions.

## See Also

* [cloudflare_zone_settings_override](https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override.html) in the _Terraform Provider Documentation_