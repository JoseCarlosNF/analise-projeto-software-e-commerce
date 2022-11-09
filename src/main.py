from cliente import Cliente
from pedido import Pedido

if __name__ == '__main__':
    cliente = Cliente('Jubiscleison', '123.456.789-99')
    pedido = Pedido(cliente)

    pedido.adicionar_item('maquina de lavar')
    pedido.adicionar_item('notebook')
    pedido.adicionar_item('geladeira')
    print('Estado do pedido após adicionar os items: ', end='')
    print(pedido.state.__class__.__qualname__)

    pedido.finalizar()
    print('Estado do pedido após FINALIZAR escolha dos items: ', end='')
    print(pedido.state.__class__.__qualname__)

    print('* Tentativa de estorno ANTES da CONFIRMAÇÃO do PAGAMENTO: ', end='\n  msg=')
    pedido.estornar()
    print('  Estado após a tentativa: ', end='')
    print(pedido.state.__class__.__qualname__)

    pedido.confirmarPagamento()
    print('Estado do pedido após CONFIRMAR PAGAMENTO: ', end='')
    print(pedido.state.__class__.__qualname__)

    pedido.estornar()
    print('Estado do pedido após solicitar o ESTORNO: ', end='')
    print(pedido.state.__class__.__qualname__)

    pedido.confirmarEstorno()
    print('Estado do pedido após CONFIRMAR ESTORNO: ', end='')
    print(pedido.state.__class__.__qualname__)
    
