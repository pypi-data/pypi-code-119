# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 22:17:28 2016

@author: HZJ
"""
import uuid
import scipy.sparse as spr
from structengpy.csys import Cartisian

class Element(object):
    def __init__(self,nodes:list,dim:int,dof:int,csys:Cartisian,name:str=None):
        self.__name=uuid.uuid1() if name==None else str(name)
        self.__hid=None #hidden id
        
        self.__dim = dim #dimension
        self.__dof = dof #degree of freedom

        self.__nodes=nodes #list of nodes

        self.__D=None
        self.__L=None

        self.__mass=None
        
        # self._T=None
        # self._Ke=None
        # self._Me=None
        # self._re=None

        self.__local_csys=csys
               
    @property
    def name(self):
        return self.__name
        
    @property
    def hid(self):
        return self.__hid
    @hid.setter
    def hid(self,hid:int):
        assert type(hid)==int
        self.__hid=hid
        
    @property
    def nodes(self):
        return self.__nodes
    
    @property
    def node_count(self):
        return len(self.__nodes)
    
    # @property  
    # def Ke(self):
    #     """
    #     integrate to get stiffness matrix.
    #     """
    #     return self._Ke
        
    # @property  
    # def Me(self):
    #     """
    #     integrate to get stiffness matrix.
    #     """
    #     return self._Me
        
    # @property
    # def re(self):
    #     return self._re
    
    # @re.setter
    # def re(self,force):
    #     if len(force)!=self._dof:
    #         raise ValueError('element nodal force must be a 12 array')
    #     self.__re=np.array(force).reshape((self._dof,1))

    @property
    def local_csys(self):
        return self.__local_csys

    @property
    def mass(self):
        raise NotImplementedError()

    @property
    def transform_matrix(self):
        raise NotImplementedError()

if __name__=="__main__":
    csys=Cartisian((0,0,0),(1,0,0),(0,1,0))
    ele=Element([],2,6,csys)
    print(ele.transform_matrix)
