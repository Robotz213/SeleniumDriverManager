COMMAND_EXTRACT_XPATH = """
function getElementXPath(elt) {
    var path = "";
    for (; elt && elt.nodeType == 1; elt = elt.parentNode) {
        idx = Array.from(elt.parentNode.children).indexOf(elt) + 1;
        path = "/" + elt.tagName.toLowerCase() + "[" + idx + "]" + path;
    }
    return path;
}
return getElementXPath(arguments[0]);
"""
"""Comando de automação usado pelo fluxo de constants."""

GET_INNER_TEXT = "return arguments[0].innerText"
"""Valor de configuração usado pelo fluxo de constants."""
COMMAND_SELECT2 = """
            const selector = $(arguments[0]);
            selector.val([arguments[1]]);
            selector.trigger("change");
            """
"""Comando de automação usado pelo fluxo de constants."""
