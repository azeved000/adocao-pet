class AlgumaCoisa:
    def __enter__(self):
        print("Estou entrando")
    
    def __exit__(self, exc_type, exc_value, traceback):
        # exc_type: O tipo da exceção que ocorreu (ex: ValueError, TypeError)
        # Se nenhuma exceção ocorreu, será None
        
        # exc_value: A instância da exceção com a mensagem de erro
        # Contém os detalhes específicos do erro que aconteceu
        
        # traceback: O objeto traceback que contém informações sobre onde o erro ocorreu
        # Inclui o caminho de execução (stack trace) até o ponto do erro
        
        print("Estou saindo")
    
with AlgumaCoisa() as coisa:
    print("Estou no meio")