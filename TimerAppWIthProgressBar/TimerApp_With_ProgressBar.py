import streamlit as st
import time as t
from datetime import time
def calciSec(val):
    m,s,mm=val.split(":")
    timeInsec=int(m)*60+int(s)+int(mm)/1000
    return timeInsec
st.header("*Progress Bar :*")
val=st.time_input("Set Timer",value=time(0,0,0))
if str(val) =="00:00:00":
    st.write("Please set timer:")
else:
    perTime=calciSec(str(val))/100
    bar=st.progress(0)
    progress_status=st.empty()
    for i in range(100):
        progress_status.write(f"{i}%")
        bar.progress((i+1))
        t.sleep(perTime)
    

st.markdown("---")