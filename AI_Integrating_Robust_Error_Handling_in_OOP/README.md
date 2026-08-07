# AI: Integrating Robust Error Handling in OOP

## Task Objective
Enhance the object-oriented `Product` and `InventoryManager` application by applying AI-assisted scaffolding to integrate robust data validation and exception handling. Using Python's `@property` decorators and a custom exception class (`InvalidProductDataError`), we protect the internal object state from illegal attribute assignments (such as negative prices or quantities) and enforce data integrity.

---

## Formulated AI Scaffolding Prompt (Gemini Code Assist)

> **Prompt:**  
> "Refactor the provided Python `Product` class to implement robust data validation for the `price` and `quantity` attributes using `@property` getters and setters. Define a custom exception named `InvalidProductDataError` that inherits from `Exception`. Ensure that setting `price` or `quantity` to non-numeric types or negative values raises `InvalidProductDataError` with a clear descriptive message, preventing invalid object creation or mutation. Provide the full refactored code alongside a detailed technical explanation of how using `@property` setters and custom exceptions enforces Data Integrity and Encapsulation."

---

## Technical Analysis & Design Evaluation

### 1. Functionality and Precedence of `@property` Setters
In standard Python classes without property decorators, attribute assignments like `self.price = price` inside `__init__()` or `product.quantity = -5` directly mutate public attributes without any checks. 

By applying `@property` and `@<attribute>.setter`:
- **Precedence & Interception:** Whenever code attempts to set `self.price = val` or `product.quantity = val`, Python automatically intercepts the assignment and routes it to the setter function.
- **Constructor Delegation:** Inside `Product.__init__`, writing `self.price = price` calls `@price.setter`. This ensures that validation is performed seamlessly during both **initial object construction** and **subsequent attribute modifications**.

### 2. Utility of Custom Exceptions (`InvalidProductDataError`)
Instead of allowing silent data corruption (e.g., negative inventory calculations or invalid string multiplication) or raising generic language-level exceptions, `InvalidProductDataError` provides domain-specific clarity.

#### Test Execution Result:
When attempting an illegal update (`manager.inventory[0].quantity = -5`), the application outputs:
```text
--- Testing Invalid Input ---
Test result: Quantity cannot be negative, got -5.
```
The error is caught gracefully, explaining precisely what broke, while the overall program execution remains stable.

### 3. Superiority Over Direct Attribute Assignment
1. **Encapsulation:** Internal representation (`_price`, `_quantity`) is shielded from uncontrolled external tampering.
2. **Data Integrity:** Guarantees that no `Product` object can exist in an invalid state at any point during its lifecycle.
3. **Single Source of Truth:** Centralizes all validation logic within setter methods, eliminating duplicate validation checks across calling code.

---

## File Structure
- `product_manager_initial.py`: Unmodified starter template.
- `product_manager_refactored.py`: Enhanced script with `@property` validation, `InvalidProductDataError`, and edge-case testing.
- `README.md`: Complete task documentation and analysis.
