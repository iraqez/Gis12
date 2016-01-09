    # cert:'4951',
    # transportTypes:'train,autocar',
    # lat:'51.3278320',lng:'28.8133440',
    # elevatorAddress:'11104, вул. Леніна, буд. 72, м. Овруч, Житомирська обл.',
    # capacity:'14000',shortName:'Овруцька реалбаза хлібопродуктів, ВАТ',
    # fullName:'Відкрите акціонерне товариство \"Овруцька реалізаційна база хлібопродуктів\"',
    # propertyType:'Приватний',
    # propertyTypeCategory:'Інші',
    # loadCapacity:'200',
    # unloadCapacity:'380',
    # odhiRegion:'Житомирська'

from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor

data = """
_elevators['4951']={cert:'4951',transportTypes:'train,autocar',lat:'51.3278320',lng:'28.8133440',elevatorAddress:'11104, вул. Леніна, буд. 72, м. Овруч, Житомирська обл.',capacity:'14000',shortName:'Овруцька реалбаза хлібопродуктів, ВАТ',fullName:'Відкрите акціонерне товариство \"Овруцька реалізаційна база хлібопродуктів\"',propertyType:'Приватний',propertyTypeCategory:'Інші',loadCapacity:'200',unloadCapacity:'380',odhiRegion:'Житомирська'};
"""

parser = Parser()
tree = parser.parse(data)
fields = {getattr(node.left, 'value', ''): getattr(node.right, 'value', '')
          for node in nodevisitor.visit(tree)
          if isinstance(node, ast.Assign)}

print(fields)