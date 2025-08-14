"""
File Modifier Script

This script reads the content of a file specified by the user, modifies the content by converting it to uppercase 
(and ensures the content ends with a newline), then writes the modified content to a new file prefixed with 'modified_'.
It includes comprehensive error handling and security checks.

Usage Instructions:
1. Run the script with Python 3:
   python your_script_name.py

2. When prompted, enter the name of the file to read (e.g., 'input.txt'). Do NOT include any directory path.

3. If successful, a new file named 'modified_<filename>' will be created with uppercase content and a trailing newline.

Examples:
- Success:
  Enter the file to read (e.g., 'input.txt'): example.txt
  ✅ Success! Modified file saved as 'modified_example.txt'.
  Operation completed.

- File not found:
  Enter the file to read (e.g., 'input.txt'): missing.txt
  ❌ Error: File 'missing.txt' not found.
  Operation completed.

- Path traversal prevention:
  Enter the file to read (e.g., 'input.txt'): ../secret.txt
  ❌ Invalid input: Filename cannot contain path separators.
  Operation completed.

Requirements:
- Python 3.x
- Input file must be UTF-8 encoded text.
- Script should be run where you have read/write permissions.

"""

class SecurityError(Exception):
    """Custom exception for security-related issues."""
    pass

def file_modifier():
    """Reads a file, modifies content, and writes to a new file with comprehensive error handling."""
    try:
        # Get filename from user (strip whitespace and check empty input)
        filename = input("Enter the file to read (e.g., 'input.txt'): ").strip()
        if not filename:
            raise ValueError("Filename cannot be empty.")
        
        # Prevent path traversal attacks by disallowing path separators
        if '/' in filename or '\\' in filename:
            raise SecurityError("Filename cannot contain path separators.")
        
        # Read original file with UTF-8 encoding
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Modify content: convert to uppercase and ensure trailing newline
        modified_content = content.upper()
        if not modified_content.endswith('\n'):
            modified_content += '\n'  # Trailing newline for POSIX compliance
        
        # Write modified content to new file prefixed with 'modified_'
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"✅ Success! Modified file saved as '{new_filename}'.")
    
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    except PermissionError:
        print(f"❌ Error: No permission to access '{filename}'.")
    except UnicodeDecodeError:
        print(f"❌ Error: File '{filename}' is not UTF-8 encoded.")
    except ValueError as ve:
        print(f"❌ Invalid input: {ve}")
    except SecurityError as se:
        print(f"❌ Invalid input: {se}")
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__} - {e}")
    finally:
        print("Operation completed.")

if __name__ == "__main__":
    file_modifier()
