Curriculum <br>
**Short Specialization** <br>

# 0x03. User authentication service

`Back-end` `Authentification`

#### Concepts

_For this project, look at these concepts:_

* [User management](https://www.intranet.alxswe.com/concepts/558)

## Resources

**Read or watch:**

* [Flask documentation](https://www.flask.palletsprojects.com/en/2.2.x/quickstart/)
* [Requests module](https://www.requests.kennethreitz.org/en/latest/user/quickstart/)
* [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

## General Requirement & Setup

* Allowed editors: `vi`, `vim`, `emacs`
* All files intrepreted/compiled on Ubuntu 18.04 LTS using `python3` (version3.7)
* All files should end with a new line
* The first line of files should be exactly shebang `#!/usr/bin/env python3`
* Mandatory `README.md` file at the root of the project folder/directory
* Code use the `pycodestyle` style (version 2.5)
* You should use `SQLAlchemy` 1.3.x
* All files must be executable
* Length of file tested using `wc`
* All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is a real sentence explaining purpose of the module, class or method (length will be verified)
* All functions should be type annotated
* The flask app should only interact with `Auth` and never with `DB` directly
* Only public methods of `Auth` and `DB` should be used outside these classes

## Setup

You will need to install `bcrypt`

```bash
pip3 install bcrypt
```

## Finally...
