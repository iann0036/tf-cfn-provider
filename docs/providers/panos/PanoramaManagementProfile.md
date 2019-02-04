# Terraform::Panos::PanoramaManagementProfile

This resource allows you to add/update/delete Panorama interface management profiles
for both templates and template stacks.

## Properties

`Template` - The template name.

`TemplateStack` - The template stack name.

`Name` - (Required) The management profile's name.

`Ping` - (Optional) Allow ping.

`Telnet` - (Optional) Allow telnet.

`Ssh` - (Optional) Allow SSH.

`Http` - (Optional) Allow HTTP.

`HttpOcsp` - (Optional) Allow HTTP OCSP.

`Https` - (Optional) Allow HTTPS.

`Snmp` - (Optional) Allow SNMP.

`ResponsePages` - (Optional) Allow response pages.

`UseridService` - (Optional) Allow User ID service.

`UseridSyslogListenerSsl` - (Optional) Allow User ID syslog listener
for SSL.

`UseridSyslogListenerUdp` - (Optional) Allow User ID syslog listener
for UDP.

`PermittedIps` - (Optional) The list of permitted IP addresses or address
ranges for this management profile.


## See Also

* [panos_panorama_management_profile](https://www.terraform.io/docs/providers/panos/r/panorama_management_profile.html) in the _Terraform Provider Documentation_