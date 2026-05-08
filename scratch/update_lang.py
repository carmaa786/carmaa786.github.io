import os
import re

def update_lang_in_html(root_dir):
    for root, dirs, files in os.walk(root_dir):
        # Skip .git directory
        if '.git' in dirs:
            dirs.remove('.git')
        
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                try:
                    # Try UTF-8 first
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    encoding = 'utf-8'
                except UnicodeDecodeError:
                    try:
                        # Try ISO-8859-1 if UTF-8 fails
                        with open(file_path, 'r', encoding='iso-8859-1') as f:
                            content = f.read()
                        encoding = 'iso-8859-1'
                    except Exception as e:
                        print(f"Could not read {file_path}: {e}")
                        continue
                
                # Update <html lang="..."> to <html lang="en-IN">
                new_content = re.sub(r'<html\s+lang=["\'][^"\']*["\']', '<html lang="en-IN"', content, flags=re.IGNORECASE)
                
                # If <html lang="..."> was not found, try adding it to <html>
                if new_content == content:
                    # Look for <html> but not already having lang
                    new_content = re.sub(r'<html(?![^>]*\blang\b)(\s+|>|/|)', r'<html lang="en-IN"\1', content, count=1, flags=re.IGNORECASE)
                
                if new_content != content:
                    with open(file_path, 'w', encoding=encoding) as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")

if __name__ == "__main__":
    update_lang_in_html(".")
