# FLEXT-Oracle-OIC

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**FLEXT-Oracle-OIC** is the Oracle Integration Cloud (OIC) client library for the FLEXT ecosystem. It provides secure patterns for authentication, integration orchestration, and deployment management, fully compliant with OIC Gen3 standards.

## 🚀 Key Features

- **Secure Authentication**: Robust implementation of OAuth2 Client Credentials flow for IDCS/IAM.
- **Integration Management**: Programmatically trigger, monitor, and manage OIC integrations.
- **Deployment Automation**: Tools to export, import, and deploy integration packages (IARs).
- **Pattern Execution**: Support for App-Driven, Scheduled, and File Transfer integration patterns.
- **FLEXT Service Architecture**: Built on `flext-core` using `FlextService` and `FlextResult` for reliable error handling.

## 📦 Installation

Install via Poetry:

```bash
poetry add flext-oracle-oic
```

## 🛠️ Usage

### Client Initialization

Configure the client with robust settings for enterprise connectivity:

```python
from flext_oracle_oic import FlextOracleOicClient, OracleOicSettings

settings = OracleOicSettings(
    base_url="https://instance-id.integration.ocp.oraclecloud.com",
    client_id="your_client_id",
    client_secret="your_client_secret",
    token_url="https://idcs-instance.identity.oraclecloud.com/oauth2/v1/token",
    scope="your_scope"
)

client = FlextOracleOicClient(settings)
```

### Triggering an Integration

Execute an integration and handle the response:

```python
payload = {"orderId": "12345", "status": "PENDING"}
result = client.integrations.trigger("PROCESS_ORDER", version="1.0", payload=payload)

if result.is_success:
    print(f"Integration triggered: {result.value.tracking_id}")
else:
    print(f"Error: {result.error}")
```

### Monitoring Execution Status

Check the status of a running integration instance:

```python
status_result = client.monitoring.get_status(tracking_id="tracking_123")
if status_result.is_success:
    print(f"Current Status: {status_result.value.status}") # e.g., SUCCEEDED, RUNNING
```

## 🏗️ Architecture

FLEXT-Oracle-OIC connects the FLEXT ecosystem to Oracle Cloud:

- **Client Layer**: Abstracts raw REST API calls into domain-specific operations.
- **Auth Service**: Handles token lifecycle, caching, and automatic refreshment.
- **Resilience**: Built-in retry logic and circuit breakers for cloud interactions.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/development.md) for details on adding new integration patterns and running contract tests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
