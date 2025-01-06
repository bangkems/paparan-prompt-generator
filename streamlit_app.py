import streamlit as st
import random
import webbrowser

def generate_title_prompt(topik, audiens, durasi):
    return f"""Tolong buatkan judul presentasi yang menarik dan profesional untuk presentasi berdurasi {durasi} menit tentang {topik}. 
Target audiens presentasi adalah {audiens}. 
Judul harus menarik tetapi tetap profesional dan dengan jelas mengkomunikasikan nilai utama presentasi.
Berikan 3 alternatif judul dalam Bahasa Indonesia."""

def generate_outline_prompt(topik, audiens, durasi, gaya):
    return f"""Tolong buatkan outline/kerangka presentasi yang detail untuk presentasi berdurasi {durasi} menit tentang {topik}.
Target audiens: {audiens}
Gaya presentasi: {gaya}
Harap sertakan:
1. Pembukaan yang menarik
2. 3-5 bagian utama dengan poin-poin kunci
3. Contoh atau studi kasus yang menarik
4. Elemen interaktif atau poin-poin diskusi
5. Kesimpulan yang kuat
Format outline dengan struktur hierarki yang jelas dan perkiraan alokasi waktu untuk setiap bagian.
Seluruh outline dalam Bahasa Indonesia."""

def open_chatgpt_with_prompt(prompt):
    # URL encode the prompt and create the ChatGPT URL
    encoded_prompt = prompt.replace('\n', '%0A')
    chatgpt_url = f"https://chat.openai.com/chat?prompt={encoded_prompt}"
    return chatgpt_url

def main():
    st.set_page_config(page_title="Generator Prompt Presentasi AI", page_icon="📊")
    
    st.title("📊 Generator Prompt Presentasi AI")
    st.write("Buat prompt profesional untuk membuat presentasi dengan bantuan AI")
    
    # Bagian Input
    st.header("Detail Presentasi")
    
    topik = st.text_input("Apa topik presentasi Anda?", 
                         placeholder="contoh: Tren Digital Marketing 2024")
    
    audiens = st.selectbox(
        "Siapa target audiens Anda?",
        ["Pemula", "Menengah", "Mahir", "Audiens Campuran", "Eksekutif", 
         "Pelajar/Mahasiswa", "Profesional", "Ahli Teknis"]
    )
    
    durasi = st.slider("Durasi Presentasi (menit)", 
                      min_value=5, max_value=120, value=30, step=5)
    
    gaya_presentasi = {
        "Profesional": "Formal dan terstruktur dengan informasi detail",
        "Interaktif": "Melibatkan partisipasi audiens dan diskusi",
        "Berbasis Cerita": "Menggunakan narasi dan studi kasus",
        "Fokus Visual": "Berfokus pada gambar, diagram, dan teks minimal",
        "Gaya Workshop": "Pembelajaran hands-on dengan latihan praktis"
    }
    
    gaya = st.selectbox(
        "Gaya presentasi apa yang Anda inginkan?",
        list(gaya_presentasi.keys())
    )
    
    st.write(f"Deskripsi gaya: *{gaya_presentasi[gaya]}*")
    
    # Generate Prompts
    if st.button("Buat Prompt"):
        if not topik:
            st.error("Mohon masukkan topik presentasi!")
            return
            
        st.header("Prompt yang Dihasilkan")
        
        # Title Prompt
        st.subheader("🎯 Prompt Pembuatan Judul")
        title_prompt = generate_title_prompt(topik, audiens, durasi)
        st.code(title_prompt, language="text")
        
        col1, col2 = st.columns(2)
        
        # Copy button for title prompt
        if col1.button("Salin Prompt Judul", key="copy_title"):
            st.toast("Prompt judul disalin ke clipboard!")
            
        # ChatGPT button for title prompt
        if col2.button("Buka dengan ChatGPT", key="chatgpt_title"):
            chatgpt_url = open_chatgpt_with_prompt(title_prompt)
            st.markdown(f'<a href="{chatgpt_url}" target="_blank">Klik untuk membuka di ChatGPT</a>', unsafe_allow_html=True)
            
        st.markdown("---")
        
        # Outline Prompt
        st.subheader("📝 Prompt Pembuatan Outline")
        outline_prompt = generate_outline_prompt(topik, audiens, durasi, gaya)
        st.code(outline_prompt, language="text")
        
        col3, col4 = st.columns(2)
        
        # Copy button for outline prompt
        if col3.button("Salin Prompt Outline", key="copy_outline"):
            st.toast("Prompt outline disalin ke clipboard!")
            
        # ChatGPT button for outline prompt
        if col4.button("Buka dengan ChatGPT", key="chatgpt_outline"):
            chatgpt_url = open_chatgpt_with_prompt(outline_prompt)
            st.markdown(f'<a href="{chatgpt_url}" target="_blank">Klik untuk membuka di ChatGPT</a>', unsafe_allow_html=True)
        
        # Tips
        st.markdown("---")
        st.header("💡 Tips Penggunaan Prompt")
        st.write("""
        1. Gunakan prompt ini dengan alat AI seperti ChatGPT, Claude, atau model bahasa lainnya
        2. Anda bisa memodifikasi prompt yang dihasilkan sesuai kebutuhan
        3. Jika hasil pertama kurang sesuai, coba generate ulang dengan parameter yang sedikit berbeda
        4. Perhatikan konteks presentasi dan sesuaikan gayanya
        5. Pastikan untuk memeriksa dan menyesuaikan hasil generate AI agar sesuai dengan kebutuhan Anda
        """)

if __name__ == "__main__":
    main()
