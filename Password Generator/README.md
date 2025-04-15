# Password Generator - Remaining Characters

## Task Overview
We are enhancing our password generator function by applying a specific flow to construct a secure and valid password.

### Password Construction Flow
1. **Start with Alphabets:**
   - Generate a random password of length `(N - 2)` using only alphabets.
   - Ensure that the **first character** of the password is an **alphabet**.

2. **Appending a Number or Alphabet:**
   - If `use_numbers` is `'Yes'`, append a random number from the `string_num` pool.
   - If `use_numbers` is `'No'`, append a random alphabet instead.
   - Now the password length becomes `(N - 1)`.

3. **Appending a Special Character or Alphabet:**
   - If `use_special_chars` is `'Yes'`, append a random special character from the `string_special` pool.
   - If `use_special_chars` is `'No'`, append a random alphabet instead.
   - The final password length becomes `N`.

## Provided String Pools
- `string_char`: All alphabet characters (uppercase + lowercase)
- `string_num`: All numeric characters (0–9)
- `string_special`: All required special characters

## Task
Implement the logic above in the `generate_password()` function.

### Function Signature
```python
def generate_password(length: int, use_special_chars: str, use_numbers: str) -> str:
    # Implementation here
```

### Parameters
- `length`: Desired length of the final password (N)
- `use_special_chars`: Either `'Yes'` or `'No'`
- `use_numbers`: Either `'Yes'` or `'No'`

Use the parent strings to construct the password step-by-step based on the conditions above.
