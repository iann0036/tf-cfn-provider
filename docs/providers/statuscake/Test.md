# Terraform::StatusCake::Test

The test resource allows StatusCake tests to be managed by Terraform.

## Properties

`WebsiteName` - (Required) This is the name of the test and the website to be monitored.

`WebsiteUrl` - (Required) The URL of the website to be monitored.

`CheckRate` - (Optional) Test check rate in seconds. Defaults to 300.

`ContactGroup` - (Optional) Set test contact groups, must be array of strings.

`TestType` - (Required) The type of Test. Either HTTP, TCP, PING, or DNS.

`Paused` - (Optional) Whether or not the test is paused. Defaults to false.

`Timeout` - (Optional) The timeout of the test in seconds.

`Confirmations` - (Optional) The number of confirmation servers to use in order to detect downtime. Defaults to 0.

`Port` - (Optional) The port to use when specifying a TCP test.

`TriggerRate` - (Optional) The number of minutes to wait before sending an alert. Default is `5`.

`CustomHeader` - (Optional) Custom HTTP header, must be supplied as JSON.

`UserAgent` - (Optional) Test with a custom user agent set.

`NodeLocations` - (Optional) Set test node locations, must be array of strings.

`PingUrl` - (Optional) A URL to ping if a site goes down.

`BasicUser` - (Optional) A Basic Auth User account to use to login.

`BasicPass` - (Optional) If BasicUser is set then this should be the password for the BasicUser.

`Public` - (Optional) Set 1 to enable public reporting, 0 to disable.

`LogoImage` - (Optional) A URL to a image to use for public reporting.

`Branding` - (Optional) Set to 0 to use branding (default) or 1 to disable public reporting branding).

`WebsiteHost` - (Optional) Used internally, when possible please add.

`Virus` - (Optional) Enable virus checking or not. 1 to enable.

`FindString` - (Optional) A string that should either be found or not found.

`DoNotFind` - (Optional) If the above string should be found to trigger a alert. 1 = will trigger if find_string found.

`RealBrowser` - (Optional) Use 1 to TURN OFF real browser testing.

`TestTags` - (Optional) Set test tags, must be array of strings.

`StatusCodes` - (Optional) Comma Seperated List of StatusCodes to Trigger Error on. Defaults are "204, 205, 206, 303, 400, 401, 403, 404, 405, 406, 408, 410, 413, 444, 429, 494, 495, 496, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 521, 522, 523, 524, 520, 598, 599".

`UseJar` - (Optional) Set to true to enable the Cookie Jar. Required for some redirects. Default is false.

`PostRaw` - (Optional) Use to populate the RAW POST data field on the test.

`FinalEndpoint` - (Optional) Use to specify the expected Final URL in the testing process.

`FollowRedirect` - (Optional) Use to specify whether redirects should be followed, set to true to enable. Default is false.


## Return Values

### Fn::GetAtt

`TestId` - A unique identifier for the test.

## See Also

* [statuscake_test](https://www.terraform.io/docs/providers/statuscake/r/test.html) in the _Terraform Provider Documentation_