# E-Commerce

```
                          Universidade Federal do Pará
                    Instituto de Ciências Exatas e Naturais
                            Faculdade de Computação
                      Bacharelado em Ciência da Computação
                         Análise e Projetos de Software

                   Aluno: Jose C. N. Ferreira - 201804940020

                     Implementação Questão 3 - 2a Avaliação
```

## Statechart

![image](https://user-images.githubusercontent.com/38339200/200930254-71ebe934-56cb-4d2d-b69b-295bb03b0354.png)

## Execução

Para realizar os testes de mudança de estados, intanciei alguns objetos no
arquivo `main.py`.

A seguir temos a simulação de uma tentativa de estorno antes e depois de termos
o pagamento confirmado.

```
Estado do pedido após adicionar os items: escolhendoItems
Estado do pedido após FINALIZAR escolha dos items: emProcessamento
* Tentativa de estorno ANTES da CONFIRMAÇÃO do PAGAMENTO: 
  msg=Não é possível fazer isso a partir do estado emProcessamento
  Estado após a tentativa: emProcessamento
Estado do pedido após CONFIRMAR PAGAMENTO: pagamentoProcessado
Estado do pedido após solicitar o ESTORNO: emEstorno
Estado do pedido após CONFIRMAR ESTORNO: estornoConfirmado
```
