import re


def get_mensage(path_absoluto: str, mensagem: str):
    campo = get_mensagem_campo(path_absoluto)

    if mensagem.__contains__("is a required property"):
        return mensagem.split("'")[2].replace("is a required property", campo + "é uma propriedade obrigatória.")

    if mensagem.__contains__("does not match '^\\\\S.*$'"):
        return mensagem.replace("'", "").replace("'", "").strip()\
            .replace("does not match ^\\\\S.*$", campo + "informado não pode estar branco ou vazio.")


def get_mensagem_campo(campo: str):
    padrao = r'\[(.*?)\]'
    indices = re.findall(padrao, campo)

    if campo.__contains__("$.nome"):
        return "O 'nome' "
    elif "$.idade" == campo:
        return "A 'idade' "
    elif "$.contatos[" + indices[0] + "].celulares[" + indices[1] + "].ddd" == campo:
        return "O 'ddd' do contato "
    elif "$.contatos[" + indices[0] + "].celulares[" + indices[1] + "].numero" == campo:
        return "O 'numero' do contato "
