import re
import math


# Function to analyze password
def analyze(password):
    score = 0
    feedback = []

    # 1. Password length
    if len(password) >= 12:
        score += 30
        feedback.append("✓ Good password length")
    elif len(password) >= 8:
        score += 20
        feedback.append("✓ Acceptable password length")
    else:
        feedback.append("✗ Password is too short")

    # 2. Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 15
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ No uppercase letters")

    # 3. Lowercase letters
    if re.search(r"[a-z]", password):
        score += 15
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ No lowercase letters")

    # 4. Numbers
    if re.search(r"[0-9]", password):
        score += 15
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ No numbers")

    # 5. Special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ No special characters")

    # 6. Extra length bonus
    if len(password) >= 14:
        score += 10
        feedback.append("✓ Extra length bonus")

    # Determine strength
    if score >= 80:
        strength = "Strong"
    elif score >= 50:
        strength = "Medium"
    else:
        strength = "Weak"

    return score, strength, feedback


# Function to calculate entropy
def entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26

    if re.search(r"[A-Z]", password):
        charset += 26

    if re.search(r"[0-9]", password):
        charset += 10

    if re.search(r"[^A-Za-z0-9]", password):
        charset += 32

    if charset == 0:
        return 0

    return len(password) * math.log2(charset)


# ==============================
# Main Program
# ==============================

print("=" * 40)
print("       PASSWORD STRENGTH ANALYZER")
print("=" * 40)

password = input("Enter password: ")

if not password:
    print("\nError: Password cannot be empty.")

else:
    score, strength, feedback = analyze(password)

    print("\nPassword Strength:", strength)
    print("Score:", score, "/ 100")

    print("\nAnalysis:")

    for item in feedback:
        print(item)

    print("\nSuggestions:")

    if len(password) < 12:
        print("• Use at least 12 characters")

    if not re.search(r"[A-Z]", password):
        print("• Add uppercase letters")

    if not re.search(r"[a-z]", password):
        print("• Add lowercase letters")

    if not re.search(r"[0-9]", password):
        print("• Add numbers")

    if not re.search(r"[^A-Za-z0-9]", password):
        print("• Add special characters")

    print("• Avoid predictable patterns and common passwords")

    print("\nEstimated Entropy:",
          round(entropy(password), 2), "bits")