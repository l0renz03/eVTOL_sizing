## Coding guidelines
_Version: 1.1, 23.05.2024_

This document contains coding guidelines for the project.

### 1. Naming conventions
1. **Variables**: Use `snake_case` for variables.
2. **Functions**: Use `snake_case` for functions.
3. **Classes**: Use `PascalCase` for classes.
4. **Files**: Use `snake_case` for files.
5. **Arguments**: Use `snake_case` for arguments.

### 2. Code formatting
1. **Blank lines**: Use blank lines to separate code blocks.
2. **Imports**: Imports should be at the beginning of the file.
3. **Comments**: Use comments to explain complex parts of the code.

### 3. Documentation
1. **Docstrings**: Use docstrings to describe modules, classes, functions, and methods.
Look at this example:
```python
def calculate_stall_speed(weight: float, wing_area: float, air_density: float, max_lift_coefficient: float) -> float:
    """Calculate the stall speed of an aircraft.

    Args:
        weight: The weight of the aircraft in Newton.
        wing_area: The wing area of the aircraft in square meters.
        air_density: The air density in kilograms per cubic meter.
        max_lift_coefficient: The lift coefficient of the aircraft.

    Returns:
        The stall speed of the aircraft in meters per second.
    """
    return np.sqrt((2 * weight) / (air_density * wing_area * max_lift_coefficient))
```
It is much better than this:
```python
def calculate_Vs(W, S, rho, CL_max):
    return np.sqrt((2 * W) / (rho * S * CL_max))
```
However, in general if the variables come from the well known equation, you don't have to name variables like `weight`, `wing_area`, `air_density`, `max_lift_coefficient`. You can use `W`, `S`, `rho`, `CL_max` instead.
But in the end the acceptable version is still like this:
```python
def calculate_stall_speed(W: float, S: float, rho: float, CL_max: float) -> float:
    """Calculate the stall speed of an aircraft.

    Args:
        W: The weight of the aircraft in Newton.
        S: The wing area of the aircraft in square meters.
        rho: The air density in kilograms per cubic meter.
        CL_max: The lift coefficient of the aircraft.

    Returns:
        The stall speed of the aircraft in meters per second.
    """
    return np.sqrt((2 * W) / (rho * S * CL_max))
```
Tip: AI tools (ChatGPT, Github Copilot) in general are quite useful in analyzing functions and variables. 
They can be used to write docs, especially if you don't have time or idea how to phrase the docs.
2. **Type hints**: Use type hints for function arguments and return values. 
These are this `-> float` and `W: float` in the example above. 
If you expect that the function will have different inputs for different usage e.g. `W` can be a float or a numpy array, you do not need to use it.
If you want to use it, you can use `Union[float, np.ndarray]` for example.


### 4. Best practices
1. **Avoid magic numbers**: Use constants instead of magic numbers. For instance:
```python
# Bad
def calculate_speed_of_sound(temperature: float) -> float:
    return np.sqrt(1.4 * 287 * temperature)

# Good
GAMMA = 1.4
R = 287
def calculate_speed_of_sound(temperature: float) -> float:
    return np.sqrt(GAMMA * R * temperature)
```
2. **Avoid duplicate code**: Refactor duplicate code into functions.
3. **Avoid global variables**: Use function arguments and return values instead of global variables.
4. **Use meaningful names**: Use descriptive names for variables, functions, classes, and files.