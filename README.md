# Craft Ops

`Craft Ops` is a template which uses automation tools to build you a virtual
DevOps environment which is tailored for [Craft CMS][craft_link]. Craft itself
is already incredibly easy to setup with tools like MAMP, and this project
aims to stay that way. This project's goal is to get you past the process
of dragging files over to FTP and using commands instead. Ideally you learn 
a thing or two about [Unix-like][unix_like_link] systems in the process.

To start, the ops workflows will be built around the use of AWS and Bitbucket.
These products both offer free options and can be fully automated.

Please also note that use of Craft is subject to their own
[license agreement][craft_license].

##### Requirements

You only need these tools installed, and both have builds for most systems.

- [Vagrant][vagrant_link]
- [VirtualBox][virtualbox_link]

> This has not been tested on Windows, but support is welcome :)

## Get started with a `dev` box...

It is really easy, just clone this repo and `vagrant up` the `dev` box.

```shell
$ git clone https://github.com/stackstrap/craft-ops.git project_name
$ vagrant up dev
```

You can then hit the dev server at `http://localhost:8000`

## Setting up the rest...

#### How the configuration works

The ops setup is configured by sourcing data from a configuration object. The
object is created by merging a series of YAML files on top of each other.

`defaults.conf` - This file is the base layer and just for reference.

`project.conf` - This is the main file where you should put custom properties.

`private.conf` (optional) - This file is where you would store private project
data like access keys. You should `.gitignore` this file or encrypt it if you do
use it.

`~/ops.conf` (optional) - This is a global config file that is pulled in from your
host system's `$HOME` directory when the `dev` box is provisioned. You can keep 
access keys here if you need them for all projects. You will need to run
`vagrant provision dev` if you change this file.

#### AWS

After you have setup your AWS account you will need to create a new user
under [IAM][aws_iam_link].  As soon as you create this user you will be given
two keys. Create a file called `private.conf` at the root of the project
and add the values in this format...

```
aws:
  access_key: This is the short one
  secret_key: This is the long one
```

You will also need to attach an **Administrator Policy** to the user. After this you
will never need to log into AWS again.

#### Bitbucket

The best way to handle bitbucket is to create a "team" for your repositories to live
under.  With teams Bitbucket allows you to generate an "API key" to use instead of your
password.  You can generate this token under "Manage team" in the top right corner.
Once you have this token you can add two more values to `private.conf`...

```
bitbucket:
  user: The name of the team
  token: The API key from the team management page
```

> Keep in mind that YAML is whitespace sensitive and your tabs must all be the same.

#### Global config

If you would like to use the same credentials for all projects you can keep all of the
above information in `~/ops.conf` on your host machine.  This will allow you to kick off
a new Craft Ops project without having to complete these steps each time.

####

[aws_iam_link]: https://console.aws.amazon.com/iam/
[craft_link]: https://buildwithcraft.com/
[craft_license]: https://buildwithcraft.com/license
[project_conf_link]: https://github.com/stackstrap/craft-ops/blob/master/project.conf#L3
[unix_like_link]:http://en.wikipedia.org/wiki/Unix-like
[vagrant_link]: http://vagrantup.com
[virtualbox_link]: http://virtualbox.org
