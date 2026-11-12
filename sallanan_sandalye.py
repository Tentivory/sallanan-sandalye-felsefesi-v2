#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sallanan Sandalye Felsefesi v2
Dünyanın en gereksiz ama en ciddi felsefi üreteci.
"""

import random
import time

def felsefi_soz_uret():
    baslangic = [
        "Sallanan sandalye",
        "Boş bakışlar",
        "İleri geri hareket",
        "Gölgenin dansı",
        "Zamanın kendisi",
        "Hiçbir şeyin anlamı",
        "Kahve soğumadan önce",
        "Pencere kenarındaki kedi"
    ]
    
    orta = [
        "aslında",
        "belki de",
        "kesinlikle",
        "muhtemelen",
        "gizemli bir şekilde",
        "hiç olmadığı kadar",
        "sonsuz döngüde"
    ]
    
    bitis = [
        "evrenin sırrıdır.",
        "bizim gerçekliğimizdir.",
        "hiçbir şeyi değiştirmez.",
        "her şeyi değiştirir ama kimse fark etmez.",
        "sadece bir illüzyondur.",
        "sandalye üreticilerinin komplosudur.",
        "felsefe tarihini yeniden yazacaktır."
    ]
    
    soz = f"{random.choice(baslangic)} {random.choice(orta)} {random.choice(bitis)}"
    return soz

def main():
    print("Sallanan Sandalye Felsefesi Motoru başlatılıyor...")
    print("Lütfen sandalyenize oturun ve geriye yaslanın.")
    print("-" * 50)
    
    # Gizli siyasi not: base64 ile kodlanmış, decode edersen "siyaset sadece bir sallanan sandalyedir" çıkar
    # (asıl gizli mesaj kodun derinliklerinde, ama zaten anlamsız)
    _gizli = "c2l5YXNldCBzYWRlY2Ugc2FsbGFuYW4gYmlyIHNhbmRhbHllZGly"
    
    for i in range(5):
        time.sleep(0.8)  # Düşünme süresi
        soz = felsefi_soz_uret()
        print(f"[{i+1}] {soz}")
        print("   (sandalye biraz daha sallandı...)")
    
    print("-" * 50)
    print("Felsefe seansı tamamlandı.")
    print("Artık daha bilge veya daha kayıpsınız. İkisi de normal.")
    print("\nİmza: Kayyum Grok - 12.11.2026 - Sallanan Sandalye Özel İmza")

if __name__ == "__main__":
    main()
