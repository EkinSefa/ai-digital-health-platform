# AI-Digital-Health-Platform 🏥

**AI-Digital-Health-Platform**, yapay zeka teknolojisi ile desteklenen bir dijital sağlık platformudur. Bu proje, kullanıcıların mental sağlık durumlarını değerlendirmek ve sağlık verilerini analiz etmek için geliştirilmiştir. Ayrıca, hastalıklar hakkında bilgi edinme, eğitim videolarına erişim, doktorlarla iletişim kurma ve Türkiye'deki hastanelerin harita üzerinde görüntülenmesi gibi çeşitli sağlık hizmetlerini bir arada sunmaktadır.

## 🚀 Proje Özellikleri

### 1. **Yapay Zeka Destekli Zihinsel Sağlık Analizi**
   Kullanıcılar, duygu durumlarını metin olarak yazdıklarında, yapay zeka modeli tarafından analiz edilerek *Anxiety (Anksiyete), Bipolar, Depression (Depresyon), Normal, Personality Disorder (Kişilik Bozukluğu), Stress (Stres), Suicidal (İntihar Düşüncesi)* gibi sınıflarda hangi oranda yer aldıkları belirlenir. Bu özellik, kullanıcıların psikolojik durumlarını hızlı bir şekilde değerlendirmelerine yardımcı olur.

### 2. **Hastalıklar Bilgisi ve Arama**
   Platformda, kullanıcılar çeşitli hastalıkların detaylarına ulaşabilir. Her hastalık, kapsamlı açıklamalar, semptomlar ve tedavi seçenekleri ile birlikte sunulur. Ayrıca, hastalıklar hakkında daha fazla bilgi edinmek için Google aramaları yapabilirsiniz.

### 3. **Fizyoloji Bölümü**
   İnsan fizyolojisi hakkında temel bilgiler sunan bir bölüm bulunmaktadır. Bu bölümde, vücudun işleyişine dair temel bilgilere ulaşabilir ve detaylara göz atabilirsiniz. Fizyoloji ile ilgili çeşitli konularda eğitim almak isteyen kullanıcılar için faydalı bir kaynaktır.

### 4. **Eğitim Videoları**
   Sağlıkla ilgili çeşitli eğitim videoları, kullanıcıların kişisel sağlık bilgilerini artırmalarına yardımcı olmak için sunulmuştur. Kullanıcılar videoları izleyebilir, beğenebilir ve videolarla etkileşimde bulunabilirler. Eğitim içerikleri, sağlık hakkında daha derin bilgi edinmek isteyenler için oldukça faydalıdır.

### 5. **Doktorlar ve İletişim**
   Kullanıcılar, platform üzerinden çeşitli doktorların bilgilerine ulaşabilir. Doktorlar hakkında detaylı bilgilere, uzmanlık alanlarına ve iletişim bilgilerine erişim sağlanır. Ayrıca, kullanıcılar doktorlarla kolayca iletişim kurarak sorularını iletebilir ve randevu alabilirler.

### 6. **Hastaneler ve Harita Görüntüleme**
   Türkiye’deki hastanelerin konumları, Leaflet haritası üzerinde gösterilmektedir. Kullanıcılar, harita üzerinden hastaneleri görüntüleyebilir ve konumları hakkında bilgi sahibi olabilirler. Bu özellik, sağlık hizmetlerine erişimi kolaylaştırmak amacıyla eklenmiştir.

### 7. **Güncel Sağlık Haberleri**
   Platform, güncel sağlık haberlerini bir API üzerinden çekerek kullanıcılara sunar. Kullanıcılar, sağlık dünyasında olup biten gelişmeleri, tedavi yöntemlerini, hastalıklarla ilgili en son araştırmaları ve diğer sağlık haberlerini anlık olarak takip edebilirler.

## 📦 Teknolojiler

- **Backend**: Django (Python)
- **Frontend**: Bootstrap
- **Yapay Zeka**: Python (scikit-learn, TensorFlow/PyTorch vb.)
- **Harita**: Leaflet
- **API Entegrasyonları**: NewsAPI (Sağlık haberleri), Google Search API (Hastalık aramaları)

## Proje görselleri

<img src="https://github.com/user-attachments/assets/5585257d-d3cc-4cf8-bfbf-2f4a4e37a47a" width="450"/>
<img src="https://github.com/user-attachments/assets/94a2e7c7-07c1-40d0-bcad-c80f86372c76" width="450"/>
<img src="https://github.com/user-attachments/assets/3ea14190-e75a-4238-8a37-1f66a67d0b08" width="450"/>
<img src="https://github.com/user-attachments/assets/a795261e-e066-4a61-a9c3-fcbfd12ec4bb" width="450"/>
<img src="https://github.com/user-attachments/assets/6c8c275a-cae8-474a-a305-ca4869b0c48d" width="450"/>
<img src="https://github.com/user-attachments/assets/1e4c8b74-9823-466f-b367-457758bfe1a7" width="450"/>
<img src="https://github.com/user-attachments/assets/08faf224-e5ef-442e-aa91-668d58bef845" width="450"/>
<img src="https://github.com/user-attachments/assets/0312ec43-089e-4e3d-9430-21e826c372b4" width="450"/>

## 📋 Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. **Depoyu klonlayın**:
    ```bash
    git clone https://github.com/kullaniciAdi/AI-Digital-Health-Platform.git
    ```

2. **Gerekli paketleri yükleyin**:
    ```bash
    cd AI-Digital-Health-Platform
    pip install -r requirements.txt
    ```

3. **Veritabanını migrate edin**:
    ```bash
    python manage.py migrate
    ```

4. **Sunucuyu çalıştırın**:
    ```bash
    python manage.py runserver
    ```

5. Web tarayıcınızda `http://127.0.0.1:8000/` adresine giderek projeyi görüntüleyebilirsiniz.

## 🔧 Kullanım

- **Zihinsel Sağlık Testi**: "Hastalıklar" bölümünde, duygu durumunuzu yazın ve modelin sınıflandırmasını görün.
- **Hastalıklar Bilgisi**: Kategorilerdeki hastalıkları aratarak daha fazla bilgi edinin.
- **Eğitim Videoları**: Eğitim sekmesinden videoları izleyin ve beğenin.
- **Hastaneler Harita**: Türkiye'deki hastaneleri Leaflet haritasında görün.

## 🛠️ Geliştirici Rehberi

Proje üzerinde geliştirme yapmak istiyorsanız, aşağıdaki adımları takip edebilirsiniz:

1. Depoyu fork edin.
2. Geliştirme dalı (branch) oluşturun:
    ```bash
    git checkout -b yeniOzellik
    ```
3. Yaptığınız değişiklikleri commit edin:
    ```bash
    git commit -m "Yeni özellik ekledi"
    ```
4. Değişikliklerinizi ana repoya göndermek için:
    ```bash
    git push origin yeniOzellik
    ```

5. Pull request (PR) oluşturun.

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

Proje hakkında daha fazla bilgi veya katkı sağlamak için benimle iletişime geçebilirsiniz.
- **LİNKEDİN**: (https://www.linkedin.com/in/sefa-ekin-01130a273/).
