import json
from django.shortcuts import redirect, render
from django.http import Http404





def fizyoloji(request):
    systems = [
    {
    "title": "İskelet Sistemi",
    "description": "İskelet sistemi, vücuttaki tüm kemikleri ve eklemleri içerir.",
    "detail_description": 
    "İskelet Sisteminin Temel Görevleri:"
    "İskelet sistemi, vücuda fiziksel destek sağlayarak dik durmamıza yardımcı olur."
    "İç organları dış darbelerden korur ve güvenli bir şekilde sarar."
    "Kaslar için bir tutunma yüzeyi oluşturarak hareketi mümkün kılar."
    "Kemik iliği, vücut için gerekli olan kan hücrelerini üretir."
    "Vücuttaki kalsiyum ve fosfor gibi minerallerin depo edilmesini sağlar."
    "İskelet Sistemi Yapısı ve Bölümleri:"
    "İnsan iskeleti, eksenel iskelet ve ekstremite iskeleti olmak üzere iki ana bölümden oluşur."
    "Eksenel iskelet; kafatası, omurga ve göğüs kafesi gibi merkezi yapıları içerir."
    "Ekstremite iskeleti; kollar, bacaklar, omuz ve kalça kemiklerini kapsar."
    "Kıkırdak dokular, kemik uçlarını kaplayarak sürtünmeyi azaltır ve esneklik sağlar."
    "Bağ dokular, kemikleri birbirine bağlayarak eklemlerde stabilite sağlar."
    "İskelet Sistemi ve Hareket:"
    "Kasların kemiklere bağlı olması sayesinde vücut çeşitli yönlerde hareket edebilir."
    "Eklemler, kemikler arasındaki bağlantıyı sağlar ve hareket aralığını belirler."
    "Bazı eklemler tamamen hareketsizken, bazıları çok yönlü hareket edebilir."
    "İskelet Sistemi Sağlığı:"
    "Sağlıklı bir iskelet sistemi için yeterli kalsiyum ve D vitamini alımı çok önemlidir."
    "Düzenli fiziksel aktivite, kemik yoğunluğunu artırarak kırılma riskini azaltır."
    "İleri yaşlarda osteoporoz gibi hastalıklar iskelet sağlığını tehdit edebilir."
    "Sigara ve aşırı alkol kullanımı, kemik sağlığını olumsuz etkiler."
    "İskelet Sistemi Hastalıkları:"
    "Osteoporoz, kemik yoğunluğunun azalmasıyla ortaya çıkan yaygın bir hastalıktır."
    "Artrit, eklemlerde iltihaplanmaya neden olarak ağrı ve hareket kısıtlılığı oluşturur."
    "Kemik kırıkları ve çıkıkları, travma sonucu sık görülen iskelet sistemi yaralanmalarıdır."
    "İskelet Sisteminin Önemi:"
    "İskelet sistemi sadece hareketi sağlamakla kalmaz, aynı zamanda hayati organların korunmasında da kritik bir rol oynar."
    "Sağlıklı bir iskelet sistemi, genel yaşam kalitesinin korunmasında temel taşlardan biridir.",
    "image_url": "https://innerbody.imgix.net/skeletal_system.png?auto=format"
},
    {
    "title": "Kas Sistemi",
    "description": "Kas sistemi, insan vücudunun hareketinden sorumludur.",
    "detail_description":
    "Kas Sistemi Görevleri:"
    "Kaslar, vücut hareketlerini sağlamak için kasılıp gevşer."
    "Kas sistemi, iskelet sistemiyle birlikte çalışarak hareketi mümkün kılar."
    "İskelet kasları, kemiklere bağlı olarak istemli hareketi sağlar."
    "Düz kaslar, iç organların çalışmasına destek olur."
    "Kalp kası, kanın tüm vücuda pompalanmasını sağlar."
    "Kaslar, vücut ısısının korunmasında önemli rol oynar."
    "Enerji harcaması sırasında kaslar, ısı üretir."
    "Kasların yapısı aktin ve miyozin filamentlerinden oluşur."
    "İstemli ve istemsiz çalışan kaslar vardır."
    "Kas sistemi; sinir sistemiyle koordineli çalışır."
    "Egzersiz, kasların güçlenmesine ve dayanıklılığının artmasına yardımcı olur."
    "Kas hücreleri enerji ihtiyaçlarını glikojen depolarıyla karşılar."
    "Yaş ilerledikçe kas kütlesi ve gücü azalabilir."
    "Kas yaralanmaları ve kas hastalıkları kas fonksiyonlarını etkileyebilir."
    "Kas spazmları, kramp gibi rahatsızlıklara yol açabilir."
    "Protein tüketimi kas sağlığı için oldukça önemlidir."
    "Düzenli egzersiz ve dengeli beslenme kas sisteminin sağlıklı kalmasına yardımcı olur.",
    "image_url": "https://innerbody.imgix.net/muscular_system.png?auto=format"
},
    {
    "title": "Kardiyovasküler Sistem",
    "description": "Kardiyovasküler sistem; kalp, kan damarları ve kan damarlarının taşıdığı yaklaşık 5 litre kandan oluşur.",
    "detail_description":
    "Kardiyovasküler Sistem Yapısı:"
    "Kalp, kardiyovasküler sistemin merkezinde yer alır."
    "Kalp dört odacıktan oluşur: iki kulakçık ve iki karıncık."
    "Atardamarlar, kanı kalpten organlara taşır."
    "Toplardamarlar, oksijensiz kanı kalbe geri getirir."
    "Kılcal damarlar, hücrelere oksijen ve besin taşır."
    "Bu sistem, vücut hücrelerinin ihtiyaç duyduğu oksijeni sağlar."
    "Atık maddelerin ve karbondioksitin uzaklaştırılmasına yardımcı olur."
    "Kalp, kasılma ve gevşeme hareketleriyle kanı pompalar."
    "Kan basıncı, kanın damar duvarlarına uyguladığı kuvvettir."
    "Sağlıklı bir kalp ve damar yapısı, yaşam kalitesi için kritiktir."
    "Ateroskleroz gibi hastalıklar damarların daralmasına yol açabilir."
    "Hipertansiyon kalp ve damar sağlığını olumsuz etkiler."
    "Egzersiz yapmak kalp kasının güçlenmesini sağlar."
    "Sigara ve kötü beslenme kalp hastalıkları riskini artırır."
    "Dengeli beslenme ve düzenli kontrol kardiyovasküler sağlığı korur."
    "Kardiyovasküler sistem, vücuttaki sıcaklık dengesini de korur.",
    "image_url": "https://innerbody.imgix.net/cardiovascular_system.png?auto=format"
},
    {
    "title": "Sindirim Sistemi",
    "description": "Sindirim sistemi, yiyecekleri enerjiye ve temel besin maddelerine dönüştürmek için birlikte çalışan organlardan oluşur.",
    "detail_description":
    "Sindirim Sisteminin Görevleri:"
    "Sindirim sistemi, vücuda alınan besinleri parçalayarak kullanılabilir forma getirir."
    "Sindirimin ilk adımı ağızda çiğneme ve tükürük salgısıyla başlar."
    "Yemek borusu, besinleri mideye taşır."
    "Mide, güçlü asitler ve enzimlerle besinleri kimyasal olarak parçalar."
    "İnce bağırsakta, besinlerin büyük bir kısmı emilir."
    "Pankreas, karaciğer ve safra kesesi sindirime destek olan salgılar üretir."
    "Karaciğer, safra üretimi yaparak yağların sindirimine yardımcı olur."
    "İnce bağırsakta emilen besinler kan dolaşımına katılır."
    "Kalın bağırsak, su ve minerallerin emilmesini sağlar."
    "Sindirim sistemi, atık maddeleri dışkı yoluyla vücuttan uzaklaştırır."
    "Bağırsak florası, sindirimi destekleyen yararlı bakteriler içerir."
    "Sağlıklı bir sindirim sistemi, güçlü bir bağışıklık sistemi ile ilişkilidir."
    "Kabızlık, ishal gibi problemler sindirim sistemi bozukluklarıdır."
    "Beslenme alışkanlıkları sindirim sisteminin sağlığını doğrudan etkiler."
    "Düzenli lif tüketimi bağırsak sağlığı için önemlidir."
    "Sindirim sistemi hastalıkları arasında ülser, reflü ve Crohn hastalığı bulunur.",
    "image_url": "https://innerbody.imgix.net/digestive_system.png?auto=format"
},
    {
    "title": "Endokrin Sistem",
    "description": "Endokrin sistem, vücuttaki tüm bezleri ve bu bezlerin ürettiği hormonları içerir.",
    "detail_description":
    "Endokrin Sistem İşlevleri:"
    "Endokrin sistem, hormonlar aracılığıyla vücudun birçok işlevini düzenler."
    "Hipofiz bezi, birçok diğer bezin çalışmasını kontrol eden ana bezdir."
    "Tiroid bezi, metabolizma hızını belirleyen hormonlar salgılar."
    "Pankreas, insülin ve glukagon salgılayarak kan şekeri düzeyini düzenler."
    "Adrenal bezler, stres yanıtı için adrenalin ve kortizol üretir."
    "Üreme hormonları, büyüme ve gelişmeyi etkiler."
    "Hormonlar, kana salınarak hedef organlara taşınır."
    "Endokrin sistem, sinir sistemiyle birlikte çalışarak homeostazı sağlar."
    "Büyüme hormonu, çocuklukta büyümenin temel faktörüdür."
    "Hormon dengesizlikleri sağlık sorunlarına yol açabilir."
    "Şeker hastalığı (diyabet), endokrin sistem bozukluklarından biridir."
    "Hashimoto hastalığı, tiroid bezinin işlev bozukluğudur."
    "Endokrin tümörler, hormon üretimini etkileyebilir."
    "Yaşam boyu hormonal değişimler normaldir."
    "Stres ve yaşam tarzı endokrin sağlığı etkileyebilir."
    "Sağlıklı beslenme ve düzenli egzersiz hormon dengesi için önemlidir.",
    "image_url": "https://innerbody.imgix.net/endocrine_system.png?auto=format"
},
    {
    "title": "Sinir Sistemi",
    "description": "Sinir sistemi; beyin, omurilik, duyu organları ve bu organları vücudun geri kalanıyla bağlayan tüm sinirlerden oluşur.",
    "detail_description":
    "Sinir Sistemi İşlevleri:"
    "Sinir sistemi, vücudun kontrol ve iletişim merkezidir."
    "Merkezi sinir sistemi (MSS), beyin ve omurilikten oluşur."
    "Çevresel sinir sistemi (ÇSS), sinir ağıyla vücudun her noktasına ulaşır."
    "Duyu organları, çevreden gelen bilgileri sinir sistemi aracılığıyla iletir."
    "Beyin, düşünme, hafıza, öğrenme ve duyguların merkezidir."
    "Omurilik, beyinle vücut arasındaki iletişimi sağlar."
    "Sinirler, motor ve duyu sinirleri olarak iki ana gruba ayrılır."
    "Refleksler, omurilik tarafından hızlıca kontrol edilen tepkilerdir."
    "Sinir sisteminde elektriksel ve kimyasal sinyaller kullanılır."
    "Nöronlar, bilgi taşıyan özel hücrelerdir."
    "Beyin, farklı loblara ayrılır ve her lob farklı işlevleri yönetir."
    "Sinir sistemi, vücut dengesini (homeostaz) korumaya yardımcı olur."
    "Multipl skleroz gibi hastalıklar sinir sistemini etkileyebilir."
    "Felç, omurilik veya beyin hasarından kaynaklanabilir."
    "Uyku, sinir sisteminin kendini yenilemesi için kritik öneme sahiptir."
    "Egzersiz ve zihinsel aktiviteler sinir sistemi sağlığını destekler.",
    "image_url": "https://innerbody.imgix.net/nervous_system.png?auto=format"
},
    {
    "title": "Solunum Sistemi",
    "description": "Solunum sistemi, vücut hücrelerine oksijen sağlarken karbondioksiti uzaklaştırır.",
    "detail_description":
    "Solunum Sisteminin İşlevleri:"
    "Solunum sistemi, yaşam için gerekli olan gaz değişimini sağlar."
    "Burun, havayı temizler, nemlendirir ve ısıtır."
    "Trakea (nefes borusu), havayı akciğerlere taşır."
    "Bronşlar, havayı akciğerlerin içine dağıtır."
    "Alveoller, oksijen ve karbondioksit değişiminin gerçekleştiği küçük hava kesecikleridir."
    "Oksijen, alveollerden kana geçerek vücut hücrelerine taşınır."
    "Karbondioksit, kandan alveollere geçerek dışarı atılır."
    "Diyafram kası, solunumda önemli bir rol oynar."
    "Solunum, hem bilinçli hem de otomatik olarak kontrol edilir."
    "Vücudun enerji üretimi için oksijene ihtiyacı vardır."
    "Solunum sistemi, spor performansını ve dayanıklılığı doğrudan etkiler."
    "Sigara kullanımı solunum sistemine ciddi zararlar verebilir."
    "Astım ve KOAH gibi hastalıklar solunum yollarını etkiler."
    "Solunum yolu enfeksiyonları, özellikle kış aylarında yaygındır."
    "Temiz hava ve düzenli egzersiz solunum sağlığı için önemlidir."
    "Akciğerler, vücudun en büyük organlarından biridir.",
    "image_url": "https://innerbody.imgix.net/respiratory_system.png?auto=format"
},
    {
    "title": "Bağışıklık / Lenfatik Sistem",
    "description": "Bağışıklık ve lenfatik sistemler birbirine yakındır ve organlar ile fizyolojik işlevleri paylaşır.",
    "detail_description":
    "Bağışıklık ve Lenfatik Sistem İşlevleri:"
    "Bağışıklık sistemi, vücudu bakteri, virüs ve diğer zararlı mikroorganizmalara karşı korur."
    "Lenfatik sistem, lenf sıvısını taşıyarak atık maddelerin ve toksinlerin uzaklaştırılmasına yardımcı olur."
    "Lenf düğümleri, enfeksiyonlara karşı savunma sağlayan özel hücreleri barındırır."
    "Dalak, kanı filtreleyerek eski ve zarar görmüş hücreleri temizler."
    "Timoz bezi, çocukluk döneminde T hücrelerinin olgunlaşmasını sağlar."
    "Bağışıklık sistemi, antikorlar üreterek patojenleri etkisiz hale getirir."
    "Doğuştan gelen (innate) ve sonradan kazanılmış (adaptive) bağışıklık olmak üzere iki ana savunma mekanizması vardır."
    "Alerjik reaksiyonlar, bağışıklık sisteminin aşırı tepkisinden kaynaklanır."
    "Otoimmün hastalıklarda, bağışıklık sistemi yanlışlıkla kendi dokularına saldırır."
    "Lenfatik sistem, sindirim sistemi ile iş birliği yaparak yağların emilmesine katkıda bulunur."
    "Lenf sıvısı, lenf damarları aracılığıyla dolaşır ve vücudun sıvı dengesini korur."
    "Aşılar, bağışıklık sistemini belirli hastalıklara karşı hazırlıklı hale getirir."
    "HIV virüsü, bağışıklık sisteminin işlevlerini zayıflatır."
    "Lenfödem, lenf sıvısının birikmesi sonucu meydana gelen bir hastalıktır."
    "Sağlıklı bir bağışıklık sistemi için dengeli beslenme, uyku ve egzersiz önemlidir."
    "Stres, bağışıklık yanıtını zayıflatabilir.",
    "image_url": "https://innerbody.imgix.net/immune_lymphatic_systems.png?auto=format"
},
    {
    "title": "İdrar Yolları Sistemi",
    "description": "İdrar yolları sistemi; böbrekler, üreterler, idrar kesesi ve üretradan oluşur.",
    "detail_description":
    "İdrar Yolları Sisteminin Temel İşlevleri:"
    "Böbrekler, kandaki atık maddeleri süzerek idrar oluşturur."
    "Üreterler, böbreklerden idrarı mesaneye taşır."
    "İdrar kesesi, idrarı depolayan esnek bir organdır."
    "Üretra, idrarın vücuttan atılmasını sağlar."
    "Böbrekler, vücudun su ve elektrolit dengesini düzenler."
    "İdrar, vücuttaki toksinlerin ve fazla sıvının atılmasına yardımcı olur."
    "Böbrekler aynı zamanda kan basıncını kontrol eden hormonlar üretir."
    "Eritropoietin hormonu, kırmızı kan hücresi üretimini destekler."
    "İdrar yolları enfeksiyonları, sık görülen sağlık sorunları arasındadır."
    "İdrar yolları taşları, minerallerin kristalleşmesiyle oluşur."
    "Böbrek sağlığı için yeterli su tüketimi önemlidir."
    "Kreatinin ve üre seviyeleri, böbrek fonksiyonlarını değerlendirmede kullanılır."
    "Glomerüller, böbreklerde kanı filtreleyen küçük yapı birimleridir."
    "İdrarın rengi ve kokusu, vücut sağlığı hakkında ipuçları verebilir."
    "Böbrek yetmezliği, acil tedavi gerektiren ciddi bir durumdur."
    "İdrar yolları sisteminin sağlığı genel vücut fonksiyonları için kritiktir.",
    "image_url": "https://innerbody.imgix.net/urinary_system.png?auto=format"
},
    {
    "title": "Kadın Üreme Sistemi",
    "description": "Yumurtalıklar, fallop tüpleri, rahim, vajina, vulva ve süt bezlerini içerir.",
    "detail_description":
    "Kadın Üreme Sistemi Temel Yapıları:"
    "Yumurtalıklar, yumurta hücrelerini üretir."
    "Fallop tüpleri, yumurtayı rahime taşır."
    "Rahim, döllenmiş yumurtanın geliştiği organdır."
    "Vajina, doğum kanalı ve cinsel ilişkinin gerçekleştiği yapıdır."
    "Vulva, dış genital organları içerir."
    "Süt bezleri, doğum sonrası süt üretimini sağlar."
    "Adet döngüsü, üreme sistemi tarafından düzenlenir."
    "Östrojen ve progesteron hormonları önemli rol oynar."
    "Döllenme fallop tüplerinde gerçekleşir."
    "Hamilelik süreci rahimde başlar ve gelişir."
    "Kadın üreme sağlığı, genel sağlık üzerinde doğrudan etkilidir."
    "Düzenli jinekolojik kontroller önemlidir."
    "Üreme sistemi bozuklukları doğurganlığı etkileyebilir.",
    "image_url": "https://innerbody.imgix.net/female_reproductive_system.png?auto=format"
},
    {
    "title": "Erkek Üreme Sistemi",
    "description": "Skrotum, testisler, sperm kanalları, cinsiyet bezleri ve penisten oluşur.",
    "detail_description":
    "Erkek Üreme Sistemi Ana Yapıları:"
    "Testisler, sperm ve testosteron üretir."
    "Skrotum, testisleri korur ve sıcaklıklarını düzenler."
    "Sperm kanalları, spermleri taşır."
    "Prostat bezi, sperm sıvısının bir kısmını üretir."
    "Penis, sperm ve idrarın dışarı atıldığı organdır."
    "Spermatogenez süreci testislerde gerçekleşir."
    "Testosteron, erkek cinsiyet özelliklerini belirler."
    "Sperm, döllenme sürecinde yumurtayı fertilize eder."
    "Erektil doku, penisin sertleşmesini sağlar."
    "Erkek doğurganlığı, sperm kalitesi ile ilişkilidir."
    "Prostat sağlığı, ilerleyen yaşta dikkat edilmesi gereken bir konudur."
    "Sağlıklı yaşam tarzı, üreme sağlığını destekler.",
    "image_url": "https://innerbody.imgix.net/male_reproductive_system.png?auto=format"
},
    {
    "title": "İntegumenter Sistem",
    "description": "Deri, saç, tırnaklar ve ekzokrin bezlerden oluşur.",
    "detail_description":
    "İntegumenter Sistem Görevleri:"
    "Deri, vücudu dış etkenlerden korur."
    "Deri, su kaybını önleyerek homeostazı destekler."
    "Tüy ve saç, fiziksel koruma sağlar."
    "Tırnaklar, parmak uçlarını korur ve destekler."
    "Ter bezleri, sıcaklık düzenlenmesine yardımcı olur."
    "Yağ bezleri cildi nemlendirir ve korur."
    "Deri, duyusal bilgileri algılayan sinir uçlarına sahiptir."
    "Melanin, cilt rengini belirler ve güneş ışınlarına karşı koruma sağlar."
    "Deri, D vitamini üretiminde rol oynar."
    "İnflamasyon, cildin savunma tepkisidir."
    "Cilt, toksinlerin bir kısmını terleme yoluyla atar."
    "İntegumenter sistem, genel bağışıklıkta ilk savunma hattıdır.",
    "image_url": "https://innerbody.imgix.net/integumentary_system.png?auto=format"
},
]
    return render(request, 'pages/fizyoloji.html', {'systems': systems})



def hastaliklar(request):
    hastaliklar = [
      {
        "id": 1,
        "title": "20lik Dis",
        "slug": "20lik-dis-nedir",
        "description": "20'lik diş ağrısı neden olur? Çekimi sonrası nelere dikkat edilmelidir?",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/yamukdisjpg_e22d.jpg",
        "kaynak": "https://www.google.com/search?q=20lik+Dis"
      },
      {
        "id": 2,
        "title": "Migren",
        "slug": "migren-nedir",
        "description": "Migrenin belirtileri, nedenleri ve tedavi yöntemleri.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Migren.jpg",
        "kaynak": "https://www.google.com/search?q=Migren"
      },
      {
        "id": 3,
        "title": "Diyabet",
        "slug": "diyabet-nedir",
        "description": "Tip 1 ve Tip 2 diyabetin farkları, belirtileri ve tedavisi.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/tip1diyabetjpg_170c.jpg",
        "kaynak": "https://www.google.com/search?q=Diyabet"
      },
      {
        "id": 4,
        "title": "Hipertansiyon",
        "slug": "hipertansiyon-nedir",
        "description": "Yüksek tansiyonun nedenleri ve kontrol yolları.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/cocuklardakasikfitigiinguinalherninedirjpg_0494.jpg",
        "kaynak": "https://www.google.com/search?q=Hipertansiyon"
      },
      {
        "id": 5,
        "title": "Astım",
        "slug": "astim-nedir",
        "description": "Astım belirtileri, tetikleyicileri ve tedavi yöntemleri.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/astim-3jpg_b258.jpg",
        "kaynak": "https://www.google.com/search?q=Ast%C4%B1m"
      },
      {
        "id": 6,
        "title": "KOAH",
        "slug": "koah-nedir",
        "description": "Kronik Obstrüktif Akciğer Hastalığı ve yaşam kalitesine etkisi.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/koah-nedir-belirti-ve-tedavi-yontemleri-nelerdir.jpg",
        "kaynak": "https://www.google.com/search?q=KOAH"
      },
      {
        "id": 7,
        "title": "Koroner Arter Hastalığı",
        "slug": "koroner-arter-hastaligi",
        "description": "Kalp damarlarında daralma ve tıkanıklık belirtileri.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/koroner-arter-hastaligijpg_de39.jpg",
        "kaynak": "https://www.google.com/search?q=Koroner+Arter+Hastal%C4%B1%C4%9F%C4%B1"
      },
      {
        "id": 8,
        "title": "Anemi",
        "slug": "anemi-nedir",
        "description": "Demir eksikliği anemisi belirtileri ve tedavi yolları.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/anemikansizliknediranemibelirtilerinelerdirjpg_f2c5.jpg",
        "kaynak": "https://www.google.com/search?q=Anemi"
      },
      {
        "id": 9,
        "title": "Tiroid Hastalıkları",
        "slug": "tiroid-hastaliklari",
        "description": "Hipotiroidi ve hipertiroidi nedir? Belirtileri nelerdir?",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/tiroidnedirjpg_c957.jpg",
        "kaynak": "https://www.google.com/search?q=Tiroid+Hastal%C4%B1klar%C4%B1"
      },
      {
        "id": 10,
        "title": "Romatoid Artrit",
        "slug": "romatoid-artrit-nedir",
        "description": "Eklemlerde iltihaplanma ile seyreden romatizmal hastalık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/romatoid-artritjpg_d7c2.jpg",
        "kaynak": "https://www.google.com/search?q=Romatoid+Artrit"
      },
      {
        "id": 11,
        "title": "Sedef Hastalığı",
        "slug": "sedef-hastaligi",
        "description": "Ciltte kızarıklık ve pullanma ile kendini gösteren hastalık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Sedef-Hastaligi.jpg",
        "kaynak": "https://www.google.com/search?q=Sedef+Hastal%C4%B1%C4%9F%C4%B1"
      },
      {
        "id": 12,
        "title": "Egzama",
        "slug": "egzama-nedir",
        "description": "Ciltte kuruluk ve kaşıntıya neden olan dermatolojik hastalık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Egzama.jpg",
        "kaynak": "https://www.google.com/search?q=Egzama"
      },
      {
        "id": 13,
        "title": "MS Hastalığı",
        "slug": "ms-hastaligi",
        "description": "Multipl Skleroz sinir sistemi üzerinde etkili bir hastalıktır.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/MS-Hastaligi.jpg",
        "kaynak": "https://www.google.com/search?q=MS+Hastal%C4%B1%C4%9F%C4%B1"
      },
      {
        "id": 14,
        "title": "Epilepsi",
        "slug": "epilepsi-nedir",
        "description": "Beyindeki ani elektriksel boşalmalar ile oluşan nörolojik hastalık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/epilepsi-nedir.jpg",
        "kaynak": "https://www.google.com/search?q=Epilepsi"
      },
      {
        "id": 15,
        "title": "Parkinson",
        "slug": "parkinson-nedir",
        "description": "İleri yaşta sık görülen hareket bozukluğu hastalığı.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/parkinson-hastaligi-nedir-belirtileri-nelerdir.jpg",
        "kaynak": "https://www.google.com/search?q=Parkinson"
      },
      {
        "id": 16,
        "title": "Alzheimer",
        "slug": "alzheimer-nedir",
        "description": "Unutkanlıkla başlayıp zamanla ilerleyen beyin hastalığı.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/alzheimer-nedir-belirtileri-ve-tedavi-yontemleri-nelerdir.jpg",
        "kaynak": "https://www.google.com/search?q=Alzheimer"
      },
      {
        "id": 17,
        "title": "Depresyon",
        "slug": "depresyon-nedir",
        "description": "Ruhsal çöküntü ile seyreden psikiyatrik bozukluk.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/distimikronikdepresyonnedirtedavisinasildirjpg_d123.jpg",
        "kaynak": "https://www.google.com/search?q=Depresyon"
      },
      {
        "id": 18,
        "title": "Anksiyete",
        "slug": "anksiyete-nedir",
        "description": "Kaygı bozukluğu olarak da bilinen psikolojik rahatsızlık.",
        "image": "https://cdn.memorial.com.tr/files/2018/12/a606c983-6205-4af1-bd26-6a99cd8c71f8.png",
        "kaynak": "https://www.google.com/search?q=Anksiyete"
      },
      {
        "id": 19,
        "title": "Bipolar Bozukluk",
        "slug": "bipolar-bozukluk",
        "description": "Duygu durum değişiklikleriyle seyreden psikiyatrik hastalık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/bipolarjpg_daf4.jpg",
        "kaynak": "https://www.google.com/search?q=Bipolar+Bozukluk"
      },
      {
        "id": 20,
        "title": "Obezite",
        "slug": "obezite-nedir",
        "description": "Aşırı kilo nedeniyle oluşan metabolik bir hastalık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/obezite-1jpg_991e.jpg",
        "kaynak": "https://www.google.com/search?q=Obezite"
      },
      {
        "id": 21,
        "title": "Grip",
        "slug": "grip-nedir",
        "description": "Mevsimsel grip belirtileri, korunma yolları ve tedavisi.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Grip.jpg",
        "kaynak": "https://www.google.com/search?q=Grip"
      },
      {
        "id": 22,
        "title": "Zatürre",
        "slug": "zaturre-nedir",
        "description": "Akciğer enfeksiyonu olan zatürre belirtileri ve tedavi yolları.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Zat%C3%BCrre.jpg",
        "kaynak": "https://www.google.com/search?q=Zat%C3%BCrre"
      },
      {
        "id": 23,
        "title": "Bronşit",
        "slug": "bronsit-nedir",
        "description": "Solunum yollarını etkileyen iltihabi hastalık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/bronsitnedirjpg_d03e.jpg",
        "kaynak": "https://www.google.com/search?q=Bron%C5%9Fit"
      },
      {
        "id": 24,
        "title": "Soğuk Algınlığı",
        "slug": "soguk-alginligi",
        "description": "Burun akıntısı ve boğaz ağrısı ile seyreden viral hastalık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/sogukhavalejpg_d10f.jpg",
        "kaynak": "https://www.google.com/search?q=So%C4%9Fuk+Alg%C4%B1nl%C4%B1%C4%9F%C4%B1"
      },
      {
        "id": 25,
        "title": "Bademcik İltihabı",
        "slug": "bademcik-iltihabi",
        "description": "Bademciklerde enfeksiyon sonucu şişlik ve ağrı oluşur.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/bademcik-iltihabi-tedavisi-nasil-olur.jpg",
        "kaynak": "https://www.google.com/search?q=Bademcik+%C4%B0ltihab%C4%B1"
      },
      {
        "id": 26,
        "title": "Boğmaca",
        "slug": "bogmaca-nedir",
        "description": "Şiddetli öksürük nöbetleriyle seyreden çocuk hastalığı.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/bogmaca-nedir-belirti-ve-tedavi-yontemleri-nelerdir.jpg",
        "kaynak": "https://www.google.com/search?q=Bo%C4%9Fmaca"
      },
      {
        "id": 27,
        "title": "Kabakulak",
        "slug": "kabakulak-nedir",
        "description": "Tükürük bezlerinin iltihaplanmasıyla oluşan bulaşıcı hastalık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/kabakulak1jpg_edba.jpg",
        "kaynak": "https://www.google.com/search?q=Kabakulak"
      },
      {
        "id": 28,
        "title": "Su Çiçeği",
        "slug": "sucicegi-nedir",
        "description": "Ciltte kabarcıklarla seyreden çocukluk çağı hastalığı.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/sucicegijpg_605d.jpg",
        "kaynak": "https://www.google.com/search?q=Su+%C3%87i%C3%A7e%C4%9Fi"
      },
      {
        "id": 29,
        "title": "Kızamık",
        "slug": "kizamik-nedir",
        "description": "Yüksek ateş ve cilt döküntüleri ile görülen bulaşıcı hastalık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Kizamik.jpg",
        "kaynak": "https://www.google.com/search?q=K%C4%B1zam%C4%B1k"
      },
      {
        "id": 30,
        "title": "Kızamıkçık",
        "slug": "kizamikcik-nedir",
        "description": "Ciltte döküntü ve hafif ateşle seyreden viral enfeksiyon.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/kizamikcikjpg_9543.jpg",
        "kaynak": "https://www.google.com/search?q=K%C4%B1zam%C4%B1k%C3%A7%C4%B1k"
      },
      {
        "id": 31,
        "title": "İshal",
        "slug": "ishal-nedir",
        "description": "Sık ve sulu dışkılamayla seyreden mide-bağırsak rahatsızlığı.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/bagirsakenfeksiyonujpg_2028.jpg",
        "kaynak": "https://www.google.com/search?q=%C4%B0shal"
      },
      {
        "id": 32,
        "title": "Kabızlık",
        "slug": "kabizlik-nedir",
        "description": "Bağırsak hareketlerinin yavaşlaması sonucu dışkılamada zorlanma.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/kordon-kisti-ve-hidrosel-su-fitigi-nedir.jpg",
        "kaynak": "https://www.google.com/search?q=Kab%C4%B1zl%C4%B1k"
      },
      {
        "id": 33,
        "title": "Gastrit",
        "slug": "gastrit-nedir",
        "description": "Mide iç yüzeyinin iltihaplanması.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Gastrit.jpg",
        "kaynak": "https://www.google.com/search?q=Gastrit"
      },
      {
        "id": 34,
        "title": "Ülser",
        "slug": "ulser-nedir",
        "description": "Mide ya da onikiparmak bağırsağında yara oluşması.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/%C3%9Clser.jpg",
        "kaynak": "https://www.google.com/search?q=%C3%9Clser"
      },
      {
        "id": 35,
        "title": "Reflü",
        "slug": "reflu-nedir",
        "description": "Mide asidinin yemek borusuna kaçmasıyla oluşan rahatsızlık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Refl%C3%BC.jpg",
        "kaynak": "https://www.google.com/search?q=Refl%C3%BC"
      },
      {
        "id": 36,
        "title": "Safra Taşı",
        "slug": "safra-tasi-nedir",
        "description": "Safra kesesinde taş oluşumu sonucu görülen rahatsızlık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/dce00039262647709780b33bd732cc3bjpg_cb86.jpg",
        "kaynak": "https://www.google.com/search?q=Safra+Ta%C5%9F%C4%B1"
      },
      {
        "id": 37,
        "title": "Hepatit B",
        "slug": "hepatit-b-nedir",
        "description": "Karaciğerde enfeksiyona yol açan ciddi bir hastalık.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/hepatit-b-nedir-belirti-ve-tedavi-yontemleri-nelerdir.jpg",
        "kaynak": "https://www.google.com/search?q=Hepatit+B"
      },
      {
        "id": 38,
        "title": "Hepatit C",
        "slug": "hepatit-c-nedir",
        "description": "Kan yoluyla bulaşan karaciğer enfeksiyonu.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/hepatit-c-nedir-belirtileri-nelerdir.jpg",
        "kaynak": "https://www.google.com/search?q=Hepatit+C"
      },
      {
        "id": 39,
        "title": "Cilt Kanseri",
        "slug": "cilt-kanseri-nedir",
        "description": "Cilt hücrelerinde kontrolsüz büyüme ile gelişen kanser türü.",
        "image": "https://cdn.memorial.com.tr/files/2017/6/39ff668c-eef7-47ad-a074-6032ac331a81.jpg",
        "kaynak": "https://www.google.com/search?q=Cilt+Kanseri"
      },
      {
        "id": 40,
        "title": "Meme Kanseri",
        "slug": "meme-kanseri-nedir",
        "description": "Kadınlarda en sık görülen kanser türlerinden biri.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/meme-kanseri-belirtileri-tanisi-ve-tedavi-yontemleri.jpg",
        "kaynak": "https://www.google.com/search?q=Meme+Kanseri"
      },
      {
        "id": 41,
        "title": "Prostat Kanseri",
        "slug": "prostat-kanseri-nedir",
        "description": "Erkeklerde sık rastlanan ürolojik kanser türü.",
        "image": "https://cdn.memorial.com.tr/files/2017/3/08f332bc-b315-4eb3-a1cc-a758ccc2ccf1.jpg",
        "kaynak": "https://www.google.com/search?q=Prostat+Kanseri"
      },
      {
        "id": 42,
        "title": "Rahim Ağzı Kanseri",
        "slug": "rahim-agzi-kanseri",
        "description": "HPV virüsü ile ilişkilendirilen kanser türü.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/rahim-kanseri-nedir-belirti-ve-tedavi-yontemleri-nelerdir.jpg",
        "kaynak": "https://www.google.com/search?q=Rahim+A%C4%9Fz%C4%B1+Kanseri"
      },
      {
        "id": 43,
        "title": "Böbrek Taşı",
        "slug": "bobrek-tasi-nedir",
        "description": "Böbreklerde mineral birikimi sonucu oluşan taşlar.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/B%C3%B6brek-Taslari.jpg",
        "kaynak": "https://www.google.com/search?q=B%C3%B6brek+Ta%C5%9F%C4%B1"
      },
      {
        "id": 44,
        "title": "İdrar Yolu Enfeksiyonu",
        "slug": "idraryolu-enfeksiyonu",
        "description": "Sık idrara çıkma ve yanma hissi ile kendini gösterir.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/idraryoluenfeksiyonujpg_f7d9.jpg",
        "kaynak": "https://www.google.com/search?q=%C4%B0drar+Yolu+Enfeksiyonu"
      },
      {
        "id": 45,
        "title": "Varis",
        "slug": "varis-nedir",
        "description": "Toplardamarların genişlemesi sonucu oluşan damar hastalığı.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/varisnedirjpg_0955.jpg",
        "kaynak": "https://www.google.com/search?q=Varis"
      },
      {
        "id": 46,
        "title": "Hemoroid",
        "slug": "hemoroid-nedir",
        "description": "Halk arasında basur olarak bilinen makat çevresindeki damar genişlemesi.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Hemoroid.jpg",
        "kaynak": "https://www.google.com/search?q=Hemoroid"
      },
      {
        "id": 47,
        "title": "Cilt Lekeleri",
        "slug": "cilt-lekeleri",
        "description": "Ciltte güneş ya da yaşlanmaya bağlı leke oluşumu.",
        "image": "https://cdn.memorial.com.tr/files/2017/6/39ff668c-eef7-47ad-a074-6032ac331a81.jpg",
        "kaynak": "https://www.google.com/search?q=Cilt+Lekeleri"
      },
      {
        "id": 48,
        "title": "Sivilce",
        "slug": "sivilce-nedir",
        "description": "Gençlik döneminde sık rastlanan cilt sorunu.",
        "image": "https://www.medicalpark.com.tr/_uploads/_images/_healthGuide/vLqRitfd.jpg",
        "kaynak": "https://www.google.com/search?q=Sivilce"
      },
      {
        "id": 49,
        "title": "Mantardan Kaynaklı Cilt Hastalıkları",
        "slug": "mantar-hastaligi",
        "description": "Ayakta, elde ya da kasıkta görülebilen mantar enfeksiyonları.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Mantar.jpg",
        "kaynak": "https://www.google.com/search?q=Mantardan+Kaynakl%C4%B1+Cilt+Hastal%C4%B1klar%C4%B1"
      },
      {
        "id": 50,
        "title": "Uyku Apnesi",
        "slug": "uyku-apnesi",
        "description": "Uykuda solunum durması ile karakterize uyku bozukluğu.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Uyku-Apnesi.jpg",
        "kaynak": "https://www.google.com/search?q=Uyku+Apnesi"
      },
      {
        "id": 61,
        "title": "Tansiyon Düşüklüğü",
        "slug": "tansiyon-dusuklugu",
        "description": "Tansiyon düşüklüğü belirtileri ve tedavi yöntemleri.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/D%C3%BCs%C3%BCk-Tansiyon.jpg",
        "kaynak": "https://www.google.com/search?q=Tansiyon+D%C3%BC%C5%9F%C3%BCkl%C3%BC%C4%9F%C3%BC"
      },
      {
        "id": 62,
        "title": "Tansiyon Yüksekliği",
        "slug": "tansiyon-yuksekligi",
        "description": "Hipertansiyonun nedenleri, belirtileri ve tedavi yöntemleri.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Y%C3%BCksek-Tansiyon.jpg",
        "kaynak": "https://www.google.com/search?q=Tansiyon+Y%C3%BCksekli%C4%9Fi"
      },
      {
        "id": 63,
        "title": "Kalp Yetmezliği",
        "slug": "kalp-yetmezligi",
        "description": "Kalp yetmezliği nedir? Neden olur? Belirtileri ve tedavisi.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/kalp-yetmezligi-nedir-nasil-tedavi-edilir.jpg",
        "kaynak": "https://www.google.com/search?q=Kalp+Yetmezli%C4%9Fi"
      },
      {
        "id": 64,
        "title": "Alerjik Rinit",
        "slug": "alerjik-rinit",
        "description": "Alerjik rinitin belirtileri, nedenleri ve tedavi seçenekleri.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/Alerji.jpg",
        "kaynak": "https://www.google.com/search?q=Alerjik+Rinit"
      },
      {
        "id": 65,
        "title": "Sinüzit",
        "slug": "sinuzit",
        "description": "Sinüzitin belirtileri, nedenleri ve tedavi yöntemleri.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/sinuzit-nedirjpg_7d97.jpg",
        "kaynak": "https://www.google.com/search?q=Sin%C3%BCzit"
      },
      {
        "id": 66,
        "title": "Tiroid Kanseri",
        "slug": "tiroid-kanseri",
        "description": "Tiroid kanseri nedir? Belirtileri ve tanı yöntemleri.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/tiroid-kanseri-belirtileri-ve-tedavi-yontemleri-nelerdir.jpg",
        "kaynak": "https://www.google.com/search?q=Tiroid+Kanseri"
      },
      {
        "id": 67,
        "title": "Yumurtalık Kisti",
        "slug": "yumurtalik-kisti",
        "description": "Yumurtalık kistleri hakkında bilmeniz gerekenler.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/yumurtalik-kistleri-nedir.jpg",
        "kaynak": "https://www.google.com/search?q=Yumurtal%C4%B1k+Kisti"
      },
      {
        "id": 68,
        "title": "Rahim Kanseri",
        "slug": "rahim-kanseri",
        "description": "Rahim kanseri belirtileri, nedenleri ve tedavi süreci.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/rahim-kanseri-nedir-belirti-ve-tedavi-yontemleri-nelerdir.jpg",
        "kaynak": "https://www.google.com/search?q=Rahim+Kanseri"
      },
      {
        "id": 69,
        "title": "Böbrek Yetmezliği",
        "slug": "bobrek-yetmezligi",
        "description": "Böbrek yetmezliğinin nedenleri, belirtileri ve tedavi yöntemleri.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/21/B%C3%B6brek-Yetmezligi.jpg",
        "kaynak": "https://www.google.com/search?q=B%C3%B6brek+Yetmezli%C4%9Fi"
      },
      {
        "id": 70,
        "title": "Skolyoz",
        "slug": "skolyoz",
        "description": "Skolyoz nedir? Omurga eğriliği hakkında detaylı bilgi.",
        "image": "https://cdn.memorial.com.tr/files/Uploads/1/15/f2c3ddc3ede743e1831f6bf7e3cd9cc6jpg_7026.jpg",
        "kaynak": "https://www.google.com/search?q=Skolyoz"
      }
    ]
    return render(request, 'pages/hastaliklar.html', {'hastaliklar': hastaliklar})




from django.shortcuts import get_object_or_404, redirect
from .views import hastaliklar  # modelin adı örnek olarak 'Hastalik'

def hastalik_detay(request, slug):
    hastaliklar = get_object_or_404(hastaliklar, slug=slug)
    return redirect(hastaliklar.kaynak)


# def iletisim(request):
#     return render(request,"pages/iletisim.html")


def hastalik_detay(request, slug):
    hastalik = next((h for h in hastaliklar if h['slug'] == slug), None)
    if not hastalik:
        raise Http404("Hastalık bulunamadı.")
    return render(request, 'hastalik_detay.html', {'hastalik': hastalik})



def iletisim(request):
    konum=[
        {
    "name": "T.C. Sağlık Bakanlığı Besni Devlet Hastanesi",
    "latitude": 37.6900,
    "longitude": 37.8610
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gölbaşı Devlet Hastanesi",
    "latitude": 37.7833,
    "longitude": 37.6333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çelikhan Devlet Hastanesi",
    "latitude": 38.0333,
    "longitude": 38.2500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sincik İlçe Devlet Hastanesi",
    "latitude": 38.0167,
    "longitude": 38.6167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kahta Göçeri İlçe Devlet Hastanesi",
    "latitude": 37.7833,
    "longitude": 38.6167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gerger İlçe Devlet Hastanesi",
    "latitude": 37.9333,
    "longitude": 39.0333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tut İlçe Devlet Hastanesi",
    "latitude": 37.7833,
    "longitude": 37.6167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Samsat İlçe Devlet Hastanesi",
    "latitude": 37.7667,
    "longitude": 38.4833
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şuhut Devlet Hastanesi",
    "latitude": 38.5333,
    "longitude": 30.5500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sandıklı Devlet Hastanesi",
    "latitude": 38.4667,
    "longitude": 30.2667
  },
  {
    "name": "T.C. Sağlık Bakanlığı Emirdağ Devlet Hastanesi",
    "latitude": 39.0167,
    "longitude": 31.1500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Dinar Devlet Hastanesi",
    "latitude": 38.0667,
    "longitude": 30.1500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bolvadin Dr.Halil İbrahim Özsoy Devlet Hastanesi",
    "latitude": 38.7167,
    "longitude": 31.0500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çay Devlet Hastanesi",
    "latitude": 38.6000,
    "longitude": 31.0333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Afyonkarahisar Devlet Hastanesi",
    "latitude": 38.7500,
    "longitude": 30.5500
  },
  {
    "name": "T.C. Sağlık Bakanlığı İscehisar Karamehmet Devlet Hastanesi",
    "latitude": 38.8167,
    "longitude": 30.7500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sinanpaşa Devlet Hastanesi",
    "latitude": 38.6833,
    "longitude": 30.2500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Başmakçı İlçe Devlet Hastanesi",
    "latitude": 38.1500,
    "longitude": 30.0000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bayat Dr.Mete Tan İlçe Devlet Hastanesi",
    "latitude": 38.9667,
    "longitude": 30.9333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çobanlar İlçe Devlet Hastanesi",
    "latitude": 38.7500,
    "longitude": 30.8333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Dazkırı İlçe Devlet Hastanesi",
    "latitude": 38.5167,
    "longitude": 29.8667
  },{
    "name": "T.C. Sağlık Bakanlığı Haydarlı İlçe Devlet Hastanesi",
    "latitude": 38.4000,
    "longitude": 30.0000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Evciler İlçe Devlet Hastanesi",
    "latitude": 38.5000,
    "longitude": 29.7000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hocalar İlçe Devlet Hastanesi",
    "latitude": 38.5667,
    "longitude": 29.9500
  },
  {
    "name": "T.C. Sağlık Bakanlığı İhsaniye İlçe Devlet Hastanesi",
    "latitude": 38.8833,
    "longitude": 30.6000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sultandağı İlçe Devlet Hastanesi",
    "latitude": 38.5333,
    "longitude": 31.2333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ağrı Eğitim ve Araştırma Hastanesi",
    "latitude": 39.7194,
    "longitude": 43.0514
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eleşkirt İlçe Devlet Hastanesi",
    "latitude": 39.8000,
    "longitude": 42.6833
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tutak İlçe Devlet Hastanesi",
    "latitude": 39.5500,
    "longitude": 42.7667
  },
  {
    "name": "T.C. Sağlık Bakanlığı Diyadin Devlet Hastanesi",
    "latitude": 39.5417,
    "longitude": 43.6667
  },
  {
    "name": "T.C. Sağlık Bakanlığı Doğubayazıt Dr. Yaşar Eryılmaz Devlet Hastanesi",
    "latitude": 39.5500,
    "longitude": 44.0833
  },
  {
    "name": "T.C. Sağlık Bakanlığı Patnos Devlet Hastanesi",
    "latitude": 39.2333,
    "longitude": 42.8500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Taşlıçay İlçe Devlet Hastanesi",
    "latitude": 39.6500,
    "longitude": 43.3833
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hamur İlçe Devlet Hastanesi",
    "latitude": 39.6167,
    "longitude": 42.9833
  },
  {
    "name": "T.C. Sağlık Bakanlığı Aksaray Eğitim ve Araştırma Hastanesi",
    "latitude": 38.3687,
    "longitude": 34.0360
  },
  {
    "name": "T.C. Sağlık Bakanlığı Aksaray Ortaköy Devlet Hastanesi",
    "latitude": 38.7333,
    "longitude": 34.0333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eskil Devlet Hastanesi",
    "latitude": 38.4000,
    "longitude": 33.4000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gülağaç İlçe Devlet Hastanesi",
    "latitude": 38.3000,
    "longitude": 34.2000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sultanhanı Dr. Hüseyin Ağır İlçe Devlet Hastanesi",
    "latitude": 38.2500,
    "longitude": 33.5500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Güzelyurt İlçe Devlet Hastanesi",
    "latitude": 38.3000,
    "longitude": 34.3000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ağaçören İlçe Devlet Hastanesi",
    "latitude": 38.9000,
    "longitude": 33.9000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sarıyahşi İlçe Devlet Hastanesi",
    "latitude": 38.9000,
    "longitude": 33.7000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Amasya Sabuncuoğlu Şerefeddin Eğitim ve Araştırma Hastanesi",
    "latitude": 40.6500,
    "longitude": 35.8333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gümüşhacıköy Devlet Hastanesi",
    "latitude": 40.8667,
    "longitude": 35.6500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Merzifon Kara Mustafa Paşa Devlet Hastanesi",
    "latitude": 40.8667,
    "longitude": 35.4667
  },
  {
    "name": "T.C. Sağlık Bakanlığı Suluova Devlet Hastanesi",
    "latitude": 40.8333,
    "longitude": 35.6500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Taşova Devlet Hastanesi",
    "latitude": 40.7667,
    "longitude": 36.3167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Göynücek İlçe Devlet Hastanesi",
    "latitude": 40.4000,
    "longitude": 35.5333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hamamözü İlçe Devlet Hastanesi",
    "latitude": 40.9500,
    "longitude": 35.0000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ankara Yenimahalle Eğitim ve Araştırma Hastanesi",
    "latitude": 39.9500,
    "longitude": 32.8333
  },{
    "name": "T.C. Sağlık Bakanlığı Şereflikoçhisar Devlet Hastanesi",
    "latitude": 39.1500,
    "longitude": 32.0000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kızılcahamam Devlet Hastanesi",
    "latitude": 40.5000,
    "longitude": 32.8500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Nallıhan Devlet Hastanesi",
    "latitude": 40.2833,
    "longitude": 31.7333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Polatlı Duatepe Devlet Hastanesi",
    "latitude": 39.5667,
    "longitude": 32.1167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Haymana Devlet Hastanesi",
    "latitude": 39.1000,
    "longitude": 32.2833
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kahramankazan Devlet Hastanesi",
    "latitude": 40.1500,
    "longitude": 32.6120
  },
  {
    "name": "T.C. Sağlık Bakanlığı Elmadağ Dr. Hulusi Alataş Devlet Hastanesi",
    "latitude": 39.9333,
    "longitude": 32.5667
  },
  {
    "name": "T.C. Sağlık Bakanlığı Beypazarı Devlet Hastanesi",
    "latitude": 40.2000,
    "longitude": 31.8333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çubuk Halil Şıvgın Devlet Hastanesi",
    "latitude": 40.2500,
    "longitude": 32.7167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ankara Etimesgut Şehit Sait Ertürk Devlet Hastanesi",
    "latitude": 39.9000,
    "longitude": 32.6167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ankara 75.Yıl Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 39.9200,
    "longitude": 32.8633
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ankara Sincan Dr. Nafiz Körez Devlet Hastanesi",
    "latitude": 39.8000,
    "longitude": 32.3700
  },
  {
    "name": "T.C. Sağlık Bakanlığı Akyurt Devlet Hastanesi",
    "latitude": 39.9167,
    "longitude": 32.5833
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ayaş Şehit Mehmet Çifci Devlet Hastanesi",
    "latitude": 39.5000,
    "longitude": 32.4500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ankara Gazi Mustafa Kemal Mesleki ve Çevresel Hastalıklar Hastanesi",
    "latitude": 39.9200,
    "longitude": 32.8490
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gölbaşı Şehit Ahmet Özsoy Devlet Hastanesi",
    "latitude": 39.4167,
    "longitude": 32.6167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Pursaklar Devlet Hastanesi",
    "latitude": 39.8667,
    "longitude": 32.8500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ankara Ceza İnfaz Kurumları Kampüs Devlet Hastanesi",
    "latitude": 39.9311,
    "longitude": 32.8678
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ankara Meclis Devlet Hastanesi",
    "latitude": 39.9322,
    "longitude": 32.8653
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ankara 29 Mayıs Devlet Hastanesi",
    "latitude": 39.9300,
    "longitude": 32.8650
  },{
    "name": "T.C. Sağlık Bakanlığı Ankara Beytepe Şehit Murat Erdi Eker Devlet Hastanesi",
    "latitude": 39.8917,
    "longitude": 32.8100
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mamak Devlet Hastanesi",
    "latitude": 39.9667,
    "longitude": 32.6500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ankara Osmanlı Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 39.9400,
    "longitude": 32.8592
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ankara Etlik Şehir Hastanesi",
    "latitude": 39.9394,
    "longitude": 32.6261
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ankara Beştepe Devlet Hastanesi",
    "latitude": 39.9294,
    "longitude": 32.8725
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kalecik İlçe Devlet Hastanesi",
    "latitude": 39.6597,
    "longitude": 32.5328
  },
  {
    "name": "T.C. Sağlık Bakanlığı Güdül İlçe Devlet Hastanesi",
    "latitude": 40.1350,
    "longitude": 32.5850
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bala İlçe Devlet Hastanesi",
    "latitude": 40.2000,
    "longitude": 32.8500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Alanya Eğitim ve Araştırma Hastanesi",
    "latitude": 36.5583,
    "longitude": 31.9997
  },
  {
    "name": "T.C. Sağlık Bakanlığı Antalya Eğitim ve Araştırma Hastanesi",
    "latitude": 36.8878,
    "longitude": 30.7043
  },
  {
    "name": "T.C. Sağlık Bakanlığı Serik Devlet Hastanesi",
    "latitude": 36.8543,
    "longitude": 31.0080
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kumluca Devlet Hastanesi",
    "latitude": 36.4220,
    "longitude": 30.4000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Manavgat Devlet Hastanesi",
    "latitude": 36.7933,
    "longitude": 31.3792
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kaş Devlet Hastanesi",
    "latitude": 36.2020,
    "longitude": 29.6347
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kemer Devlet Hastanesi",
    "latitude": 36.6040,
    "longitude": 30.4430
  },
  {
    "name": "T.C. Sağlık Bakanlığı Korkuteli Devlet Hastanesi",
    "latitude": 36.9800,
    "longitude": 30.4140
  },
  {
    "name": "T.C. Sağlık Bakanlığı Elmalı Devlet Hastanesi",
    "latitude": 36.3747,
    "longitude": 30.2280
  },
  {
    "name": "T.C. Sağlık Bakanlığı Finike Devlet Hastanesi",
    "latitude": 36.2867,
    "longitude": 30.1060
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gazipaşa Devlet Hastanesi",
    "latitude": 36.2670,
    "longitude": 32.0700
  },
  {
    "name": "T.C. Sağlık Bakanlığı Akseki İlçe Devlet Hastanesi",
    "latitude": 37.0167,
    "longitude": 31.3000
  },{
    "name": "T.C. Sağlık Bakanlığı Demre Devlet Hastanesi",
    "latitude": 36.2475,
    "longitude": 30.5717
  },
  {
    "name": "T.C. Sağlık Bakanlığı Antalya Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 36.8870,
    "longitude": 30.7047
  },
  {
    "name": "T.C. Sağlık Bakanlığı Antalya Atatürk Devlet Hastanesi",
    "latitude": 36.8900,
    "longitude": 30.7119
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gündoğmuş İlçe Devlet Hastanesi",
    "latitude": 36.9739,
    "longitude": 31.3897
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kepez Devlet Hastanesi",
    "latitude": 36.9778,
    "longitude": 30.7039
  },
  {
    "name": "T.C. Sağlık Bakanlığı Göle Devlet Hastanesi",
    "latitude": 40.4333,
    "longitude": 42.5461
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ardahan Devlet Hastanesi",
    "latitude": 41.1100,
    "longitude": 42.7025
  },
  {
    "name": "T.C. Sağlık Bakanlığı Posof İlçe Devlet Hastanesi",
    "latitude": 41.4400,
    "longitude": 42.2794
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çıldır İlçe Devlet Hastanesi",
    "latitude": 41.4530,
    "longitude": 42.4020
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şavşat Devlet Hastanesi",
    "latitude": 41.3772,
    "longitude": 41.4114
  },
  {
    "name": "T.C. Sağlık Bakanlığı Arhavi Devlet Hastanesi",
    "latitude": 41.2711,
    "longitude": 41.6100
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hopa Devlet Hastanesi",
    "latitude": 41.4028,
    "longitude": 41.4144
  },
  {
    "name": "T.C. Sağlık Bakanlığı Artvin Devlet Hastanesi",
    "latitude": 41.8200,
    "longitude": 41.2600
  },
  {
    "name": "T.C. Sağlık Bakanlığı Yusufeli Devlet Hastanesi",
    "latitude": 41.4247,
    "longitude": 41.6000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Borçka Devlet Hastanesi",
    "latitude": 41.8750,
    "longitude": 41.6725
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ardanuç İlçe Devlet Hastanesi",
    "latitude": 41.3350,
    "longitude": 41.4939
  },
  {
    "name": "T.C. Sağlık Bakanlığı Murgul İlçe Devlet Hastanesi",
    "latitude": 41.2764,
    "longitude": 41.7375
  },
  {
    "name": "T.C. Sağlık Bakanlığı Nazilli Devlet Hastanesi",
    "latitude": 37.9708,
    "longitude": 27.8333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Söke Fehime Faik Kocagöz Devlet Hastanesi",
    "latitude": 37.6533,
    "longitude": 27.3747
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kuşadası Devlet Hastanesi",
    "latitude": 37.8683,
    "longitude": 27.2578
  },{
    "name": "T.C. Sağlık Bakanlığı Çine Devlet Hastanesi",
    "latitude": 37.8486,
    "longitude": 27.5378
  },
  {
    "name": "T.C. Sağlık Bakanlığı Aydın Devlet Hastanesi",
    "latitude": 37.8611,
    "longitude": 27.8481
  },
  {
    "name": "T.C. Sağlık Bakanlığı Didim Devlet Hastanesi",
    "latitude": 37.3767,
    "longitude": 27.2150
  },
  {
    "name": "T.C. Sağlık Bakanlığı Aydın Atatürk Devlet Hastanesi",
    "latitude": 37.8547,
    "longitude": 27.8478
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bozdoğan Rasim Menteşe İlçe Devlet Hastanesi",
    "latitude": 37.5667,
    "longitude": 28.0647
  },
  {
    "name": "T.C. Sağlık Bakanlığı Aydın Kadın Doğum ve Çocuk Hastalıkları Hastanesi",
    "latitude": 37.8647,
    "longitude": 27.8475
  },
  {
    "name": "T.C. Sağlık Bakanlığı Germencik Devlet Hastanesi",
    "latitude": 37.9075,
    "longitude": 27.8592
  },
  {
    "name": "T.C. Sağlık Bakanlığı Koçarlı İlçe Devlet Hastanesi",
    "latitude": 37.6789,
    "longitude": 27.6886
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sultanhisar İlçe Devlet Hastanesi",
    "latitude": 37.7981,
    "longitude": 27.6658
  },
  {
    "name": "T.C. Sağlık Bakanlığı Buharkent İlçe Devlet Hastanesi",
    "latitude": 37.4875,
    "longitude": 28.1081
  },
  {
    "name": "T.C. Sağlık Bakanlığı Aydın Yenipazar İlçe Devlet Hastanesi",
    "latitude": 37.8622,
    "longitude": 27.8678
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karpuzlu İlçe Devlet Hastanesi",
    "latitude": 37.5947,
    "longitude": 27.4517
  },
  {
    "name": "T.C. Sağlık Bakanlığı Köşk İlçe Devlet Hastanesi",
    "latitude": 37.6736,
    "longitude": 27.6428
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kuyucak İlçe Devlet Hastanesi",
    "latitude": 37.7347,
    "longitude": 27.5994
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sındırgı Devlet Hastanesi",
    "latitude": 39.4658,
    "longitude": 28.2153
  },
  {
    "name": "T.C. Sağlık Bakanlığı Susurluk Devlet Hastanesi",
    "latitude": 39.4717,
    "longitude": 28.2328
  },
  {
    "name": "T.C. Sağlık Bakanlığı İvrindi Devlet Hastanesi",
    "latitude": 39.4717,
    "longitude": 27.6228
  },
  {
    "name": "T.C. Sağlık Bakanlığı Manyas Devlet Hastanesi",
    "latitude": 40.3442,
    "longitude": 27.8625
  },
  {
    "name": "T.C. Sağlık Bakanlığı Erdek Neyyire Sıtkı Devlet Hastanesi",
    "latitude": 40.5633,
    "longitude": 27.4289
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gönen Devlet Hastanesi",
    "latitude": 40.1850,
    "longitude": 27.3992
  },{
    "name": "T.C. Sağlık Bakanlığı Havran Devlet Hastanesi",
    "latitude": 39.5431,
    "longitude": 27.6592
  },
  {
    "name": "T.C. Sağlık Bakanlığı Burhaniye Devlet Hastanesi",
    "latitude": 39.5067,
    "longitude": 26.9703
  },
  {
    "name": "T.C. Sağlık Bakanlığı Dursunbey Devlet Hastanesi",
    "latitude": 39.7156,
    "longitude": 28.8444
  },
  {
    "name": "T.C. Sağlık Bakanlığı Edremit Devlet Hastanesi",
    "latitude": 39.5778,
    "longitude": 27.0094
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bigadiç Devlet Hastanesi",
    "latitude": 39.4797,
    "longitude": 28.4722
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ayvalık Devlet Hastanesi",
    "latitude": 39.3206,
    "longitude": 26.6544
  },
  {
    "name": "T.C. Sağlık Bakanlığı Balıkesir Devlet Hastanesi",
    "latitude": 39.6403,
    "longitude": 27.8892
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bandırma Eğitim ve Araştırma Hastanesi",
    "latitude": 40.3639,
    "longitude": 27.9767
  },
  {
    "name": "T.C. Sağlık Bakanlığı Balıkesir Atatürk Şehir Hastanesi",
    "latitude": 39.6425,
    "longitude": 27.8928
  },
  {
    "name": "T.C. Sağlık Bakanlığı Savaştepe Devlet Hastanesi",
    "latitude": 39.5956,
    "longitude": 28.4333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Balıkesir Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 39.6422,
    "longitude": 27.8878
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gömeç İlçe Devlet Hastanesi",
    "latitude": 39.4547,
    "longitude": 26.6572
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kepsut İlçe Devlet Hastanesi",
    "latitude": 39.5836,
    "longitude": 28.4961
  },
  {
    "name": "T.C. Sağlık Bakanlığı Balya İlçe Devlet Hastanesi",
    "latitude": 39.4456,
    "longitude": 27.9672
  },
  {
    "name": "T.C. Sağlık Bakanlığı Marmara Süleyman İlik İlçe Devlet Hastanesi",
    "latitude": 40.4881,
    "longitude": 27.3931
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bartın Devlet Hastanesi",
    "latitude": 41.6356,
    "longitude": 32.3211
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ulus Şehit Piyade Er Hasan Hüseyin Oğuz İlçe Devlet Hastanesi",
    "latitude": 41.5733,
    "longitude": 32.4975
  },
  {
    "name": "T.C. Sağlık Bakanlığı Amasra İlçe Devlet Hastanesi",
    "latitude": 41.2786,
    "longitude": 32.0344
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kozluk Devlet Hastanesi",
    "latitude": 38.1942,
    "longitude": 41.0833
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sason Devlet Hastanesi",
    "latitude": 37.8747,
    "longitude": 41.4292
  },{
    "name": "T.C. Sağlık Bakanlığı Gercüş Devlet Hastanesi",
    "latitude": 37.7483,
    "longitude": 41.1478
  },
  {
    "name": "T.C. Sağlık Bakanlığı Batman Eğitim ve Araştırma Hastanesi",
    "latitude": 37.8872,
    "longitude": 41.1350
  },
  {
    "name": "T.C. Sağlık Bakanlığı Batman İluh Devlet Hastanesi",
    "latitude": 37.8619,
    "longitude": 41.1494
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hasankeyf İlçe Devlet Hastanesi",
    "latitude": 37.3686,
    "longitude": 41.3442
  },
  {
    "name": "T.C. Sağlık Bakanlığı Beşiri İlçe Devlet Hastanesi",
    "latitude": 37.9033,
    "longitude": 41.2319
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bayburt Devlet Hastanesi",
    "latitude": 40.2561,
    "longitude": 40.2575
  },
  {
    "name": "T.C. Sağlık Bakanlığı Söğüt Devlet Hastanesi",
    "latitude": 40.0097,
    "longitude": 29.0847
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bozüyük Devlet Hastanesi",
    "latitude": 40.1342,
    "longitude": 30.0306
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bilecik Eğitim ve Araştırma Hastanesi",
    "latitude": 40.1414,
    "longitude": 29.9783
  },
  {
    "name": "T.C. Sağlık Bakanlığı Osmaneli Mustafa Selahattin Çetintaş Devlet Hastanesi",
    "latitude": 40.1731,
    "longitude": 30.0172
  },
  {
    "name": "T.C. Sağlık Bakanlığı Pazaryeri İlçe Devlet Hastanesi",
    "latitude": 40.1072,
    "longitude": 29.8375
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gölpazarı İlçe Devlet Hastanesi",
    "latitude": 40.0811,
    "longitude": 30.0800
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bilecik Yenipazar İlçe Devlet Hastanesi",
    "latitude": 40.2042,
    "longitude": 29.5917
  },
  {
    "name": "T.C. Sağlık Bakanlığı İnhisar İlçe Devlet Hastanesi",
    "latitude": 40.0078,
    "longitude": 29.4142
  },
  {
    "name": "T.C. Sağlık Bakanlığı Solhan Devlet Hastanesi",
    "latitude": 38.9892,
    "longitude": 40.3944
  },
  {
    "name": "T.C. Sağlık Bakanlığı Genç Devlet Hastanesi",
    "latitude": 38.9961,
    "longitude": 40.3097
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bingöl Devlet Hastanesi",
    "latitude": 38.8867,
    "longitude": 40.4942
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bingöl Kadın Doğum ve Çocuk Hastalıkları Hastanesi",
    "latitude": 38.8875,
    "longitude": 40.4906
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karlıova Devlet Hastanesi",
    "latitude": 39.3636,
    "longitude": 40.4447
  },
  {
    "name": "T.C. Sağlık Bakanlığı Adaklı İlçe Devlet Hastanesi",
    "latitude": 39.5206,
    "longitude": 40.3583
  },{
    "name": "T.C. Sağlık Bakanlığı Kiğı İlçe Devlet Hastanesi",
    "latitude": 39.0542,
    "longitude": 41.2689
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ahlat Devlet Hastanesi",
    "latitude": 38.9733,
    "longitude": 42.4694
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tatvan Devlet Hastanesi",
    "latitude": 38.5361,
    "longitude": 42.2706
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bitlis Devlet Hastanesi",
    "latitude": 38.3942,
    "longitude": 42.1078
  },
  {
    "name": "T.C. Sağlık Bakanlığı Adilcevaz Onkoloji Hastanesi",
    "latitude": 38.9597,
    "longitude": 42.6233
  },
  {
    "name": "T.C. Sağlık Bakanlığı Güroymak Devlet Hastanesi",
    "latitude": 38.6275,
    "longitude": 42.0819
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hizan Devlet Hastanesi",
    "latitude": 38.6553,
    "longitude": 42.5072
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mutki İlçe Devlet Hastanesi",
    "latitude": 38.6819,
    "longitude": 42.4067
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bolu İzzet Baysal Eğitim ve Araştırma Hastanesi",
    "latitude": 40.7231,
    "longitude": 31.6119
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bolu İzzet Baysal Fizik Tedavi ve Rehabilitasyon Eğitim ve Araştırma Hastanesi",
    "latitude": 40.7231,
    "longitude": 31.6119
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bolu İzzet Baysal Ruh Sağlığı ve Hastalıkları Hastanesi",
    "latitude": 40.7231,
    "longitude": 31.6119
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gerede Devlet Hastanesi",
    "latitude": 40.6250,
    "longitude": 31.5353
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mudurnu İlçe Devlet Hastanesi",
    "latitude": 40.5639,
    "longitude": 31.2444
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bolu İzzet Baysal Devlet Hastanesi",
    "latitude": 40.7231,
    "longitude": 31.6119
  },
  {
    "name": "T.C. Sağlık Bakanlığı Göynük Şehit Ziya Sarpkaya İlçe Devlet Hastanesi",
    "latitude": 40.4861,
    "longitude": 31.9375
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mengen Dr.Mustafa Körpeoğlu İlçe Devlet Hastanesi",
    "latitude": 40.5300,
    "longitude": 31.8853
  },
  {
    "name": "T.C. Sağlık Bakanlığı Yeniçağa İlçe Devlet Hastanesi",
    "latitude": 40.3797,
    "longitude": 31.9894
  },
  {
    "name": "T.C. Sağlık Bakanlığı Yeşilova Devlet Hastanesi",
    "latitude": 37.5281,
    "longitude": 30.9519
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gölhisar Devlet Hastanesi",
    "latitude": 37.4964,
    "longitude": 30.8686
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bucak Devlet Hastanesi",
    "latitude": 37.7353,
    "longitude": 30.1078
  },{
    "name": "T.C. Sağlık Bakanlığı Burdur Devlet Hastanesi",
    "latitude": 37.4653,
    "longitude": 30.0572
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tefenni İlçe Devlet Hastanesi",
    "latitude": 37.4772,
    "longitude": 29.5539
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ağlasun İlçe Devlet Hastanesi",
    "latitude": 37.5247,
    "longitude": 30.3886
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karamanlı İlçe Devlet Hastanesi",
    "latitude": 37.1986,
    "longitude": 30.3489
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çavdır İlçe Devlet Hastanesi",
    "latitude": 37.4911,
    "longitude": 30.3028
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bursa Ağız ve Diş Sağlığı Eğitim ve Araştırma Hastanesi",
    "latitude": 40.1908,
    "longitude": 29.0729
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bursa Yüksek İhtisas Eğitim ve Araştırma Hastanesi",
    "latitude": 40.1689,
    "longitude": 29.0461
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bursa Şehir Hastanesi",
    "latitude": 40.1936,
    "longitude": 29.0697
  },
  {
    "name": "T.C. Sağlık Bakanlığı Yenişehir Devlet Hastanesi",
    "latitude": 40.3708,
    "longitude": 29.6172
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mudanya Devlet Hastanesi",
    "latitude": 40.3953,
    "longitude": 28.8936
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mustafakemalpaşa Devlet Hastanesi",
    "latitude": 40.2114,
    "longitude": 28.5911
  },
  {
    "name": "T.C. Sağlık Bakanlığı Orhaneli Devlet Hastanesi",
    "latitude": 40.0442,
    "longitude": 28.4917
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karacabey Devlet Hastanesi",
    "latitude": 40.5889,
    "longitude": 28.3686
  },
  {
    "name": "T.C. Sağlık Bakanlığı İnegöl Devlet Hastanesi",
    "latitude": 40.0814,
    "longitude": 29.5972
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gemlik Devlet Hastanesi",
    "latitude": 40.3850,
    "longitude": 28.9872
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bursa Ali Osman Sönmez Onkoloji Hastanesi",
    "latitude": 40.1819,
    "longitude": 29.0694
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bursa Dörtçelik Çocuk Hastalıkları Hastanesi",
    "latitude": 40.1878,
    "longitude": 29.0720
  },
  {
    "name": "T.C. Sağlık Bakanlığı Orhangazi Devlet Hastanesi",
    "latitude": 40.4233,
    "longitude": 29.6469
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bursa Dr. Ayten Bozkaya Spastik Çocuklar Hastanesi ve Rehabilitasyon Merkezi",
    "latitude": 40.1794,
    "longitude": 29.0667
  },
  {
    "name": "T.C. Sağlık Bakanlığı İznik Devlet Hastanesi",
    "latitude": 40.4397,
    "longitude": 29.7172
  },{
    "name": "T.C. Sağlık Bakanlığı Bursa Çekirge Devlet Hastanesi",
    "latitude": 40.1802,
    "longitude": 29.0625
  },
  {
    "name": "T.C. Sağlık Bakanlığı İnegöl Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 40.0825,
    "longitude": 29.5969
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gürsu Cüneyt Yıldız Devlet Hastanesi",
    "latitude": 40.2356,
    "longitude": 29.0669
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kestel Devlet Hastanesi",
    "latitude": 40.2450,
    "longitude": 29.3581
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bursa İlker Çelikcan Fizik Tedavi ve Rehabilitasyon Hastanesi",
    "latitude": 40.1810,
    "longitude": 29.0733
  },
  {
    "name": "T.C. Sağlık Bakanlığı Büyükorhan İlçe Devlet Hastanesi",
    "latitude": 40.0106,
    "longitude": 28.7369
  },
  {
    "name": "T.C. Sağlık Bakanlığı Keles İlçe Devlet Hastanesi",
    "latitude": 40.0919,
    "longitude": 28.8606
  },
  {
    "name": "T.C. Sağlık Bakanlığı Harmancık İlçe Devlet Hastanesi",
    "latitude": 39.8556,
    "longitude": 28.9731
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gökçeada Devlet Hastanesi",
    "latitude": 40.2575,
    "longitude": 26.2800
  },
  {
    "name": "T.C. Sağlık Bakanlığı Lapseki Devlet Hastanesi",
    "latitude": 40.1247,
    "longitude": 26.3336
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çanakkale Yenice Devlet Hastanesi",
    "latitude": 40.0692,
    "longitude": 27.1328
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ezine Devlet Hastanesi",
    "latitude": 40.3314,
    "longitude": 26.6811
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gelibolu Şehit Koray Onay Devlet Hastanesi",
    "latitude": 40.3592,
    "longitude": 26.4097
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çan Devlet Hastanesi",
    "latitude": 40.1511,
    "longitude": 27.0000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çanakkale Mehmet Akif Ersoy Devlet Hastanesi",
    "latitude": 40.1490,
    "longitude": 26.4131
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çanakkale Ayvacık Devlet Hastanesi",
    "latitude": 40.2314,
    "longitude": 26.3806
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bayramiç Devlet Hastanesi",
    "latitude": 40.1264,
    "longitude": 27.1528
  },
  {
    "name": "T.C. Sağlık Bakanlığı Biga Devlet Hastanesi",
    "latitude": 40.1378,
    "longitude": 27.0025
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eceabat İlçe Devlet Hastanesi",
    "latitude": 40.2167,
    "longitude": 26.2222
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ilgaz Devlet Hastanesi",
    "latitude": 40.7333,
    "longitude": 33.9825
  },{
    "name": "T.C. Sağlık Bakanlığı Çerkeş Devlet Hastanesi",
    "latitude": 40.5425,
    "longitude": 33.5972
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çankırı Devlet Hastanesi",
    "latitude": 40.6000,
    "longitude": 33.6111
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kurşunlu Devlet Hastanesi",
    "latitude": 40.5314,
    "longitude": 33.7194
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kızılırmak İlçe Devlet Hastanesi",
    "latitude": 40.4411,
    "longitude": 34.5078
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şabanözü Dr. Sami Baran İlçe Devlet Hastanesi",
    "latitude": 40.7275,
    "longitude": 33.3172
  },
  {
    "name": "T.C. Sağlık Bakanlığı Orta İlçe Devlet Hastanesi",
    "latitude": 40.3533,
    "longitude": 33.9700
  },
  {
    "name": "T.C. Sağlık Bakanlığı Atkaracalar İlçe Devlet Hastanesi",
    "latitude": 40.4236,
    "longitude": 33.9569
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çorum Erol Olçok Eğitim ve Araştırma Hastanesi",
    "latitude": 40.5792,
    "longitude": 34.9556
  },
  {
    "name": "T.C. Sağlık Bakanlığı Osmancık Devlet Hastanesi",
    "latitude": 40.3594,
    "longitude": 35.2275
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sungurlu Devlet Hastanesi",
    "latitude": 40.4828,
    "longitude": 34.8694
  },
  {
    "name": "T.C. Sağlık Bakanlığı İskilip Atıf Hoca Devlet Hastanesi",
    "latitude": 40.4561,
    "longitude": 34.7672
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kargı Ahmet Hamdi Akpınar İlçe Devlet Hastanesi",
    "latitude": 40.6250,
    "longitude": 35.3378
  },
  {
    "name": "T.C. Sağlık Bakanlığı Alaca Devlet Hastanesi",
    "latitude": 40.6806,
    "longitude": 34.8611
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bayat Devlet Hastanesi",
    "latitude": 40.6814,
    "longitude": 34.7967
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çorum Göğüs Hastalıkları Hastanesi",
    "latitude": 40.5747,
    "longitude": 34.9478
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mecitözü İlçe Devlet Hastanesi",
    "latitude": 40.5950,
    "longitude": 35.2081
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çorum Ortaköy İlçe Devlet Hastanesi",
    "latitude": 40.4247,
    "longitude": 34.9953
  },
  {
    "name": "T.C. Sağlık Bakanlığı Oğuzlar İlçe Devlet Hastanesi",
    "latitude": 40.5647,
    "longitude": 35.0200
  },
  {
    "name": "T.C. Sağlık Bakanlığı Dodurga İlçe Devlet Hastanesi",
    "latitude": 40.5950,
    "longitude": 35.0200
  },
  {
    "name": "T.C. Sağlık Bakanlığı Uğurludağ Şehit Sami Saygı İlçe Devlet Hastanesi",
    "latitude": 40.4311,
    "longitude": 34.9286
  },{
    "name": "T.C. Sağlık Bakanlığı Boğazkale İlçe Devlet Hastanesi",
    "latitude": 40.0125,
    "longitude": 34.5083
  },
  {
    "name": "T.C. Sağlık Bakanlığı Denizli Kale İlçe Devlet Hastanesi",
    "latitude": 37.5275,
    "longitude": 29.5147
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tavas Devlet Hastanesi",
    "latitude": 37.4400,
    "longitude": 29.3850
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çal Devlet Hastanesi",
    "latitude": 37.3544,
    "longitude": 29.3808
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çivril Şehit Hilmi Öz Devlet Hastanesi",
    "latitude": 37.5247,
    "longitude": 29.7033
  },
  {
    "name": "T.C. Sağlık Bakanlığı Buldan Göğüs Hastalıkları Hastanesi",
    "latitude": 37.8300,
    "longitude": 29.9136
  },
  {
    "name": "T.C. Sağlık Bakanlığı Acıpayam Devlet Hastanesi",
    "latitude": 37.2017,
    "longitude": 29.7028
  },
  {
    "name": "T.C. Sağlık Bakanlığı Denizli Devlet Hastanesi",
    "latitude": 37.7747,
    "longitude": 29.1406
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çameli İlçe Devlet Hastanesi",
    "latitude": 37.3486,
    "longitude": 29.8364
  },
  {
    "name": "T.C. Sağlık Bakanlığı Honaz İlçe Devlet Hastanesi",
    "latitude": 37.6850,
    "longitude": 29.1733
  },
  {
    "name": "T.C. Sağlık Bakanlığı Denizli Servergazi Devlet Hastanesi",
    "latitude": 37.6722,
    "longitude": 29.0742
  },
  {
    "name": "T.C. Sağlık Bakanlığı Denizli Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 37.7686,
    "longitude": 29.0964
  },
  {
    "name": "T.C. Sağlık Bakanlığı Serinhisar İlçe Devlet Hastanesi",
    "latitude": 37.4000,
    "longitude": 29.3317
  },
  {
    "name": "T.C. Sağlık Bakanlığı Güney İlçe Devlet Hastanesi",
    "latitude": 37.4364,
    "longitude": 29.5406
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çardak İlçe Devlet Hastanesi",
    "latitude": 37.7361,
    "longitude": 29.2689
  },
  {
    "name": "T.C. Sağlık Bakanlığı Diyarbakır Gazi Yaşargil Eğitim ve Araştırma Hastanesi",
    "latitude": 37.9261,
    "longitude": 40.1917
  },
  {
    "name": "T.C. Sağlık Bakanlığı Silvan Dr. Yusuf Azizoğlu Devlet Hastanesi",
    "latitude": 38.1247,
    "longitude": 40.5906
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bismil Devlet Hastanesi",
    "latitude": 37.8992,
    "longitude": 40.6083
  },
  {
    "name": "T.C. Sağlık Bakanlığı Diyarbakır Selahaddin Eyyubi Devlet Hastanesi",
    "latitude": 37.9075,
    "longitude": 40.1533
  },
  {
    "name": "T.C. Sağlık Bakanlığı Diyarbakır Çocuk Hastalıkları Hastanesi",
    "latitude": 37.9019,
    "longitude": 40.2286
  },{
    "name": "T.C. Sağlık Bakanlığı Ergani Devlet Hastanesi",
    "latitude": 38.2764,
    "longitude": 40.3497
  },
  {
    "name": "T.C. Sağlık Bakanlığı Diyarbakır Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 37.9075,
    "longitude": 40.1575
  },
  {
    "name": "T.C. Sağlık Bakanlığı Diyarbakır Dağ Kapı Devlet Hastanesi",
    "latitude": 37.8886,
    "longitude": 40.1639
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çermik Devlet Hastanesi",
    "latitude": 38.0278,
    "longitude": 39.3731
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çınar İlçe Devlet Hastanesi",
    "latitude": 37.8850,
    "longitude": 40.2881
  },
  {
    "name": "T.C. Sağlık Bakanlığı Dicle Devlet Hastanesi",
    "latitude": 37.6650,
    "longitude": 40.3297
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hani İlçe Devlet Hastanesi",
    "latitude": 38.1264,
    "longitude": 40.5908
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eğil İlçe Devlet Hastanesi",
    "latitude": 37.6564,
    "longitude": 40.2386
  },
  {
    "name": "T.C. Sağlık Bakanlığı Lice Halis Toprak Vakfı Devlet Hastanesi",
    "latitude": 38.3408,
    "longitude": 40.2836
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kulp Dr. Abdullah Biroğul İlçe Devlet Hastanesi",
    "latitude": 38.1386,
    "longitude": 40.7028
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hazro İlçe Devlet Hastanesi",
    "latitude": 38.1844,
    "longitude": 40.3411
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kocaköy İlçe Devlet Hastanesi",
    "latitude": 37.9983,
    "longitude": 40.4531
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çüngüş İlçe Devlet Hastanesi",
    "latitude": 37.6717,
    "longitude": 40.5008
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bismil Tepe İlçe Devlet Hastanesi",
    "latitude": 37.9333,
    "longitude": 40.6283
  },
  {
    "name": "T.C. Sağlık Bakanlığı Düzce Atatürk Devlet Hastanesi",
    "latitude": 40.8425,
    "longitude": 31.1628
  },
  {
    "name": "T.C. Sağlık Bakanlığı Akçakoca Devlet Hastanesi",
    "latitude": 41.4417,
    "longitude": 31.1064
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kaynaşlı İlçe Devlet Hastanesi",
    "latitude": 40.9031,
    "longitude": 31.0175
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gümüşova İlçe Devlet Hastanesi",
    "latitude": 40.6722,
    "longitude": 30.7969
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gölyaka İlçe Devlet Hastanesi",
    "latitude": 40.8058,
    "longitude": 31.2692
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çilimli İlçe Devlet Hastanesi",
    "latitude": 40.8247,
    "longitude": 31.3147
  }, {
    "name": "T.C. Sağlık Bakanlığı Yığılca İlçe Devlet Hastanesi",
    "latitude": 40.9125,
    "longitude": 31.1919
  },
  {
    "name": "T.C. Sağlık Bakanlığı Edirne Sultan 1. Murat Devlet Hastanesi",
    "latitude": 41.6797,
    "longitude": 26.5619
  },
  {
    "name": "T.C. Sağlık Bakanlığı Uzunköprü Devlet Hastanesi",
    "latitude": 41.1019,
    "longitude": 26.7114
  },
  {
    "name": "T.C. Sağlık Bakanlığı Keşan Devlet Hastanesi",
    "latitude": 40.8483,
    "longitude": 26.6047
  },
  {
    "name": "T.C. Sağlık Bakanlığı İpsala Devlet Hastanesi",
    "latitude": 40.7258,
    "longitude": 26.4542
  },
  {
    "name": "T.C. Sağlık Bakanlığı Enez İlçe Devlet Hastanesi",
    "latitude": 40.9764,
    "longitude": 26.2950
  },
  {
    "name": "T.C. Sağlık Bakanlığı Süloğlu İlçe Devlet Hastanesi",
    "latitude": 41.2886,
    "longitude": 26.3911
  },
  {
    "name": "T.C. Sağlık Bakanlığı Meriç İlçe Devlet Hastanesi",
    "latitude": 41.0886,
    "longitude": 26.3436
  },
  {
    "name": "T.C. Sağlık Bakanlığı Lalapaşa İlçe Devlet Hastanesi",
    "latitude": 41.2992,
    "longitude": 26.2614
  },
  {
    "name": "T.C. Sağlık Bakanlığı Elazığ Fethi Sekin Şehir Hastanesi",
    "latitude": 38.6869,
    "longitude": 39.2247
  },
  {
    "name": "T.C. Sağlık Bakanlığı Elazığ Ruh Sağlığı ve Hastalıkları Hastanesi",
    "latitude": 38.6769,
    "longitude": 39.2356
  },
  {
    "name": "T.C. Sağlık Bakanlığı Palu İlçe Devlet Hastanesi",
    "latitude": 38.3722,
    "longitude": 39.1983
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karakoçan Devlet Hastanesi",
    "latitude": 38.4900,
    "longitude": 39.2997
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kovancılar Devlet Hastanesi",
    "latitude": 38.6347,
    "longitude": 39.2406
  },
  {
    "name": "T.C. Sağlık Bakanlığı Maden Şehit Cengiz Erdur İlçe Devlet Hastanesi",
    "latitude": 38.4286,
    "longitude": 39.3878
  },
  {
    "name": "T.C. Sağlık Bakanlığı Arıcak İlçe Devlet Hastanesi",
    "latitude": 38.3444,
    "longitude": 39.4442
  },
  {
    "name": "T.C. Sağlık Bakanlığı Elazığ Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 38.6792,
    "longitude": 39.2228
  },
  {
    "name": "T.C. Sağlık Bakanlığı Baskil İlçe Devlet Hastanesi",
    "latitude": 38.3728,
    "longitude": 39.2697
  },
  {
    "name": "T.C. Sağlık Bakanlığı Erzincan Mengücek Gazi Eğitim ve Araştırma Hastanesi",
    "latitude": 39.7503,
    "longitude": 39.1211
  },
  {
    "name": "T.C. Sağlık Bakanlığı Erzincan Ağız ve Diş Sağlığı Eğitim ve Araştırma Hastanesi",
    "latitude": 39.7450,
    "longitude": 39.1361
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tercan İlçe Devlet Hastanesi",
    "latitude": 39.3781,
    "longitude": 40.1419
  },
  {
    "name": "T.C. Sağlık Bakanlığı Refahiye Dr. Fahrettin Uğur İlçe Devlet Hastanesi",
    "latitude": 39.6353,
    "longitude": 39.6725
  },
  {
    "name": "T.C. Sağlık Bakanlığı Üzümlü İlçe Devlet Hastanesi",
    "latitude": 39.7383,
    "longitude": 39.7244
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çayırlı İlçe Devlet Hastanesi",
    "latitude": 39.6597,
    "longitude": 39.6789
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kemah İlçe Devlet Hastanesi",
    "latitude": 39.5511,
    "longitude": 39.7497
  },
  {
    "name": "T.C. Sağlık Bakanlığı İliç İlçe Devlet Hastanesi",
    "latitude": 39.2531,
    "longitude": 39.9256
  },
  {
    "name": "T.C. Sağlık Bakanlığı Otlukbeli İlçe Devlet Hastanesi",
    "latitude": 39.0608,
    "longitude": 40.0956
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kemaliye İlçe Devlet Hastanesi",
    "latitude": 38.7819,
    "longitude": 39.8661
  },
  {
    "name": "T.C. Sağlık Bakanlığı Erzurum Bölge Eğitim ve Araştırma Hastanesi",
    "latitude": 39.9119,
    "longitude": 41.2631
  },
  {
    "name": "T.C. Sağlık Bakanlığı Pasinler İbrahim Hakkı Devlet Hastanesi",
    "latitude": 39.8167,
    "longitude": 41.4075
  },
  {
    "name": "T.C. Sağlık Bakanlığı Oltu Devlet Hastanesi",
    "latitude": 40.1075,
    "longitude": 41.2425
  },
  {
    "name": "T.C. Sağlık Bakanlığı İspir Devlet Hastanesi",
    "latitude": 40.3800,
    "longitude": 41.2928
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hınıs Şehit Yavuz Yürekseven Devlet Hastanesi",
    "latitude": 40.0889,
    "longitude": 41.3122
  },
  {
    "name": "T.C. Sağlık Bakanlığı Horasan Devlet Hastanesi",
    "latitude": 40.2719,
    "longitude": 41.3858
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çat İlçe Devlet Hastanesi",
    "latitude": 39.8983,
    "longitude": 41.6106
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karaçoban İlçe Devlet Hastanesi",
    "latitude": 39.8597,
    "longitude": 41.7147
  },
  {
    "name": "T.C. Sağlık Bakanlığı Aşkale İlçe Devlet Hastanesi",
    "latitude": 40.1553,
    "longitude": 41.7453
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tortum İlçe Devlet Hastanesi",
    "latitude": 40.1492,
    "longitude": 41.9206
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karayazı Türk Eczacıları Birliği İlçe Devlet Hastanesi",
    "latitude": 40.1936,
    "longitude": 41.9778
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tekman Şehit Piyade Çavuş Muhammet Binici Devlet Hastanesi",
    "latitude": 40.5236,
    "longitude": 41.6400
  },{
    "name": "T.C. Sağlık Bakanlığı Erzurum Mareşal Çakmak Devlet Hastanesi",
    "latitude": 39.9206,
    "longitude": 41.2700
  },
  {
    "name": "T.C. Sağlık Bakanlığı Narman İlçe Devlet Hastanesi",
    "latitude": 40.2325,
    "longitude": 41.4422
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şenkaya İlçe Devlet Hastanesi",
    "latitude": 40.1136,
    "longitude": 41.5544
  },
  {
    "name": "T.C. Sağlık Bakanlığı Köprüköy İlçe Devlet Hastanesi",
    "latitude": 40.3631,
    "longitude": 41.4536
  },
  {
    "name": "T.C. Sağlık Bakanlığı Uzundere Şehit İhsan Erdoğan İlçe Devlet Hastanesi",
    "latitude": 40.4169,
    "longitude": 41.5286
  },
  {
    "name": "T.C. Sağlık Bakanlığı Olur İlçe Devlet Hastanesi",
    "latitude": 40.6900,
    "longitude": 41.5206
  },
  {
    "name": "T.C. Sağlık Bakanlığı Pazaryolu Hasan Basri Demirbağ İlçe Devlet Hastanesi",
    "latitude": 40.3900,
    "longitude": 41.5600
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sivrihisar Devlet Hastanesi",
    "latitude": 39.6194,
    "longitude": 30.4175
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çifteler Devlet Hastanesi",
    "latitude": 39.4581,
    "longitude": 30.8531
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eskişehir Yunus Emre Devlet Hastanesi",
    "latitude": 39.7769,
    "longitude": 30.5228
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eskişehir Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 39.7742,
    "longitude": 30.5206
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eskişehir Şehir Hastanesi",
    "latitude": 39.7847,
    "longitude": 30.5461
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mihalıççık Gün Sazak İlçe Devlet Hastanesi",
    "latitude": 39.5494,
    "longitude": 30.8722
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mahmudiye İlçe Devlet Hastanesi",
    "latitude": 39.5275,
    "longitude": 30.7425
  },
  {
    "name": "T.C. Sağlık Bakanlığı Alpu İlçe Devlet Hastanesi",
    "latitude": 39.5500,
    "longitude": 30.7000
  },
  {
    "name": "T.C. Sağlık Bakanlığı Günyüzü Şehit Melih Özcan İlçe Devlet Hastanesi",
    "latitude": 39.5486,
    "longitude": 30.4556
  },
  {
    "name": "T.C. Sağlık Bakanlığı Beylikova İlçe Devlet Hastanesi",
    "latitude": 39.7428,
    "longitude": 30.7592
  },
  {
    "name": "T.C. Sağlık Bakanlığı Nizip Devlet Hastanesi",
    "latitude": 37.0714,
    "longitude": 37.3586
  },
  {
    "name": "T.C. Sağlık Bakanlığı İslahiye Devlet Hastanesi",
    "latitude": 37.0411,
    "longitude": 37.3697
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karkamış Şehit Fuat Oğuzcan İlçe Devlet Hastanesi",
    "latitude": 37.1019,
    "longitude": 37.4917
  },{
    "name": "T.C. Sağlık Bakanlığı Yavuzeli İlçe Devlet Hastanesi",
    "latitude": 37.4594,
    "longitude": 37.3842
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gaziantep 25 Aralık Devlet Hastanesi",
    "latitude": 37.0663,
    "longitude": 37.3834
  },
  {
    "name": "T.C. Sağlık Bakanlığı Oğuzeli İlçe Devlet Hastanesi",
    "latitude": 37.1850,
    "longitude": 37.4706
  },
  {
    "name": "T.C. Sağlık Bakanlığı Araban İlçe Devlet Hastanesi",
    "latitude": 37.2247,
    "longitude": 37.2339
  },
  {
    "name": "T.C. Sağlık Bakanlığı Nurdağı İlçe Devlet Hastanesi",
    "latitude": 37.0656,
    "longitude": 37.5461
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gaziantep Şehitkamil Devlet Hastanesi",
    "latitude": 37.0644,
    "longitude": 37.3767
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şahinbey Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 37.0669,
    "longitude": 37.3811
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gaziantep Abdulkadir Yüksel Devlet Hastanesi",
    "latitude": 37.0692,
    "longitude": 37.3700
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gaziantep Cengiz Gökçek Kadın Doğum ve Çocuk Hastalıkları Hastanesi",
    "latitude": 37.0750,
    "longitude": 37.3861
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gaziantep Dr. Ersin Arslan Eğitim ve Araştırma Hastanesi",
    "latitude": 37.0733,
    "longitude": 37.3867
  },
  {
    "name": "T.C. Sağlık Bakanlığı Giresun Prof. Dr. A. İlhan Özdemir Devlet Hastanesi",
    "latitude": 40.9106,
    "longitude": 38.2872
  },
  {
    "name": "T.C. Sağlık Bakanlığı Giresun Kadın Doğum ve Çocuk Hastalıkları Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9111,
    "longitude": 38.2900
  },
  {
    "name": "T.C. Sağlık Bakanlığı Giresun Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9094,
    "longitude": 38.2897
  },
  {
    "name": "T.C. Sağlık Bakanlığı Giresun Dr. Ali Menekşe Göğüs Hastalıkları Hastanesi",
    "latitude": 40.9125,
    "longitude": 38.2875
  },
  {
    "name": "T.C. Sağlık Bakanlığı Giresun Fizik Tedavi ve Rehabilitasyon Merkezi",
    "latitude": 40.9122,
    "longitude": 38.2894
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şebinkarahisar Devlet Hastanesi",
    "latitude": 40.2900,
    "longitude": 38.6400
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tirebolu Devlet Hastanesi",
    "latitude": 40.7447,
    "longitude": 38.6828
  },
  {
    "name": "T.C. Sağlık Bakanlığı Espiye Devlet Hastanesi",
    "latitude": 40.7731,
    "longitude": 38.4550
  },
  {
    "name": "T.C. Sağlık Bakanlığı Görele Op. Dr. Ergun Özdemir Devlet Hastanesi",
    "latitude": 40.7528,
    "longitude": 38.5322
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bulancak Devlet Hastanesi",
    "latitude": 40.9717,
    "longitude": 38.3406
  },{
    "name": "T.C. Sağlık Bakanlığı Bulancak Devlet Hastanesi",
    "latitude": 40.9717,
    "longitude": 38.3406
  },
  {
    "name": "T.C. Sağlık Bakanlığı Yağlıdere İlçe Devlet Hastanesi",
    "latitude": 40.8697,
    "longitude": 38.5311
  },
  {
    "name": "T.C. Sağlık Bakanlığı Alucra İlçe Devlet Hastanesi",
    "latitude": 40.5589,
    "longitude": 38.4911
  },
  {
    "name": "T.C. Sağlık Bakanlığı Dereli İlçe Devlet Hastanesi",
    "latitude": 40.8111,
    "longitude": 38.8778
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eynesil İlçe Devlet Hastanesi",
    "latitude": 40.8939,
    "longitude": 38.5744
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çamoluk İlçe Devlet Hastanesi",
    "latitude": 40.5100,
    "longitude": 38.6028
  },
  {
    "name": "T.C. Sağlık Bakanlığı Güce İlçe Devlet Hastanesi",
    "latitude": 40.7461,
    "longitude": 38.7608
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gümüşhane Devlet Hastanesi",
    "latitude": 40.4600,
    "longitude": 39.4728
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şiran Devlet Hastanesi",
    "latitude": 40.3833,
    "longitude": 39.1500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kelkit Devlet Hastanesi",
    "latitude": 40.3306,
    "longitude": 39.5086
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kürtün İlçe Devlet Hastanesi",
    "latitude": 40.4797,
    "longitude": 39.3014
  },
  {
    "name": "T.C. Sağlık Bakanlığı Torul İlçe Devlet Hastanesi",
    "latitude": 40.6217,
    "longitude": 39.5747
  },
  {
    "name": "T.C. Sağlık Bakanlığı Köse İlçe Devlet Hastanesi",
    "latitude": 40.5933,
    "longitude": 39.2986
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şemdinli Devlet Hastanesi",
    "latitude": 37.2972,
    "longitude": 44.6822
  },
  {
    "name": "T.C. Sağlık Bakanlığı Yüksekova Devlet Hastanesi",
    "latitude": 37.5731,
    "longitude": 44.3106
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hakkari Devlet Hastanesi",
    "latitude": 37.5714,
    "longitude": 43.7378
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çukurca Devlet Hastanesi",
    "latitude": 37.4850,
    "longitude": 43.0564
  },
  {
    "name": "T.C. Sağlık Bakanlığı Derecik Devlet Hastanesi",
    "latitude": 37.4686,
    "longitude": 43.1275
  },
  {
    "name": "T.C. Sağlık Bakanlığı Reyhanlı Devlet Hastanesi",
    "latitude": 36.6450,
    "longitude": 36.7828
  },
  {
    "name": "T.C. Sağlık Bakanlığı Samandağ Devlet Hastanesi",
    "latitude": 36.2842,
    "longitude": 36.1728
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kırıkhan Devlet Hastanesi",
    "latitude": 36.9061,
    "longitude": 36.8386
  },{
    "name": "T.C. Sağlık Bakanlığı Dörtyol Devlet Hastanesi",
    "latitude": 36.4531,
    "longitude": 36.2100
  },
  {
    "name": "T.C. Sağlık Bakanlığı İskenderun Devlet Hastanesi",
    "latitude": 36.5892,
    "longitude": 36.1661
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hassa Devlet Hastanesi",
    "latitude": 36.3922,
    "longitude": 36.7306
  },
  {
    "name": "T.C. Sağlık Bakanlığı Altınözü Devlet Hastanesi",
    "latitude": 36.4397,
    "longitude": 36.2033
  },
  {
    "name": "T.C. Sağlık Bakanlığı Erzin Devlet Hastanesi",
    "latitude": 36.0861,
    "longitude": 36.2833
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kumlu İlçe Devlet Hastanesi",
    "latitude": 36.3372,
    "longitude": 36.8144
  },
  {
    "name": "T.C. Sağlık Bakanlığı Arsuz Devlet Hastanesi",
    "latitude": 36.1197,
    "longitude": 36.1350
  },
  {
    "name": "T.C. Sağlık Bakanlığı Yayladağı Devlet Hastanesi",
    "latitude": 36.3100,
    "longitude": 36.1578
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hatay Eğitim ve Araştırma Hastanesi",
    "latitude": 36.2761,
    "longitude": 36.1706
  },
  {
    "name": "T.C. Sağlık Bakanlığı Iğdır Dr.Nevruz Erez Devlet Hastanesi",
    "latitude": 39.9294,
    "longitude": 44.0497
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tuzluca İlçe Devlet Hastanesi",
    "latitude": 40.0900,
    "longitude": 43.9828
  },
  {
    "name": "T.C. Sağlık Bakanlığı Aralık İlçe Devlet Hastanesi",
    "latitude": 40.5614,
    "longitude": 43.6194
  },
  {
    "name": "T.C. Sağlık Bakanlığı Yalvaç Devlet Hastanesi",
    "latitude": 37.7817,
    "longitude": 30.6994
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şarkikaraağaç Dr. Sadettin Bilgiç Devlet Hastanesi",
    "latitude": 37.4536,
    "longitude": 31.1786
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eğirdir Kemik Eklem Hastalıkları Tedavi ve Rehabilitasyon Hastanesi",
    "latitude": 37.9317,
    "longitude": 30.8581
  },
  {
    "name": "T.C. Sağlık Bakanlığı Isparta Şehir Hastanesi",
    "latitude": 37.7489,
    "longitude": 30.5350
  },
  {
    "name": "T.C. Sağlık Bakanlığı Isparta Şehit Yunus Emre Devlet Hastanesi",
    "latitude": 37.7667,
    "longitude": 30.5494
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gelendost İlçe Devlet Hastanesi",
    "latitude": 37.6906,
    "longitude": 30.5608
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sütçüler İlçe Devlet Hastanesi",
    "latitude": 37.6736,
    "longitude": 30.7078
  },
  {
    "name": "T.C. Sağlık Bakanlığı Senirkent İlçe Devlet Hastanesi",
    "latitude": 37.6067,
    "longitude": 30.6778
  },{
    "name": "T.C. Sağlık Bakanlığı Keçiborlu İlçe Devlet Hastanesi",
    "latitude": 37.6556,
    "longitude": 30.5153
  },
  {
    "name": "T.C. Sağlık Bakanlığı Uluborlu İlçe Devlet Hastanesi",
    "latitude": 37.6181,
    "longitude": 30.6247
  },
  {
    "name": "T.C. Sağlık Bakanlığı Pendik Eğitim ve Araştırma Hastanesi",
    "latitude": 40.8820,
    "longitude": 29.2639
  },
  {
    "name": "T.C. Sağlık Bakanlığı Göztepe Prof. Dr. Süleyman Yalçın Şehir Hastanesi",
    "latitude": 40.9828,
    "longitude": 29.1072
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Fizik Tedavi ve Rehabilitasyon Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0201,
    "longitude": 28.9644
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Zeynep Kamil Kadın ve Çocuk Hastalıkları Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9986,
    "longitude": 29.2000
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Haydarpaşa Numune Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9850,
    "longitude": 29.0297
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Yedikule Göğüs Hastalıkları ve Göğüs Cerrahisi Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9703,
    "longitude": 28.9656
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şişli Hamidiye Etfal Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0622,
    "longitude": 28.9817
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Baltalimanı Metin Sabancı Kemik Hastalıkları Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0867,
    "longitude": 29.0033
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kartal Dr. Lütfi Kırdar Şehir Hastanesi",
    "latitude": 40.8575,
    "longitude": 29.2078
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Haseki Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0114,
    "longitude": 28.9411
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kartal Koşuyolu Yüksek İhtisas Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9914,
    "longitude": 29.2125
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gaziosmanpaşa Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0650,
    "longitude": 28.9286
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bakırköy Dr. Sadi Konuk Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9647,
    "longitude": 28.8444
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Prof. Dr. Mazhar Osman Ruh Sağlığı ve Sinir Hastalıkları Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0403,
    "longitude": 28.7847
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Dr. Siyami Ersek Göğüs Kalp ve Damar Cerrahisi Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0347,
    "longitude": 28.9417
  },
  {
    "name": "T.C. Sağlık Bakanlığı Beyoğlu Göz Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0278,
    "longitude": 28.9797
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ümraniye Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9919,
    "longitude": 29.1222
  },
  {
    "name": "T.C. Sağlık Bakanlığı Erenköy Ruh ve Sinir Hastalıkları Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9981,
    "longitude": 29.1014
  },{
    "name": "T.C. Sağlık Bakanlığı İstanbul Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0057,
    "longitude": 28.9539
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Prof. Dr. Cemil Taşcıoğlu Şehir Hastanesi",
    "latitude": 41.0400,
    "longitude": 28.9596
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Süreyyapaşa Göğüs Hastalıkları ve Göğüs Cerrahisi Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9867,
    "longitude": 29.1361
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Fatih Sultan Mehmet Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0206,
    "longitude": 28.9097
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bağcılar Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0222,
    "longitude": 28.8625
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Mehmet Akif Ersoy Göğüs Kalp ve Damar Cerrahisi Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9944,
    "longitude": 28.8000
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Kanuni Sultan Süleyman Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0147,
    "longitude": 28.8664
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Sultan 2. Abdülhamid Han Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0669,
    "longitude": 28.8706
  },
  {
    "name": "T.C. Sağlık Bakanlığı Başakşehir Çam ve Sakura Şehir Hastanesi",
    "latitude": 41.1444,
    "longitude": 28.8297
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sancaktepe Şehit Prof. Dr. İlhan Varank Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9792,
    "longitude": 29.2325
  },
  {
    "name": "T.C. Sağlık Bakanlığı Taksim Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0356,
    "longitude": 28.9831
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sultanbeyli Devlet Hastanesi",
    "latitude": 40.9806,
    "longitude": 29.2269
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şile Devlet Hastanesi",
    "latitude": 41.1536,
    "longitude": 29.5647
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çatalca İlyas Çokay Devlet Hastanesi",
    "latitude": 41.2181,
    "longitude": 28.4983
  },
  {
    "name": "T.C. Sağlık Bakanlığı Silivri Devlet Hastanesi",
    "latitude": 41.1392,
    "longitude": 28.5336
  },
  {
    "name": "T.C. Sağlık Bakanlığı Pendik Devlet Hastanesi",
    "latitude": 40.8692,
    "longitude": 29.2822
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstinye Devlet Hastanesi",
    "latitude": 41.1356,
    "longitude": 29.0314
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Lepra Deri ve Zührevi Hastalıkları Hastanesi",
    "latitude": 41.0258,
    "longitude": 28.9733
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bayrampaşa Devlet Hastanesi",
    "latitude": 41.0436,
    "longitude": 28.9394
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Ataşehir Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 40.9928,
    "longitude": 29.0956
  },
  {
    "name": "T.C. Sağlık Bakanlığı Beylikdüzü Devlet Hastanesi",
    "latitude": 41.0169,
    "longitude": 28.6486
  },
  {
    "name": "T.C. Sağlık Bakanlığı İstanbul Okmeydanı Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 41.0611,
    "longitude": 28.9792
  },
  {
    "name": "T.C. Sağlık Bakanlığı Erenköy Fizik Tedavi ve Rehabilitasyon Hastanesi",
    "latitude": 40.9908,
    "longitude": 29.1231
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eyüpsultan Devlet Hastanesi",
    "latitude": 41.0850,
    "longitude": 28.9292
  },
  {
    "name": "T.C. Sağlık Bakanlığı Beykoz Devlet Hastanesi",
    "latitude": 41.1986,
    "longitude": 29.1436
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tuzla Devlet Hastanesi",
    "latitude": 40.8661,
    "longitude": 29.2172
  },
  {
    "name": "T.C. Sağlık Bakanlığı Üsküdar Devlet Hastanesi",
    "latitude": 41.0225,
    "longitude": 29.0272
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kağıthane Devlet Hastanesi",
    "latitude": 41.0992,
    "longitude": 28.9900
  },
  {
    "name": "T.C. Sağlık Bakanlığı Başakşehir Devlet Hastanesi",
    "latitude": 41.1256,
    "longitude": 28.8422
  },
  {
    "name": "T.C. Sağlık Bakanlığı Esenyurt Necmi Kadıoğlu Devlet Hastanesi",
    "latitude": 41.0383,
    "longitude": 28.6356
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tacirler Eğitim Vakfı Sultanbeyli Ağız ve Diş Sağlığı Eğitim ve Araştırma Hastanesi",
    "latitude": 40.9761,
    "longitude": 29.2336
  },
  {
    "name": "T.C. Sağlık Bakanlığı Arnavutköy Devlet Hastanesi",
    "latitude": 41.1667,
    "longitude": 28.7533
  },
  {
    "name": "T.C. Sağlık Bakanlığı Beşiktaş Sait Çiftçi Devlet Hastanesi",
    "latitude": 41.0472,
    "longitude": 29.0197
  },
  {
    "name": "T.C. Sağlık Bakanlığı Pendik Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 40.8769,
    "longitude": 29.2736
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sultangazi Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 41.0850,
    "longitude": 28.9072
  },
  {
    "name": "T.C. Sağlık Bakanlığı Büyükçekmece Mimar Sinan Devlet Hastanesi",
    "latitude": 41.0183,
    "longitude": 28.6097
  },
  {
    "name": "T.C. Sağlık Bakanlığı Maltepe Devlet Hastanesi",
    "latitude": 40.9394,
    "longitude": 29.1517
  },
  {
    "name": "T.C. Sağlık Bakanlığı Marmara Ceza İnfaz Kurumu Devlet Hastanesi",
    "latitude": 40.9614,
    "longitude": 29.2222
  },
  {
    "name": "T.C. Sağlık Bakanlığı Esenler Kadın Doğum ve Çocuk Hastalıkları Hastanesi",
    "latitude": 41.0528,
    "longitude": 28.8569
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bahçelievler Devlet Hastanesi",
    "latitude": 41.0075,
    "longitude": 28.8583
  },{
    "name": "T.C. Sağlık Bakanlığı Avcılar Murat Kölük Devlet Hastanesi",
    "latitude": 40.9994,
    "longitude": 28.7139
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bağcılar Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 41.0528,
    "longitude": 28.8769
  },
  {
    "name": "T.C. Sağlık Bakanlığı Küçükçekmece Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 41.0078,
    "longitude": 28.7406
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çiğli Eğitim ve Araştırma Hastanesi",
    "latitude": 38.4708,
    "longitude": 27.1469
  },
  {
    "name": "T.C. Sağlık Bakanlığı Buca Seyfi Demirsoy Eğitim ve Araştırma Hastanesi",
    "latitude": 38.4850,
    "longitude": 27.1633
  },
  {
    "name": "T.C. Sağlık Bakanlığı İzmir Atatürk Eğitim ve Araştırma Hastanesi",
    "latitude": 38.4314,
    "longitude": 27.1444
  },
  {
    "name": "T.C. Sağlık Bakanlığı İzmir Dr. Suat Seren Göğüs Hastalıkları ve Cerrahisi Eğitim ve Araştırma Hastanesi",
    "latitude": 38.4433,
    "longitude": 27.1686
  },
  {
    "name": "T.C. Sağlık Bakanlığı İzmir Dr. Behçet Uz Çocuk Hastalıkları ve Cerrahisi Eğitim ve Araştırma Hastanesi",
    "latitude": 38.4272,
    "longitude": 27.1419
  },
  {
    "name": "T.C. Sağlık Bakanlığı İzmir Bozyaka Eğitim ve Araştırma Hastanesi",
    "latitude": 38.4669,
    "longitude": 27.1322
  },
  {
    "name": "T.C. Sağlık Bakanlığı İzmir Tepecik Eğitim ve Araştırma Hastanesi",
    "latitude": 38.4425,
    "longitude": 27.1531
  },
  {
    "name": "T.C. Sağlık Bakanlığı Torbalı Devlet Hastanesi",
    "latitude": 38.2139,
    "longitude": 27.3714
  },
  {
    "name": "T.C. Sağlık Bakanlığı Urla Devlet Hastanesi",
    "latitude": 38.3250,
    "longitude": 26.7069
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tire Devlet Hastanesi",
    "latitude": 38.2272,
    "longitude": 27.5367
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ödemiş Devlet Hastanesi",
    "latitude": 38.2800,
    "longitude": 27.5656
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kiraz Devlet Hastanesi",
    "latitude": 38.3572,
    "longitude": 27.6208
  },
  {
    "name": "T.C. Sağlık Bakanlığı Menemen Devlet Hastanesi",
    "latitude": 38.5583,
    "longitude": 27.0197
  },
  {
    "name": "T.C. Sağlık Bakanlığı Foça Devlet Hastanesi",
    "latitude": 38.6508,
    "longitude": 26.7475
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bergama Necla Mithat Öztüre Devlet Hastanesi",
    "latitude": 39.1161,
    "longitude": 27.1839
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bayındır Devlet Hastanesi",
    "latitude": 38.2475,
    "longitude": 27.6417
  },
  {
    "name": "T.C. Sağlık Bakanlığı İzmir Eğitim Diş Hastanesi",
    "latitude": 38.4364,
    "longitude": 27.1411
  },{
    "name": "T.C. Sağlık Bakanlığı İzmir Alsancak Nevvar Salih İşgören Devlet Hastanesi",
    "latitude": 38.4331,
    "longitude": 27.1425
  },
  {
    "name": "T.C. Sağlık Bakanlığı Selçuk Devlet Hastanesi",
    "latitude": 37.9633,
    "longitude": 27.3650
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çeşme Alper Çizgenakat Devlet Hastanesi",
    "latitude": 38.3064,
    "longitude": 26.3925
  },
  {
    "name": "T.C. Sağlık Bakanlığı Seferihisar Nejat Hepkon Devlet Hastanesi",
    "latitude": 38.9417,
    "longitude": 26.9381
  },
  {
    "name": "T.C. Sağlık Bakanlığı Aliağa Devlet Hastanesi",
    "latitude": 38.7308,
    "longitude": 26.9333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kemalpaşa Devlet Hastanesi",
    "latitude": 38.3278,
    "longitude": 27.1967
  },
  {
    "name": "T.C. Sağlık Bakanlığı Dikili Devlet Hastanesi",
    "latitude": 38.9500,
    "longitude": 26.8556
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bornova Türkan Özilhan Devlet Hastanesi",
    "latitude": 38.4792,
    "longitude": 27.2158
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kınık Devlet Hastanesi",
    "latitude": 38.8144,
    "longitude": 27.3950
  },
  {
    "name": "T.C. Sağlık Bakanlığı Menderes Devlet Hastanesi",
    "latitude": 38.3167,
    "longitude": 27.0908
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gaziemir Nevvar Salih İşgören Devlet Hastanesi",
    "latitude": 38.4606,
    "longitude": 27.0914
  },
  {
    "name": "T.C. Sağlık Bakanlığı Aliağa Ceza İnfaz Kurumları Kampüs Devlet Hastanesi",
    "latitude": 38.7333,
    "longitude": 26.9242
  },
  {
    "name": "T.C. Sağlık Bakanlığı Beydağ İlçe Devlet Hastanesi",
    "latitude": 38.2764,
    "longitude": 27.4300
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karaburun İlçe Devlet Hastanesi",
    "latitude": 38.4264,
    "longitude": 26.6647
  },
  {
    "name": "T.C. Sağlık Bakanlığı Göksun Devlet Hastanesi",
    "latitude": 37.2825,
    "longitude": 36.9708
  },
  {
    "name": "T.C. Sağlık Bakanlığı Pazarcık Devlet Hastanesi",
    "latitude": 37.3458,
    "longitude": 37.4219
  },
  {
    "name": "T.C. Sağlık Bakanlığı Andırın Devlet Hastanesi",
    "latitude": 37.3464,
    "longitude": 36.9800
  },
  {
    "name": "T.C. Sağlık Bakanlığı Elbistan Devlet Hastanesi",
    "latitude": 38.2786,
    "longitude": 37.4619
  },
  {
    "name": "T.C. Sağlık Bakanlığı Afşin Devlet Hastanesi",
    "latitude": 37.4083,
    "longitude": 37.2458
  },
  {
    "name": "T.C. Sağlık Bakanlığı Türkoğlu Dr. Kemal Beyazıt Devlet Hastanesi",
    "latitude": 37.2667,
    "longitude": 37.1000
  },{
    "name": "T.C. Sağlık Bakanlığı Kahramanmaraş Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 37.5736,
    "longitude": 36.9361
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çağlayancerit İlçe Devlet Hastanesi",
    "latitude": 37.5814,
    "longitude": 37.1447
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kahramanmaraş Necip Fazıl Şehir Hastanesi",
    "latitude": 37.5603,
    "longitude": 36.9347
  },
  {
    "name": "T.C. Sağlık Bakanlığı Nurhak İlçe Devlet Hastanesi",
    "latitude": 37.5864,
    "longitude": 37.3228
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ekinözü İlçe Devlet Hastanesi",
    "latitude": 37.3042,
    "longitude": 37.3997
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karabük Eğitim ve Araştırma Hastanesi",
    "latitude": 41.2069,
    "longitude": 32.6275
  },
  {
    "name": "T.C. Sağlık Bakanlığı Safranbolu Devlet Hastanesi",
    "latitude": 41.8967,
    "longitude": 32.6781
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karabük Yenice İlçe Devlet Hastanesi",
    "latitude": 41.3111,
    "longitude": 32.7800
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karabük Ağız ve Diş Sağlığı Eğitim ve Araştırma Hastanesi",
    "latitude": 41.2083,
    "longitude": 32.6333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eskipazar İlçe Devlet Hastanesi",
    "latitude": 41.1728,
    "longitude": 32.6036
  },
  {
    "name": "T.C. Sağlık Bakanlığı Eflani İlçe Devlet Hastanesi",
    "latitude": 41.3242,
    "longitude": 32.1736
  },
  {
    "name": "T.C. Sağlık Bakanlığı Karaman Eğitim ve Araştırma Hastanesi",
    "latitude": 37.1742,
    "longitude": 33.2214
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ermenek Devlet Hastanesi",
    "latitude": 36.8767,
    "longitude": 32.4297
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sarıveliler İlçe Devlet Hastanesi",
    "latitude": 37.5378,
    "longitude": 32.2831
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ayrancı İlçe Devlet Hastanesi",
    "latitude": 37.5489,
    "longitude": 32.7222
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kazımkarabekir İlçe Devlet Hastanesi",
    "latitude": 37.6847,
    "longitude": 33.2167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kağızman Devlet Hastanesi",
    "latitude": 40.2328,
    "longitude": 42.6619
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sarıkamış Devlet Hastanesi",
    "latitude": 40.1075,
    "longitude": 42.5247
  },
  {
    "name": "T.C. Sağlık Bakanlığı Harakani Devlet Hastanesi",
    "latitude": 40.3325,
    "longitude": 42.7750
  },
  {
    "name": "T.C. Sağlık Bakanlığı Selim İlçe Devlet Hastanesi",
    "latitude": 40.1928,
    "longitude": 42.5536
  },{
    "name": "T.C. Sağlık Bakanlığı Digor İlçe Devlet Hastanesi",
    "latitude": 40.1628,
    "longitude": 42.5375
  },
  {
    "name": "T.C. Sağlık Bakanlığı Arpaçay İlçe Devlet Hastanesi",
    "latitude": 40.4814,
    "longitude": 43.2364
  },
  {
    "name": "T.C. Sağlık Bakanlığı Akyaka İlçe Devlet Hastanesi",
    "latitude": 37.7869,
    "longitude": 28.3858
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kastamonu Eğitim ve Araştırma Hastanesi",
    "latitude": 41.3872,
    "longitude": 33.7769
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tosya Devlet Hastanesi",
    "latitude": 41.4428,
    "longitude": 34.9911
  },
  {
    "name": "T.C. Sağlık Bakanlığı İnebolu Devlet Hastanesi",
    "latitude": 41.2789,
    "longitude": 33.6936
  },
  {
    "name": "T.C. Sağlık Bakanlığı Taşköprü Devlet Hastanesi",
    "latitude": 41.5272,
    "longitude": 33.5844
  },
  {
    "name": "T.C. Sağlık Bakanlığı Cide İlçe Devlet Hastanesi",
    "latitude": 41.4872,
    "longitude": 33.9942
  },
  {
    "name": "T.C. Sağlık Bakanlığı Daday İlçe Devlet Hastanesi",
    "latitude": 41.2397,
    "longitude": 33.8781
  },
  {
    "name": "T.C. Sağlık Bakanlığı Devrekani İlçe Devlet Hastanesi",
    "latitude": 41.2419,
    "longitude": 33.3497
  },
  {
    "name": "T.C. Sağlık Bakanlığı Araç İlçe Devlet Hastanesi",
    "latitude": 41.4153,
    "longitude": 33.8436
  },
  {
    "name": "T.C. Sağlık Bakanlığı Bozkurt İlçe Devlet Hastanesi",
    "latitude": 41.4178,
    "longitude": 33.7325
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kastamonu Fizik Tedavi ve Rehabilitasyon Merkezi",
    "latitude": 41.3797,
    "longitude": 33.7764
  },
  {
    "name": "T.C. Sağlık Bakanlığı Azdavay İlçe Devlet Hastanesi",
    "latitude": 41.5425,
    "longitude": 33.9764
  },
  {
    "name": "T.C. Sağlık Bakanlığı Çatalzeytin İlçe Devlet Hastanesi",
    "latitude": 41.6006,
    "longitude": 34.0128
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kastamonu Pınarbaşı İlçe Devlet Hastanesi",
    "latitude": 41.2675,
    "longitude": 34.2178
  },
  {
    "name": "T.C. Sağlık Bakanlığı Küre İlçe Devlet Hastanesi",
    "latitude": 41.6111,
    "longitude": 34.3058
  },
  {
    "name": "T.C. Sağlık Bakanlığı İhsangazi İlçe Devlet Hastanesi",
    "latitude": 41.6006,
    "longitude": 33.9497
  },
  {
    "name": "T.C. Sağlık Bakanlığı Doğanyurt İlçe Devlet Hastanesi",
    "latitude": 41.4236,
    "longitude": 33.5919
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şenpazar İlçe Devlet Hastanesi",
    "latitude": 41.5714,
    "longitude": 33.5425
  },{
    "name": "T.C. Sağlık Bakanlığı Malatya Eğitim ve Araştırma Hastanesi",
    "latitude": 38.3225,
    "longitude": 38.3550
  },
  {
    "name": "T.C. Sağlık Bakanlığı Battalgazi Devlet Hastanesi",
    "latitude": 38.3244,
    "longitude": 38.2731
  },
  {
    "name": "T.C. Sağlık Bakanlığı Pütürge Devlet Hastanesi",
    "latitude": 38.2781,
    "longitude": 37.8047
  },
  {
    "name": "T.C. Sağlık Bakanlığı Darende Hulusi Efendi Devlet Hastanesi",
    "latitude": 38.2069,
    "longitude": 37.7878
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hekimhan Devlet Hastanesi",
    "latitude": 38.5781,
    "longitude": 37.9347
  },
  {
    "name": "T.C. Sağlık Bakanlığı Malatya Yeşilyurt Hasan Çalık Devlet Hastanesi",
    "latitude": 38.3517,
    "longitude": 38.2944
  },
  {
    "name": "T.C. Sağlık Bakanlığı Akçadağ Şehit Gökhan Aslan Devlet Hastanesi",
    "latitude": 38.4172,
    "longitude": 38.6756
  },
  {
    "name": "T.C. Sağlık Bakanlığı Doğanşehir Şehit Esra Köse Başaran Devlet Hastanesi",
    "latitude": 38.1172,
    "longitude": 37.5236
  },
  {
    "name": "T.C. Sağlık Bakanlığı Malatya Şehit Mehmet Kılınç Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 38.3222,
    "longitude": 38.3555
  },
  {
    "name": "T.C. Sağlık Bakanlığı Arapgir Ali Özge Devlet Hastanesi",
    "latitude": 38.0697,
    "longitude": 37.7886
  },
  {
    "name": "T.C. Sağlık Bakanlığı Yazıhan Şehit Eyüp Hacıoğlu İlçe Devlet Hastanesi",
    "latitude": 38.2997,
    "longitude": 38.3206
  },
  {
    "name": "T.C. Sağlık Bakanlığı Malatya Kale İlçe Devlet Hastanesi",
    "latitude": 38.4436,
    "longitude": 38.3400
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kuluncak Şehit Mehmet Ali Şekerci İlçe Devlet Hastanesi",
    "latitude": 38.5200,
    "longitude": 38.4125
  },
  {
    "name": "T.C. Sağlık Bakanlığı Selendi Devlet Hastanesi",
    "latitude": 38.6000,
    "longitude": 38.7156
  },{
    "name": "T.C. Sağlık Bakanlığı Midyat Devlet Hastanesi",
    "latitude": 37.4750,
    "longitude": 41.4625
  },
  {
    "name": "T.C. Sağlık Bakanlığı Nusaybin Devlet Hastanesi",
    "latitude": 37.0708,
    "longitude": 41.2275
  },
  {
    "name": "T.C. Sağlık Bakanlığı Derik Devlet Hastanesi",
    "latitude": 37.5125,
    "longitude": 41.2308
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kızıltepe Devlet Hastanesi",
    "latitude": 37.5000,
    "longitude": 40.1050
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mardin Eğitim ve Araştırma Hastanesi",
    "latitude": 37.5000,
    "longitude": 40.7222
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mazıdağı İlçe Devlet Hastanesi",
    "latitude": 37.3125,
    "longitude": 40.4575
  },
  {
    "name": "T.C. Sağlık Bakanlığı Dargeçit İlçe Devlet Hastanesi",
    "latitude": 37.4069,
    "longitude": 40.7497
  },
  {
    "name": "T.C. Sağlık Bakanlığı Savur Prof. Dr. Aziz Sancar İlçe Devlet Hastanesi",
    "latitude": 37.3467,
    "longitude": 41.0625
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ömerli İlçe Devlet Hastanesi",
    "latitude": 37.3069,
    "longitude": 41.1833
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mersin Şehir Hastanesi",
    "latitude": 36.8172,
    "longitude": 34.6333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tarsus Devlet Hastanesi",
    "latitude": 37.0000,
    "longitude": 34.8867
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gülnar Devlet Hastanesi",
    "latitude": 36.4125,
    "longitude": 34.4047
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mut Devlet Hastanesi",
    "latitude": 36.4297,
    "longitude": 33.1847
  },
  {
    "name": "T.C. Sağlık Bakanlığı Silifke Devlet Hastanesi",
    "latitude": 36.2047,
    "longitude": 33.8472
  },
  {
    "name": "T.C. Sağlık Bakanlığı Erdemli Devlet Hastanesi",
    "latitude": 36.5417,
    "longitude": 34.0931
  },
  {
    "name": "T.C. Sağlık Bakanlığı Anamur Devlet Hastanesi",
    "latitude": 36.5667,
    "longitude": 32.8806
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mersin Aydıncık Devlet Hastanesi",
    "latitude": 36.1833,
    "longitude": 34.2097
  },
  {
    "name": "T.C. Sağlık Bakanlığı Mersin Ağız Diş Sağlığı Hastanesi",
    "latitude": 36.8139,
    "longitude": 34.6389
  },
  {
    "name": "T.C. Sağlık Bakanlığı Toros Devlet Hastanesi",
    "latitude": 36.8047,
    "longitude": 34.636
  },{
    "name": "T.C. Sağlık Bakanlığı Suşehri Devlet Hastanesi",
    "latitude": 40.0783,
    "longitude": 37.4186
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şarkışla Devlet Hastanesi",
    "latitude": 39.7375,
    "longitude": 36.8561
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gürün Devlet Hastanesi",
    "latitude": 38.4469,
    "longitude": 37.2250
  },
  {
    "name": "T.C. Sağlık Bakanlığı Kangal Devlet Hastanesi",
    "latitude": 38.9139,
    "longitude": 37.9772
  },
  {
    "name": "T.C. Sağlık Bakanlığı Divriği Sadık Özgür Devlet Hastanesi",
    "latitude": 39.1211,
    "longitude": 37.7236
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sivas Numune Hastanesi",
    "latitude": 39.7469,
    "longitude": 37.0167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sivas Devlet Hastanesi",
    "latitude": 39.7456,
    "longitude": 37.0167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gemerek Devlet Hastanesi",
    "latitude": 39.5139,
    "longitude": 36.8583
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sivas Ağız ve Diş Sağlığı Hastanesi",
    "latitude": 39.7469,
    "longitude": 37.0167
  },
  {
    "name": "T.C. Sağlık Bakanlığı Ulaş İlçe Devlet Hastanesi",
    "latitude": 39.0500,
    "longitude": 36.9467
  },
  {
    "name": "T.C. Sağlık Bakanlığı Hafik Hacı Esma Kocacık İlçe Devlet Hastanesi",
    "latitude": 39.2833,
    "longitude": 37.2792
  },
  {
    "name": "T.C. Sağlık Bakanlığı Altınyayla İlçe Devlet Hastanesi",
    "latitude": 39.4342,
    "longitude": 37.3719
  },
  {
    "name": "T.C. Sağlık Bakanlığı Koyulhisar İlçe Devlet Hastanesi",
    "latitude": 40.2481,
    "longitude": 37.6247
  },
  {
    "name": "T.C. Sağlık Bakanlığı İmranlı İlçe Devlet Hastanesi",
    "latitude": 39.4100,
    "longitude": 37.5861
  },
  {
    "name": "T.C. Sağlık Bakanlığı Akıncılar İlçe Devlet Hastanesi",
    "latitude": 39.6556,
    "longitude": 37.5547
  },
  {
    "name": "T.C. Sağlık Bakanlığı Gölova İlçe Devlet Hastanesi",
    "latitude": 39.3897,
    "longitude": 37.7075
  },
  {
    "name": "T.C. Sağlık Bakanlığı Doğanşar İlçe Devlet Hastanesi",
    "latitude": 39.5286,
    "longitude": 37.7117
  },
  {
    "name": "T.C. Sağlık Bakanlığı Şanlıurfa Mehmet Akif İnan Eğitim ve Araştırma Hastanesi",
    "latitude": 37.1586,
    "longitude": 38.8014
  },
  {
    "name": "T.C. Sağlık Bakanlığı Suruç Devlet Hastanesi",
    "latitude": 37.1953,
    "longitude": 38.5272
  },{
    "name": "T.C. Sağlık Bakanlığı Niksar Devlet Hastanesi",
    "latitude": 40.1156,
    "longitude": 36.9275
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tokat Devlet Hastanesi",
    "latitude": 40.3153,
    "longitude": 36.5539
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tokat Dr. Cevdet Aykan Ruh Sağlığı ve Hastalıkları Hastanesi",
    "latitude": 40.3156,
    "longitude": 36.5500
  },
  {
    "name": "T.C. Sağlık Bakanlığı Almus Devlet Hastanesi",
    "latitude": 40.8772,
    "longitude": 37.6878
  },
  {
    "name": "T.C. Sağlık Bakanlığı Pazar İlçe Devlet Hastanesi",
    "latitude": 40.5294,
    "longitude": 37.7442
  },
  {
    "name": "T.C. Sağlık Bakanlığı Yeşilyurt İlçe Devlet Hastanesi",
    "latitude": 40.7361,
    "longitude": 37.9333
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sulusaray İlçe Devlet Hastanesi",
    "latitude": 40.4633,
    "longitude": 37.7011
  },
  {
    "name": "T.C. Sağlık Bakanlığı Başçiftlik İlçe Devlet Hastanesi",
    "latitude": 40.3536,
    "longitude": 37.6069
  },
  {
    "name": "T.C. Sağlık Bakanlığı Artova İlçe Devlet Hastanesi",
    "latitude": 40.3606,
    "longitude": 36.8186
  },
  {
    "name": "T.C. Sağlık Bakanlığı Trabzon Ahi Evren Göğüs Kalp ve Damar Cerrahisi Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0028,
    "longitude": 39.7222
  },
  {
    "name": "T.C. Sağlık Bakanlığı Trabzon Kanuni Eğitim ve Araştırma Hastanesi",
    "latitude": 41.0214,
    "longitude": 39.7222
  },
  {
    "name": "T.C. Sağlık Bakanlığı Tonya Devlet Hastanesi",
    "latitude": 40.7875,
    "longitude": 39.3522
  },
  {
    "name": "T.C. Sağlık Bakanlığı Vakfıkebir Devlet Hastanesi",
    "latitude": 40.7061,
    "longitude": 39.3428
  },
  {
    "name": "T.C. Sağlık Bakanlığı Sürmene Devlet Hastanesi",
    "latitude": 40.3997,
    "longitude": 39.8014
  },
  {
    "name": "T.C. Sağlık Bakanlığı Trabzon Ataköy Ruh ve Sinir Hastalıkları Hastanesi",
    "latitude": 41.0194,
    "longitude": 39.7250
  },
  {
    "name": "T.C. Sağlık Bakanlığı Trabzon Yavuz Selim Kemik Hastalıkları ve Rehabilitasyon Hastanesi",
    "latitude": 41.0014,
    "longitude": 39.7264
  },
  {
    "name": "T.C. Sağlık Bakanlığı Of Devlet Hastanesi",
    "latitude": 40.9800,
    "longitude": 39.4347
  }

    ]
    return render(request, 'pages/iletisim.html', {'konum': json.dumps(konum)})


def doktorlar(request):
    doktorlar=[
   {
        "ad": "Ahmet",
        "soyad": "Yılmaz",
        "uzmanlik": "Kardiyoloji",
        "telefon": "05001234567",
        "resim": "https://randomuser.me/api/portraits/men/32.jpg",
        "hakkinda": "20 yıllık kardiyoloji tecrübesi ile kalp hastalıkları üzerine çalışmalar yapmaktadır. Hasta odaklı yaklaşımı ile tanınır."
    },
    {
        "ad": "Ayşe",
        "soyad": "Demir",
        "uzmanlik": "Nöroloji",
        "telefon": "05007654321",
        "resim": "https://randomuser.me/api/portraits/women/44.jpg",
        "hakkinda": "Sinir sistemi hastalıklarında uzmandır. Migren ve epilepsi üzerine birçok konferansa katılmıştır."
    },
    {
        "ad": "Mehmet",
        "soyad": "Koç",
        "uzmanlik": "Ortopedi",
        "telefon": "05321234567",
        "resim": "https://randomuser.me/api/portraits/men/65.jpg",
        "hakkinda": "Kemik ve eklem hastalıkları üzerine 15 yıllık deneyime sahiptir. Sporcu sağlığı konusunda uzmandır."
    },
    {
        "ad": "Elif",
        "soyad": "Arslan",
        "uzmanlik": "Göz Hastalıkları",
        "telefon": "05441234567",
        "resim": "https://randomuser.me/api/portraits/women/33.jpg",
        "hakkinda": "Retina hastalıkları ve lazer tedavileri konusunda çalışmaktadır. Teknolojik tedavi yöntemlerine ilgi duyar."
    },
    {
        "ad": "Kemal",
        "soyad": "Bozkurt",
        "uzmanlik": "Dahiliye",
        "telefon": "05009874561",
        "resim": "https://randomuser.me/api/portraits/men/51.jpg",
        "hakkinda": "İç hastalıkları alanında 18 yıldır hizmet vermektedir. Diyabet ve tansiyon hastalıkları konusunda uzmandır."
    },
    {
        "ad": "Zeynep",
        "soyad": "Kaya",
        "uzmanlik": "Kadın Hastalıkları ve Doğum",
        "telefon": "05006789123",
        "resim": "https://randomuser.me/api/portraits/women/27.jpg",
        "hakkinda": "Anne ve bebek sağlığı konusunda özel çalışmalar yürütmektedir. Doğum öncesi danışmanlık hizmetleri vermektedir."
    },
    {
        "ad": "Bülent",
        "soyad": "Arslan",
        "uzmanlik": "Üroloji",
        "telefon": "05440099887",
        "resim": "https://randomuser.me/api/portraits/men/78.jpg",
        "hakkinda": "İdrar yolları ve böbrek hastalıkları üzerinde çalışır. Robotik cerrahi alanında eğitim almıştır."
    },
    {
        "ad": "Fatma",
        "soyad": "Şahin",
        "uzmanlik": "Psikiyatri",
        "telefon": "05325554433",
        "resim": "https://randomuser.me/api/portraits/women/11.jpg",
        "hakkinda": "Ruh sağlığı alanında bireysel terapiler sunmaktadır. Gençlerle çalışma konusunda deneyimlidir."
    },
    {
        "ad": "Burak",
        "soyad": "Öztürk",
        "uzmanlik": "Dermatoloji",
        "telefon": "05003334455",
        "resim": "https://randomuser.me/api/portraits/men/12.jpg",
        "hakkinda": "Cilt hastalıkları ve estetik uygulamalar üzerine çalışır. Leke tedavisi ve akne konusunda uzmandır."
    }
]
    uzmanliklar = list({doktor["uzmanlik"] for doktor in doktorlar})  # set ile unique yapıyoruz
    uzmanliklar.sort()  # istersen alfabetik sırala

    return render(request, "pages/doktorlar.html", {
        "doktorlar": doktorlar,
        "uzmanliklar": uzmanliklar
    })


def egitimler(request):
    return render(request,"pages/egitimler.html")




from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages  # bilgi mesajı gösterebilmek için

def gorus_gonder(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        full_message = f"İsim: {name}\n\nMesaj:\n{message}"

        try:
            send_mail(
                subject="Yeni İletişim Mesajı",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,  # sistem mailinden
                recipient_list=['sefaekin072@gmail.com'],  # sabit adres
                fail_silently=False,
            )
            messages.success(request, "Mesajınız başarıyla gönderildi. Teşekkür ederiz!")
        except Exception as e:
            messages.error(request, f"Mesaj gönderilirken bir hata oluştu: {str(e)}")
        return redirect('iletisim')

    return redirect('iletisim')



from django.shortcuts import render
from model_files.predict import predict_text
from  .views import hastaliklar

from django.http import JsonResponse
from django.shortcuts import render
import json

def predict_view(request):
    result = None
    class_probs = None
    user_text = ""

    # AJAX istek kontrolü (JSON veriyle gelen POST isteği)
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            try:
                data = json.loads(request.body)
                user_text = data.get('user_text', '').strip()
                if user_text:
                    result, class_probs = predict_text(user_text)
                    return JsonResponse({'result': result, 'class_probs': class_probs})
                else:
                    return JsonResponse({'error': 'Boş metin girdiniz.'}, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

        # Geleneksel form gönderimi
        else:
            user_text = request.POST.get('user_text', '').strip()
            if user_text:
                result, class_probs = predict_text(user_text)

    return render(request, 'pages/hastaliklar.html', {
        'result': result,
        'class_probs': class_probs,
        'user_text': user_text,
    })




