import unittest
from app import create_app
from app.data.sqliteDAO import DAOManagerSqlite
from app.data.DAO import DAOManager
from app.data.models import User
from db import create_tables
import time

class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')        
        self.daoManager = DAOManagerSqlite()
        create_tables(self.daoManager.conecction.cursor(),'app/schema.sql')
        for i in range(10):
            user = User('Alvaro{}'.format(i),'Niño','16/12/19','alvaruto@gmail.com')
            self.daoManager.do(DAOManager.USER, DAOManager.CREATE,user)
        self.daoManager.commit()

    def test_user_creation(self):        
        
        # format date dd/mm/aa
        user = User('AlvaroCre','Niño','12-15-2019','alvaruto@gmail.com')
        res = self.daoManager.do(DAOManager.USER, DAOManager.CREATE,user)
        self.daoManager.commit()
        self.assertFalse(res)

        # format date dd/mm/aa
        user = User('AlvaroCre','Niño','fecha','alvaruto@gmail.com')
        res = self.daoManager.do(DAOManager.USER, DAOManager.CREATE,user)
        self.daoManager.commit()
        self.assertFalse(res)

        # no empty fields 
        user = User('','','16/12/19','')
        res = self.daoManager.do(DAOManager.USER, DAOManager.CREATE,user)
        self.daoManager.commit()
        self.assertFalse(res)

        # user equal None 
        user = None
        res = self.daoManager.do(DAOManager.USER, DAOManager.CREATE,user)
        self.daoManager.commit()
        self.assertFalse(res)

    
    def test_user_deletion(self):
        
        res = self.daoManager.do(DAOManager.USER,DAOManager.DELETE,1)        
        self.daoManager.commit()
        self.assertTrue(res)

        # delete a row where id out range
        res = self.daoManager.do(DAOManager.USER,DAOManager.DELETE,20)
        self.daoManager.commit()
        self.assertFalse(res)        

        # delete a row where id is not correctly
        res = self.daoManager.do(DAOManager.USER,DAOManager.DELETE,'borrar')
        self.daoManager.commit()
        self.assertFalse(res)

    def test_user_update(self):        

        # format date dd/mm/aa
        userUpdate = User('Alvaro2','Niño','12-15-2019','alvaruto@gmail.com')
        userUpdate.id = 1
        res = self.daoManager.do(DAOManager.USER, DAOManager.UPDATE,userUpdate)
        self.daoManager.commit()
        self.assertFalse(res)

        # format date dd/mm/aa
        userUpdate = User('Alvaro2','Niño','fecha','alvaruto@gmail.com')
        userUpdate.id = 1
        res = self.daoManager.do(DAOManager.USER, DAOManager.UPDATE,userUpdate)
        self.daoManager.commit()
        self.assertFalse(res)

        # no empty fields 
        userUpdate = User('','','16/12/19','')
        userUpdate.id = 1
        res = self.daoManager.do(DAOManager.USER, DAOManager.UPDATE,userUpdate)
        self.daoManager.commit()
        self.assertFalse(res)

        # user equal None 
        userUpdate = None        
        res = self.daoManager.do(DAOManager.USER, DAOManager.UPDATE,userUpdate)
        self.daoManager.commit()
        self.assertFalse(res)

        # update a row where id out range
        userUpdate = User('Alvaro2','Niño','6/12/19','alvaruto@gmail.com')
        userUpdate.id = 30
        res = self.daoManager.do(DAOManager.USER, DAOManager.UPDATE,userUpdate)
        self.daoManager.commit()
        self.assertFalse(res)

        # update a row where id is not correctly
        userUpdate = User('Alvaro2','Niño','6/12/19','alvaruto@gmail.com')
        userUpdate.id = 'no'
        res = self.daoManager.do(DAOManager.USER, DAOManager.UPDATE,userUpdate)
        self.daoManager.commit()
        self.assertFalse(res)


    def test_user_get_one(self):

        idUser = 1
        userGet = self.daoManager.do(DAOManager.USER, DAOManager.GET_ONE,idUser)
        self.assertIsInstance(userGet, User)

        # id no found
        idUser = 80
        userGet = self.daoManager.do(DAOManager.USER, DAOManager.GET_ONE,idUser)
        self.assertIsNone(userGet, User)        

        idUser = 'no'
        userGet = self.daoManager.do(DAOManager.USER, DAOManager.GET_ONE,idUser)
        self.assertIsNone(userGet, User)

    
    def test_user_get_all(self):        
           
        usersGet = self.daoManager.do(DAOManager.USER, DAOManager.GET_ALL)
        self.assertIsInstance(usersGet, list)

    
    
        

        


if __name__ == "__main__":
    unittest.main()