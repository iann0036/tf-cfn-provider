# Terraform::OpenStack::ObjectstorageTempurlV1

Use this resource to generate an OpenStack Object Storage temporary URL.

The temporary URL will be valid for as long as TTL is set to (in seconds).
Once the URL has expired, it will no longer be valid, but the resource
will remain in place. If you wish to automatically regenerate a URL, set
the `regenerate` argument to `true`. This will create a new resource with
a new ID and URL.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - Computed md5 hash based on the generated url.

`Container` - See Argument Reference above.

`Object` - See Argument Reference above.

`Ttl` - See Argument Reference above.

`Method` - See Argument Reference above.

`Url` - The URL.

`Region` - The region the endpoint is located in.

## See Also

* [openstack_objectstorage_tempurl_v1](https://www.terraform.io/docs/providers/openstack/r/objectstorage_tempurl_v1.html) in the _Terraform Provider Documentation_