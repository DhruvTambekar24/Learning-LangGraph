import json

nb_path = r"c:/Users/dtamb/OneDrive/Desktop/AgenticLangraph/3-Debugging/debugging.ipynb"

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell.get("id") == "b644990c":
        # Found the target cell
        source = cell["source"]
        # We replace the whole source list to be safe and exact
        new_source = [
            "## Stategraph\n",
            "from langgraph.graph import StateGraph,START,END\n",
            "from langgraph.prebuilt import ToolNode\n",
            "from langgraph.prebuilt import tools_condition\n",
            "\n",
            "## Node definition\n",
            "def call_llm_model(state:State):\n",
            "    return {\"messages\":[llm_with_tools.invoke(state['messages'])]}\n",
            "## Grpah\n",
            "builder=StateGraph(State)\n",
            "builder.add_node(\"tool_calling_llm\",call_llm_model)\n",
            "tools=[add]\n",
            "builder.add_node(\"tools\",ToolNode(tools))\n",
            "\n",
            "## Add Edges\n",
            "builder.add_edge(START, \"tool_calling_llm\")\n",
            "builder.add_conditional_edges(\n",
            "    \"tool_calling_llm\",\n",
            "    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools\n",
            "    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END\n",
            "    tools_condition\n",
            ")\n",
            "builder.add_edge(\"tools\",\"tool_calling_llm\")\n",
            "\n",
            "## compile the graph\n",
            "graph=builder.compile()\n",
            "\n",
            "from IPython.display import Image, display\n",
            "display(Image(graph.get_graph().draw_mermaid_png()))"
        ]
        cell["source"] = new_source
        print("Updated cell b644990c")
        break

with open(nb_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)
    print("Saved debugging.ipynb")
