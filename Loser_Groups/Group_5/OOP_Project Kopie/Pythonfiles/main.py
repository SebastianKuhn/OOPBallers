import ModelBasic as Model
import Controller as Controller
import View as View

c = Controller.Controller(Model.Model(), View.View())

if __name__ == '__main__':
    c.get_userloc()
