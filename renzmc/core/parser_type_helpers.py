from renzmc.core.token import TokenType
from renzmc.core.ast import TypeHint


def parse_type_hint_advanced(parser):
    type_parts = []
    token = parser.current_token

    type_component = parse_single_type_component(parser)
    if not type_component:
        return None

    type_parts.append(type_component)

    while parser.current_token.type in (TokenType.BIT_ATAU, TokenType.PIPE):
        parser.eat(parser.current_token.type)

        next_component = parse_single_type_component(parser)
        if next_component:
            type_parts.append(next_component)

    full_type_name = " | ".join(type_parts)

    return TypeHint(full_type_name, token)


def parse_single_type_component(parser):
    if parser.current_token.type != TokenType.IDENTIFIER:
        return None

    base_type = parser.current_token.value
    parser.eat(TokenType.IDENTIFIER)

    if parser.current_token.type in (TokenType.DAFTAR_AWAL, TokenType.LBRACKET):
        parser.eat(parser.current_token.type)

        generic_params = []

        if parser.current_token.type in (TokenType.IDENTIFIER, TokenType.TEKS, TokenType.STRING_CONST, TokenType.ANGKA, TokenType.INTEGER_CONST, TokenType.FLOAT_CONST):
            if parser.current_token.type in (TokenType.TEKS, TokenType.STRING_CONST):
                param_parts = [f'"{parser.current_token.value}"']
                parser.eat(parser.current_token.type)
                
                if parser.current_token.type in (TokenType.TITIK_DUA, TokenType.COLON):
                    param_parts.append(":")
                    parser.eat(parser.current_token.type)
                    if parser.current_token.type == TokenType.IDENTIFIER:
                        param_parts.append(parser.current_token.value)
                        parser.eat(TokenType.IDENTIFIER)
            elif parser.current_token.type in (TokenType.ANGKA, TokenType.INTEGER_CONST, TokenType.FLOAT_CONST):
                param_parts = [str(parser.current_token.value)]
                parser.eat(parser.current_token.type)
            else:
                param_parts = [parser.current_token.value]
                parser.eat(TokenType.IDENTIFIER)

                while parser.current_token.type in (TokenType.BIT_ATAU, TokenType.PIPE):
                    param_parts.append("|")
                    parser.eat(parser.current_token.type)
                    if parser.current_token.type == TokenType.IDENTIFIER:
                        param_parts.append(parser.current_token.value)
                        parser.eat(TokenType.IDENTIFIER)

            generic_params.append(" ".join(param_parts))

            while parser.current_token.type in (TokenType.KOMA, TokenType.COMMA):
                parser.eat(parser.current_token.type)
                if parser.current_token.type in (TokenType.TEKS, TokenType.STRING_CONST):
                    param_parts = [f'"{parser.current_token.value}"']
                    parser.eat(parser.current_token.type)
                    
                    if parser.current_token.type in (TokenType.TITIK_DUA, TokenType.COLON):
                        param_parts.append(":")
                        parser.eat(parser.current_token.type)
                        if parser.current_token.type == TokenType.IDENTIFIER:
                            param_parts.append(parser.current_token.value)
                            parser.eat(TokenType.IDENTIFIER)
                    
                    generic_params.append(" ".join(param_parts))
                elif parser.current_token.type in (TokenType.ANGKA, TokenType.INTEGER_CONST, TokenType.FLOAT_CONST):
                    param_parts = [str(parser.current_token.value)]
                    parser.eat(parser.current_token.type)
                    generic_params.append(" ".join(param_parts))
                elif parser.current_token.type == TokenType.IDENTIFIER:
                    param_parts = [parser.current_token.value]
                    parser.eat(TokenType.IDENTIFIER)

                    while parser.current_token.type in (TokenType.BIT_ATAU, TokenType.PIPE):
                        param_parts.append("|")
                        parser.eat(parser.current_token.type)
                        if parser.current_token.type == TokenType.IDENTIFIER:
                            param_parts.append(parser.current_token.value)
                            parser.eat(TokenType.IDENTIFIER)

                    generic_params.append(" ".join(param_parts))

        if parser.current_token.type in (TokenType.DAFTAR_AKHIR, TokenType.RBRACKET):
            parser.eat(parser.current_token.type)

        generic_str = ", ".join(generic_params)
        base_type = f"{base_type}[{generic_str}]"

    if hasattr(parser.current_token, 'type') and parser.current_token.type == TokenType.TANYA_MARK:
        parser.eat(TokenType.TANYA_MARK)
        base_type = f"{base_type}?"

    return base_type
