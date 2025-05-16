# MCP Server Kubernetes

MCP Server for a Kubernetes cluster written in Python.

## Usage with Claude Desktop

```json
{
  "mcpServers": {
    "kubernetes": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/mcp-kubernetes/",
        "run",
        "server.py"
      ]
    }
  }
}
```

The server uses the official [Kubernetes Python client](https://github.com/kubernetes-client/python). This will automatically try and load your kubeconfig via the `KUBECONFIG` environment variable and default to `~/.kube/config` if no environment variable is set.

## Local Development

This project uses [uv](https://github.com/astral-sh/uv) for package management.

Create the virtual environment and activate it:

```bash
uv venv

source .venv/bin/activate
```

Install dependencies:

```bash
uv sync
```

Start MCP inspector:

```bash
uv run mcp dev server.py
```