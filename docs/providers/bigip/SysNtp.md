# Terraform::BIGIP::SysNtp

`BigipSysNtp` provides details about a specific bigip

This resource is helpful when configuring NTP server on the BIG-IP.

## Properties

`BigipSysNtp` - Is the resource is used to configure ntp server on the BIG-IP.

`/Common/NTP1` - Is the description of the NTP server in the main or common partition of BIG-IP.

`Time.facebook.com` - Is the  NTP server configured on the BIG-IP.

`Servers` - (Optional) Adds NTP servers to or deletes NTP servers from the BIG-IP system.

`Timezone` - (Optional) Specifies the time zone that you want to use for the system time.


## See Also

* [bigip_sys_ntp](https://www.terraform.io/docs/providers/bigip/r/sys_ntp.html) in the _Terraform Provider Documentation_