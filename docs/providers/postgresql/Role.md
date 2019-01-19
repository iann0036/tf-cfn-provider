# Terraform::PostgreSQL::Role

The ``postgresql_role`` resource creates and manages a role on a PostgreSQL
server.

When a ``postgresql_role`` resource is removed, the PostgreSQL ROLE will
automatically run a [`REASSIGN
OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html)
and [`DROP
OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html) to
the `CURRENT_USER` (normally the connected user for the provider).  If the
specified PostgreSQL ROLE owns objects in multiple PostgreSQL databases in the
same PostgreSQL Cluster, one PostgreSQL provider per database must be created
and all but the final ``postgresql_role`` must specify a `skip_drop_role`.

~> **Note:** All arguments including role name and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

TBC

## See Also

* [postgresql_role](https://www.terraform.io/docs/providers/postgresql/r/role.html) in the _Terraform Provider Documentation_