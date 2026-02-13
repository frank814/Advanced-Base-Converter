# Quick Start Guide - Advanced Number Base Converter

**Author: Arthur Frank** | **Version: 2.0.0**

This guide will help you get started with the Advanced Number Base Converter in just a few minutes.

## 🚀 Quick Installation

### Step 1: Install Python

Make sure you have Python 3.7 or higher installed:

```bash
python --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install colorama
```

### Step 3: Verify Installation

```bash
python bin_dec_converter.py
```

You should see the welcome header and menu.

## 📖 Basic Usage

### Launch the Converter

```bash
python bin_dec_converter.py
```

### Main Menu Options

| Option | Description |
|--------|-------------|
| 1-12 | Basic conversions (Decimal, Binary, Octal, Hex) |
| 13 | Decimal → Any Base (2-16) |
| 14 | Any Base (2-16) → Decimal |
| 15 | Decimal Float → Any Base |
| 16 | ASCII → Character |
| 17 | Character → ASCII |
| 18 | Number Base Detection |
| 19 | Toggle Color Scheme |
| 20 | Quit |

## 🎯 Common Use Cases

### Example 1: Decimal to Binary

1. Select option **1**
2. Enter decimal number: `42`
3. View the result: `101010`
4. See step-by-step conversion process

### Example 2: Binary to Decimal

1. Select option **2**
2. Enter binary: `101010`
3. View the result: `42`

### Example 3: ASCII to Character

1. Select option **16**
2. Enter ASCII code: `65`
3. View the result: `A`

### Example 4: Character to ASCII

1. Select option **17**
2. Enter character: `A`
3. View the result: `65`

### Example 5: Floating-Point Conversion

1. Select option **15**
2. Enter decimal float: `0.625`
3. Enter target base: `2`
4. View the result: `0.101`

### Example 6: Any Base Conversion

1. Select option **13**
2. Enter decimal number: `42`
3. Enter target base: `8`
4. View the result: `52`

## 🎨 Color Scheme

The converter supports two color schemes:

- **Dark Mode** (default): Better for low-light environments
- **Light Mode**: Better for bright environments

To toggle between modes:

1. Select option **19**
2. The color scheme will change immediately

## 📊 Output Formats

### Interactive Mode

- **Colorful Interface**: Dark/light mode with terminal colors
- **Step-by-Step Explanations**: Educational conversion processes
- **Formatted Results**: Clean, organized output

### Script Mode

Use as a module in your Python scripts:

```python
from bin_dec_converter import dec_to_bin, bin_to_dec

# Convert decimal to binary
binary = dec_to_bin(42)
print(f"42 in binary: {binary}")

# Convert binary to decimal
decimal = bin_to_dec("101010")
print(f"101010 in decimal: {decimal}")

# Convert with steps
result, steps = dec_to_bin(42, show_steps=True)
print(f"Result: {result}")
for step in steps:
    print(step)
```

## ⚙️ Performance Tips

- **For Quick Conversions**: Use basic options (1-12)
- **For Educational Purposes**: Use any option to see step-by-step explanations
- **For Precision**: Use floating-point conversion (option 15) for decimal fractions
- **For Speed**: Use the converter as a module in your scripts

## 🐛 Troubleshooting

### Import Errors

If you see "ModuleNotFoundError", install dependencies:

```bash
pip install -r requirements.txt
```

### Color Issues on Windows

Make sure colorama is installed:

```bash
pip install colorama
```

### Input Errors

- **Binary**: Use only 0 and 1
- **Octal**: Use only 0-7
- **Hexadecimal**: Use only 0-9, A-F
- **Any Base**: Use only valid digits for that base

### Performance Issues

- The converter is optimized for speed
- Large numbers may take slightly longer
- Floating-point conversions with high precision may take longer

## 📚 Next Steps

1. Read the full [README.md](README.md) for detailed documentation
2. Explore all conversion options
3. Check the [GITHUB_DEPLOYMENT.md](GITHUB_DEPLOYMENT.md) for GitHub deployment
4. Contribute to the project

## ⚠️ Important Reminders

- **Use responsibly** for educational and professional purposes
- **Validate input** to ensure correct conversions
- **Check results** for accuracy, especially with complex conversions
- **Report issues** on GitHub if you encounter problems

## 🆘 Getting Help

For more information:

```bash
python bin_dec_converter.py --help
```

Or check the full documentation in [README.md](README.md).

---

**Made with ❤️ by Arthur Frank**
