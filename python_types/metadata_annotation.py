from typing import Annotated

def greeting(name: Annotated[str, "this is where you enter your name"]) -> str:
    return f"Hello {name}"


print(greeting("Mai"))