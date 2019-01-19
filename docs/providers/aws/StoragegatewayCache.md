# Terraform::AWS::StoragegatewayCache

Manages an AWS Storage Gateway cache.

~> **NOTE:** The Storage Gateway API provides no method to remove a cache disk. Destroying this Terraform resource does not perform any Storage Gateway actions.

## Properties

`DiskId` - (Required) Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

`GatewayArn` - (Required) The Amazon Resource Name (ARN) of the gateway.


## See Also

* [aws_storagegateway_cache](https://www.terraform.io/docs/providers/aws/r/storagegateway_cache.html) in the _Terraform Provider Documentation_