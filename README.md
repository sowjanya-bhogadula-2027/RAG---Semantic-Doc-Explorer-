# 📄 RAG - Semantic Doc Explorer 

An **𝗲𝗻𝘁𝗲𝗿𝗽𝗿𝗶𝘀𝗲-𝗴𝗿𝗮𝗱𝗲** RAG application built with **𝗣𝘆𝘁𝗵𝗼𝗻** and **𝗦𝘁𝗿𝗲𝗮𝗺𝗹𝗶𝘁**. This tool allows users to upload multiple **𝗣𝗗𝗙 𝗱𝗼𝗰𝘂𝗺𝗲𝗻𝘁𝘀**, index them into a **𝗙𝗔𝗜𝗦𝗦 𝘃𝗲𝗰𝘁𝗼𝗿 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲**, and perform context-aware Q&A using **𝗟𝗮𝗻𝗴𝗖𝗵𝗮𝗶𝗻** and **𝗚𝗿𝗼𝗾 (𝗟𝗹𝗮𝗺𝗮 𝟯.𝟭)**.

---

### 🚀 **𝗞𝗲𝘆 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀**
* **𝗠𝘂𝗹𝘁𝗶-𝗣𝗗𝗙 𝗦𝘂𝗽𝗽𝗼𝗿𝘁**: Upload and process several research papers or reports simultaneously.
* **𝗜𝗻𝘀𝘁𝗮𝗻𝘁 𝗘𝗺𝗯𝗲𝗱𝗱𝗶𝗻𝗴𝘀**: Utilizes **𝗢𝗽𝗲𝗻𝗔𝗜 𝗘𝗺𝗯𝗲𝗱𝗱𝗶𝗻𝗴𝘀** for high-accuracy semantic search.
* **𝗛𝗶𝗴𝗵-𝗦𝗽𝗲𝗲𝗱 𝗜𝗻𝗳𝗲𝗿𝗲𝗻𝗰𝗲**: Powered by **𝗚𝗿𝗼𝗾** for near-instant response generation.
* **𝗜𝗻𝘁𝗲𝗿𝗮𝗰𝘁𝗶𝘃𝗲 𝗨𝗜**: A modern interface with **𝗿𝗲𝗮𝗹-𝘁𝗶𝗺𝗲 𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘀𝘁𝗮𝘁𝘂𝘀** updates.
* **𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗶𝘁𝗮𝘁𝗶𝗼𝗻𝘀**: Answers include an **𝗲𝘅𝗽𝗮𝗻𝗱𝗮𝗯𝗹𝗲 𝗿𝗲𝗳𝗲𝗿𝗲𝗻𝗰𝗲 𝘀𝗲𝗰𝘁𝗶𝗼𝗻** showing the document and page.

---

### 🛠️ **𝗧𝗲𝗰𝗵 𝗦𝘁𝗮𝗰𝗸**
* **𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲:** Python 3.9+
* **𝗟𝗟𝗠 𝗢𝗿𝗰𝗵𝗲𝘀𝘁𝗿𝗮𝘁𝗶𝗼𝗻:** LangChain, LangGraph
* **𝗜𝗻𝗳𝗲𝗿𝗲𝗻𝗰𝗲 𝗘𝗻𝗴𝗶𝗻𝗲:** Groq (Llama-3.1-8b-instant)
* **𝗩𝗲𝗰𝘁𝗼𝗿 𝗦𝘁𝗼𝗿𝗲:** FAISS (Facebook AI Similarity Search)
* **𝗙𝗿𝗼𝗻𝘁𝗲𝗻𝗱:** Streamlit

---

### ⚠️ **𝗜𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁 𝗡𝗼𝘁𝗲𝘀**
* **𝗔𝗣𝗜 𝗨𝘀𝗮𝗴𝗲**: Ensure you have an active **𝗢𝗽𝗲𝗻𝗔𝗜 𝗔𝗣𝗜 𝗞𝗲𝘆** for embeddings and a **𝗚𝗿𝗼𝗾 𝗔𝗣𝗜 𝗞𝗲𝘆** for the model.
* **𝗙𝗶𝗹𝗲 𝗟𝗶𝗺𝗶𝘁𝘀**: Large PDFs may take longer; it is recommended to start with **𝟱𝟬 𝗽𝗮𝗴𝗲𝘀 𝗼𝗿 𝗳𝗲𝘄𝗲𝗿** for testing.
