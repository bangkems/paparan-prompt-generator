import streamlit as st
import random
from urllib.parse import quote

# Add custom CSS to hide the GitHub icon
hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

def generate_prompt(topik, audiens, durasi, gaya):
    return f"""[JUDUL]
Tolong buatkan judul presentasi yang menarik dan profesional untuk presentasi berdurasi {durasi} menit tentang {topik}. 
Target audiens presentasi adalah {audiens}. 
Judul harus menarik tetapi tetap profesional dan dengan jelas mengkomunikasikan nilai utama presentasi.
Berikan 3 alternatif judul dalam Bahasa Indonesia.

[OUTLINE]
Tolong buatkan outline/kerangka presentasi yang detail dengan alokasi waktu untuk presentasi berdurasi {durasi} menit tentang {topik}.
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

def create_chatgpt_link(prompt):
    encoded_prompt = quote(prompt)
    return f'<a href="https://chat.openai.com/?prompt={encoded_prompt}" target="_blank" style="display: inline-block; background-color: #10a37f; color: white; padding: 0.5rem 1rem; text-decoration: none; border-radius: 0.375rem; font-weight: 500;">💬 Buka di ChatGPT</a>'

def main():
    st.set_page_config(page_title="AI Prompt Generator untuk Presentasi", page_icon="🧑‍💻")
    
    st.title("🧑‍💻 AI Prompt Generator untuk Presentasi")
    st.write("Bantu buat AI Prompt untuk Menghasilkan Ide Judul dan Outline Presentasi")
    
    # Bagian Input
    st.header("Detail Presentasi")
    
    topik = st.text_input("Apa topik presentasi Anda?", 
                         placeholder="contoh: Tren Digital Marketing 2025")
    
    audiens = st.selectbox(
        "Siapa target audiens Anda?",
        ["Pemula", "Menengah", "Mahir", "Audiens Campuran", "Eksekutif", 
         "Pelajar/Mahasiswa", "Profesional", "Ahli Teknis"]
    )
    
    durasi = st.slider("Durasi Presentasi (menit)", 
                      min_value=5, max_value=120, value=30, step=5)
    
    gaya_presentasi = {
        "Profesional": "Formal dan terstruktur dengan informasi detail",
        "Interaktif": "Dominan melibatkan partisipasi audiens dengan diskusi dua arah",
        "Berbasis Cerita": "Menggunakan narasi dan studi kasus",
        "Fokus Visual": "Berfokus pada gambar, diagram, dan teks yang sedikit",
        "Gaya Workshop": "Terdapat hands-on pada sesi presentasi"
    }
    
    gaya = st.selectbox(
        "Gaya presentasi apa yang Anda inginkan?",
        list(gaya_presentasi.keys())
    )
    
    st.write(f"Deskripsi gaya: *{gaya_presentasi[gaya]}*")
    
    # Buat Prompt
    if st.button("Buat Prompt"):
        if not topik:
            st.error("Mohon masukkan topik presentasi!")
            return
            
        st.header("Prompt yang Dihasilkan")
        
        # Menampilkan hasil prompt
        combined_prompt = generate_prompt(topik, audiens, durasi, gaya)
        
        # Prompt Format Markdown
        st.markdown("### 📝 Prompt Presentasi")
        st.code(combined_prompt, language="text")
        
        # Shortcut ke ChatGPT
        st.markdown(create_chatgpt_link(combined_prompt), unsafe_allow_html=True)
        
        
        # Tips
        st.markdown("---")
        st.header("💡 Tips Penggunaan Prompt")
        st.write("""
        1. Gunakan prompt ini di tools AI favorit Anda seperti ChatGPT, Claude, dsb
        2. Boleh memodifikasi prompt yang dihasilkan sesuai kebutuhan
        3. Jika hasil pertama kurang sesuai, coba generate ulang dengan parameter yang sedikit berbeda
        4. Perhatikan konteks presentasi dan sesuaikan gayanya
        5. Pastikan untuk memeriksa dan menyesuaikan hasil yang ditampilkan tools AI agar sesuai dengan kebutuhan Anda
        6. Selamat mencoba! 👨‍🍳
        """)

if __name__ == "__main__":
    main()
