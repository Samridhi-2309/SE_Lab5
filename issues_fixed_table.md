# Static Code Analysis – Issues Fixed Summary

| Issue | Tool(s) Reported | Line(s) | Description | Fix Implemented |
|--------|------------------|----------|---------------|-----------------|
| Mutable default argument (`logs=[]`) | **Pylint** | 11 | Using a mutable default (list) causes shared state between function calls. | Changed default to `logs=None` and initialized list inside function. |
| Bare `except:` | **Bandit, Pylint** | 27 | Catching all exceptions hides actual errors. | Replaced with `except KeyError:` and `except IOError:` for specific exceptions. |
| Insecure function usage (`eval()`) | **Bandit** | 61 | `eval()` can execute arbitrary code. | Removed `eval()` completely. |
| Invalid input types causing runtime errors | **Pylint, Runtime** | 16 | Function accepted invalid types (e.g., int for item, str for qty). | Added `isinstance()` validation for all inputs. |
| Unsafe file handling without context managers | **Flake8, Bandit** | 38, 46 | File objects not properly closed after operations. | Used `with open(...) as f:` for all file read/write operations. |
| Missing logging configuration | **Pylint (style)** | — | Logging used but not configured. | Added `logging.basicConfig()` with level and format in global scope. |

**Total Fixes Implemented:** 6 (minimum 4 required)

All identified high and medium severity issues were resolved.  
The final version passes Bandit, Flake8, and Pylint checks with minimal warnings.
