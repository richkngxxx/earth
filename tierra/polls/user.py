from aca va lo de la base de datos import archivo de usuarios de la base

class Users:
    def _init_(self):
        pass


    def isAuthenticated(self, userName, password):
        usuarios = readFileSheet("Usuario")
        flag= False
        for usuario in usuarios.itertuples(index=False):
            usuario_db = usuario[1]
            pass_db = usuario[2]
            if  usuario_db == str(userName) and password == str(pass_db):
                flag = True
                break
        return flag