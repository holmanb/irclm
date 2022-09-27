IRC Log Manager
===============

Manage a local cache of irc logs.


Getting Started
---------------

If no configuration is found, the default one will be created at
`~/.config/irclm/irclm.toml` to configure.

```bash
pip install irclm
irclm
$EDITOR ~/.config/irclm/irclm.toml
irclm
```

Conveniently Grep Log Cache
---------------------------

```bash
irclm - grep <key>
irclm - rg <key>
```

Design Goals
============

- be simple, reliable, slim
- good netizinship - defaults to keep the servers happy

Capabilities
------------

- incremental cache update by default
- convenience wrapper for grep
- session reuse


Server Support
--------------
- irclogs.ubuntu.com
- Open a PR or a bug
