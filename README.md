# molecule-test-role

Test Role to play with Molecule. This setup has been tested on VM running Ubuntu 18.04.

## Table of contents
1. [Prerequisites](#prerequisites)
    * [Docker](#docker)
    * [Python VirtualEnv](#python-virtualEnv)
       * [Installation](#installation)
       * [Create a new Python VirtualEnv](#create-a-new-python-virtualEnv)

## Prerequisites

### Docker

Install Docker using the following tutorial:
* https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

### Python VirtualEnv

#### Installation

Install Python and VirtualEnv using the following tutorial:
* https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-18-04-quickstart

#### Create a new Python VirtualEnv

```
[+:DEV:~]$ virtualenv --python=python3 --no-site-packages .venv/
Already using interpreter /usr/bin/python3
Using base prefix '/usr'
New python executable in .venv/bin/python3
Also creating executable in .venv/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.
```

#### Enable the newly-created VirtualEnv

```
[+:DEV:~]$ source .venv/bin/activate
```

#### Install Ansible and Molecule in the VirtualEnv:

```
[+(.venv) :DEV:~]$ pip install ansible molecule docker
Collecting ansible
...
Collecting molecule
...
Collecting docker
...
```

#### Test the installation

```
[+(.venv) :DEV:~]$ ansible --version
ansible 2.7.10
[+(.venv) :DEV:~]$ molecule --version
molecule, version 2.20.1
[+(.venv) :DEV:~]$ docker --version
Docker version 18.09.6, build 481bc77
```

## Test role

### Single step

```
[+(.venv) :DEV:molecule-test-role]$ molecule lint
--> Validating schema molecule-test-role/molecule/default/molecule.yml.
Validation completed successfully.
--> Test matrix

└── default
    └── lint

--> Scenario: 'default'
--> Action: 'lint'
--> Executing Yamllint on files found in molecule-test-role/...
Lint completed successfully.
--> Executing Flake8 on files found in molecule-test-role/molecule/default/tests/...
Lint completed successfully.
--> Executing Ansible Lint on molecule-test-role/molecule/default/playbook.yml...
Lint completed successfully.
```

### Full test scenario

```
[+(.venv) :DEV:molecule-test-role]$ molecule test
--> Validating schema molecule-test-role/molecule/default/molecule.yml.
Validation completed successfully.
--> Test matrix

└── default
    ├── lint
    ├── destroy
    ├── dependency
    ├── syntax
    ├── create
    ├── prepare
    ├── converge
    ├── idempotence
    ├── side_effect
    ├── verify
    └── destroy
...
```
