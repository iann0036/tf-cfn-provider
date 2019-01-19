# Terraform::Brightbox::Container

Provides a Brightbox Container resource. This can be used to create,
modify, and delete Containers in Orbit.

## Properties

`Name` - (Required) A label assigned to the Container.

`Description` - (Optional) A further description of the Container.

`OrbitUrl` - (Optional) The Orbit URL you wish to talk to. This defaults to either `https://orbit.brightbox.com/v1/` or the contents of the `BRIGHTBOX_ORBIT_URL` environment variable if set.


## Return Values

### Fn::GetAtt

`AuthUser` - the api client id used to access the container.

`AuthKey` - the client secret used to access the container.

`AccountId` - the account under which the container is stored.

## See Also

* [brightbox_container](https://www.terraform.io/docs/providers/brightbox/r/container.html) in the _Terraform Provider Documentation_