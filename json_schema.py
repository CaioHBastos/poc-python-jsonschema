def schema():
    return {
        "properties": {
            "nome": {
                "type": "string",
                "pattern": r"^\S.*$"
            },
            "idade": {
                "type": "number"
            },
            "contatos": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "celulares": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "ddd": {
                                        "type": "string",
                                        "pattern": r"^\S.*$"
                                    },
                                    "numero": {
                                        "type": "string",
                                        "pattern": r"^\S.*$"
                                    }
                                },
                                "required": [
                                    "ddd",
                                    "numero"
                                ]
                            }
                        },
                        "emails": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "valor": {
                                        "type": "string",
                                        "pattern": r"^\S.*$"
                                    }
                                },
                                "required": [
                                    "email"
                                ]
                            }
                        }
                    },
                    "required": [
                        "celulares",
                        "emails"
                    ]
                }
            },
            "endereco": {
                "properties": {
                    "logradouro": {
                        "type": "string",
                        "pattern": r"^\S.*$"
                    },
                    "estado": {
                        "properties": {
                            "nome": {
                                "type": "string",
                                "pattern": r"^\S.*$"
                            }
                        },
                        "required": [
                            "nome"
                        ]
                    }
                },
                "required": [
                    "logradouro",
                    "estado"
                ]
            }
        },
        "required": [
            "nome",
            "idade",
            "contatos"
        ],
        "additionalProperties": False
    }
