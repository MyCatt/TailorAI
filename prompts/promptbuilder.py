import copy
from prompts import structures


def build_prompt(key, **kwargs):
    prompt = copy.deepcopy(structures.prompts[key])
    for i in range(len(prompt)):
        for arg in kwargs:
            prompt[i]['content'] = prompt[i]['content'].replace("{" + arg + "}", f"{kwargs[arg]}")

    return prompt
