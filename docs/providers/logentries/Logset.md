# Terraform::Logentries::Logset

Provides a Logentries logset resource. A logset is a collection of `Terraform::Logentries::Log` resources.

## Properties

`Name` - (Required) The log set name, which should be short and descriptive. For example, www, db1.

`Location` - (Optional, default "nonlocation") A location is for your convenience only. You can specify a DNS entry such as web.example.com, IP address or arbitrary comment.


## See Also

* [logentries_logset](https://www.terraform.io/docs/providers/logentries/r/logset.html) in the _Terraform Provider Documentation_