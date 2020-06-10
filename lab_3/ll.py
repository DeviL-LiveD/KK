from graphviz import Digraph
from grammar import Grammar, NoTermSymbol, TermSymbol


class TreeNode:
    def __init__(self, value: str, children: list = None):
        self.value = value
        self.children = children or []

    def clear_children(self):
        self.children = []

    def append_child(self, node: 'TreeNode'):
        self.children.append(node)

    def __str__(self):
        return f'{self.value} -> {self.children}'

    def __repr__(self):
        return str(self)


def build_tree(grammar: Grammar, current_symbol, string_to_read) -> (TreeNode, str):
    if isinstance(current_symbol, TermSymbol):  # Если терминал
        if current_symbol == grammar.eps_terminal:  # Если эпс-символ, то просто возвращаем его
            return TreeNode(current_symbol.symbol), string_to_read
        elif current_symbol.symbol == string_to_read[:len(current_symbol)]:  # Если в начале строки есть терминал, то ок
            return TreeNode(current_symbol.symbol), string_to_read[len(current_symbol):]
        else:  # Иначе ошибка, возвращаем None
            return None, string_to_read
    else:  # Если нетерминал
        for rule in grammar.rules[current_symbol]:  # По каждому правилу из грамматики по переданному нетерминалу
            new_str = string_to_read
            ret_node = TreeNode(current_symbol.symbol)
            for symbol in rule:  # По каждому символу в правиле
                symbol_children, new_str = build_tree(grammar, symbol, new_str)
                if symbol_children is None:  # Если хотя бы по одному символу ошибка -- правило не подходит
                    break
                ret_node.append_child(symbol_children)
            else:  # Если вышли без брейка, то нашли нужное поддерево
                return ret_node, new_str
    return None, string_to_read  # Если не нашлось верного правила, значит ошибка
