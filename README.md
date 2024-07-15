# Sak System Library

Welcome to the Sak System library. This library includes three mathematical systems: Sak, Rel, and Onri. Each system has its own rules and operations.

## Sak System

The Sak system uses a baseline value of 0.5, and all operations between Sak objects are adjusted based on this value.

### Sak Class

The `Sak` class represents the Sak system. It includes methods for basic arithmetic operations (`+`, `-`, `*`, `/`, `**`) and static methods for common mathematical functions like inverse, summation, integration, and square root.

### SakMath Class

The `SakMath` class provides trigonometric functions (`sin`, `cos`, `tan`), exponential, logarithmic, and other mathematical functions tailored for the Sak system.

## Rel System

The Rel system incorporates three variables: `x`, `s`, and `t`. Operations between Rel objects adjust these variables accordingly.

### Rel Class

The `Rel` class represents the Rel system. It includes methods for basic arithmetic operations (`+`, `-`, `*`, `/`, `**`). This system handles calculations involving three variables, making it more complex than the Sak system.

### RelMath Class

The `RelMath` class provides trigonometric functions (`sin`, `cos`, `tan`), exponential, logarithmic, and other mathematical functions tailored for the Rel system.

## Onri System

The Onri system uses two variables: `f` and `i`. Operations between Onri objects adjust these variables.

### Onri Class

The `Onri` class represents the Onri system. It includes methods for basic arithmetic operations (`+`, `-`, `*`, `/`, `**`). This system is designed to handle values within a specific range, making it unique compared to Sak and Rel.

### OnriMath Class

The `OnriMath` class provides trigonometric functions (`sin`, `cos`, `tan`), exponential, logarithmic, and other mathematical functions tailored for the Onri system.

## Utility Functions

Utility functions for handling arrays and generating random values are provided for each system.

### SakUtil

The `SakUtil` class includes methods for creating arrays of Sak objects and generating random Sak values.

### RelUtil

The `RelUtil` class includes methods for creating arrays of Rel objects and generating random Rel values.

### OnriUtil

The `OnriUtil` class includes methods for creating arrays of Onri objects and generating random Onri values.

## Encryption and Decryption Functions

These functions allow for encrypting and decrypting values within each system.

### Sak Encryption

The Sak encryption functions convert a Sak object's value into an integer, apply an XOR operation with a key, and return the encrypted value. The decryption function reverses this process.

### Rel Encryption

The Rel encryption functions convert the `x`, `s`, and `t` values of a Rel object into integers, apply an XOR operation with a key, and return the encrypted values. The decryption function reverses this process.

### Onri Encryption

The Onri encryption functions convert the `f` and `i` values of an Onri object into integers, apply an XOR operation with a key, and return the encrypted values. The decryption function reverses this process.

## Integration Functions

These functions provide conversions between the different systems.

- `sak_to_rel`: Converts a Sak object to a Rel object.
- `rel_to_sak`: Converts a Rel object to a Sak object.
- `sak_to_onri`: Converts a Sak object to an Onri object.
- `onri_to_sak`: Converts an Onri object to a Sak object.
- `rel_to_onri`: Converts a Rel object to an Onri object.
