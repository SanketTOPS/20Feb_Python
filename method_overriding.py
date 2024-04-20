class masterpage:
    def header(self): #original
        print("This is Header!")
    
    def fotter(self):
        print("This is fotter!")


class home(masterpage):
    def header(self): #xerox
        return super().header()
    
    def fotter(self):
        return super().fotter()
    
class about(masterpage):
    def header(self): #xerox
        return super().header()
    
    def fotter(self):
        return super().fotter()


h=home()
h.header()
h.fotter()

a=about()
a.header()
a.fotter()