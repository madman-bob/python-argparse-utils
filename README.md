# argparse_utils

[`argparse_utils`](https://github.com/madman-bob/python-argparse-utils)
provides a collection of utilities for the Python standard-library
[`argparse`](https://docs.python.org/3/library/argparse.html)
module.
These utilities assist with parsing command-line arguments to Python objects.

## Example

Consider a simple command-line script which accepts a colour as it's only argument,
and immediately prints the Python representation of that object.

```python
from argparse import ArgumentParser
from enum import Enum

from argparse_utils import enum_action

class Colours(Enum):
    red = 1
    green = 2
    blue = 3

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('colour', action=enum_action(Colours))

    arguments = parser.parse_args()

    print(repr(arguments.colour))
```

```bash
$ argparse_utils_example.py red
<Colours.red: 1>
```

Without the `enum_action` action, `arguments.colour` would be the string `'red'`,
rather than the enum value `Colours.red`.
What's more, the action ensures that only the values given in the enum are allowed,
instead of any string value.

## Reference

- `mapping_action(possible_values)`

  Takes a dictionary whose keys are the allowed values,
  and maps those values to the values found in the dictionary.
  Only the values found as keys in the dictionary are allowed as command-line arguments.

  eg. An action of

  ```python
  mapping_action({
      'red': (255, 0, 0),
      'green': (0, 255, 0),
      'blue': (0, 0, 255)
  })
  ```

  would map a command-line argument of `red` to the Python object `(255, 0, 0)`.

- `enum_action(enum_class)`

  Takes an `Enum` class,
  and maps the string representation of the keys to the appropriate enum value.
  Only the values found in the enum are allowed as command-line arguments.

  eg. Using the `Colour` enum, from the first example, an action of

  ```python
  enum_action(Colour)
  ```

  would map a command-line argument of `red` to the enum `Colour.red` value.
