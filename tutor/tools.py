from langchain_core.tools import tool
from typing import Annotated
from langchain_experimental.utilities import  PythonREPL
repl=PythonREPL()

@tool
def python_tool(
        code: Annotated[str,"the python code to execute to generate your output."]
):
    """Use this to execute python code. If you want to see the output of a values,
    You should print it out with the print() statement. This is visible to the user."""

    try:
        res=repl.run(code)
    except BaseException as e:
        return f"failed to execute. Error: {repr(e)}"
    return f"successfully executed:\n\n ```python\n{code}\n```Stdout:{res}"