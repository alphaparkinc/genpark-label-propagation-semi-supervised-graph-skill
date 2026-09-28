import sys
import json
from client import LabelPropagationClassifier

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-label-propagation-semi-supervised-graph-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "propagate_graph_labels",
                        "description": "Propagate seed labels through graph edges using semi-supervised majority voting",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "adjacency": {"type": "object"},
                                "seed_labels": {"type": "object"},
                                "max_iterations": {"type": "integer", "default": 20}
                            },
                            "required": ["adjacency", "seed_labels"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "propagate_graph_labels":
            adj = args.get("adjacency", {})
            seeds = args.get("seed_labels", {})
            m = args.get("max_iterations", 20)
            res = LabelPropagationClassifier.propagate(adj, seeds, max_iter=m)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps({"labels": res})}]
                }
            }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
