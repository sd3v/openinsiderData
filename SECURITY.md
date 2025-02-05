# Security Policy

## Supported Versions

The following versions of OpenInsider Scraper receive security updates:

| Version  | Supported          |
|----------|--------------------|
| 1.0.0    | ✅ Active support  |
| < 1.0.0  | ❌ No longer maintained |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, **please do not report it publicly**. Instead, follow these steps:

1. **Email us** at [sokkadev@gmx.de] with a detailed description of the issue.
2. **Include reproduction steps** to help us verify and fix the vulnerability quickly.
3. **Do not create a GitHub issue** for security reports to prevent exploitation before a fix is available.

We aim to respond to security reports **within 48 hours** and will provide updates as we work on a resolution.

## Security Best Practices

To ensure the security of your deployment, we recommend the following:

- **Use a virtual environment** (`venv`) to isolate dependencies.
- **Keep dependencies updated** by running `pip list --outdated` regularly.
- **Avoid exposing logs with sensitive data** (e.g., API keys, tokens).
- **Enable Docker security measures** if running in a containerized environment.

## Responsible Disclosure

We appreciate responsible disclosure and will acknowledge security researchers who report vulnerabilities responsibly.

Thank you for helping to keep OpenInsider Scraper secure!
