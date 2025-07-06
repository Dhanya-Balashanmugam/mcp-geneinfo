"""
MCP Server implementation for mcpatlas.
"""

import json
import sys
from typing import Any, Dict, List, Optional

from .bridge import Bridge, Config


class MCPServer:
    """MCP Server for mcpatlas."""
    
    def __init__(self):
        """Initialize the MCP server."""
        self.bridge = Bridge()
        self.request_id = 0
    
    def send_response(self, result: Any, error: Optional[str] = None):
        """Send a JSON-RPC response."""
        response = {
            "jsonrpc": "2.0",
            "id": self.request_id,
        }
        
        if error:
            response["error"] = {"code": -1, "message": error}
        else:
            response["result"] = result
        
        print(json.dumps(response))
        sys.stdout.flush()
    
    def handle_request(self, request: Dict[str, Any]):
        """Handle a JSON-RPC request."""
        method = request.get("method")
        params = request.get("params", {})
        self.request_id = request.get("id", 0)
        
        try:
            if method == "initialize":
                self.handle_initialize(params)
            elif method == "tools/list":
                self.handle_list_tools()
            elif method == "tools/call":
                self.handle_call_tool(params)
            else:
                self.send_response(None, f"Unknown method: {method}")
        except Exception as e:
            self.send_response(None, str(e))
    
    def handle_initialize(self, params: Dict[str, Any]):
        """Handle initialize request."""
        response = {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": "mcpatlas-mcp",
                "version": "0.1.0"
            }
        }
        self.send_response(response)
    
    def handle_list_tools(self):
        """Handle tools/list request."""
        tools = [
            {
                "name": "method1",
                "description": "Run method 1",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "param1": {
                            "type": "string",
                            "description": "Parameter 1"
                        }
                    },
                    "required": ["param1"]
                }
            },
            {
                "name": "method2",
                "description": "Run method 2",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "param1": {
                            "type": "string",
                            "description": "Parameter 1"
                        },
                        "param2": {
                            "type": "integer",
                            "description": "Parameter 2"
                        }
                    },
                    "required": ["param1", "param2"]
                }
            },
            {
                "name": "method3",
                "description": "Run method 3",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            }
        ]
        
        self.send_response({"tools": tools})
    
    def handle_call_tool(self, params: Dict[str, Any]):
        """Handle tools/call request."""
        name = params.get("name")
        arguments = params.get("arguments", {})
        
        try:
            if name == "method1":
                param1 = arguments.get("param1")
                if not param1:
                    raise ValueError("param1 is required")
                result = self.bridge.method1(param1)
                self.send_response({"content": [{"type": "text", "text": json.dumps(result, indent=2)}]})
            
            elif name == "method2":
                param1 = arguments.get("param1")
                param2 = arguments.get("param2")
                if not param1 or param2 is None:
                    raise ValueError("param1 and param2 are required")
                result = self.bridge.method2(param1, param2)
                self.send_response({"content": [{"type": "text", "text": json.dumps(result, indent=2)}]})
            
            elif name == "method3":
                result = self.bridge.method3()
                self.send_response({"content": [{"type": "text", "text": result}]})
            
            else:
                raise ValueError(f"Unknown tool: {name}")
        
        except Exception as e:
            self.send_response(None, str(e))
    
    def run(self):
        """Main event loop for the MCP server."""
        print("mcpatlas MCP server ready...", file=sys.stderr)
        
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            
            try:
                request = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Bad JSON from host: {e}", file=sys.stderr)
                continue
            
            self.handle_request(request) 