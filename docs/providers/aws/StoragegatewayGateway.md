# Terraform::AWS::StoragegatewayGateway

Manages an AWS Storage Gateway file, tape, or volume gateway in the provider region.

~> NOTE: The Storage Gateway API requires the gateway to be connected to properly return information after activation. If you are receiving `The specified gateway is not connected` errors during resource creation (gateway activation), ensure your gateway instance meets the [Storage Gateway requirements](https://docs.aws.amazon.com/storagegateway/latest/userguide/Requirements.html).

## Properties

`GatewayName` - (Required) Name of the gateway.

`GatewayTimezone` - (Required) Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.

`ActivationKey` - (Optional) Gateway activation key during resource creation. Conflicts with `GatewayIpAddress`. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

`GatewayIpAddress` - (Optional) Gateway IP address to retrieve activation key during resource creation. Conflicts with `ActivationKey`. Gateway must be accessible on port 80 from where Terraform is running. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

`GatewayType` - (Optional) Type of the gateway. The default value is `STORED`. Valid values: `CACHED`, `FILE_S3`, `STORED`, `VTL`.

`MediaChangerType` - (Optional) Type of medium changer to use for tape gateway. Terraform cannot detect drift of this argument. Valid values: `STK-L700`, `AWS-Gateway-VTL`.

`SmbActiveDirectorySettings` - (Optional) Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `ActiveDirectory` authentication SMB file shares. More details below.

`SmbGuestPassword` - (Optional) Guest password for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `GuestAccess` authentication SMB file shares. Terraform can only detect drift of the existence of a guest password, not its actual value from the gateway. Terraform can however update the password with changing the argument.

`TapeDriveType` - (Optional) Type of tape drive to use for tape gateway. Terraform cannot detect drift of this argument. Valid values: `IBM-ULT3580-TD5`.


## See Also

* [aws_storagegateway_gateway](https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway.html) in the _Terraform Provider Documentation_