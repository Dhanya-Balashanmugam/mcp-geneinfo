# mcpatlas

Get tissue and cancer specific protein expression info from Human Protein Atlas

## Installation

Install the package in development mode:

```bash
pip install -e .
```

Or install from PyPI (when available):

```bash
pip install mcpatlas
```

## Usage




### MCP Server

The package provides an MCP server for integration with MCP-compatible clients:

```bash
# Run the MCP server
mcpatlas-server
```

The MCP server provides the following tools:

- **tool1**: Description of tool1
- **tool2**: Description of tool2
- **tool3**: Description of tool3


### Python API

```python
from mcpatlas.main import mcpatlasBridge

# Initialize the bridge
bridge = mcpatlasBridge()

# Use your functionality
result = bridge.your_method()
```

## Features

- **Feature 1**: Description of feature 1
- **Feature 2**: Description of feature 2
- **Feature 3**: Description of feature 3

- **MCP Integration**: Full Model Context Protocol server implementation


## API Methods

### Core Methods

- `method1()`: Description of method1
- `method2()`: Description of method2
- `method3()`: Description of method3

### Configuration

The package uses a configuration class for settings:

```python
from mcpatlas.main import mcpatlasConfig, mcpatlasBridge

config = mcpatlasConfig(
    base_url="https://api.example.com",
    api_key="your_api_key",
    timeout=30.0
)

bridge = mcpatlasBridge(config)
```


## MCP Server Configuration

To use the MCP server with an MCP client, configure it as follows:

```json
{
  "mcpServers": {
    "mcpatlas": {
      "command": "mcpatlas-server",
      "env": {}
    }
  }
}
```

The server will automatically handle:
- JSON-RPC communication
- Tool discovery and invocation
- Error handling and reporting


## Development

### Setup Development Environment

```bash
# Install in development mode with dev dependencies
pip install -e .[dev]

# Run tests
pytest

# Format code
black mcpatlas/

# Type checking
mypy mcpatlas/
```

### Project Structure

```
mcpatlas/
├── pyproject.toml      # Package configuration
├── README.md          # This file
├── LICENSE            # MIT License
├── mcpatlas/         # Main package
│   ├── __init__.py    # Package initialization
│   ├── main.py        # Core functionality


│   └── mcp_server.py  # MCP server implementation

└── tests/             # Test files
    ├── __init__.py
    └── test_main.py   # Tests for main functionality
```

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run the test suite
6. Submit a pull request

## Support

For issues and questions, please use the GitHub issue tracker. 