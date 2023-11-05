from core.nodes import *
from core.values import *
import math
import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

CONST = {"e": math.e}
class Interpreter:
    def __init__(self):
        pass  

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)
        
    def visit_NumberNode(self, node):
        return Number(node.value)
    
    def visit_EConstNode(self,node):
        return Number(math.e)
    
    def visit_PiNode(self, node):
        return Number(math.pi)
    
    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            return Number(float("infinity"))
        
    def visit_PlusNode(self, node):
        return self.visit(node.node)
    
    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)

    def visit_PowerNode(self, node):
        base = self.visit(node.node_a).value
        pow = self.visit(node.node_b).value
        if int(pow) - pow != 0:
            if int(1/pow) - 1/pow == 0:
                if (1/pow) % 2 != 0:
                    if base < 0:
                        return Number(-((-base)**pow))
                    else:
                        return Number(base**pow)
                else:
                    if base < 0:
                        raise Exception("Error: Runtime math error")
                    else:
                        return Number(base**pow)
                        
            else:
                if base < 0:
                    raise Exception("Error: Runtime math error")
                else:
                    return Number(base**pow)
        else:
            return Number(base ** pow)
        
    def visit_AbsoluteValueNode(self, node):
        check_num = self.visit(node.node).value

        if (check_num < 0):
            return Number(check_num*(-1))
        else:
            return Number(check_num)
    
    def visit_SqrtNode(self, node):
        val = self.visit(node.node).value
        if val >= 0:
            return Number(math.sqrt(val))
        else:
            raise Exception("Error: x must be a non-negative value")

    def visit_SinNode(self,node):
        val = self.visit(node.node).value
        return Number(math.sin(val))
    
    def visit_CosNode(self,node):
        val = self.visit(node.node).value
        return Number(math.sin((math.pi/2) - val))
    
    def visit_TanNode(self,node):
        val = self.visit(node.node).value
        return Number(math.tan(val))
    
    def visit_CotNode(self,node):
        val = self.visit(node.node).value
        return Number(1 / math.tan(val))
    
    def visit_ArcSinNode(self, node):
        val = self.visit(node.node).value
        return Number(math.asin(val))
    
    def visit_ArcCosNode(self, node):
        val = self.visit(node.node).value
        return Number(math.acos(val))
    
    def visit_ArcTanNode(self, node):
        val = self.visit(node.node).value
        return Number(math.atan(val))
    
    def visit_ArcCotNode(self, node):
        val = self.visit(node.node).value
        return Number((math.pi)/2 - math.atan(val))
    
    def visit_ExpNode(self,node):
        val = self.visit(node.node).value
        return Number(math.exp(val))
    
    def visit_LnNode(self,node):
        val = self.visit(node.node).value
        return Number(math.log(val)) if val > 0 else float("infinity")
    
    def visit_CommaNode(self, node):
        val1 = self.visit(node.node_a).value
        val2 = self.visit(node.node_b).value
        return (val1, val2)
    
    def visit_LogNode(self,node):
        try:
            arg = self.visit_CommaNode(node.node)
            if arg[1] <=0 or arg[1] == 1:
                raise Exception("Error: Invalid base")
            else:
                if arg[0] <= 0:
                    # raise Exception("Error: x must be a positive number")
                    return Number(float("infinity"))
                return Number(math.log(arg[0], arg[1]))
        except AttributeError:
            val = self.visit(node.node).value
            if val <= 0:
                # raise Exception("Error: x must be a positive number")
                return Number(float("infinity"))
            return Number(math.log(val, 10))

    def visit_FactNode(self,node):
        val = self.visit(node.node).value
        return Number(math.factorial(int(val)))

    def visit_NrootNode(self, node):
        try:
            arg = self.visit_CommaNode(node.node)
            val = arg[0]
            root = arg[1] 
               
            if root <= 0:
                return float('infinity')
            else:
                if root % 2 == 0:
                    if val < 0:
                        raise Exception("Error: Even n-th root only accept non-negative value")
                    return Number(val ** (1/root))

                elif root % 2 == 1:
                    if val < 0:
                        return Number(-((-val)**(1/root)))
                    else:
                        return Number(val ** (1/root))		
                else:
                    raise Exception("Error: n must be a positive integer number")
                
        except AttributeError:
            val = self.visit(node.node).value
            if val < 0:
                raise Exception("Error: Even n-th root only accept non-negative value")
            return Number(math.sqrt(val)) 
