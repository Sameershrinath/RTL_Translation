

Click here to open App:-

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-orange)](https://sam-rtlprocess.streamlit.app/)

# RTL Converter - Register Transfer Level Expression Converter

A Python-based educational tool that converts simple arithmetic expressions into their Register Transfer Level (RTL) representation using Streamlit for the user interface.

## Features

- **Simple Expression Parsing**: Converts expressions like `x = 6 + 9` into RTL operations
- **Step-by-step RTL Generation**: Shows each register operation clearly
- **Interactive Web Interface**: Built with Streamlit for easy use
- **Educational Focus**: Perfect for Computer Architecture lab demonstrations
- **Left-to-Right Processing**: Processes expressions without operator precedence (educational simplification)

## Supported Operations

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)

## Installation

1. Ensure you have Python 3.7+ installed
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser to the displayed URL (typically `http://localhost:8501`)

3. Enter an arithmetic expression in the format: `variable = expression`
   - Example: `x = 6 + 9`
   - Example: `result = a + b - c`

4. Click "Convert to RTL" to see the step-by-step register operations

## Example Conversion

**Input**: `x = 6 + 9`

**RTL Output**:
```
1. R1 <- 6
2. R2 <- 9
3. R3 <- R1 + R2
4. x <- R3
```

**Input**: `result = 10 - 5 + 3`

**RTL Output**:
```
1. R1 <- 10
2. R2 <- 5
3. R3 <- R1 - R2
4. R4 <- 3
5. R5 <- R3 + R4
6. result <- R5
```

## How It Works

1. **Expression Parsing**: The input expression is tokenized into variables, numbers, and operators
2. **Register Allocation**: Each operand is assigned to a register (R1, R2, R3, ...)
3. **Left-to-Right Processing**: Operations are processed sequentially without operator precedence
4. **RTL Generation**: Each step is converted into a register transfer operation
5. **Final Assignment**: The result is transferred to the destination variable

## Educational Notes

- This tool intentionally processes expressions left-to-right without operator precedence
- This simplification helps students understand the basic concept of RTL operations
- In real processors, operator precedence and optimization would be considered
- Each intermediate result is stored in a new register for clarity

## Project Structure

```
RTL_proj/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Future Enhancements

- Support for parentheses and operator precedence
- Variable storage and reuse
- More complex expressions
- Assembly code generation
- Register optimization
- Support for different data types

## Contributing

This is an educational project. Feel free to enhance it for learning purposes!
