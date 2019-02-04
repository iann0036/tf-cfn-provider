# Terraform::NSXT::LbCookiePersistenceProfile

Provides a resource to configure lb cookie persistence profile on NSX-T manager

## Properties

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Description` - (Optional) Description of this resource.

`CookieMode` - (Optional) The cookie persistence mode. Accepted values: PREFIX, REWRITE and INSERT which is the default.

`CookieName` - (Required) cookie name.

`PersistenceShared` - (Optional) A boolean flag which reflects whether the cookie persistence is private or shared. When false (which is the default value), the cookie persistence is private to each virtual server and is qualified by the pool. If set to true, in cookie insert mode, cookie persistence could be shared across multiple virtual servers that are bound to the same pools.

`CookieFallback` - (Optional) A boolean flag which reflects whether once the server points by this cookie is down, a new server is selected, or the requests will be rejected.

`CookieGarble` - (Optional) A boolean flag which reflects whether the cookie value (server IP and port) would be encrypted or in plain text.

`InsertModeParams` - (Optional) Additional parameters for the INSERT cookie mode:
* `CookieDomain` - (Optional) HTTP cookie domain (for INSERT mode only).
* `CookiePath` - (Optional) HTTP cookie path (for INSERT mode only).
* `CookieExpiryType` - (Optional) Type of cookie expiration timing (for INSERT mode only). Accepted values: SESSION_COOKIE_TIME for session cookie time setting and PERSISTENCE_COOKIE_TIME for persistence cookie time setting.
* `MaxIdleTime` - (Required if cookie_expiry_type is set) Maximum interval the cookie is valid for from the last time it was seen in a request.
* `MaxLifeTime` - (Required for INSERT mode with SESSION_COOKIE_TIME expiration) Maximum interval the cookie is valid for from the first time the cookie was seen in a request.

`CookieDomain` - (Optional) HTTP cookie domain (for INSERT mode only).
* `CookiePath` - (Optional) HTTP cookie path (for INSERT mode only).
* `CookieExpiryType` - (Optional) Type of cookie expiration timing (for INSERT mode only). Accepted values: SESSION_COOKIE_TIME for session cookie time setting and PERSISTENCE_COOKIE_TIME for persistence cookie time setting.
* `MaxIdleTime` - (Required if cookie_expiry_type is set) Maximum interval the cookie is valid for from the last time it was seen in a request.
* `MaxLifeTime` - (Required for INSERT mode with SESSION_COOKIE_TIME expiration) Maximum interval the cookie is valid for from the first time the cookie was seen in a request.

`CookiePath` - (Optional) HTTP cookie path (for INSERT mode only).
* `CookieExpiryType` - (Optional) Type of cookie expiration timing (for INSERT mode only). Accepted values: SESSION_COOKIE_TIME for session cookie time setting and PERSISTENCE_COOKIE_TIME for persistence cookie time setting.
* `MaxIdleTime` - (Required if cookie_expiry_type is set) Maximum interval the cookie is valid for from the last time it was seen in a request.
* `MaxLifeTime` - (Required for INSERT mode with SESSION_COOKIE_TIME expiration) Maximum interval the cookie is valid for from the first time the cookie was seen in a request.

`CookieExpiryType` - (Optional) Type of cookie expiration timing (for INSERT mode only). Accepted values: SESSION_COOKIE_TIME for session cookie time setting and PERSISTENCE_COOKIE_TIME for persistence cookie time setting.
* `MaxIdleTime` - (Required if cookie_expiry_type is set) Maximum interval the cookie is valid for from the last time it was seen in a request.
* `MaxLifeTime` - (Required for INSERT mode with SESSION_COOKIE_TIME expiration) Maximum interval the cookie is valid for from the first time the cookie was seen in a request.

`MaxIdleTime` - (Required if cookie_expiry_type is set) Maximum interval the cookie is valid for from the last time it was seen in a request.
* `MaxLifeTime` - (Required for INSERT mode with SESSION_COOKIE_TIME expiration) Maximum interval the cookie is valid for from the first time the cookie was seen in a request.

`MaxLifeTime` - (Required for INSERT mode with SESSION_COOKIE_TIME expiration) Maximum interval the cookie is valid for from the first time the cookie was seen in a request.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb cookie persistence profile.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb cookie persistence profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_cookie_persistence_profile](https://www.terraform.io/docs/providers/nsxt/r/lb_cookie_persistence_profile.html) in the _Terraform Provider Documentation_