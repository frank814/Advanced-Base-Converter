#!/usr/bin/env python3
"""
Advanced Number Base Converter
A professional tool for converting between decimal, binary, octal, hexadecimal, and other number systems.

Author: Frank Arthur 
Version: 2.0.0

Features:
- Supports bidirectional conversion between all number bases (2-16)
- Handles negative numbers with proper two's complement representation
- Comprehensive floating-point number conversions
- ASCII and Unicode character conversion
- Comprehensive input validation and error handling
- User-friendly command-line interface with clear formatting
- Step-by-step conversion explanations for educational purposes
- Efficient implementation with manual algorithms
- Multiple output formats
- Dark mode support
"""

import re
import sys
from typing import Union, Callable, Dict, Tuple, List

# Try to import colorama for Windows color support
try:
    import colorama
    colorama.init()
    HAS_COLORAMA = True
except ImportError:
    HAS_COLORAMA = False

# ------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------
HEX_DIGITS = "0123456789ABCDEF"
VERSION = "2.0.0"
AUTHOR = "Frank Arthur"
GITHUB = "frank814"

# Additional number base constants
BASE_DIGITS = "0123456789ABCDEF"
MAX_BASE = 16
MIN_BASE = 2

# Color schemes
COLOR_SCHEMES = {
    'light': {
        'RESET': "\033[0m",
        'RED': "\033[31m",
        'GREEN': "\033[32m",
        'YELLOW': "\033[33m",
        'BLUE': "\033[34m",
        'PURPLE': "\033[35m",
        'CYAN': "\033[36m",
        'WHITE': "\033[37m",
        'BOLD': "\033[1m",
        'UNDERLINE': "\033[4m"
    },
    'dark': {
        'RESET': "\033[0m",
        'RED': "\033[91m",
        'GREEN': "\033[92m",
        'YELLOW': "\033[93m",
        'BLUE': "\033[94m",
        'PURPLE': "\033[95m",
        'CYAN': "\033[96m",
        'WHITE': "\033[97m",
        'BOLD': "\033[1m",
        'UNDERLINE': "\033[4m"
    }
}

# Current color scheme
CURRENT_SCHEME = 'dark'

# ANSI Color Codes
class Colors:
    def __init__(self, scheme='dark'):
        self.scheme = scheme
        self.colors = COLOR_SCHEMES.get(scheme, COLOR_SCHEMES['dark'])
        
    def __getattr__(self, name):
        return self.colors.get(name, "")

# Create global Colors instance
colors = Colors(CURRENT_SCHEME)

# Maximum bits for two's complement representation
MAX_BITS = 64

# ------------------------------------------------------------------
# 1. Low-level converters (manual algorithms)
# ------------------------------------------------------------------

# ---------- General base conversion functions

def dec_to_base(n: int, base: int, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """
    Convert a decimal integer to any base representation (2-16).
    Handles both positive and negative numbers.
    
    Args:
        n: Decimal integer to convert
        base: Target base (2-16)
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the string representation or a tuple of (string, steps list)
    """
    steps = []
    original_n = n
    
    if n == 0:
        if show_steps:
            steps.append(f"0 in decimal is 0 in base {base}")
            return "0", steps
        return "0"
    
    if not MIN_BASE <= base <= MAX_BASE:
        raise ValueError(f"Base must be between {MIN_BASE} and {MAX_BASE}")
    
    is_negative = n < 0
    if is_negative:
        steps.append(f"Converting negative number: {original_n}")
        n = abs(n)
        steps.append(f"Taking absolute value: {n}")
    
    digits = []
    working_n = n
    
    if show_steps:
        steps.append(f"Starting decimal to base {base} conversion of {working_n}:")
        steps.append("Step | Decimal | Divided by Base | Remainder | Digit")
        steps.append("---- | ------- | --------------- | --------- | -----")
        step_num = 1
    
    while working_n:
        remainder = working_n % base
        digit = BASE_DIGITS[remainder]
        if show_steps:
            steps.append(f"{step_num:4} | {working_n:7} | {base:15} | {remainder:9} | {digit}")
        digits.append(digit)
        working_n = working_n // base
        step_num += 1 if show_steps else 0
    
    result = "".join(reversed(digits))
    final_result = f"-{result}" if is_negative else result
    
    if show_steps:
        steps.append(f"Reading remainders from bottom to top: {result}")
        if is_negative:
            steps.append(f"Adding negative sign: {final_result}")
        steps.append(f"Final result: {original_n} in decimal = {final_result} in base {base}")
        return final_result, steps
    
    return final_result


def base_to_dec(number_str: str, base: int, show_steps: bool = False) -> Union[int, Tuple[int, List[str]]]:
    """
    Convert a number string from any base (2-16) to decimal integer.
    
    Args:
        number_str: Number string to convert
        base: Base of the number system (2-16)
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the decimal integer or a tuple of (decimal integer, steps list)
    """
    steps = []
    original_str = number_str
    
    if not MIN_BASE <= base <= MAX_BASE:
        raise ValueError(f"Base must be between {MIN_BASE} and {MAX_BASE}")
    
    # Handle negative numbers
    is_negative = number_str.startswith('-')
    if is_negative:
        steps.append(f"Converting negative number: {original_str}")
        number_str = number_str[1:]
        steps.append(f"Removing negative sign for conversion: {number_str}")
    
    # Validate the number string
    valid_chars = BASE_DIGITS[:base]
    if not re.fullmatch(f"[{valid_chars}]+" , number_str.upper()):
        raise ValueError(f"Invalid number for base {base}")
    
    if show_steps:
        steps.append(f"Starting base {base} to decimal conversion of {number_str}:")
        steps.append("Position | Digit | Digit Value | Value = Digit Value × {base}^Position".format(base=base))
        steps.append("-------- | ----- | ----------- | -----------------------------------------")
    
    decimal_value = 0
    # Process from right to left (least significant digit to most significant digit)
    for i, digit in enumerate(reversed(number_str.upper())):
        digit_value = BASE_DIGITS.index(digit)
        position_value = digit_value * (base ** i)
        decimal_value += position_value
        
        if show_steps:
            steps.append(f"{i:8} | {digit:5} | {digit_value:11} | {position_value:38}")
    
    # Apply negative sign if needed
    if is_negative:
        decimal_value = -decimal_value
        if show_steps:
            steps.append(f"Applying negative sign: {decimal_value}")
    
    if show_steps:
        steps.append(f"Final result: {original_str} in base {base} = {decimal_value} in decimal")
        return decimal_value, steps
    
    return decimal_value

# ---------- Floating-point conversion functions

def dec_to_base_float(decimal: float, base: int, precision: int = 10, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """
    Convert a decimal floating-point number to any base representation.
    
    Args:
        decimal: Decimal floating-point number
        base: Target base (2-16)
        precision: Number of fractional digits
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the string representation or a tuple of (string, steps list)
    """
    steps = []
    original_decimal = decimal
    
    if decimal == 0:
        if show_steps:
            steps.append(f"0.0 in decimal is 0.0 in base {base}")
            return "0.0", steps
        return "0.0"
    
    if not MIN_BASE <= base <= MAX_BASE:
        raise ValueError(f"Base must be between {MIN_BASE} and {MAX_BASE}")
    
    # Handle negative numbers
    is_negative = decimal < 0
    if is_negative:
        steps.append(f"Converting negative number: {original_decimal}")
        decimal = abs(decimal)
        steps.append(f"Taking absolute value: {decimal}")
    
    # Separate integer and fractional parts
    int_part = int(decimal)
    frac_part = decimal - int_part
    
    # Convert integer part
    int_result = dec_to_base(int_part, base)
    
    # Convert fractional part
    frac_result = []
    working_frac = frac_part
    
    if show_steps:
        steps.append(f"Converting integer part {int_part}: {int_result}")
        steps.append(f"Converting fractional part {frac_part}:")
        steps.append("Step | Fractional | Multiplied by Base | Result    | Integer Part")
        steps.append("---- | ---------- | ------------------ | --------- | ------------")
        step_num = 1
    
    for _ in range(precision):
        working_frac *= base
        int_digit = int(working_frac)
        frac_result.append(BASE_DIGITS[int_digit])
        
        if show_steps:
            steps.append(f"{step_num:4} | {working_frac/base:10.6f} | {base:20} | {working_frac:9.6f} | {int_digit:12}")
            step_num += 1
        
        working_frac -= int_digit
        if working_frac == 0:
            break
    
    # Combine results
    result = f"{int_result}.{''.join(frac_result)}" if frac_result else int_result
    final_result = f"-{result}" if is_negative else result
    
    if show_steps:
        steps.append(f"Combining results: {final_result}")
        if is_negative:
            steps.append(f"Adding negative sign: {final_result}")
        steps.append(f"Final result: {original_decimal} in decimal = {final_result} in base {base}")
        return final_result, steps
    
    return final_result

# ---------- ASCII and Unicode conversion functions

def char_to_ascii(char: str, show_steps: bool = False) -> Union[int, Tuple[int, List[str]]]:
    """
    Convert a character to its ASCII/Unicode code point.
    
    Args:
        char: Single character to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the code point or a tuple of (code point, steps list)
    """
    steps = []
    
    if len(char) != 1:
        raise ValueError("Please enter a single character")
    
    code_point = ord(char)
    
    if show_steps:
        steps.append(f"Character: '{char}'")
        steps.append(f"ASCII/Unicode code point: {code_point}")
        steps.append(f"Binary representation: {bin(code_point)[2:]}")
        steps.append(f"Hexadecimal representation: {hex(code_point)[2:].upper()}")
        return code_point, steps
    
    return code_point

def ascii_to_char(code_point: int, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """
    Convert an ASCII/Unicode code point to its corresponding character.
    
    Args:
        code_point: Integer code point (0-1114111)
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the character or a tuple of (character, steps list)
    """
    steps = []
    
    if not 0 <= code_point <= 1114111:
        raise ValueError("Code point must be between 0 and 1114111")
    
    try:
        char = chr(code_point)
    except ValueError:
        raise ValueError(f"Invalid code point: {code_point}")
    
    if show_steps:
        steps.append(f"Code point: {code_point}")
        steps.append(f"Character: '{char}'")
        steps.append(f"Binary representation: {bin(code_point)[2:]}")
        steps.append(f"Hexadecimal representation: {hex(code_point)[2:].upper()}")
        return char, steps
    
    return char

# ---------- Utility functions

def detect_base(number_str: str) -> int:
    """
    Detect the base of a number string based on prefix or format.
    
    Args:
        number_str: Number string to detect
        
    Returns:
        Detected base (2, 8, 10, 16) or 0 if unknown
    """
    number_str = number_str.strip()
    
    # Check for prefixes
    if number_str.lower().startswith('0b'):
        return 2
    elif number_str.lower().startswith('0o'):
        return 8
    elif number_str.lower().startswith('0x'):
        return 16
    
    # Check format
    if re.fullmatch(r'-?[01]+', number_str):
        return 2
    elif re.fullmatch(r'-?[0-7]+', number_str):
        return 8
    elif re.fullmatch(r'-?[0-9]+', number_str):
        return 10
    elif re.fullmatch(r'-?[0-9A-Fa-f]+', number_str):
        return 16
    
    return 0

# ---------- decimal to ...
def dec_to_bin(n: int, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """
    Convert a decimal integer to its binary representation.
    Handles both positive and negative numbers using two's complement.
    
    Args:
        n: Decimal integer to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the binary string or a tuple of (binary string, steps list)
    """
    steps = []
    original_n = n
    
    if n == 0:
        if show_steps:
            steps.append("0 in decimal is 0 in binary")
            return "0", steps
        return "0"
    
    is_negative = n < 0
    if is_negative:
        steps.append(f"Converting negative number: {original_n}")
        # For negative numbers, we'll use Python's bit_length to determine
        # an appropriate number of bits for two's complement representation
        bits_needed = n.bit_length() + 1  # +1 for sign bit
        steps.append(f"Determined {bits_needed} bits needed for two's complement representation")
        n = (1 << bits_needed) + n  # Compute two's complement
        steps.append(f"Computed two's complement value: {n}")
    
    bits = []
    working_n = n
    
    if show_steps:
        steps.append(f"Starting decimal to binary conversion of {working_n}:")
        steps.append("Step | Decimal | Divided by 2 | Remainder")
        steps.append("---- | ------- | ------------ | ---------")
        step_num = 1
    
    while working_n:
        remainder = working_n & 1
        if show_steps:
            steps.append(f"{step_num:4} | {working_n:7} | 2           | {remainder}")
        bits.append(str(remainder))
        working_n >>= 1
        step_num += 1 if show_steps else 0
    
    result = "".join(reversed(bits))
    final_result = f"-{result}" if is_negative else result
    
    if show_steps:
        steps.append(f"Reading remainders from bottom to top: {result}")
        if is_negative:
            steps.append(f"Adding negative sign: {final_result}")
        steps.append(f"Final result: {original_n} in decimal = {final_result} in binary")
        return final_result, steps
    
    return final_result


def dec_to_oct(n: int, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """
    Convert a decimal integer to its octal representation.
    
    Args:
        n: Decimal integer to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the octal string or a tuple of (octal string, steps list)
    """
    steps = []
    original_n = n
    
    if n == 0:
        if show_steps:
            steps.append("0 in decimal is 0 in octal")
            return "0", steps
        return "0"
    
    is_negative = n < 0
    if is_negative:
        steps.append(f"Converting negative number: {original_n}")
        n = abs(n)
        steps.append(f"Taking absolute value: {n}")
    
    chars = []
    working_n = n
    
    if show_steps:
        steps.append(f"Starting decimal to octal conversion of {working_n}:")
        steps.append("Step | Decimal | Divided by 8 | Remainder")
        steps.append("---- | ------- | ------------ | ---------")
        step_num = 1
    
    while working_n:
        remainder = working_n & 7
        if show_steps:
            steps.append(f"{step_num:4} | {working_n:7} | 8           | {remainder}")
        chars.append(str(remainder))
        working_n >>= 3
        step_num += 1 if show_steps else 0
    
    result = "".join(reversed(chars))
    final_result = f"-{result}" if is_negative else result
    
    if show_steps:
        steps.append(f"Reading remainders from bottom to top: {result}")
        if is_negative:
            steps.append(f"Adding negative sign: {final_result}")
        steps.append(f"Final result: {original_n} in decimal = {final_result} in octal")
        return final_result, steps
    
    return final_result


def dec_to_hex(n: int, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """
    Convert a decimal integer to its hexadecimal representation.
    
    Args:
        n: Decimal integer to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the hexadecimal string or a tuple of (hexadecimal string, steps list)
    """
    steps = []
    original_n = n
    
    if n == 0:
        if show_steps:
            steps.append("0 in decimal is 0 in hexadecimal")
            return "0", steps
        return "0"
    
    is_negative = n < 0
    if is_negative:
        steps.append(f"Converting negative number: {original_n}")
        n = abs(n)
        steps.append(f"Taking absolute value: {n}")
    
    chars = []
    working_n = n
    
    if show_steps:
        steps.append(f"Starting decimal to hexadecimal conversion of {working_n}:")
        steps.append("Step | Decimal | Divided by 16 | Remainder | Hex Digit")
        steps.append("---- | ------- | ------------ | --------- | ---------")
        step_num = 1
    
    while working_n:
        remainder = working_n & 15
        hex_digit = HEX_DIGITS[remainder]
        if show_steps:
            steps.append(f"{step_num:4} | {working_n:7} | 16          | {remainder:9} | {hex_digit}")
        chars.append(hex_digit)
        working_n >>= 4
        step_num += 1 if show_steps else 0
    
    result = "".join(reversed(chars))
    final_result = f"-{result}" if is_negative else result
    
    if show_steps:
        steps.append(f"Reading remainders from bottom to top: {result}")
        if is_negative:
            steps.append(f"Adding negative sign: {final_result}")
        steps.append(f"Final result: {original_n} in decimal = {final_result} in hexadecimal")
        return final_result, steps
    
    return final_result


# ---------- string to decimal (validation + built-in int())
def validate_and_convert(number_str: str, pattern: str, base: int, number_type: str) -> int:
    """
    Validate a number string against a pattern and convert it to decimal.
    
    Args:
        number_str: The number string to validate and convert
        pattern: Regular expression pattern to validate against
        base: Base of the number system
        number_type: Name of the number type (for error messages)
        
    Returns:
        Integer representation of the number
        
    Raises:
        ValueError: If the number string is invalid
    """
    # Handle negative numbers
    is_negative = False
    if number_str.startswith('-'):
        is_negative = True
        number_str = number_str[1:]
    
    # Validate the number string
    if not re.fullmatch(pattern, number_str):
        raise ValueError(f"Invalid {number_type} number")
    
    # Convert to decimal
    value = int(number_str, base)
    return -value if is_negative else value

def bin_to_dec(bstr: str, show_steps: bool = False) -> Union[int, Tuple[int, List[str]]]:
    """
    Convert a binary string to decimal integer.
    
    Args:
        bstr: Binary string to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the decimal integer or a tuple of (decimal integer, steps list)
    """
    steps = []
    original_bstr = bstr
    
    # Handle negative numbers
    is_negative = bstr.startswith('-')
    if is_negative:
        steps.append(f"Converting negative binary number: {original_bstr}")
        bstr = bstr[1:]
        steps.append(f"Removing negative sign for conversion: {bstr}")
    
    # Validate the binary string
    if not re.fullmatch(r"[01]+", bstr):
        raise ValueError("Invalid binary number")
    
    if show_steps:
        steps.append(f"Starting binary to decimal conversion of {bstr}:")
        steps.append("Position | Digit | Value = Digit × 2^Position")
        steps.append("-------- | ----- | --------------------------")
    
    decimal_value = 0
    # Process from right to left (least significant bit to most significant bit)
    for i, digit in enumerate(reversed(bstr)):
        digit_value = int(digit)
        position_value = digit_value * (2 ** i)
        decimal_value += position_value
        
        if show_steps:
            steps.append(f"{i:8} | {digit:5} | {position_value:24}")
    
    # Apply negative sign if needed
    if is_negative:
        decimal_value = -decimal_value
        if show_steps:
            steps.append(f"Applying negative sign: {decimal_value}")
    
    if show_steps:
        steps.append(f"Final result: {original_bstr} in binary = {decimal_value} in decimal")
        return decimal_value, steps
    
    return decimal_value

def oct_to_dec(ostr: str, show_steps: bool = False) -> Union[int, Tuple[int, List[str]]]:
    """
    Convert an octal string to decimal integer.
    
    Args:
        ostr: Octal string to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the decimal integer or a tuple of (decimal integer, steps list)
    """
    steps = []
    original_ostr = ostr
    
    # Handle negative numbers
    is_negative = ostr.startswith('-')
    if is_negative:
        steps.append(f"Converting negative octal number: {original_ostr}")
        ostr = ostr[1:]
        steps.append(f"Removing negative sign for conversion: {ostr}")
    
    # Validate the octal string
    if not re.fullmatch(r"[0-7]+", ostr):
        raise ValueError("Invalid octal number")
    
    if show_steps:
        steps.append(f"Starting octal to decimal conversion of {ostr}:")
        steps.append("Position | Digit | Value = Digit × 8^Position")
        steps.append("-------- | ----- | --------------------------")
    
    decimal_value = 0
    # Process from right to left (least significant digit to most significant digit)
    for i, digit in enumerate(reversed(ostr)):
        digit_value = int(digit)
        position_value = digit_value * (8 ** i)
        decimal_value += position_value
        
        if show_steps:
            steps.append(f"{i:8} | {digit:5} | {position_value:24}")
    
    # Apply negative sign if needed
    if is_negative:
        decimal_value = -decimal_value
        if show_steps:
            steps.append(f"Applying negative sign: {decimal_value}")
    
    if show_steps:
        steps.append(f"Final result: {original_ostr} in octal = {decimal_value} in decimal")
        return decimal_value, steps
    
    return decimal_value

def hex_to_dec(hstr: str, show_steps: bool = False) -> Union[int, Tuple[int, List[str]]]:
    """
    Convert a hexadecimal string to decimal integer.
    
    Args:
        hstr: Hexadecimal string to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the decimal integer or a tuple of (decimal integer, steps list)
    """
    steps = []
    original_hstr = hstr
    hstr = hstr.upper()  # Convert to uppercase for consistency
    
    # Handle negative numbers
    is_negative = hstr.startswith('-')
    if is_negative:
        steps.append(f"Converting negative hexadecimal number: {original_hstr}")
        hstr = hstr[1:]
        steps.append(f"Removing negative sign for conversion: {hstr}")
    
    # Validate the hexadecimal string
    if not re.fullmatch(r"[0-9A-F]+", hstr):
        raise ValueError("Invalid hexadecimal number")
    
    if show_steps:
        steps.append(f"Starting hexadecimal to decimal conversion of {hstr}:")
        steps.append("Position | Digit | Digit Value | Value = Digit Value × 16^Position")
        steps.append("-------- | ----- | ----------- | -----------------------------------")
    
    decimal_value = 0
    # Process from right to left (least significant digit to most significant digit)
    for i, digit in enumerate(reversed(hstr)):
        digit_value = HEX_DIGITS.index(digit)
        position_value = digit_value * (16 ** i)
        decimal_value += position_value
        
        if show_steps:
            steps.append(f"{i:8} | {digit:5} | {digit_value:11} | {position_value:35}")
    
    # Apply negative sign if needed
    if is_negative:
        decimal_value = -decimal_value
        if show_steps:
            steps.append(f"Applying negative sign: {decimal_value}")
    
    if show_steps:
        steps.append(f"Final result: {original_hstr} in hexadecimal = {decimal_value} in decimal")
        return decimal_value, steps
    
    return decimal_value


# ---------- cross conversions via decimal
def bin_to_oct(bstr: str, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """Convert a binary string to octal string.
    
    Args:
        bstr: Binary string to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the octal string or a tuple of (octal string, steps list)
    """
    if show_steps:
        steps = []
        steps.append(f"Starting binary to octal conversion of {bstr}")
        steps.append("Step 1: Convert binary to decimal")
        steps.append("=" * 50)
        
        # Convert binary to decimal with steps
        dec_value, bin_to_dec_steps = bin_to_dec(bstr, show_steps=True)
        steps.extend(bin_to_dec_steps)
        
        steps.append("")
        steps.append("Step 2: Convert decimal to octal")
        steps.append("=" * 50)
        
        # Convert decimal to octal with steps
        oct_value, dec_to_oct_steps = dec_to_oct(dec_value, show_steps=True)
        steps.extend(dec_to_oct_steps)
        
        steps.append("")
        steps.append("=" * 50)
        steps.append(f"Complete conversion: {bstr} (binary) = {oct_value} (octal)")
        
        return oct_value, steps
    
    return dec_to_oct(bin_to_dec(bstr))

def bin_to_hex(bstr: str, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """Convert a binary string to hexadecimal string.
    
    Args:
        bstr: Binary string to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the hexadecimal string or a tuple of (hexadecimal string, steps list)
    """
    if show_steps:
        steps = []
        steps.append(f"Starting binary to hexadecimal conversion of {bstr}")
        steps.append("Step 1: Convert binary to decimal")
        steps.append("=" * 50)
        
        # Convert binary to decimal with steps
        dec_value, bin_to_dec_steps = bin_to_dec(bstr, show_steps=True)
        steps.extend(bin_to_dec_steps)
        
        steps.append("")
        steps.append("Step 2: Convert decimal to hexadecimal")
        steps.append("=" * 50)
        
        # Convert decimal to hexadecimal with steps
        hex_value, dec_to_hex_steps = dec_to_hex(dec_value, show_steps=True)
        steps.extend(dec_to_hex_steps)
        
        steps.append("")
        steps.append("=" * 50)
        steps.append(f"Complete conversion: {bstr} (binary) = {hex_value} (hexadecimal)")
        
        return hex_value, steps
    
    return dec_to_hex(bin_to_dec(bstr))

def oct_to_bin(ostr: str, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """Convert an octal string to binary string.
    
    Args:
        ostr: Octal string to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the binary string or a tuple of (binary string, steps list)
    """
    if show_steps:
        steps = []
        steps.append(f"Starting octal to binary conversion of {ostr}")
        steps.append("Step 1: Convert octal to decimal")
        steps.append("=" * 50)
        
        # Convert octal to decimal with steps
        dec_value, oct_to_dec_steps = oct_to_dec(ostr, show_steps=True)
        steps.extend(oct_to_dec_steps)
        
        steps.append("")
        steps.append("Step 2: Convert decimal to binary")
        steps.append("=" * 50)
        
        # Convert decimal to binary with steps
        bin_value, dec_to_bin_steps = dec_to_bin(dec_value, show_steps=True)
        steps.extend(dec_to_bin_steps)
        
        steps.append("")
        steps.append("=" * 50)
        steps.append(f"Complete conversion: {ostr} (octal) = {bin_value} (binary)")
        
        return bin_value, steps
    
    return dec_to_bin(oct_to_dec(ostr))

def oct_to_hex(ostr: str, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """Convert an octal string to hexadecimal string.
    
    Args:
        ostr: Octal string to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the hexadecimal string or a tuple of (hexadecimal string, steps list)
    """
    if show_steps:
        steps = []
        steps.append(f"Starting octal to hexadecimal conversion of {ostr}")
        steps.append("Step 1: Convert octal to decimal")
        steps.append("=" * 50)
        
        # Convert octal to decimal with steps
        dec_value, oct_to_dec_steps = oct_to_dec(ostr, show_steps=True)
        steps.extend(oct_to_dec_steps)
        
        steps.append("")
        steps.append("Step 2: Convert decimal to hexadecimal")
        steps.append("=" * 50)
        
        # Convert decimal to hexadecimal with steps
        hex_value, dec_to_hex_steps = dec_to_hex(dec_value, show_steps=True)
        steps.extend(dec_to_hex_steps)
        
        steps.append("")
        steps.append("=" * 50)
        steps.append(f"Complete conversion: {ostr} (octal) = {hex_value} (hexadecimal)")
        
        return hex_value, steps
    
    return dec_to_hex(oct_to_dec(ostr))

def hex_to_bin(hstr: str, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """Convert a hexadecimal string to binary string.
    
    Args:
        hstr: Hexadecimal string to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the binary string or a tuple of (binary string, steps list)
    """
    if show_steps:
        steps = []
        steps.append(f"Starting hexadecimal to binary conversion of {hstr}")
        steps.append("Step 1: Convert hexadecimal to decimal")
        steps.append("=" * 50)
        
        # Convert hexadecimal to decimal with steps
        dec_value, hex_to_dec_steps = hex_to_dec(hstr, show_steps=True)
        steps.extend(hex_to_dec_steps)
        
        steps.append("")
        steps.append("Step 2: Convert decimal to binary")
        steps.append("=" * 50)
        
        # Convert decimal to binary with steps
        bin_value, dec_to_bin_steps = dec_to_bin(dec_value, show_steps=True)
        steps.extend(dec_to_bin_steps)
        
        steps.append("")
        steps.append("=" * 50)
        steps.append(f"Complete conversion: {hstr} (hexadecimal) = {bin_value} (binary)")
        
        return bin_value, steps
    
    return dec_to_bin(hex_to_dec(hstr))

def hex_to_oct(hstr: str, show_steps: bool = False) -> Union[str, Tuple[str, List[str]]]:
    """Convert a hexadecimal string to octal string.
    
    Args:
        hstr: Hexadecimal string to convert
        show_steps: Whether to return the conversion steps
        
    Returns:
        Either the octal string or a tuple of (octal string, steps list)
    """
    if show_steps:
        steps = []
        steps.append(f"Starting hexadecimal to octal conversion of {hstr}")
        steps.append("Step 1: Convert hexadecimal to decimal")
        steps.append("=" * 50)
        
        # Convert hexadecimal to decimal with steps
        dec_value, hex_to_dec_steps = hex_to_dec(hstr, show_steps=True)
        steps.extend(hex_to_dec_steps)
        
        steps.append("")
        steps.append("Step 2: Convert decimal to octal")
        steps.append("=" * 50)
        
        # Convert decimal to octal with steps
        oct_value, dec_to_oct_steps = dec_to_oct(dec_value, show_steps=True)
        steps.extend(dec_to_oct_steps)
        
        steps.append("")
        steps.append("=" * 50)
        steps.append(f"Complete conversion: {hstr} (hexadecimal) = {oct_value} (octal)")
        
        return oct_value, steps
    
    return dec_to_oct(hex_to_dec(hstr))


# ------------------------------------------------------------------
# 2. UI helpers
# ------------------------------------------------------------------
def read_number(prompt: str, validator: Callable[[str], bool], error_msg: str) -> str:
    """
    Read and validate user input with a custom validator function.
    
    Args:
        prompt: The prompt to display to the user
        validator: A function that returns True if the input is valid
        error_msg: The error message to display if validation fails
        
    Returns:
        The validated user input
    """
    while True:
        try:
            s = input(prompt).strip()
            if validator(s):
                return s
            raise ValueError(error_msg)
        except ValueError as e:
            print(f"✗  {e}")


def read_int(prompt: str) -> int:
    """
    Read an integer from user input.
    
    Args:
        prompt: The prompt to display to the user
        
    Returns:
        The integer entered by the user
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("✗  Please enter a valid integer")


def read_bin() -> str:
    """Read a binary number from user input."""
    return read_number(
        "Enter binary: ", 
        lambda s: bool(re.fullmatch(r"-?[01]+", s)),
        "Invalid binary number (use only 0 and 1, optional negative sign)"
    )

def read_oct() -> str:
    """Read an octal number from user input."""
    return read_number(
        "Enter octal: ", 
        lambda s: bool(re.fullmatch(r"-?[0-7]+", s)),
        "Invalid octal number (use only 0-7, optional negative sign)"
    )

def read_hex() -> str:
    """Read a hexadecimal number from user input."""
    return read_number(
        "Enter hexadecimal: ", 
        lambda s: bool(re.fullmatch(r"-?[0-9A-Fa-f]+", s)),
        "Invalid hexadecimal number (use only 0-9, A-F, a-f, optional negative sign)"
    ).upper()


def toggle_color_scheme() -> str:
    """
    Toggle between light and dark color schemes.
    
    Returns:
        Confirmation message
    """
    global CURRENT_SCHEME
    global colors
    
    if CURRENT_SCHEME == 'dark':
        CURRENT_SCHEME = 'light'
    else:
        CURRENT_SCHEME = 'dark'
    
    colors = Colors(CURRENT_SCHEME)
    return f"Color scheme changed to {CURRENT_SCHEME}"


# ------------------------------------------------------------------
# 3. Menu system and application logic
# ------------------------------------------------------------------
CONVERSIONS: Dict[int, Tuple[str, Callable]] = {
    # decimal
    1:  ("Decimal → Binary", lambda: dec_to_bin(read_int("Enter decimal: "))),
    2:  ("Binary → Decimal", lambda: bin_to_dec(read_bin())),
    3:  ("Decimal → Octal",  lambda: dec_to_oct(read_int("Enter decimal: "))),
    4:  ("Octal → Decimal",  lambda: oct_to_dec(read_oct())),
    5:  ("Decimal → Hex",    lambda: dec_to_hex(read_int("Enter decimal: "))),
    6:  ("Hex → Decimal",    lambda: hex_to_dec(read_hex())),
    # binary ↔ octal / hex
    7:  ("Binary → Octal",   lambda: bin_to_oct(read_bin())),
    8:  ("Octal → Binary",   lambda: oct_to_bin(read_oct())),
    9:  ("Binary → Hex",     lambda: bin_to_hex(read_bin())),
    10: ("Hex → Binary",     lambda: hex_to_bin(read_hex())),
    11: ("Octal → Hex",      lambda: oct_to_hex(read_oct())),
    12: ("Hex → Octal",      lambda: hex_to_oct(read_hex())),
    # Advanced features
    13: ("Decimal → Any Base (2-16)", lambda: dec_to_base(read_int("Enter decimal: "), read_int("Enter target base (2-16): "))),
    14: ("Any Base (2-16) → Decimal", lambda: base_to_dec(input("Enter number: "), read_int("Enter source base (2-16): "))),
    15: ("Decimal Float → Any Base", lambda: dec_to_base_float(float(input("Enter decimal float: ")), read_int("Enter target base (2-16): "))),
    16: ("ASCII → Character", lambda: ascii_to_char(read_int("Enter ASCII code: "))),
    17: ("Character → ASCII", lambda: char_to_ascii(input("Enter character: "))),
    18: ("Number Base Detection", lambda: detect_base(input("Enter number: "))),
    19: ("Toggle Color Scheme", lambda: toggle_color_scheme()),
}

def print_header() -> None:
    """Print the application header with version information and colors."""
    header = f"""
{colors.BOLD}{colors.CYAN}╔══════════════════════════════════════════════════════╗{colors.RESET}
{colors.BOLD}{colors.GREEN}║                  Advanced Number Base Converter      ║{colors.RESET}
{colors.BOLD}{colors.BLUE}║                        Version {VERSION}              ║{colors.RESET}
{colors.BOLD}{colors.CYAN}╚══════════════════════════════════════════════════════╝{colors.RESET}
{colors.BOLD}{colors.PURPLE}║                    Author: {AUTHOR}                  ║{colors.RESET}
{colors.BOLD}{colors.PURPLE}║                  GitHub: {GITHUB}                   ║{colors.RESET}
{colors.BOLD}{colors.CYAN}╚══════════════════════════════════════════════════════╝{colors.RESET}
"""
    print(header)

def display_result(result: Union[int, str]) -> None:
    """
    Display the conversion result in a formatted way.
    
    Args:
        result: The result to display
    """
    print("\n" + "=" * 50)
    print(f"Result: {result}")
    print("=" * 50)

def menu() -> None:
    """Display the main menu and handle user choices."""
    print_header()
    
    while True:
        print(f"\n{colors.BOLD}{colors.PURPLE}Available Conversions:{colors.RESET}")
        # Group conversions by type for better readability
        decimal_group = [k for k, (desc, _) in CONVERSIONS.items() if "Decimal" in desc and "Any Base" not in desc]
        binary_group = [k for k, (desc, _) in CONVERSIONS.items() if "Binary" in desc and "Decimal" not in desc]
        octal_group = [k for k, (desc, _) in CONVERSIONS.items() if "Octal" in desc and "Decimal" not in desc and "Binary" not in desc]
        hex_group = [k for k, (desc, _) in CONVERSIONS.items() if "Hex" in desc and "Decimal" not in desc and "Binary" not in desc and "Octal" not in desc]
        advanced_group = [k for k, (desc, _) in CONVERSIONS.items() if any(keyword in desc for keyword in ["Any Base", "Float", "ASCII", "Detection", "Color Scheme"])]
        
        # Print decimal conversions first
        if decimal_group:
            print(f"\n{colors.BOLD}{colors.GREEN}Decimal Conversions:{colors.RESET}")
            for k in decimal_group:
                print(f"{colors.BOLD}{colors.YELLOW}{k:2}){colors.RESET} {CONVERSIONS[k][0]}")
        
        # Print other groups
        if binary_group:
            print(f"\n{colors.BOLD}{colors.BLUE}Binary Conversions:{colors.RESET}")
            for k in binary_group:
                print(f"{colors.BOLD}{colors.YELLOW}{k:2}){colors.RESET} {CONVERSIONS[k][0]}")
        
        if octal_group:
            print(f"\n{colors.BOLD}{colors.CYAN}Octal Conversions:{colors.RESET}")
            for k in octal_group:
                print(f"{colors.BOLD}{colors.YELLOW}{k:2}){colors.RESET} {CONVERSIONS[k][0]}")
        
        if hex_group:
            print(f"\n{colors.BOLD}{colors.RED}Hexadecimal Conversions:{colors.RESET}")
            for k in hex_group:
                print(f"{colors.BOLD}{colors.YELLOW}{k:2}){colors.RESET} {CONVERSIONS[k][0]}")
        
        # Print advanced features
        if advanced_group:
            print(f"\n{colors.BOLD}{colors.PURPLE}Advanced Features:{colors.RESET}")
            for k in advanced_group:
                print(f"{colors.BOLD}{colors.YELLOW}{k:2}){colors.RESET} {CONVERSIONS[k][0]}")
        
        print(f"\n{colors.BOLD}{colors.YELLOW}20){colors.RESET} Quit")
        
        try:
            choice = input("\nSelect an option (1-20): ").strip()
            if choice == "20":
                print(f"\n{colors.BOLD}{colors.GREEN}Thank you for using Advanced Number Base Converter. Good-bye!{colors.RESET}")
                sys.exit(0)
            
            if not choice.isdigit() or int(choice) not in CONVERSIONS:
                print("✗  Invalid choice. Please enter a number between 1 and 20.")
                continue
            
            # Execute the selected conversion
            option_num = int(choice)
            conversion_name, conversion_func = CONVERSIONS[option_num]
            
            # Display conversion header with colors
            print(f"\n{colors.BOLD}{colors.CYAN}{'=' * 50}{colors.RESET}")
            print(f"{colors.BOLD}{colors.GREEN}Conversion: {conversion_name}{colors.RESET}")
            print(f"{colors.BOLD}{colors.CYAN}{'=' * 50}{colors.RESET}")
            
            try:
                # Handle each conversion type explicitly to show steps
                if option_num == 1:  # Decimal → Binary
                    n = read_int("Enter decimal number: ")
                    result, steps = dec_to_bin(n, show_steps=True)
                elif option_num == 2:  # Binary → Decimal
                    bstr = read_bin()
                    result, steps = bin_to_dec(bstr, show_steps=True)
                elif option_num == 3:  # Decimal → Octal
                    n = read_int("Enter decimal number: ")
                    result, steps = dec_to_oct(n, show_steps=True)
                elif option_num == 4:  # Octal → Decimal
                    ostr = read_oct()
                    result, steps = oct_to_dec(ostr, show_steps=True)
                elif option_num == 5:  # Decimal → Hexadecimal
                    n = read_int("Enter decimal number: ")
                    result, steps = dec_to_hex(n, show_steps=True)
                elif option_num == 6:  # Hexadecimal → Decimal
                    hstr = read_hex()
                    result, steps = hex_to_dec(hstr, show_steps=True)
                elif option_num == 7:  # Binary → Octal
                    bstr = read_bin()
                    result, steps = bin_to_oct(bstr, show_steps=True)
                elif option_num == 8:  # Octal → Binary
                    ostr = read_oct()
                    result, steps = oct_to_bin(ostr, show_steps=True)
                elif option_num == 9:  # Binary → Hexadecimal
                    bstr = read_bin()
                    result, steps = bin_to_hex(bstr, show_steps=True)
                elif option_num == 10:  # Hexadecimal → Binary
                    hstr = read_hex()
                    result, steps = hex_to_bin(hstr, show_steps=True)
                elif option_num == 11:  # Octal → Hexadecimal
                    ostr = read_oct()
                    result, steps = oct_to_hex(ostr, show_steps=True)
                elif option_num == 12:  # Hexadecimal → Octal
                    hstr = read_hex()
                    result, steps = hex_to_oct(hstr, show_steps=True)
                elif option_num == 13:  # Decimal → Any Base
                    n = read_int("Enter decimal number: ")
                    base = read_int("Enter target base (2-16): ")
                    result, steps = dec_to_base(n, base, show_steps=True)
                elif option_num == 14:  # Any Base → Decimal
                    number_str = input("Enter number: ")
                    base = read_int("Enter source base (2-16): ")
                    result, steps = base_to_dec(number_str, base, show_steps=True)
                elif option_num == 15:  # Decimal Float → Any Base
                    decimal = float(input("Enter decimal float: "))
                    base = read_int("Enter target base (2-16): ")
                    result, steps = dec_to_base_float(decimal, base, show_steps=True)
                elif option_num == 16:  # ASCII → Character
                    code = read_int("Enter ASCII code: ")
                    result, steps = ascii_to_char(code, show_steps=True)
                elif option_num == 17:  # Character → ASCII
                    char = input("Enter character: ")
                    result, steps = char_to_ascii(char, show_steps=True)
                elif option_num == 18:  # Number Base Detection
                    number_str = input("Enter number: ")
                    result = detect_base(number_str)
                    steps = [f"Detected base for '{number_str}': {result}"]
                elif option_num == 19:  # Toggle Color Scheme
                    result = conversion_func()
                    steps = [result]
                else:
                    # Fallback in case of unknown option
                    result = conversion_func()
                    steps = None
                
                # Display the result and steps with colors
                print(f"\n{colors.BOLD}{colors.GREEN}Result: {colors.CYAN}{result}{colors.RESET}")
                
                if steps:
                    print(f"\n{colors.BOLD}{colors.CYAN}{'=' * 50}{colors.RESET}")
                    print(f"{colors.BOLD}{colors.YELLOW}Step-by-Step Conversion Process:{colors.RESET}")
                    print(f"{colors.BOLD}{colors.CYAN}{'=' * 50}{colors.RESET}")
                    for step in steps:
                        # Colorize different parts of the steps for better readability
                        if any(keyword in step for keyword in ["Step", "Position", "Digit", "Value"]):
                            print(f"{colors.BOLD}{colors.PURPLE}{step}{colors.RESET}")
                        elif any(keyword in step.lower() for keyword in ["final", "result"]):
                            print(f"{colors.BOLD}{colors.GREEN}{step}{colors.RESET}")
                        elif any(keyword in step for keyword in ["-", "|"]):
                            print(f"{colors.BOLD}{colors.BLUE}{step}{colors.RESET}")
                        else:
                            print(step)
                else:
                    print("\nDetailed steps not available for this conversion.")
                
            except Exception as e:
                # If there's an error, fall back to the original method
                print(f"\n{colors.BOLD}{colors.RED}✗  Error: {e}{colors.RESET}")
                print("\nUsing simplified conversion...")
                result = conversion_func()
                print(f"Result: {result}")
            
            # Ask user if they want to perform another conversion
            another = input("\nWould you like to perform another conversion? (y/n): ").lower().strip()
            if another != 'y':
                print("\nThank you for using Advanced Number Base Converter. Good-bye!")
                sys.exit(0)
                
        except ValueError as e:
            print(f"✗  Error: {e}")
        except Exception as e:
            print(f"✗  Unexpected error: {e}")


# ------------------------------------------------------------------
# 4. Command-line interface and entry point
# ------------------------------------------------------------------
def main() -> None:
    """Main entry point for the application."""
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Good-bye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
