# Terraform::Panos::Telemetry

This resource allows you to add/update/delete telemetry sharing.

Join other Palo Alto Networks customers in a global sharing community, helping
to raise the bar against the latest attack techniques. Your participation
allows us to deliver new threat prevention controls across the attack
lifecycle. Choose the type of data you share across applications, threat
intelligence, and device health information to improve the fidelity of the
protections we deliver. This is an opt-in feature controlled with granular
policy, and we encourage you to join the community.

## Properties

`ApplicationReports` - (Bool, optional) Application reports.

`ThreatPreventionReports` - (Bool, optional) Threat reports.

`UrlReports` - (Bool, optional) URL reports.

`FileTypeIdentificationReports` - (Bool, optional) File type identification reports.

`ThreatPreventionData` - (Bool, optional) Threat prevention data.

`ThreatPreventionPacketCaptures` - (Bool, optional) Enable sending packet- captures with threat prevention information. This requires that `ThreatPreventionData` also be enabled.

`ProductUsageStats` - (Bool, optional) Health and performance reports.

`PassiveDnsMonitoring` - (Bool, optional) Passive DNS monitoring.


## See Also

* [panos_telemetry](https://www.terraform.io/docs/providers/panos/r/telemetry.html) in the _Terraform Provider Documentation_