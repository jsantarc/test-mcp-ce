import uuid
import requests



SERVER_URL = "http://localhost:8080/mcp"

BASE_HEADERS = {
    "Accept": "application/json, text/event-stream",
    "Content-Type": "application/json",
}


def send_json_rpc(method:str, params:dict, headers:dict)->requests.Response:
    #this method 
    body = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),
        "method": method,
        "params": params,
    }

    return requests.post(SERVER_URL, json=body, headers=headers)


def test_simple_mcp():

    headers = BASE_HEADERS.copy()
    print("▶ Starting MCP test\n")

    # ---- 1) Initialize MCP session ----
    init_body = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),
        "method": "initialize",
        "params": {
            "protocolVersion": "2025-06-18",
            "capabilities": {"tools": {}},
            "clientInfo": {"name": "simple-test", "version": "1.0"},
        },
    }
    print("→ Sending initialize request...")
    init_resp = send_json_rpc(method="initialize", params=init_body["params"], headers=BASE_HEADERS )
    
    print("  HTTP status:", init_resp.status_code)

    # Print raw response text (server info is inside this JSON)
    print("  Initialize raw response:")
    print(init_resp.text)

    # Grab session ID from headers
    session_id = init_resp.headers.get("mcp-session-id")
    print("  MCP Session ID:", session_id)

    if not session_id:
        print("\n❌ No MCP session ID returned, cannot continue.")
        return

    # ---- 2) Call the get_unique_fact tool ----
    tool_body = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),
        "method": "tools/call",
        "params": {
            "name": "get_unique_fact",
            "arguments": {},
        },
    }

    headers["Mcp-Session-Id"] = session_id

    print("\n→ Calling get_unique_fact tool...")
    tool_resp = send_json_rpc(method="tools/call", params=tool_body["params"], headers=headers)
    print("  HTTP status:", tool_resp.status_code)
    print("  Raw response:")
    print(tool_resp.text)

    # Very simple extraction of the fact text from the response
    marker = '"text":"'
    if marker in tool_resp.text:
        fact = tool_resp.text.split(marker, 1)[1].split('"', 1)[0]
        print("\n🎉 Fact returned from server:")
        print(f"  {fact}")
    else:
        print("\n⚠ Could not find a 'text' field in the response.")


if __name__ == "__main__":
    test_simple_mcp()
