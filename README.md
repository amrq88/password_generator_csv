```markdown
# Random Password Generator

This is a simple Tkinter-based GUI application for generating random passwords and storing them in a CSV file.

## Features

- Generate random passwords with options for customization.
- Input fields for purpose, URL, and email.
- Save generated passwords along with input information in a CSV file.
- User-friendly interface.

## Getting Started

### Prerequisites

- Python 3.x
- Install required packages using the following command:

  ```bash
  pip install -r requirements.txt
  ```

### Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/amrq88/password_generator_csv.git
   ```

2. Navigate to the project directory:

   ```bash
   cd password_generator_csv
   ```

3. Run the application:

   ```bash
   python password_generator.py
   ```

4. Enter the purpose, URL, and email, then click the "Generate" button to create a random password.

5. The generated password and input information will be saved in the `passwords.csv` file.

## Customization

You can customize the password generation options by modifying the `password_generator.py` file.

```python
# Example options for password generation
password_gen = PasswordGenerator()
password_gen.minlen = 12
password_gen.maxlen = 16
password_gen.minuchars = 2
password_gen.minlchars = 2
password_gen.minnumbers = 2
password_gen.minschars = 2
password = password_gen.generate_password()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [password_generator](https://pypi.org/project/password-generator/) - Library for generating random passwords.

Feel free to contribute and open issues if you encounter any problems or have suggestions for improvements.
