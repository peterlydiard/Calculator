'''
Created on 22 Jan 2022

@author: peter
'''

class Model:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.previous_value = ''
        self.value = ''
        self.operator = ''
    
    def calculate(self, caption):
        if caption == 'C':             # 'Clear' button
            self.previous_value = ''
            self.value = ''
            self.operator = ''
            
        elif caption =='+/-':
            # remove minus sign if present or add it it if not present
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
            
        elif caption == '%':
            pass
        
        elif caption == '=':
            self.value = str(self._evaluate())
        
        elif caption == '.':
            if not caption in self.value:
                self.value += '.'
            
        elif isinstance(caption, int): # check type of caption is integer
            self.value += str(caption) # append next digit to displayed value
            
        else:
            if self.value:             # check value string is not empty
                self.operator = caption
                self.previous_value = self.value
                self.value = ''
            
        return self.value
    
    def _evaluate(self):
        return eval(self.previous_value + self.operator + self.value)
    
    
