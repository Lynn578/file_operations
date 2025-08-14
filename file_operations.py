def file_modifier():
    """Reads a file, modifies content, and writes to a new file with comprehensive error handling."""
    try:
        # Get filename from user (strip whitespace and check empty input)
        filename = input("Enter the file to read (e.g., 'input.txt'): ").strip()
        if not filename:
            raise ValueError("Filename cannot be empty.")

        # Read original file (explicit UTF-8 encoding for cross-platform compatibility)
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Modify content (example: uppercase + ensure newline at end)
        modified_content = content.upper()
        if not modified_content.endswith('\n'):
            modified_content += '\n'  # Ensure trailing newline for POSIX compliance
        
        # Write to new file (validate filename doesn't contain path traversal)
        if '/' in filename or '\\' in filename:
            raise SecurityError("Filename cannot contain path separators.")
            
        new_filename = f"modified_{filename.split('/')[-1].split('\\')[-1]}"  # Handle subdirs
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
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__} - {e}")
    finally:
        print("Operation completed.")

class SecurityError(Exception):
    """Custom exception for security-related issues."""
    pass

if __name__ == "__main__":
    file_modifier()