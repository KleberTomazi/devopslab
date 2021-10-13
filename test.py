# -*- coding: utf-8 -*-  
from app import app                                                                                                                                                                                      
import unittest                                                                                                                                                                                          

class Test(unittest.TestCase):                                                                                                                                                                           

    def setUp(self):                                                                                                                                                                                     
        # cria uma instância do unittest, precisa do nome "setUp"                                                                                                                                        
        self.app = app.test_client()                                                                                                                                                                     

        # envia uma requisição GET para a URL                                                                                                                                                            
        self.result = self.app.get('/')                                                                                                                                                                  

    def test_requisicao(self):                                                                                                                                                                           
        # compara o status da requisição (precisa ser igual a 200)                                                                                                                                       
        self.assertEqual(self.result.status_code, 200)                                                                                                                                                   

    def test_conteudo(self):                                                                                                                                                                             
        # verifica o retorno do conteúdo da página                                                                                                                                                       
        self.assertEqual(self.result.data.decode('utf-8'), "Hello World")