import streamlit as st 
import requests
import subprocess


st.title("AGENTIC BASED POWERPOINT GENETETOR")

prompt = st.text_area("please write the details of how you want to create the ppt")


if st.button("Generate PPT"):
    if prompt:
        response = requests.post(url="https://shrutikakkapade.app.n8n.cloud/webhook-test/660956d8-966d-4cda-9a3d-93bd524c384e", json={"prompt":prompt})

        if response.status_code==200:
            st.write("Success")
            
            with open("app1.py", "w") as file:
                file.write(response.json()["output"].strip("```python"))
            
            subprocess.run(["python","app1.py"])

with open(r"D:\Innomatics Research lab\Powerpoint_presentation_streamlitn8n\generated_presentation.pptx", "rb") as f:
    st.download_button(
                        label="📥 Download Presentation",
                        data=f,
                        file_name="presentation.pptx"
                    )