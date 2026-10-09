import re

text = "Contact us at abc@gmail.com or support@company.com"

try:
    if not text.strip():
        raise ValueError("Text is empty")

    pattern = r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,4}"
    emails = re.findall(pattern, text)

    if emails:
        print("Email addresses found:")
        for email in emails:
            print(email)
    else:
        print("No valid email addresses found.")

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Unexpected error:", e)
