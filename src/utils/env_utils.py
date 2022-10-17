import os
from typing import Any

from errors import EnvVarNotFound


def get_env_var(var_name: str, to_type: Any = None, raise_if_none: bool = True) -> Any:
    var = os.getenv(var_name, False)

    if not var and raise_if_none:
        raise EnvVarNotFound(f'No environment variable found with name "{var_name}"')

    if to_type:
        var = to_type(var)

    return var
