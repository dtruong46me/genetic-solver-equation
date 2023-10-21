class Utils:
    @staticmethod
    def text_handle(text, num = 1.0):
        if 'x' in text:
            # num = float(input(">Enter value for x: "))
            return text.replace('x', str(num))
        else:
            return text
        

