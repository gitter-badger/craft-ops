# Craft Ops

`Craft Ops` is a template which uses common sense and automation 
configurations to build a CLI tailored for operating and deploying 
[Craft CMS][craft_link] on virtual servers. Craft itself is already
incredibly easy to setup if you use tools like MAMP, and this project
aims to ensure things stay that way. This project just goes a step
further to ensure that modern DevOps tools can be utilized without
the burden of configuration.

Please also note that use of Craft is subject to their own
[license agreement][craft_license].

##### Requirements

- [Vagrant][vagrant_link]
- [VirtualBox][virtualbox_link]

> This has not been tested on Windows, but support is welcome :)

## Getting Started

Clone this repo as the name of your project.

```
git clone https://github.com/stackstrap/craft-ops.git project_name
```

Come up with a `short_name` value your project. This value will be
used to label things in the system. It should be short and easy to
type. Try to leave out special characters or things could fail.
You will need to enter this value into the proper place in the
[`project.conf`][project_conf_link] file.

Then build the `dev` vm:

```
vagrant up dev
```

[craft_link]: https://buildwithcraft.com/
[craft_license]: https://buildwithcraft.com/license
[project_conf_link]: https://github.com/stackstrap/craft-ops/blob/master/project.conf
[vagrant_link]: http://vagrantup.com
[virtualbox_link]: http://virtualbox.org
