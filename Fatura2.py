produtos=list()
class Fatura():
    def __init__(self, pro):
        self.numero=pro._numero
        self.nome=pro._nome
        self.quantidade=pro._quantidade
        self.valor=pro._valor

    def Total(self):
        return pro._quantidade*pro._valor
    
    def Mostrar(produtos):
        op=int(input("numero do produto: "))
        for i in produtos:
            if op==i[0]:
                print("===============================")
                print(f'numero.....:{i[0]}') 
                print(f'nome.......:{i[1]}')
                print(f'quantidade.:{i[2]}')
                print(f'valor......:{i[3]}')
                print("==========Fatura===========")
                print(f'Fatura.....:{fat.Total()}')
            else: 
                print("Numero não cadastrado")
    
    def MostrarTodos(produtos):
        s=0
        for i in produtos:
            print("===============================")
            print(f'numero.....:{i[0]}') 
            print(f'nome.......:{i[1]}')
            print(f'quantidade.:{i[2]}')
            print(f'valor......:{i[3]}')
            print("==========Fatura===========")
            print(f'Fatura.....:{i[2]*i[3]}')
            s+=i[2]*i[3]
            print("==========Fatura Total===========")
            print(f'Fatura Total: {s}')
            print()

class Produto():
    def __init__(self, num, nome, quant, valor):
        self.numero=num
        self.nome=nome
        self.quantidade=quant
        self.valor=valor
        produtos.append(list((self._numero, self._nome, self._quantidade, self._valor)))

    @property
    def numero(self):
        return self._numero
    
    @property
    def nome(self):
        return self._nome

    @property
    def quantidade(self):
        return self._quantidade
    
    @property
    def valor(self):
        return self._valor
    
    @numero.setter
    def numero(self, valor):
        if isinstance(valor, int):
            self._numero=valor

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str):
            self._nome=valor

    @quantidade.setter
    def quantidade(self, valor):
        if isinstance(valor, int):
            self._quantidade=valor

    @valor.setter
    def valor(self, valor):
        if valor<0:
            valor=0
        if isinstance(valor, float):
            self._valor=valor


while True: 
    print( 
        """
        ---------- Menu Principal ----------
        1.Adicionar Produto 
        2.Mudar Valores
        3.Mostrar Item
        4.Mostrar Todos
        0.Sair
        ------------------------------------
        """)
     
    op=int(input("Opção: "))
    if op==1:
        print('============ADICIONANDO=================')
        num=int(input("numero: "))
        nome=str(input("Nome do Produto: "))
        quant=int(input("Quantidade:"))
        if quant<0:
            quant=0
        valor=float(input("Valor unitário: "))
        if valor <0:
            valor=0
        pro=Produto(num, nome, quant, valor)
        fat=Fatura(pro)

    if op==2:
        print('============MUDANDO=================')
        opc=int(input("Numero do Produto a ser mudado: "))
        for i in produtos:
            if opc==i[0]:
                produtos.remove(i[:])
                pro._numero=int(input("Numero novo: "))
                pro._nome=str(input("Nome novo: "))
                pro._quantidade=int(input("Quantidade nova: "))
                pro._valor=float(input("Valor novo: "))
                produtos.append(list((pro._numero, pro._nome, pro._quantidade, pro._valor)))
    
    if op==3:
        Fatura.Mostrar(produtos)

    if op==4: 
        Fatura.MostrarTodos(produtos)
    if op==0:
        break

