import streamlit as st
import re
from typing import List, Tuple

class RTLConverter:
    """
    A class to convert arithmetic expressions to Register Transfer Level (RTL) representation.
    """
    
    def __init__(self):
        self.register_counter = 1
        self.rtl_instructions = []
    
    def reset(self):
        """Reset the converter for a new expression."""
        self.register_counter = 1
        self.rtl_instructions = []
    
    def parse_expression(self, expression: str) -> List[str]:
        """
        Parse the arithmetic expression into tokens.
        Returns a list of tokens (numbers, variables, operators).
        """
        tokens = re.findall(r'\d+|\w+|[+\-*/]', expression.replace(' ', ''))
        return tokens
    
    def is_number(self, token: str) -> bool:
        """Check if a token is a number."""
        try:
            int(token)
            return True
        except ValueError:
            return False
    
    def is_operator(self, token: str) -> bool:
        """Check if a token is an operator."""
        return token in ['+', '-', '*', '/']
    
    def get_next_register(self) -> str:
        """Get the next available register name."""
        register_name = f"R{self.register_counter}"
        self.register_counter += 1
        return register_name
    
    def convert_to_rtl(self, expression: str) -> Tuple[List[str], str]:
        """
        Convert an arithmetic expression to RTL instructions.
        Returns a tuple of (RTL instructions list, error message if any).
        """
        self.reset()
        
        try:
            if '=' not in expression:
                return [], "Error: Expression must contain an assignment (=)"
            
            parts = expression.split('=')
            if len(parts) != 2:
                return [], "Error: Invalid assignment format"
            
            variable = parts[0].strip()
            expr = parts[1].strip()
            
            if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable):
                return [], "Error: Invalid variable name"
            
            tokens = self.parse_expression(expr)
            
            if len(tokens) == 0:
                return [], "Error: Empty expression"
            
            if len(tokens) == 1:
                if self.is_number(tokens[0]) or tokens[0].isalpha():
                    self.rtl_instructions.append(f"{variable} <- {tokens[0]}")
                    return self.rtl_instructions, ""
                else:
                    return [], "Error: Invalid single token"
            
            current_register = None
            
            i = 0
            while i < len(tokens):
                if i == 0:
                    if self.is_number(tokens[i]) or tokens[i].isalpha():
                        current_register = self.get_next_register()
                        self.rtl_instructions.append(f"{current_register} <- {tokens[i]}")
                    else:
                        return [], f"Error: Expected number or variable at position {i}"
                
                elif i % 2 == 1:
                    if not self.is_operator(tokens[i]):
                        return [], f"Error: Expected operator at position {i}"
                    
                    if i + 1 >= len(tokens):
                        return [], "Error: Missing operand after operator"
                    
                    next_operand = tokens[i + 1]
                    if not (self.is_number(next_operand) or next_operand.isalpha()):
                        return [], f"Error: Expected number or variable at position {i + 1}"
                    
                    next_register = self.get_next_register()
                    self.rtl_instructions.append(f"{next_register} <- {next_operand}")
                    
                    result_register = self.get_next_register()
                    operator = tokens[i]
                    self.rtl_instructions.append(f"{result_register} <- {current_register} {operator} {next_register}")
                    
                    current_register = result_register
                    
                    i += 1
                
                i += 1
            
            if current_register:
                self.rtl_instructions.append(f"{variable} <- {current_register}")
            
            return self.rtl_instructions, ""
            
        except Exception as e:
            return [], f"Error: {str(e)}"

def main():
    """Main Streamlit application."""
    st.set_page_config(
        page_title="RTL Converter",
        page_icon="🔧",
        layout="wide"
    )
    
    st.title("🔧 Register Transfer Level (RTL) Converter")
    st.markdown("---")
    
    st.markdown("""
    ### About this tool
    This tool converts simple arithmetic expressions into their Register Transfer Level (RTL) representation.
    It demonstrates how high-level expressions are broken down into low-level register operations.
    
    **Features:**
    - Supports basic operators: `+`, `-`, `*`, `/`
    - Processes expressions left-to-right (no operator precedence)
    - Generates step-by-step RTL instructions
    - Educational tool for Computer Architecture concepts
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("Input")
        
        expression = st.text_input(
            "Enter an arithmetic expression:",
            value="x = 6 + 9",
            help="Example: x = 6 + 9 or result = a + b - 3"
        )
    
    with col2:
        st.header("RTL Output")
        
        if st.button("Convert to RTL", type="primary"):
            converter = RTLConverter()
            rtl_instructions, error = converter.convert_to_rtl(expression)
            
            if error:
                st.error(error)
            else:
                st.success("Conversion successful!")
                
                # Display RTL instructions
                st.subheader("RTL Instructions:")
                for i, instruction in enumerate(rtl_instructions, 1):
                    st.code(f"{i}. {instruction}", language="text")
                
                # Download option
                rtl_text = "\n".join([f"{i}. {instruction}" for i, instruction in enumerate(rtl_instructions, 1)])
                st.download_button(
                    label="Download RTL Instructions",
                    data=rtl_text,
                    file_name=f"rtl_instructions_{expression.split('=')[0].strip()}.txt",
                    mime="text/plain"
                )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    ### How it works:
    1. **Input parsing**: The expression is broken down into tokens (numbers, variables, operators)
    2. **Register allocation**: Each operand is loaded into a register (R1, R2, R3, ...)
    3. **Operation execution**: Operations are performed left-to-right using registers
    4. **Final assignment**: The result is stored in the destination variable
    
    **Note**: This tool processes expressions left-to-right without considering operator precedence.
    For example, `3 + 2 * 4` is processed as `(3 + 2) * 4 = 20`, not `3 + (2 * 4) = 11`.
    """)

if __name__ == "__main__":
    main()