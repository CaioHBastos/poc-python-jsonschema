import re

from jsonschema import exceptions
from jsonschema.validators import Draft202012Validator

import json_request
import json_schema
import mensagem_personalizada


def validator():
    padrao_regex = r"'([^']*)'"
    errors = []

    results = Draft202012Validator(json_schema.schema()).iter_errors(json_request.request())
    for result in sorted(results, key=exceptions.relevance):
        path = re.search(padrao_regex, result.message)

        path_absoluto = result.json_path + '.' + path.group(1)
        mensagem = mensagem_personalizada.get_mensage(path_absoluto, result.message)

        errors.append({
            "campo": path_absoluto,
            "mensagem": mensagem
        })

    print(errors)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    validator()
