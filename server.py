from mcp.server.fastmcp import FastMCP
from kubernetes import config

from tools.list_pods import list_pods
from tools.list_services import list_services
from tools.get_events import get_events
from tools.list_deployments import list_deployments

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

# Create an MCP server
mcp = FastMCP("kubernetes")

mcp.add_tool(list_pods)
mcp.add_tool(list_services)
mcp.add_tool(get_events)
mcp.add_tool(list_deployments)

if __name__ == "__main__":
    mcp.run(transport="stdio")
