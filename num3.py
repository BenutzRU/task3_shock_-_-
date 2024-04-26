# Типизация функций

from typing import Union, List, Dict

def simple_function(search: str, status: bool, *args: Union[int, str], **kwargs: Dict[str, str]) -> Union[List[int], str]:

  result: List[int] = []
  output: str = ""

  if search == "args":
    if status:
      for arg in args:
        if isinstance(arg, int):
          result.append(arg)
    else:
      for arg in args:
        output += f" {arg}"
  elif search == "kwargs":
    for key, value in kwargs.items():
      output += f" key: {key}, value: {value}; "
  else:
    print("Error.")

  if result:
    return result
  else:
    return output

search_type = "args"
search_status = True
search_args = (1, 2, 3, "string")
search_kwargs = {"key1": "value1", "key2": 2}

result = simple_function(search_type, search_status, *search_args, **search_kwargs)

if isinstance(result, list):
  print(f"num list: {result}")
else:
  print(f"string: {result}")
