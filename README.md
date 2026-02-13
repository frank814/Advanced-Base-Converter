# 🔢 Advanced Number Base Converter

<div align="center">

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Author](https://img.shields.io/badge/author-Arthur%20ArthurFrank-purple.svg)

**A professional tool for converting between decimal, binary, octal, hexadecimal, and other number systems.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Examples](#-examples)
- [Output Formats](#-output-formats)
- [Command Line Arguments](#-command-line-arguments)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#)

---

## 🎯 About

The **Advanced Number Base Converter** is a sophisticated Python-based tool designed for educational and professional use. It enables users to seamlessly convert between different number systems, including decimal, binary, octal, hexadecimal, and any other base from 2 to 16.

**Developed by Arthur Frank** - This tool combines powerful algorithms, comprehensive error handling, and a user-friendly interface to provide an exceptional number conversion experience. GitHub: [Arthur Frank](https://github.com/ArthurFrank814)

### Key Capabilities

- **Universal Base Support** - Convert between any number base (2-16)
- **Floating-Point Support** - Handle decimal fractions with precision
- **ASCII/Unicode Conversion** - Convert between characters and their code points
- **Step-by-Step Explanations** - Educational step-by-step conversion processes
- **Negative Number Support** - Proper two's complement representation
- **Colorful Interface** - Dark/light mode support with terminal colors
- **Multiple Output Formats** - Clear, formatted output for different use cases

---

## ✨ Features

### 🔢 Number Base Support

| Base | Name | Supported |
|------|------|-----------|
| 2 | Binary | ✅ |
| 3 | Ternary | ✅ |
| 4 | Quaternary | ✅ |
| 5 | Quinary | ✅ |
| 6 | Senary | ✅ |
| 7 | Septenary | ✅ |
| 8 | Octal | ✅ |
| 9 | Nonary | ✅ |
| 10 | Decimal | ✅ |
| 11 | Undecimal | ✅ |
| 12 | Duodecimal | ✅ |
| 13 | Tridecimal | ✅ |
| 14 | Tetradecimal | ✅ |
| 15 | Pentadecimal | ✅ |
| 16 | Hexadecimal | ✅ |

### 📊 Conversion Types

| Conversion Type | Status |
|----------------|--------|
| Decimal ↔ Binary | ✅ |
| Decimal ↔ Octal | ✅ |
| Decimal ↔ Hexadecimal | ✅ |
| Decimal ↔ Any Base (2-16) | ✅ |
| Binary ↔ Octal | ✅ |
| Binary ↔ Hexadecimal | ✅ |
| Octal ↔ Hexadecimal | ✅ |
| Any Base ↔ Decimal | ✅ |
| Decimal Float ↔ Any Base | ✅ |
| ASCII ↔ Character | ✅ |
| Unicode ↔ Character | ✅ |
| Number Base Detection | ✅ |

### 🎨 Interface Features

- **Colorful Terminal Interface** - Dark/light mode support
- **Step-by-Step Explanations** - Educational conversion processes
- **Real-time Input Validation** - Immediate error feedback
- **Formatted Output** - Clean, organized results
- **Interactive Menu** - Easy navigation between conversion types
- **Error Handling** - Comprehensive error messages

### 🚀 Performance Features

- **Efficient Algorithms** - Manual conversion algorithms for speed
- **Memory Optimized** - Minimal memory usage
- **Fast Execution** - Quick conversion times
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **No External Dependencies** - Core functionality works without additional packages

---

## 📦 Installation

### Prerequisites

- ✅ Python 3.7 or higher
- ✅ pip (Python package manager)

### Method 1: Clone from GitHub

```bash
git clone https://github.com/ArthurFrank814/advanced-number-base-converter.git
cd advanced-number-base-converter
pip install -r requirements.txt
```

### Method 2: Install via pip

```bash
# Coming soon to PyPI
# pip install advanced-number-base-converter
```

### Method 3: Run Directly

```bash
# Download the repository
# Navigate to the project folder
pip install colorama  # For color support on Windows
python bin_dec_converter.py
```

### Optional Dependencies

For enhanced functionality:

```bash
pip install numpy matplotlib  # For advanced features
```

---

## 🖥️ Usage

### Basic Usage

```bash
python bin_dec_converter.py
```

This will launch the interactive menu where you can select from various conversion options.

### Command Line Usage

```bash
python bin_dec_converter.py [options]
```

### Script Usage

```python
from bin_dec_converter import dec_to_bin, bin_to_dec, dec_to_hex, hex_to_dec

# Convert decimal to binary
binary = dec_to_bin(42)
print(f"42 in binary: {binary}")

# Convert binary to decimal
decimal = bin_to_dec("101010")
print(f"101010 in decimal: {decimal}")
```

---

## 💡 Examples

### Example 1: Decimal to Binary

```bash
$ python bin_dec_converter.py

╔══════════════════════════════════════════════════════╗
║                  Advanced Number Base Converter      ║
║                        Version 2.0.0                ║
╚══════════════════════════════════════════════════════╝
║                    Author: Arthur Frank                  ║
╚══════════════════════════════════════════════════════╝

Available Conversions:

Decimal Conversions:
 1) Decimal → Binary
 2) Binary → Decimal
 3) Decimal → Octal
 4) Octal → Decimal
 5) Decimal → Hex
 6) Hex → Decimal

Binary Conversions:
 7) Binary → Octal
 8) Octal → Binary
 9) Binary → Hex
10) Hex → Binary

Octal Conversions:
11) Octal → Hex
12) Hex → Octal

Advanced Features:
13) Decimal → Any Base (2-16)
14) Any Base (2-16) → Decimal
15) Decimal Float → Any Base
16) ASCII → Character
17) Character → ASCII
18) Number Base Detection
19) Toggle Color Scheme

20) Quit

Select an option (1-20): 1

==================================================
Conversion: Decimal → Binary
==================================================
Enter decimal number: 42

Result: 101010

==================================================
Step-by-Step Conversion Process:
==================================================
Converting decimal to binary:
Step | Decimal | Divided by 2 | Remainder
---- | ------- | ------------ | ---------
   1 |      42 | 2           | 0
   2 |      21 | 2           | 1
   3 |      10 | 2           | 0
   4 |       5 | 2           | 1
   5 |       2 | 2           | 0
   6 |       1 | 2           | 1
Reading remainders from bottom to top: 101010
Final result: 42 in decimal = 101010 in binary

Would you like to perform another conversion? (y/n): n

Thank you for using Advanced Number Base Converter. Good-bye!
```

### Example 2: ASCII to Character

```bash
Select an option (1-20): 16

==================================================
Conversion: ASCII → Character
==================================================
Enter ASCII code: 65

Result: A

==================================================
Step-by-Step Conversion Process:
==================================================
Code point: 65
Character: 'A'
Binary representation: 1000001
Hexadecimal representation: 41
```

### Example 3: Decimal Float to Binary

```bash
Select an option (1-20): 15

==================================================
Conversion: Decimal Float → Any Base
==================================================
Enter decimal float: 0.625
Enter target base (2-16): 2

Result: 0.101

==================================================
Step-by-Step Conversion Process:
==================================================
Converting integer part 0: 0
Converting fractional part 0.625:
Step | Fractional | Multiplied by Base | Result    | Integer Part
---- | ---------- | ------------------ | --------- | ------------
   1 |    0.625000 |                  2 |  1.250000 |           1
   2 |    0.250000 |                  2 |  0.500000 |           0
   3 |    0.500000 |                  2 |  1.000000 |           1
Combining results: 0.101
Final result: 0.625 in decimal = 0.101 in base 2
```

### Example 4: Any Base to Decimal

```bash
Select an option (1-20): 14

==================================================
Conversion: Any Base (2-16) → Decimal
==================================================
Enter number: 1A3F
Enter source base (2-16): 16

Result: 6719

==================================================
Step-by-Step Conversion Process:
==================================================
Starting base 16 to decimal conversion of 1A3F:
Position | Digit | Digit Value | Value = Digit Value × 16^Position
-------- | ----- | ----------- | -----------------------------------------
       0 | F     |          15 |                                      15
       1 | 3     |           3 |                                      48
       2 | A     |          10 |                                     2560
       3 | 1     |           1 |                                     4096
Final result: 1A3F in base 16 = 6719 in decimal
```

---

## 📄 Output Formats

### Interactive Menu

The primary output format is the interactive menu, which provides:

- **Colorful Interface** - Dark/light mode support
- **Step-by-Step Explanations** - Educational conversion processes
- **Real-time Input Validation** - Immediate error feedback
- **Formatted Results** - Clean, organized output

### Script Output

When used as a module, the functions return:

- **Strings** - For basic conversions
- **Tuples** - For conversions with steps (result, steps list)
- **Integers** - For decimal results
- **Characters** - For ASCII/Unicode conversions

### Example Script Output

```python
from bin_dec_converter import dec_to_bin, bin_to_dec

# Basic conversion
binary = dec_to_bin(42)
print(f"42 → {binary}")  # Output: 42 → 101010

# Conversion with steps
result, steps = dec_to_bin(42, show_steps=True)
print(f"Result: {result}")
for step in steps:
    print(step)
```

---

## 🎛️ Command Line Arguments

### Coming Soon

The Advanced Number Base Converter will soon support command line arguments for direct conversions:

```bash
# Convert decimal to binary directly
python bin_dec_converter.py --decimal 42 --to binary

# Convert binary to decimal directly  
python bin_dec_converter.py --binary 101010 --to decimal

# Convert with steps
python bin_dec_converter.py --decimal 42 --to binary --steps
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Write clear commit messages
- Test your changes thoroughly
- Update documentation as needed

### Reporting Issues

If you find a bug or have a feature request:

1. Check existing issues
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details (OS, Python version)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Arthur Frank

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 Author

**Arthur Frank**

- GitHub: [@Arthur Frank](https://github.com/ArthurFrank814)
- Project: Advanced Number Base Converter
- Version: 2.0.0

### Acknowledgments

- Built with Python 3.7+
- Uses colorama for cross-platform color support
- Inspired by educational needs and professional use cases

---

## 📞 Support

For questions, issues, or suggestions:

- Open an issue on GitHub
- Check the documentation
- Review the examples

---

## 🔗 Related Projects

- [Binary Calculator](https://github.com/example/binary-calculator)
- [Hex Editor](https://github.com/example/hex-editor)
- [ASCII Table Generator](https://github.com/example/ascii-table-generator)

---

<div align="center">

**Made with ❤️ by Arthur Frank**

[⬆ Back to Top](#-advanced-number-base-converter)

</div>
