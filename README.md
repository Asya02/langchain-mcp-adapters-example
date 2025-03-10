# langchain-mcp-adapters-example

Simple MCP example for GigaChat

# Stdio mode (local)
## Configuration
1. Setup GigaChat credentials in .env 
2. Install requirements

## Run client and server (do not start server directly!)
```
uv run client.py
```

## Example output:
```
uv run client.py 
[03/10/25 15:00:47] INFO     Processing request of type ListToolsRequest       server.py:534
[03/10/25 15:00:51] INFO     Processing request of type CallToolRequest        server.py:534
[03/10/25 15:00:52] INFO     Processing request of type CallToolRequest        server.py:534
Результат выражения (3 + 5) умноженное на 12 равен 96.
```

# HTTP mode (SSE)
## Start server
```
uv run math_server.py sse
```

## Run client
```

```
