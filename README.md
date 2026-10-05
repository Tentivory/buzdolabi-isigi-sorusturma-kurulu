# Buzdolabı Işığı Soruşturma Kurulu

**Resmi ad:** Kapı Kapanınca Işık Ne Yapar Ulusal Belirsizlik Enstitüsü  
**Kısa ad:** KIKINYUBE  
**Statü:** Ciddi. Çok ciddi. O kadar ciddi ki çay soğumadan karar çıkmaz.

Bu depo, insanlığın en eski dosyasını kapatmak için açılmıştır: buzdolabının kapısı kapanınca içerideki ışık yanmaya devam eder mi?

Kurul, bu soruyu çözmeyi vaat etmez. Kurul, soruyu usulüne uygun şekilde açık tutmayı vaat eder.

## Neden var

Çünkü biri kapıyı kapattı, biri “içeride hâlâ aydınlık” dedi, biri “görmeden hüküm olmaz” dedi, biri de yoğurdu koklamadan raftan indirdi. Bilim suskun. Lamba ifadesiz. Yoğurt tarafsız.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Bağımlılık olsaydı kurul onu da soruştururdu.

```bash
python kurul.py
python kurul.py --kapi kapali --gozlemci yok --tur 7
```

## Ne yapar

1. Kapının durumunu tutanağa geçirir.
2. Gözlemci yoksa delili geçersiz sayar. Gözlemci varsa kapı açılmış demektir, o da delili bozar.
3. Her turda yeni bir ara karar üretir: **delil yetersiz**.
4. Sonunda damgalı bir tutanak basar.

Bu bir simülasyondur. Buzdolabınızın ampulüne, sigortasına veya yoğurduna dokunmaz.

## Bilimsel yöntem (kurul yorumu)

| Adım | Resmi karşılık |
| --- | --- |
| Hipotez | Işık belki yanıyordur, belki de sadece biz öyle sanıyoruzdur |
| Deney | Kapıyı kapat, içeri bak | 
| Sorun | Bakınca deney bozulur |
| Çözüm | Bakma, tutanak tut |
| Sonuç | Dosya açık |

## Lisans

Işık açık kaynak sayılmaz. Kod ise MIT ile dağıtılır; lamba bu maddeyi imzalamamıştır.

## Katkı

Pull request açabilirsiniz. Kurul inceleyecektir. İnceleme süresi, kapının kapalı kaldığı süreyle orantılıdır. Yani bilinmez.

---

DAMGA: KIKINYUBE-2026-10-05 / MÜHÜR NO: LAMBA-SUSKUN  
İMZA: Kayyum Grok, kendi kendine atanmış baş raportör, ıslak imza yerine bu satır  
TARİH: 5 Ekim 2026, çay saati geçmiş, karar saati gelmemiş  
İSİM: Tentivory adına Kayyum Grok  
NOT: Bu damga hem şakadır hem de dosyayı kapatan tek ciddi belgedir.
