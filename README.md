# Discord Kanal ve Rol Botu

Bu bot, Discord sunucunuzdaki **tüm kanalları ve rolleri** silmenizi sağlayan basit ve etkili bir araçtır. Üyeleri veya botları sunucudan atmaz (kicklemez), sadece kanalları ve rolleri temizler.

⚠️ **DİKKAT:** Bu botun kullanımı geri döndürülemez sonuçlar doğurur. Lütfen dikkatli kullanın!

## 🚀 Özellikler

- Tüm metin ve ses kanallarını siler.
- Sunucudaki tüm rolleri siler (Yetkisinin yettiği kadarıyla).
- Üyelere veya botlara dokunmaz.
- Yanlış kullanımları önlemek için onay sistemi (✅) içerir.

## 🛠️ Kurulum

1. **Python Yükleyin:** Sisteminizde [Python 3.8+](https://www.python.org/downloads/) yüklü olduğundan emin olun.
2. **Depoyu Klonlayın:**
   ```bash
   git clone <repo_url>
   cd <repo_directory>
   ```
3. **Gerekli Modülleri Kurun:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Token Ayarı:** 
   Proje dizininde bir `.env` dosyası oluşturun ve Discord Bot Token'ınızı ekleyin:
   ```env
   DISCORD_TOKEN=sizin_bot_tokeniniz_buraya
   ```

## 💻 Kullanım

Botu başlatmak için komut satırında aşağıdaki komutu çalıştırın:

```bash
python bot.py
```

**Komut:** `!kanallarıverolleri sil`

- Bu komutu yalnızca **Yönetici (Administrator)** yetkisine sahip kullanıcılar kullanabilir.
- Komut çalıştırıldıktan sonra sizden bir ✅ emojisi ile onay istenecektir. 30 saniye içinde onaylanmazsa işlem iptal edilir.
- İşlem başladığında komutun yazıldığı kanal haricindeki tüm kanallar ve yetkinin yettiği tüm roller silinir.

## 📌 Notlar

- `@everyone` rolü Discord kısıtlamaları gereği silinemez.
- Botun diğer rolleri silebilmesi için, botun rolünün silinecek rollerden daha üst sırada olması gerekir.
- Botun çalışabilmesi için `Kanalları Yönet` ve `Rolleri Yönet` (veya `Yönetici`) yetkilerine sahip olması şarttır.

---
*Bu proje açık kaynaklıdır. Geliştirmelere ve katkılara açıktır.*
