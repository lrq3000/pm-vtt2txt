# pm-vtt2txt

[![PyPI - Version](https://img.shields.io/pypi/v/vtt2txt-ng.svg)](https://pypi.org/project/vtt2txt-ng)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vtt2txt-ng.svg)](https://pypi.org/project/vtt2txt-ng)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pipx install vtt2txt-ng
```

Then run:

```console
vtt2txt my_file.vtt
```

This package is installed under the `pm` package namespace.
To use it in Python code import like this:

```python
from vtt2txt import vtt_to_text
```

## Publish

```console
hatch build
hatch publish
```

## License

`vtt2txt-ng` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

This is an updated fork from Trey Hunner's [pm-vtt2txt](https://github.com/lrq3000/vtt2txt-ng) with bugfixes and a more pythonic module architecture.

