Err plugin for Rules
===

The plugin simply allows to specify the channels 'rules' or 'code of conduct'.

The commands must be executed within a public channel.


Requirements
------------

No external libraries necessary.


Installation
------------

Install via the `!repos` command.

```
!repos install https://github.com/sijis/err-rules.git
```

Usage
-----

Simple example usages

```
# Refer to a website
!rules add http://github.com/sijis/err-rules/raw/rules-of-channel.txt

# Add the rules directly
!rules add No yelling allowed!

# Delete the rule
!rules delete

# List all channels with a rule defined
!rules list
```

Feedback
--------

Feedback and pull requests are always welcomed.
