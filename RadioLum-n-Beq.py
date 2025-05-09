#Version-01
import streamlit as st
import pandas as pd 
C_1 = 6.266e+18   # in CGS unit  
C_3 = 2.368e-03   # in CGS unit  
pi=3.14159 
me=9.1093837e-28    #CGS 
c=2.99792458e+10    #CGS

def E(gamma):
  E = (gamma*me*c**2) 
  return E
def Beq(V,alpha,z,D_LMpc,nuo_MHz, So_nuo_Jy,gamma_1, gamma_2):  
  
  Term_1 = (16*pi/V) 
  Term_2 = C_1**(1-alpha)/C_3  
  D_Lcm= D_LMpc*3.0857e24  # In CGS 
  nuo=nuo_MHz*1e+6 
  So_nuo=So_nuo_Jy*1e-23  # in CGS (erg/s/cm^2/Hz )  
  Term_3 = (4*pi*D_Lcm**2)/(1-2*alpha)  
  Term_4 = (So_nuo*nuo**alpha)/((1+z)**(1-alpha))   
  E_1 = E(gamma_1)
  E_2 = E(gamma_2)   
  Term_5=E_2**(1-2*alpha) - E_1**(1-2*alpha)
  Beq= (Term_1*Term_2*Term_3*Term_4*Term_5)**(1/(3+alpha))   
  return Beq 
#st.write(Beq(1e70, 0.75, 0.02, 100, 600, 10, 10, 1e+5))    
# Taking inputs
inputs=st.text_input("Give V, alpha, z, D_LMpc, nuo_MHz, So_nuo_Jy, gamma_1, gamma_2")  # it will create a slot in streamlit for taking inouts 
if inputs:
  values=inputs.split(",") 
  V, alpha, z, D_LMpc, nuo_MHz, So_nuo_Jy, gamma_1, gamma_2 = map(float, values) 
  st.info(f"Beq = {Beq(V, alpha, z, D_LMpc, nuo_MHz, So_nuo_Jy, gamma_1, gamma_2)} Gauss") 
  st.write(f"Beq = {Beq(V, alpha, z, D_LMpc, nuo_MHz, So_nuo_Jy, gamma_1, gamma_2)} Gauss") 
  st.write(Beq(V, alpha, z, D_LMpc, nuo_MHz, So_nuo_Jy, gamma_1, gamma_2))
else:
  "Enter the values of the parameters"
  
#st.write("output") 
