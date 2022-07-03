"""
Configuracoes iniciais para os testes
"""
import sys
import os

parent_folder = os.path.dirname(__file__)
base_project_folder = os.path.dirname(parent_folder)

if base_project_folder not in sys.path:
    sys.path.append(base_project_folder)
