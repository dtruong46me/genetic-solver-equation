class Utils:
    @staticmethod
    def text_handle(text, num):
        if 'x' in text:
            # num = float(input(">Enter value for x: "))
            return text.replace('x', str(num))
        else:
            return text
        

