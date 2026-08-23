# AI: Scaffolding a Robust API Integration

**Author:** Kingsley Kipkoech  
**Module:** High Level Programming — Networks (Part 2)  
**Project:** AI Lab Assignment: Scaffolding a Robust API Integration  

---

## Overview

This project demonstrates the application of **Contextual Prompting** to refactor an existing Python API client (`sentiment_analyzer.py`) into production-grade code with secure authentication scaffolding and granular error handling.

---

## Files in this Task Folder

| File | Description |
|------|-------------|
| `sentiment_analyzer_initial.py` | Original sentiment analyzer implementation before refactoring |
| `sentiment_analyzer_refactored.py` | Production-ready version with Bearer auth scaffolding and expanded exception handling |
| `README.md` | Comprehensive documentation of prompt engineering, code comparisons, and architectural reflection |

---

## 1. Contextual AI Prompt Used

The following single contextual prompt was formulated and submitted to the AI:

```text
You are a senior Python software engineer reviewing an API client script.

Below is the current implementation of our `sentiment_analyzer.py` tool:

```python
#!/usr/bin/python3
"""
Sentiment Analysis Tool
Analyzes the sentiment of a given sentence using a public API.
"""
import requests
import sys


def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using the Text Processing API.

    Args:
        text (str): The sentence to analyze

    Returns:
        str: The sentiment label (positive, negative, or neutral)
    """
    url = "https://api.text-processing.com/api/sentiment/"
    payload = {"text": text}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raises exception for 4xx/5xx status codes
        data = response.json()
        label = data.get('label', 'neutral')

        # Map API response format to our desired output
        if label == 'pos':
            return 'positive'
        elif label == 'neg':
            return 'negative'
        else:
            return 'neutral'
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}", file=sys.stderr)
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        return None
    except (KeyError, ValueError) as e:
        print(f"Invalid response format: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./sentiment_analyzer.py <text>")
        sys.exit(1)

    sentence = " ".join(sys.argv[1:])
    result = analyze_sentiment(sentence)
    if result:
        print(result)
    else:
        sys.exit(1)
```

Please refactor this code to satisfy two critical production requirements:

1. **Authentication Scaffolding:** Securely read an API key from the environment variable `TEXT_PROCESSING_API_KEY` using Python's `os` module. If present, attach it to the request headers using the standard `Authorization: Bearer <key>` format.
2. **Granular Exception Handling:** Make error handling robust by explicitly catching `requests.exceptions.Timeout` and `requests.exceptions.ConnectionError` before generic HTTP/Request exceptions, printing informative, differentiated error messages to `sys.stderr` for each failure mode. Ensure a reasonable request timeout (e.g. 10 seconds) is configured.
```

---

## 2. Refactoring Comparison

### A. Authentication Scaffolding
* **Before:** No authentication mechanism existed. The API was called anonymously without header management.
* **After:** Securely reads `TEXT_PROCESSING_API_KEY` via `os.environ.get()` and dynamically constructs headers (`Authorization: Bearer <token>`), preventing hardcoded secret leaks and adhering to the Twelve-Factor App methodology.

### B. Granular Exception Hierarchy
* **Before:** Only caught generic `HTTPError`, `RequestException`, and parse errors. Network timeouts and dropped connections were lumped into generic failures.
* **After:** Added explicit `requests.exceptions.Timeout` and `requests.exceptions.ConnectionError` handlers with customized stderr messages and configured explicit `timeout=10` on the network request.

---

## 3. Verification & Reflection Analysis

### Verification of Adherence to Best Practices
The refactored code directly enforces modern secure API communication standards:
1. **Secret Management:** By querying environment variables rather than accepting hardcoded keys or CLI argument exposure, sensitive API tokens remain isolated from version control and command history logs.
2. **Defensive Network Programming:** Implementing an explicit `timeout=10` safeguards against hung worker processes and thread pool exhaustion. Granular exception catching enables observability tools to pinpoint network-layer versus transport-layer versus application-layer failures.

### Reflection on Contextual Prompting
Providing the existing codebase alongside strict architectural constraints dramatically improves AI output fidelity. Rather than generating an over-engineered rewrite with extraneous dependencies, the Contextual Prompting approach preserved the exact function signatures, argument parsing logic, and return contracts while surgically upgrading non-functional requirements (security, resilience, maintainability).
