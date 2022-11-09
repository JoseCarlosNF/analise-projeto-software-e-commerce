from cliente import Cliente


class escolhendoItems:
    def __init__(self) -> None:
        # Restreamento de preferencias.
        pass


class emProcessamento:
    def __init__(self) -> None:
        # Comunicação com outros sistemas externos de processamento de
        # pagamentos.
        pass


class pagamentoProcessado:
    def __init__(self) -> None:
        # Confirmação de pagamento. Registro da compra nas bases de dados.
        pass


class pagamentoRecusado:
    def __init__(self) -> None:
        # Registra a recusa do pagamento por parte da operadora nas bases de
        # dados.
        pass


class cancelado:
    def __init__(self) -> None:
        # Registra um canecelamento nas bases de dados internas.
        pass


class emEstorno:
    def __init__(self) -> None:
        # Solicita estorno aos sistemas de processamento de processamentos.
        pass


class estornoConfirmado:
    def __init__(self) -> None:
        # Registra nas bases de dados a confirmação do estorno.
        pass


class entregaEmAndamento:
    def __init__(self) -> None:
        # Registra solicitação de coleta do produto no sistema das
        # transportadoras.
        pass


class emRetorno:
    def __init__(self) -> None:
        # Registra a solicitação da logistica reversa no sistema das
        # transportadoras.
        pass


class entregue:
    def __init__(self) -> None:
        # Confirma o recebimento do produto.
        pass


class feedbackCliente:
    def __init__(self) -> None:
        # Solicita ao cliente feedback sobre o produto.
        pass


class Pedido:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.items = []
        self.state = escolhendoItems()

    def adicionar_item(self, item) -> None:
        self.items.append(item)

    def remover_item(self, index_item) -> None:
        self.items.pop(index_item)

    def finalizar(self):
        self.state = emProcessamento()

    def confirmarPagamento(self):
        self.state = pagamentoProcessado()

    def emcaminharTransporte(self):
        if type(self.state) == pagamentoProcessado:
            self.state = entregaEmAndamento()
        else:
            print(f'Não é possível mudar do estado {__name__} para {self.state.__class__.__name__}')

    def estornar(self):
        if type(self.state) == pagamentoProcessado:
            self.state = emEstorno()
        else:
            print(f'Não é possível fazer isso a partir do estado {self.state.__class__.__name__}')

    def confirmarEstorno(self):
        self.state = estornoConfirmado()

    def cancelar(self):
        if type(self.state) in (pagamentoRecusado, estornoConfirmado):
            self.state = cancelado()
        else:
            print(f'Não é possível fazer isso a partir do estado {self.state.__class__.__name__}')

    def logisticaReversa(self):
        if type(self.state) in (entregaEmAndamento, entregue):
            self.state = emRetorno()
        else:
            print(f'Não é possível fazer isso a partir do estado {self.state.__class__.__name__}')

    def feedback(self):
        if type(self.state) in (entregue):
            self.state = feedbackCliente()
        else:
            print(f'Não é possível fazer isso a partir do estado {self.state}')
