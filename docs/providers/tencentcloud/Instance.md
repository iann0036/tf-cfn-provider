# Terraform::TencentCloud::Instance

Provides CBS stoarge attachment resource.

## Properties

`StorageId` - (Required, Forces new resource) ID of the storage to be attached.

`InstanceId` - (Required, Forces new resource) ID of the CVM instance to attache to.


## Return Values

### Fn::GetAtt

`StorageId` - ID of the storage.

`InstanceId` - ID of the CVM instance.

## See Also

* [tencentcloud_instance](https://www.terraform.io/docs/providers/tencentcloud/r/instance.html) in the _Terraform Provider Documentation_