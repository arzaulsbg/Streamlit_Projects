import streamlit as st
st.sidebar.write("# AzaanTech")
# st.sidebar.markdown("---")
# st.sidebar.markdown("[Home]()")
# st.sidebar.markdown("[Contact]()")
# st.sidebar.markdown("[Offer]()")
# st.sidebar.markdown("[Sign In]()")
# form=st.sidebar.form("form-1")
# form.text_input("home")
# form.form_submit_button("submit")

import matplotlib.pyplot as plt
import numpy as np
# line graph
x = np.linspace(1,10,100)
# y = [2, 4, 6, 8, 10]
line_graph=plt.figure()
plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
plt.plot(x, np.cos(x))
plt.plot(x,np.sin(x),"--")

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.legend()



# bar graph
bar_graph=plt.figure()
plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
x = ['A', 'B', 'C', 'D']
y = [5, 7, 3, 8]
plt.bar(x, y, color='orange')
plt.title('Bar Graph')

# 3️⃣ Scatter Plot
scatter_plot=plt.figure()
x = [5, 7, 8, 10, 12]
y = [1, 4, 6, 7, 9]
plt.scatter(x, y, color='green')
plt.title('Scatter Plot')
# 4️⃣ Histogram
histogram=plt.figure()
data = [5, 10, 10, 15, 20, 25, 20, 30, 35, 40, 45, 50]
plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title('Histogram')
# 5️⃣ Pie Chart
pieChart=plt.figure()
labels = ['Apple', 'Banana', 'Cherry', 'Mango']
sizes = [30, 25, 25, 20]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['red', 'yellow', 'pink', 'orange'])
plt.title('Pie Chart')

plt.tight_layout()

opt=st.sidebar.radio("Select any Graph",options=["line graph","bar graph","scatter plot","Histogram","Pie Chart"])
if opt=="line graph":
    st.write(line_graph)
elif opt =="bar graph":
    st.write(bar_graph)

elif opt =="scatter plot":
    st.write(scatter_plot)
elif opt=="Histogram":
    st.write(histogram)
elif opt=="Pie Chart":
    st.write(pieChart)


