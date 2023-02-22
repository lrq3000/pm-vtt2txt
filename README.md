# pm-vtt2txt

[![PyPI - Version](https://img.shields.io/pypi/v/pm-vtt2txt.svg)](https://pypi.org/project/pm-vtt2txt)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pm-vtt2txt.svg)](https://pypi.org/project/pm-vtt2txt)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pipx install pm-vtt2txt
```

Then run:

```console
vtt2txt my_file.vtt
```

This package is installed under the `pm` package namespace.
To use it in Python code import like this:

```python
from pm.vtt2txt import vtt_to_text
```

## Publish

```console
hatch build
hatch publish
```

## License

`pm-vtt2txt` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
