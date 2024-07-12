# Sak-Rel-Onri Number Systems

## Overview

The Sak-Rel-Onri package implements three number systems: Sak, Rel, and Onri. These systems provide unique mathematical frameworks that challenge traditional numerical concepts and offer new perspectives on computation and representation.

### Key Features

- **Sak System**: A number system where all values are ≥ 0.5, redefining basic arithmetic and advanced mathematical operations.
- **Rel System**: A relational number system that incorporates contextual factors into numerical representations.
- **Onri System**: A system that models the interplay between fiction and reality in numerical form.
- Advanced arithmetic operations for each system
- Mathematical functions (trigonometric, exponential, logarithmic) adapted for each system
- Utility functions for array creation and random number generation
- Basic encryption and decryption capabilities
- Interoperability functions for converting between systems

## Installation

You can install the Sak-Rel-Onri package using pip:

```bash
pip install sak-rel-onri
```

## Usage

### Basic Operations

```python
from sak_rel_onri import Sak, Rel, Onri

# Sak System
s1 = Sak(0.7)
s2 = Sak(0.8)
s_sum = s1 + s2
print(f"Sak sum: {s_sum}")

# Rel System
r1 = Rel(1, 0.8, 0.9)
r2 = Rel(2, 0.7, 0.6)
r_product = r1 * r2
print(f"Rel product: {r_product}")

# Onri System
o1 = Onri(0.5, 2)
o2 = Onri(0.3, 1)
o_diff = o1 - o2
print(f"Onri difference: {o_diff}")
```

### Advanced Mathematics

```python
from sak_rel_onri import SakMath, RelMath, OnriMath

# Sak Mathematics
s = Sak(0.7)
s_sin = SakMath.sin(s)
s_log = SakMath.log(s)
print(f"Sak sin: {s_sin}, Sak log: {s_log}")

# Rel Mathematics
r = Rel(1, 0.8, 0.9)
r_cos = RelMath.cos(r)
r_exp = RelMath.exp(r)
print(f"Rel cos: {r_cos}, Rel exp: {r_exp}")

# Onri Mathematics
o = Onri(0.5, 2)
o_tan = OnriMath.tan(o)
o_sqrt = OnriMath.sqrt(o)
print(f"Onri tan: {o_tan}, Onri sqrt: {o_sqrt}")
```

### Utility Functions

```python
from sak_rel_onri import SakUtil, RelUtil, OnriUtil

# Create arrays
sak_array = SakUtil.array([0.6, 0.7, 0.8])
rel_array = RelUtil.array([1, 2, 3])
onri_array = OnriUtil.array([0.2, 0.4, 0.6])

# Generate random numbers
random_sak = SakUtil.random(0.5, 1)
random_rel = RelUtil.random(0, 10)
random_onri = OnriUtil.random(0, 1)
```

### Encryption and Decryption

```python
from sak_rel_onri import encrypt_sak, decrypt_sak

s = Sak(0.7)
key = 12345
encrypted = encrypt_sak(s, key)
decrypted = decrypt_sak(encrypted, key)
print(f"Original: {s}, Decrypted: {decrypted}")
```

### System Interoperability

```python
from sak_rel_onri import sak_to_rel, rel_to_onri, onri_to_sak

s = Sak(0.7)
r = sak_to_rel(s)
o = rel_to_onri(r)
s_again = onri_to_sak(o)
print(f"Sak -> Rel -> Onri -> Sak: {s_again}")
```

## Contributing

Contributions to the Sak-Rel-Onri package are welcome! Please feel free to submit pull requests, create issues, or suggest new features.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Sak system was inspired by the concept that nothingness cannot exist in mathematics.
- The Rel system draws from ideas in relational mathematics and contextual number theory.
- The Onri system was motivated by explorations into the mathematical representation of fiction and reality.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/VNylle/sak-rel-onri](https://github.com/VNylle/sak-rel-onri)

---

We hope you find the Sak-Rel-Onri package intriguing and useful for your mathematical explorations. Reminder, The Sak System is what I create for fun.


(This README.md is ai generated btw)
