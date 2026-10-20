# 🎬 MASTER KURGU YÖNETMENİ MANİFESTOSU & YARATICI PRODÜKSİYON BEYNİ
> **Bu belge, "Şirket Meselesi" ve "Sistem Açığı Kanks" kanallarının kurgu DNA'sını, yaratıcı vizyonunu ve slayt gösterisi kurguyu yerle bir eden Hollywood / Vox seviyesi dinamik montaj standartlarını kalıcı olarak belirler.**

---

## 👁️ BÖLÜM 1: FELSEFE — "SLAYT GÖSTERİSİ DEĞİL, YAŞAYAN BİR SİNEMA"
YouTube edutainment izleyicisi bir resmin yavaşça büyümesini (Lineer 100 -> 110 scale) 1.5 saniyeden fazla izlemez; tıklar ve videodan çıkar. 
Gerçek bir edutainment videosu **statik resimlerin ardı ardına gelmesi değildir; birbiriyle konuşan katmanların, fırlayan objelerin ve ritmik kamera dansının bütünüdür.**

---

## ⚡ BÖLÜM 2: 5 TEMEL YARATICI KURGU SÜTUNU

### 1. Kamera Fiziği & Sinematik Smoothness (Lineer Harekete Son)
* **Smooth Easing (Bezier Eğrileri):** Kamera hareketleri robotik bir makine gibi düz çizgide gitmez. Hızlı başlar, duracağı noktaya doğru sinematik bir ivmeyle süzülür (`Ease-Out / Exponential Decay`).
* **Whip Pan (Kamçı Geçişi):** İki sahne veya iki zıt duygu arasında kamera aniden bir tarafa hızlıca fırlar (blur / whoosh), yeni sahne ters yönden süzülerek yerine oturur.
* **Micro-Shake (Darbe Titremesi):** Cümledeki şok edici bir fiyasko veya çöküş anında kamera sadece zoomlamaz; anlık 3 karelik (0.1 sn) mikro bir sarsıntı geçirir (etki hissi).
* **Paralaks Hissi (Derinlik):** Arka plan hafifçe sağa kayarken, üstteki obje sola doğru süzülür. Bu iki zıt hareket 2D çizime 3D derinlik katar.

---

### 2. Katmanlı Obje & Çıkartma Fiziği (Floating Cutout Props — Track V2/V3)
* **Objelerin Boşa Gitmesi Yasaktır:** Senaryoda bir nesneden bahsedildiğinde (New Coke kutusu, gizli formül kasası, para destesi, protesto pankartı, borsa grafiği):
  - Bu obje arka planın içine gömülü kalmaz!
  - İzole bir **şeffaf PNG çıkartma (sticker)** olarak V2 veya V3 katmanından sahneye dalar!
* **The Bounce (Fiziksel Yaylanma Formülü):**
  - `0. ms:` Scale %0, Hafif 12° açı (Anticipation) + `Bubble Pop / Snap SFX`.
  - `80. ms:` Scale %125 (Overshoot — Gözü yakalayan aşırı büyüme).
  - `160. ms:` Scale %95 (Tepki ve geri sekme).
  - `240. ms:` Scale %100 (Yerine oturma).
* **Floating (Havada Süzülme):** Obje yerine oturduktan sonra kaskatı donmaz; sahne boyunca hafifçe havada süzülür (-2° ile +2° arasında nefes alır).

---

### 3. Kinetik Tipografi: Bilinçaltı Darbe Kelimeleri ("Punch Words")
* **Bütün Cümleyi Basmak Yasaktır:** İzleyici altyazı okumaya gelmedi. Ekrana yalnızca ve yalnızca **izleyicinin dikkatini mıhlayacak kelimeler** basılır:
  - **Sayılar & İstatistikler:** Her zaman devasa, altın sarısı veya neon yeşil (`8.000 ÇAĞRI`, `1985`, `$4 MİLYAR`).
  - **Dramatik Fiiller & Reaksiyonlar:** Konturlu kalın tipografi (`PANİKLEDİLER!`, `FİYASKO`, `KOVULDU`, `HACKLENDİ`).
  - **İronik Etiketler:** Tırnak içinde, açılı ve kırmızı damga efektiyle (`"MÜKEMMEL HATA"`).
* **Kinetik Animasyon:** Kelime tam seslendirmenin o heceyi patlattığı milisaniyede `Scale %80 -> %125 -> %100` yaylanmasıyla belirir, 0.8 saniye sonra hafifçe yukarı doğru uçarak veya sönerek kaybolur.

---

### 4. Karakter Mimik & Durum Kurgusu (Reaction Cuts)
* **Karakter Sabit Bir Heykel Değildir:**
  - Karakter konuşurken normal durur.
  - Alaycı cümle geldiğinde ("Fun fact: no"): Karakterin kafasının üstünde anlık dev bir kırmızı `X` damgası veya soru işareti (`?`) patlar.
  - Şirket battığında: Karakterin gözleri spiral döner veya masaya kapanır.
  - Sistem açığı bulunduğunda: Glitch'in yüzü `>_>` mimik değiştirir ve gözlerinde yeşil `$` yanar.

---

### 5. Ses Tasarımı (Soundscapes & Foley — Gizli Yönetmen)
Her görsel hareketin ve duygunun akustik bir karşılığı vardır:
| Görsel Eylem | Ses Efekti (SFX) | Karakter / Ton |
| :--- | :--- | :--- |
| **Punch-In Zoom Snap** | Bass Thud / Sub Drop / Kick | Tok, sarsıcı, derin |
| **Obje / Çıkartma Fırlaması** | Bubble Pop / Snap / Su Sesi | Tatmin edici, organik |
| **Whip Pan / Hızlı Sahne Kesimi** | Deep Whoosh / Digital Glitch Sweep | Rüzgar, süzülme |
| **İroni / Şaşkınlık / Hata** | Blip / Komik Tık / Record Stop | Sarkastik, kuru mizah |
| **Rakam / Veri Akışı** | Retro Keyboard / Ticker / Para Sayma | Hızlı, ritmik |

---

## 📂 BÖLÜM 3: DOSYA VE SİSTEM MİMARİSİ (NEREDE NE VAR?)

1. **`capcut-editing-automation/`:**
   - `build_capcut.py`: 2-saniye beat-split kurgu motorunu, akıllı karakter kadraj tespitini (`ink_map`) ve dinamik scale/pan hesaplayıcısını içerir.
   - `preview.py`: PositionX, PositionY ve ScaleX keyframe'lerini CapCut ile birebir aynı hesaplayan görsel QA önizleme motorudur.
   - `make_plan.py`: Yeni videolar için otomatik olarak hyper-dynamic retention bayraklarını üretir.
2. **`auto_capcut_editor.py` (Kök Dizinde):**
   - Tek tıkla CapCut'ın açık olup olmadığını denetleyen, draft dosyalarını yedekleyen, kurguyu inşa edip doğrudan CapCut projesine enjekte eden ana orkestrasyon scriptidir.
3. **`sirket_meselesi_masterprompt.txt` & `sistem_acigi_masterprompt.txt`:**
   - Her iki kanalın üretim zincirinin sonuna **AŞAMA 5** olarak bu dinamik kurgu motoru ve kurgu kuralları kalıcı olarak kazınmıştır.
4. **`KURGU_YONETMENI_MANIFESTOSU.md` (Bu Belge):**
   - Sistemin yaratıcı manifestosu olarak kök dizinde daimi rehber olarak yaşar.
