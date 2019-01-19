# Terraform::Panos::GeneralSettings

This resource allows you to update the general device settings, such as DNS
or the hostname.

All params are optional for this resource.  If any options are not specified,
then whatever is already configured on the firewall is left as-is.  The
general device settings will always exist on the firewall, so `terraform
destroy` does not remove config from the firewall.

## Properties

`Hostname` - Firewall hostname.

`Timezone` - The timezone (e.g. - `US/Pacific`).

`Domain` - The domain.

`UpdateServer` - The update server (Default: `updates.paloaltonetworks.com`).

`VerifyUpdateServer` - Verify update server identity (Default: `true`).

`DnsPrimary` - Primary DNS server.

`DnsSecondary` - Secondary DNS server.

`NtpPrimaryAddress` - Primary NTP server.

`NtpPrimaryAuthType` - Primary NTP auth type.  This can be `none`, `autokey`, or `symmetric-key`.

`NtpPrimaryKeyId` - Primary NTP `symmetric-key` key ID.

`NtpPrimaryAlgorithm` - Primary NTP `symmetric-key` algorithm.  This can be `sha1` or `md5`.

`NtpPrimaryAuthKey` - Primary NTP `symmetric-key` auth key.  This is the SHA1 hash if the algorithm is `sha1`, or the md5sum if the algorithm is `md5`.

`NtpSecondaryAddress` - Secondary NTP server.

`NtpSecondaryAuthType` - Secondary NTP auth type.  This can be `none`, `autokey`, or `symmetric-key`.

`NtpSecondaryKeyId` - Secondary NTP `symmetric-key` key ID.

`NtpSecondaryAlgorithm` - Secondary NTP `symmetric-key` algorithm.  This can be `sha1` or `md5`.

`NtpSecondaryAuthKey` - Secondary NTP `symmetric-key` auth key.  This is the SHA1 hash if the algorithm is `sha1`, or the md5sum if the algorithm is `md5`.


## See Also

* [panos_general_settings](https://www.terraform.io/docs/providers/panos/r/general_settings.html) in the _Terraform Provider Documentation_