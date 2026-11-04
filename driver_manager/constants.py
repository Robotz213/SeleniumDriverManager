"""Forneca recursos do modulo constants."""

GET_INNER_TEXT = "return arguments[0].innerText"
"""Valor de configuração usado pelo fluxo de constants."""
COMMAND_SELECT2 = """
            const selector = $(arguments[0]);
            selector.val([arguments[1]]);
            selector.trigger("change");
            """
"""Comando de automação usado pelo fluxo de constants."""
