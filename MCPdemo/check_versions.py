import importlib.metadata
try:
    print(f"Core: {importlib.metadata.version('langchain-core')}")
except:
    print("Core: Not installed")
try:
    print(f"MCP: {importlib.metadata.version('langchain-mcp-adapters')}")
except:
    print("MCP: Not installed")
try:
    print(f"LangChain: {importlib.metadata.version('langchain')}")
except:
    print("LangChain: Not installed")
