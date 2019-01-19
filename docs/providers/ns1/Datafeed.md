# Terraform::NS1::Datafeed

Provides a NS1 Data Feed resource. This can be used to create, modify, and delete data feeds.

## Properties

`SourceId` - (Required) The data source id that this feed is connected to.

`Name` - (Required) The free form name of the data feed.

`Config` - (Optional) The feeds configuration matching the specification in 'feed\_config' from /data/sourcetypes.


## See Also

* [ns1_datafeed](https://www.terraform.io/docs/providers/ns1/r/datafeed.html) in the _Terraform Provider Documentation_