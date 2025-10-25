# Reflection on Static Code Analysis

### 1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest fixes were syntax and style-related issues, like replacing `except:` with a specific exception and adding context managers for file handling.  
The hardest issue was handling mutable default arguments because it required understanding Python’s function memory model and redesigning the function signature.

---

### 2. Did the static analysis tools report any false positives? If so, describe one example.
Bandit flagged some lower-severity warnings that weren’t critical in this context, such as missing docstrings for every function. While valid for best practices, they didn’t affect security or functionality, so they can be considered mild false positives for a small script.

---

### 3. How would you integrate static analysis tools into your actual software development workflow?
Static analysis can be integrated into a **CI/CD pipeline** (e.g., GitHub Actions) so that Pylint, Bandit, and Flake8 automatically run whenever code is committed or a pull request is opened.  
This ensures that code quality, security, and style standards are consistently enforced throughout the development cycle.

---

### 4. What tangible improvements did you observe in the code quality, readability, or robustness after applying the fixes?
After applying the fixes:
- The program no longer crashes on invalid input.
- Files are safely opened and closed.
- The code follows consistent logging and naming conventions.
- It’s easier to understand and maintain due to structured functions and safer practices.
Overall, the code became **more secure, maintainable, and reliable**.
