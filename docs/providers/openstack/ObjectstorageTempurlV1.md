# Terraform::OpenStack::ObjectstorageTempurlV1

Use this resource to generate an OpenStack Object Storage temporary URL.

The temporary URL will be valid for as long as TTL is set to (in seconds).
Once the URL has expired, it will no longer be valid, but the resource
will remain in place. If you wish to automatically regenerate a URL, set
the `Regenerate` argument to `true`. This will create a new resource with
a new ID and URL.

## Properties

`Region` - (Optional) The region the tempurl is located in.

`Container` - (Required) The container name the object belongs to.

`Object` - (Required) The object name the tempurl is for.

`Ttl` - (Required) The TTL, in seconds, for the URL. For how long it should be valid.

`Method` - (Optional) The method allowed when accessing this URL. Valid values are `GET`, and `POST`. Default is `GET`.

`Regenerate` - (Optional) Whether to automatically regenerate the URL when it has expired. If set to true, this will create a new resource with a new ID and new URL. Defaults to false.


## Return Values

### Fn::GetAtt

`Id` - Computed md5 hash based on the generated url.

`Container` - See Properties above.

`Object` - See Properties above.

`Ttl` - See Properties above.

`Method` - See Properties above.

`Url` - The URL.

`Region` - The region the endpoint is located in.

## See Also

* [openstack_objectstorage_tempurl_v1](https://www.terraform.io/docs/providers/openstack/r/objectstorage_tempurl_v1.html) in the _Terraform Provider Documentation_