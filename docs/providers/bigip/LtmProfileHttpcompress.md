# Terraform::BIGIP::LtmProfileHttpcompress

`Terraform::BIGIP::LtmProfileHttpcompress`  Virtual server HTTP compression profile configuration


For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`DefaultsFrom` - (Optional) Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

`UriExclude` - (Optional) Disables compression on a specified list of HTTP Request-URI responses. Use a regular expression to specify a list of URIs you do not want to compress.

`UriInclude` - (Optional) Enables compression on a specified list of HTTP Request-URI responses. Use a regular expression to specify a list of URIs you want to compress.

`ContentTypeInclude` - (Optional) Specifies a list of content types for compression of HTTP Content-Type responses. Use a string list to specify a list of content types you want to compress.

`ContentTypeExclude` - (Optional) Excludes a specified list of content types from compression of HTTP Content-Type responses. Use a string list to specify a list of content types you want to compress.


## See Also

* [bigip_ltm_profile_httpcompress](https://www.terraform.io/docs/providers/bigip/r/ltm_profile_httpcompress.html) in the _Terraform Provider Documentation_