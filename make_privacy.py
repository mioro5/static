#!/usr/bin/env python3
import os

LANGS = ['et', 'ru', 'en', 'fi']

META = {
    'et': {
        'lang': 'et',
        'title': 'Privaatsuspoliitika | MV Therapy',
        'desc': 'MV Therapy privaatsuspoliitika – kuidas töötleme ja kaitseme teie isikuandmeid vastavalt GDPR-ile ja IKS-ile.',
        'og_url': 'https://mvtherapy.ee/et/privaatsuspoliitika.html',
        'og_title': 'Privaatsuspoliitika | MV Therapy – Massaaž Tallinnas',
        'og_desc': 'Lugege, kuidas MV Therapy kogub, töötleb ja kaitseb teie isikuandmeid vastavalt GDPR-ile.',
        'tw_url': 'https://mvtherapy.ee/et/privaatsuspoliitika.html',
        'tw_title': 'Privaatsuspoliitika | MV Therapy',
        'tw_desc': 'Lugege, kuidas MV Therapy kogub, töötleb ja kaitseb teie isikuandmeid vastavalt GDPR-ile.',
        'canonical': 'https://mvtherapy.ee/et/privaatsuspoliitika.html',
        'og_locale': 'et_EE',
        'skip_link': 'Liigu põhisisu juurde',
        'brand_home': '/et/home.html',
        'brand_sub': 'Medical Verified Therapy',
        'stebby_label': 'Stebby – maksmine Stebby kaudu',
        'arve_href': '/et/arve.html',
        'arve_label': 'Arve – väljastame arveid',
        'partner_href': '/et/partner.html',
        'partner_label': 'Koostöö ettevõtetega',
        'nav': [
            ('/et/home.html', 'Avaleht'),
            ('/et/services.html', 'Massaažid'),
            ('/et/Diagnosis.html', 'Diagnoosid'),
            ('/et/campaign.html', 'Kampaaniad'),
            ('/et/workshops.html', 'Koolitused'),
            ('/et/team.html', 'Meeskond'),
            ('/et/kkk.html', 'KKK'),
            ('/et/blog.html', 'Blogi'),
        ],
        'lang_links': [
            ('/et/privaatsuspoliitika.html', 'EST', True),
            ('/ru/privaatsuspoliitika.html', 'РУС', False),
            ('/en/privaatsuspoliitika.html', 'ENG', False),
            ('/fi/privaatsuspoliitika.html', 'FIN', False),
        ],
        'menu_label': 'Ava menüü',
        'location_label': 'Asukoht:',
        'city_active': 'Tallinn / Viimsi',
        'city_other_href': '/et/parnu.html',
        'city_other': 'Pärnu',
        'footer_copy': '© 2026 MV Therapy – Meditsiiniline massaaž Tallinnas',
        'footer_addr': 'Aadress',
        'footer_contact': 'Kontakt',
        'footer_pages': 'Lehed',
        'footer_pages_links': [
            ('/et/services.html', 'Teenused'),
            ('/et/Diagnosis.html', 'Diagnoosid'),
            ('/et/blog.html', 'Blogi'),
            ('/et/kkk.html', 'KKK'),
            ('/et/tingimused.html', 'Tingimused'),
            ('/et/privaatsuspoliitika.html', 'Privaatsuspoliitika'),
        ],
        'go_top_label': 'Keri lehe algusesse',
        'book_info_strong': 'MV Therapy',
        'book_info_addr': 'Ravi tee 4, Haabneeme',
        'book_btn': 'Broneeri',
        'cookie_text': 'Kasutame küpsiseid teie sirvimiskogemuse parandamiseks, isikupärastatud sisu esitamiseks ja liikluse analüüsimiseks.',
        'cookie_btn': 'OK, nõustun',
        'cookie_label': 'Küpsiste teade',
        'sl_lang': 'et',
        'sl_btn_text': 'Broneeri aeg',
        'h1': 'Privaatsuspoliitika',
        'intro': 'Käesolev privaatsuspoliitika selgitab, kuidas MV Therapy OÜ (registrikood: 14609777, aadress: Viimsi Haigla, Ravi tee 4, 74001 Haabneeme, Harjumaa, Eesti; e-post: info@mvtherapy.ee) kogub, töötleb ja kaitseb teie isikuandmeid vastavalt Euroopa Liidu isikuandmete kaitse üldmäärusele (GDPR) ning Eesti isikuandmete kaitse seadusele (IKS).',
    },
    'ru': {
        'lang': 'ru',
        'title': 'Политика конфиденциальности | MV Therapy',
        'desc': 'Политика конфиденциальности MV Therapy – как мы обрабатываем и защищаем ваши персональные данные в соответствии с GDPR.',
        'og_url': 'https://mvtherapy.ee/ru/privaatsuspoliitika.html',
        'og_title': 'Политика конфиденциальности | MV Therapy – Массаж в Таллинне',
        'og_desc': 'Узнайте, как MV Therapy собирает, обрабатывает и защищает ваши персональные данные в соответствии с GDPR.',
        'tw_url': 'https://mvtherapy.ee/ru/privaatsuspoliitika.html',
        'tw_title': 'Политика конфиденциальности | MV Therapy',
        'tw_desc': 'Узнайте, как MV Therapy собирает, обрабатывает и защищает ваши персональные данные в соответствии с GDPR.',
        'canonical': 'https://mvtherapy.ee/ru/privaatsuspoliitika.html',
        'og_locale': 'ru_RU',
        'skip_link': 'Перейти к основному содержимому',
        'brand_home': '/ru/home.html',
        'brand_sub': 'Medical Verified Therapy',
        'stebby_label': 'Stebby – оплата через Stebby',
        'arve_href': '/ru/arve.html',
        'arve_label': 'Счёт – выставляем счета',
        'partner_href': '/ru/partner.html',
        'partner_label': 'Сотрудничество с предприятиями',
        'nav': [
            ('/ru/home.html', 'Главная'),
            ('/ru/services.html', 'Массажи'),
            ('/ru/Diagnosis.html', 'Диагнозы'),
            ('/ru/campaign.html', 'Акции'),
            ('/ru/workshops.html', 'Обучение'),
            ('/ru/team.html', 'Команда'),
            ('/ru/kkk.html', 'FAQ'),
            ('/ru/blog.html', 'Блог'),
        ],
        'lang_links': [
            ('/et/privaatsuspoliitika.html', 'EST', False),
            ('/ru/privaatsuspoliitika.html', 'РУС', True),
            ('/en/privaatsuspoliitika.html', 'ENG', False),
            ('/fi/privaatsuspoliitika.html', 'FIN', False),
        ],
        'menu_label': 'Открыть меню',
        'location_label': 'Расположение:',
        'city_active': 'Таллинн / Виймси',
        'city_other_href': '/ru/parnu.html',
        'city_other': 'Пярну',
        'footer_copy': '© 2026 MV Therapy – Медицинский массаж в Таллинне',
        'footer_addr': 'Адрес',
        'footer_contact': 'Контакт',
        'footer_pages': 'Страницы',
        'footer_pages_links': [
            ('/ru/services.html', 'Услуги'),
            ('/ru/Diagnosis.html', 'Диагнозы'),
            ('/ru/blog.html', 'Блог'),
            ('/ru/kkk.html', 'FAQ'),
            ('/ru/tingimused.html', 'Условия'),
            ('/ru/privaatsuspoliitika.html', 'Политика конфиденциальности'),
        ],
        'go_top_label': 'Прокрутить наверх',
        'book_info_strong': 'MV Therapy',
        'book_info_addr': 'Ravi tee 4, Haabneeme',
        'book_btn': 'Записаться',
        'cookie_text': 'Мы используем файлы cookie для улучшения вашего опыта просмотра, персонализации контента и анализа трафика.',
        'cookie_btn': 'OK, согласен',
        'cookie_label': 'Уведомление о cookie',
        'sl_lang': 'ru',
        'sl_btn_text': 'Записаться на приём',
        'h1': 'Политика конфиденциальности',
        'intro': 'Настоящая политика конфиденциальности объясняет, как MV Therapy OÜ (регистрационный код: 14609777, адрес: Viimsi Haigla, Ravi tee 4, 74001 Haabneeme, Harjumaa, Эстония; e-mail: info@mvtherapy.ee) собирает, обрабатывает и защищает ваши персональные данные в соответствии с Общим регламентом защиты данных ЕС (GDPR) и Законом Эстонии о защите персональных данных (IKS).',
    },
    'en': {
        'lang': 'en',
        'title': 'Privacy Policy | MV Therapy',
        'desc': 'MV Therapy privacy policy – how we collect, process and protect your personal data in accordance with GDPR.',
        'og_url': 'https://mvtherapy.ee/en/privaatsuspoliitika.html',
        'og_title': 'Privacy Policy | MV Therapy – Massage in Tallinn',
        'og_desc': 'Learn how MV Therapy collects, processes and protects your personal data in accordance with GDPR.',
        'tw_url': 'https://mvtherapy.ee/en/privaatsuspoliitika.html',
        'tw_title': 'Privacy Policy | MV Therapy',
        'tw_desc': 'Learn how MV Therapy collects, processes and protects your personal data in accordance with GDPR.',
        'canonical': 'https://mvtherapy.ee/en/privaatsuspoliitika.html',
        'og_locale': 'en_US',
        'skip_link': 'Skip to main content',
        'brand_home': '/en/home.html',
        'brand_sub': 'Medical Verified Therapy',
        'stebby_label': 'Stebby – pay via Stebby',
        'arve_href': '/en/arve.html',
        'arve_label': 'Invoice – we issue invoices',
        'partner_href': '/en/partner.html',
        'partner_label': 'Corporate partnerships',
        'nav': [
            ('/en/home.html', 'Home'),
            ('/en/services.html', 'Massages'),
            ('/en/Diagnosis.html', 'Diagnoses'),
            ('/en/campaign.html', 'Campaigns'),
            ('/en/workshops.html', 'Workshops'),
            ('/en/team.html', 'Team'),
            ('/en/kkk.html', 'FAQ'),
            ('/en/blog.html', 'Blog'),
        ],
        'lang_links': [
            ('/et/privaatsuspoliitika.html', 'EST', False),
            ('/ru/privaatsuspoliitika.html', 'РУС', False),
            ('/en/privaatsuspoliitika.html', 'ENG', True),
            ('/fi/privaatsuspoliitika.html', 'FIN', False),
        ],
        'menu_label': 'Open menu',
        'location_label': 'Location:',
        'city_active': 'Tallinn / Viimsi',
        'city_other_href': '/en/parnu.html',
        'city_other': 'Pärnu',
        'footer_copy': '© 2026 MV Therapy – Medical massage in Tallinn',
        'footer_addr': 'Address',
        'footer_contact': 'Contact',
        'footer_pages': 'Pages',
        'footer_pages_links': [
            ('/en/services.html', 'Services'),
            ('/en/Diagnosis.html', 'Diagnoses'),
            ('/en/blog.html', 'Blog'),
            ('/en/kkk.html', 'FAQ'),
            ('/en/tingimused.html', 'Terms'),
            ('/en/privaatsuspoliitika.html', 'Privacy Policy'),
        ],
        'go_top_label': 'Scroll to top',
        'book_info_strong': 'MV Therapy',
        'book_info_addr': 'Ravi tee 4, Haabneeme',
        'book_btn': 'Book now',
        'cookie_text': 'We use cookies to improve your browsing experience, personalise content and analyse traffic.',
        'cookie_btn': 'OK, I agree',
        'cookie_label': 'Cookie notice',
        'sl_lang': 'en',
        'sl_btn_text': 'Book appointment',
        'h1': 'Privacy Policy',
        'intro': 'This privacy policy explains how MV Therapy OÜ (registration code: 14609777, address: Viimsi Haigla, Ravi tee 4, 74001 Haabneeme, Harjumaa, Estonia; email: info@mvtherapy.ee) collects, processes and protects your personal data in accordance with the EU General Data Protection Regulation (GDPR) and the Estonian Personal Data Protection Act (IKS).',
    },
    'fi': {
        'lang': 'fi',
        'title': 'Tietosuojakäytäntö | MV Therapy',
        'desc': 'MV Therapy tietosuojakäytäntö – kuinka keräämme, käsittelemme ja suojaamme henkilötietojasi GDPR:n mukaisesti.',
        'og_url': 'https://mvtherapy.ee/fi/privaatsuspoliitika.html',
        'og_title': 'Tietosuojakäytäntö | MV Therapy – Hieronta Tallinnassa',
        'og_desc': 'Lue, kuinka MV Therapy kerää, käsittelee ja suojaa henkilötietojasi GDPR:n mukaisesti.',
        'tw_url': 'https://mvtherapy.ee/fi/privaatsuspoliitika.html',
        'tw_title': 'Tietosuojakäytäntö | MV Therapy',
        'tw_desc': 'Lue, kuinka MV Therapy kerää, käsittelee ja suojaa henkilötietojasi GDPR:n mukaisesti.',
        'canonical': 'https://mvtherapy.ee/fi/privaatsuspoliitika.html',
        'og_locale': 'fi_FI',
        'skip_link': 'Siirry pääsisältöön',
        'brand_home': '/fi/home.html',
        'brand_sub': 'Medical Verified Therapy',
        'stebby_label': 'Stebby – maksaminen Stebbyn kautta',
        'arve_href': '/fi/arve.html',
        'arve_label': 'Lasku – laskutuspalvelu',
        'partner_href': '/fi/partner.html',
        'partner_label': 'Yhteistyö yritysten kanssa',
        'nav': [
            ('/fi/home.html', 'Etusivu'),
            ('/fi/services.html', 'Hieronnat'),
            ('/fi/Diagnosis.html', 'Diagnoosit'),
            ('/fi/campaign.html', 'Kampanjat'),
            ('/fi/workshops.html', 'Koulutukset'),
            ('/fi/team.html', 'Tiimi'),
            ('/fi/kkk.html', 'UKK'),
            ('/fi/blog.html', 'Blogi'),
        ],
        'lang_links': [
            ('/et/privaatsuspoliitika.html', 'EST', False),
            ('/ru/privaatsuspoliitika.html', 'РУС', False),
            ('/en/privaatsuspoliitika.html', 'ENG', False),
            ('/fi/privaatsuspoliitika.html', 'FIN', True),
        ],
        'menu_label': 'Avaa valikko',
        'location_label': 'Sijainti:',
        'city_active': 'Tallinna / Viimsi',
        'city_other_href': '/fi/parnu.html',
        'city_other': 'Pärnu',
        'footer_copy': '© 2026 MV Therapy – Lääketieteellinen hieronta Tallinnassa',
        'footer_addr': 'Osoite',
        'footer_contact': 'Yhteystiedot',
        'footer_pages': 'Sivut',
        'footer_pages_links': [
            ('/fi/services.html', 'Palvelut'),
            ('/fi/Diagnosis.html', 'Diagnoosit'),
            ('/fi/blog.html', 'Blogi'),
            ('/fi/kkk.html', 'UKK'),
            ('/fi/tingimused.html', 'Ehdot'),
            ('/fi/privaatsuspoliitika.html', 'Tietosuojakäytäntö'),
        ],
        'go_top_label': 'Vieritä ylös',
        'book_info_strong': 'MV Therapy',
        'book_info_addr': 'Ravi tee 4, Haabneeme',
        'book_btn': 'Varaa',
        'cookie_text': 'Käytämme evästeitä selauskokemuksesi parantamiseen, sisällön personointiin ja liikenteen analysointiin.',
        'cookie_btn': 'OK, hyväksyn',
        'cookie_label': 'Evästeilmoitus',
        'sl_lang': 'fi',
        'sl_btn_text': 'Varaa aika',
        'h1': 'Tietosuojakäytäntö',
        'intro': 'Tämä tietosuojakäytäntö selittää, kuinka MV Therapy OÜ (rekisterikoodi: 14609777, osoite: Viimsi Haigla, Ravi tee 4, 74001 Haabneeme, Harjumaa, Viro; sähköposti: info@mvtherapy.ee) kerää, käsittelee ja suojaa henkilötietojasi EU:n yleisen tietosuoja-asetuksen (GDPR) ja Viron henkilötietolain (IKS) mukaisesti.',
    },
}

SECTIONS = {
    'et': [
        ('1. Milliseid isikuandmeid kogume',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Kontaktandmed:</strong> nimi, telefoninumber, e-posti aadress.</li>'
         '<li><strong>Tervisega seotud andmed:</strong> anamnees, terviseseisund, vastunäidustused, seansside märkmed ja muud tervislikku seisundit kirjeldavad andmed.</li>'
         '<li><strong>Broneerimisandmed:</strong> broneeringu kuupäev, kellaaeg, teenuse liik, makseinfo (arve number, makse kinnitus).</li>'
         '<li><strong>Suhtlusandmed:</strong> e-kirjade, SMS-ide ja muude sõnumite sisu, mida jagate meiega suhtlemise käigus.</li>'
         '<li><strong>Tehniline info:</strong> küpsised, IP-aadress, brauseri tüüp ja lehekülgede külastusstatistika (ainult anonüümsel/pseudonüümsel kujul).</li>'
         '</ul>'),
        ('2. Isikuandmete töötlemise õiguslikud alused',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Lepingu täitmine (GDPR art 6(1)(b)):</strong> Kontaktandmeid ja broneerimisandmeid töötleme broneeringu haldamiseks ja teenuse osutamiseks.</li>'
         '<li><strong>Nõusolek (GDPR art 6(1)(a) ja art 9(2)(a)):</strong> Tervisega seotud andmeid (eriliiki isikuandmeid) töötleme ainult teie selgesõnalise nõusoleku alusel, mille annate broneeringu kinnitamisel vastavalt meie broneerimis- ja kohaleilmumise tingimustele.</li>'
         '<li><strong>Õiguslik kohustus (GDPR art 6(1)(c)):</strong> Teatud andmeid (nt arved) säilitame seadusest tuleneva raamatupidamiskohustuse täitmiseks.</li>'
         '<li><strong>Õigustatud huvi (GDPR art 6(1)(f)):</strong> Anonüümset külastusstatistikat kasutame veebilehe toimimise ja turunduse parendamiseks.</li>'
         '</ul>'),
        ('3. Kuidas andmeid kogume',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li>Otseselt teilt (broneeringuvorm, e-post, SMS, telefon, kohapeal täidetav ankeet).</li>'
         '<li>SalonLife broneerimissüsteemi kaudu (kolmanda osapoole tarkvarateenus).</li>'
         '<li>Stebby, Kingituste Saar või muude vahendusplatvormide kaudu, kui kasutate nende vautšereid või kingituskaarte.</li>'
         '<li>Veebilehe küpsiste ja analüütika (Matomo) kaudu – ainult anonüümselt.</li>'
         '</ul>'),
        ('4. Andmete edastamine kolmandatele isikutele',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Me ei müü ega vahenda teie isikuandmeid kolmandatele isikutele turunduslikul eesmärgil. Andmeid võime edastada üksnes järgmistel juhtudel:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Teenusepakkujad:</strong> SalonLife OÜ (broneerimissüsteem) – ainult lepingu täitmiseks vajalikus mahus.</li>'
         '<li><strong>Makseprotsessorid:</strong> pangad ja makseettevõtted arveldustoimingute teostamiseks.</li>'
         '<li><strong>Riigiasutused:</strong> seadusest tuleneva kohustuse täitmiseks (nt maksuamet).</li>'
         '<li>Kolmandate osapoolte platvormid (Stebby, Kingituste Saar jt) töötlevad vaid neid andmeid, mis on vajalikud nende vahendusteenuse osutamiseks – vastavalt nende oma privaatsuspoliitikale.</li>'
         '</ul>'),
        ('5. Andmete säilitamise tähtajad',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Tervisega seotud andmed ja seansside märkmed:</strong> säilitatakse kuni 3 aastat viimasest külastusest või nõusoleku tagasivõtmiseni (kumb saabub varem).</li>'
         '<li><strong>Arved ja makseandmed:</strong> säilitatakse 7 aastat vastavalt raamatupidamisseadusele.</li>'
         '<li><strong>Kontakt- ja suhtlusandmed:</strong> säilitatakse kuni 2 aastat viimasest kontaktist.</li>'
         '<li><strong>Anonüümne statistika:</strong> säilitatakse tähtajatult.</li>'
         '</ul>'),
        ('6. Andmesubjekti õigused',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Teil on GDPR-i alusel järgmised õigused:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Tutvumisõigus:</strong> õigus saada teada, milliseid isikuandmeid me teie kohta töötleme.</li>'
         '<li><strong>Parandamisõigus:</strong> õigus nõuda ebatäpsete andmete parandamist.</li>'
         '<li><strong>Kustutamisõigus ("õigus olla unustatud"):</strong> õigus nõuda andmete kustutamist, kui töötlemiseks puudub õiguslik alus.</li>'
         '<li><strong>Töötlemise piiramise õigus:</strong> õigus nõuda töötlemise piiramist teatud tingimustel.</li>'
         '<li><strong>Andmete ülekandmise õigus:</strong> õigus saada oma andmed masinloetavas vormis.</li>'
         '<li><strong>Vastuväite esitamise õigus:</strong> õigus esitada vastuväide õigustatud huvi alusel toimuvale töötlemisele.</li>'
         '<li><strong>Nõusoleku tagasivõtmine:</strong> nõusolekupõhist töötlemist võite igal ajal lõpetada, võttes ühendust aadressil info@mvtherapy.ee. See ei mõjuta enne tagasivõtmist toimunud töötlemise seaduslikkust.</li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Õiguste teostamiseks pöörduge palun: <a href="mailto:info@mvtherapy.ee" style="color:var(--brand);">info@mvtherapy.ee</a>. Vastame 30 päeva jooksul.</p>'),
        ('7. Küpsised (cookies)',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Kasutame oma veebilehel järgmisi küpsiseid:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Hädavajalikud küpsised:</strong> veebilehe toimimiseks vajalikud (nt sessiooniküpsised). Nende kasutamine ei nõua nõusolekut.</li>'
         '<li><strong>Analüütilised küpsised (Matomo):</strong> veebilehe kasutuse mõõtmiseks. Kasutame isemajutatud Matomo lahendust, mis ei edasta andmeid kolmandatele isikutele. Andmed on anonüümistatud.</li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Saate küpsised oma brauseri seadetest igal ajal keelata.</p>'),
        ('8. Andmeturve',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Rakendame asjakohaseid tehnilisi ja organisatsioonilisi meetmeid teie isikuandmete kaitsmiseks loata juurdepääsu, muutmise, avalikustamise või hävitamise eest:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li>Andmeedastus toimub krüpteeritud HTTPS-ühenduse kaudu.</li>'
         '<li>Füüsilised dokumendid säilitatakse lukustatud ruumides.</li>'
         '<li>Digitaalsed andmed on juurdepääsupiirangutega kaitstud.</li>'
         '<li>Andmetöötluslepingud on sõlmitud kõigi kolmanda osapoole teenusepakkujatega.</li>'
         '</ul>'),
        ('9. Kontakt ja vaidluste lahendamine',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Küsimuste, päringute või kaebuste korral pöörduge:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>MV Therapy OÜ</strong>, Viimsi Haigla, Ravi tee 4, 74001 Haabneeme</li>'
         '<li>E-post: <a href="mailto:info@mvtherapy.ee" style="color:var(--brand);">info@mvtherapy.ee</a></li>'
         '<li>Tel: <a href="tel:+37258189561" style="color:var(--brand);">+372 5818 9561</a></li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Kui leiate, et teie andmeid töödeldakse ebaseaduslikult, on teil õigus esitada kaebus Andmekaitse Inspektsioonile (AKI): <a href="https://www.aki.ee" target="_blank" rel="noopener noreferrer" style="color:var(--brand);">www.aki.ee</a>.</p>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Privaatsuspoliitikat uuendatakse vajadusel. Viimati uuendatud: juuni 2026.</p>'),
    ],
    'ru': [
        ('1. Какие персональные данные мы собираем',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Контактные данные:</strong> имя, номер телефона, адрес электронной почты.</li>'
         '<li><strong>Данные о здоровье:</strong> анамнез, состояние здоровья, противопоказания, записи сеансов и другие данные о состоянии здоровья.</li>'
         '<li><strong>Данные о бронировании:</strong> дата и время бронирования, тип услуги, платёжная информация (номер счёта, подтверждение платежа).</li>'
         '<li><strong>Коммуникационные данные:</strong> содержание электронных писем, SMS-сообщений и других сообщений, которыми вы делитесь с нами.</li>'
         '<li><strong>Техническая информация:</strong> файлы cookie, IP-адрес, тип браузера и статистика посещений страниц (только в анонимном/псевдонимном виде).</li>'
         '</ul>'),
        ('2. Правовые основания обработки персональных данных',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Исполнение договора (GDPR ст. 6(1)(b)):</strong> Контактные данные и данные о бронировании обрабатываются для управления бронированием и оказания услуг.</li>'
         '<li><strong>Согласие (GDPR ст. 6(1)(a) и ст. 9(2)(a)):</strong> Данные о здоровье (специальные категории персональных данных) обрабатываются только на основании вашего явного согласия, предоставленного при подтверждении бронирования.</li>'
         '<li><strong>Юридическое обязательство (GDPR ст. 6(1)(c)):</strong> Определённые данные (например, счета) хранятся для выполнения законодательного требования бухгалтерского учёта.</li>'
         '<li><strong>Законный интерес (GDPR ст. 6(1)(f)):</strong> Анонимная статистика посещений используется для улучшения работы сайта и маркетинга.</li>'
         '</ul>'),
        ('3. Как мы собираем данные',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li>Непосредственно от вас (форма бронирования, электронная почта, SMS, телефон, анкета на месте).</li>'
         '<li>Через систему бронирования SalonLife (сторонний программный сервис).</li>'
         '<li>Через Stebby, Kingituste Saar или другие посреднические платформы при использовании их ваучеров или подарочных карт.</li>'
         '<li>Через файлы cookie сайта и аналитику (Matomo) — только анонимно.</li>'
         '</ul>'),
        ('4. Передача данных третьим лицам',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Мы не продаём и не передаём ваши персональные данные третьим лицам в маркетинговых целях. Данные могут быть переданы только в следующих случаях:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Поставщики услуг:</strong> SalonLife OÜ (система бронирования) — только в объёме, необходимом для исполнения договора.</li>'
         '<li><strong>Платёжные процессоры:</strong> банки и платёжные компании для проведения расчётных операций.</li>'
         '<li><strong>Государственные органы:</strong> для выполнения законодательных обязательств (например, налоговые органы).</li>'
         '<li>Сторонние платформы (Stebby, Kingituste Saar и др.) обрабатывают только те данные, которые необходимы для предоставления их посреднических услуг — согласно их собственной политике конфиденциальности.</li>'
         '</ul>'),
        ('5. Сроки хранения данных',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Данные о здоровье и записи сеансов:</strong> хранятся до 3 лет с момента последнего посещения или до отзыва согласия (в зависимости от того, что наступит раньше).</li>'
         '<li><strong>Счета и платёжные данные:</strong> хранятся 7 лет в соответствии с законодательством о бухгалтерском учёте.</li>'
         '<li><strong>Контактные и коммуникационные данные:</strong> хранятся до 2 лет с момента последнего контакта.</li>'
         '<li><strong>Анонимная статистика:</strong> хранится бессрочно.</li>'
         '</ul>'),
        ('6. Права субъекта данных',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">В соответствии с GDPR у вас есть следующие права:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Право на доступ:</strong> право узнать, какие персональные данные мы обрабатываем о вас.</li>'
         '<li><strong>Право на исправление:</strong> право требовать исправления неточных данных.</li>'
         '<li><strong>Право на удаление ("право быть забытым"):</strong> право требовать удаления данных при отсутствии правового основания для обработки.</li>'
         '<li><strong>Право на ограничение обработки:</strong> право требовать ограничения обработки при определённых условиях.</li>'
         '<li><strong>Право на переносимость данных:</strong> право получить свои данные в машиночитаемом формате.</li>'
         '<li><strong>Право на возражение:</strong> право возражать против обработки на основании законного интереса.</li>'
         '<li><strong>Отзыв согласия:</strong> вы можете в любое время прекратить обработку на основе согласия, обратившись по адресу info@mvtherapy.ee. Это не влияет на законность обработки до отзыва.</li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Для реализации прав обращайтесь: <a href="mailto:info@mvtherapy.ee" style="color:var(--brand);">info@mvtherapy.ee</a>. Мы ответим в течение 30 дней.</p>'),
        ('7. Файлы cookie',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">На нашем сайте используются следующие типы файлов cookie:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Обязательные файлы cookie:</strong> необходимы для работы сайта (например, сессионные cookie). Их использование не требует согласия.</li>'
         '<li><strong>Аналитические файлы cookie (Matomo):</strong> для измерения использования сайта. Мы используем самостоятельно размещённое решение Matomo, которое не передаёт данные третьим лицам. Данные анонимизированы.</li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Вы можете в любое время отключить файлы cookie в настройках вашего браузера.</p>'),
        ('8. Безопасность данных',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Мы применяем соответствующие технические и организационные меры для защиты ваших персональных данных от несанкционированного доступа, изменения, раскрытия или уничтожения:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li>Передача данных осуществляется через зашифрованное HTTPS-соединение.</li>'
         '<li>Физические документы хранятся в закрытых помещениях.</li>'
         '<li>Цифровые данные защищены ограничениями доступа.</li>'
         '<li>Со всеми сторонними поставщиками услуг заключены договоры об обработке данных.</li>'
         '</ul>'),
        ('9. Контакт и разрешение споров',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">По вопросам, запросам или жалобам обращайтесь:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>MV Therapy OÜ</strong>, Viimsi Haigla, Ravi tee 4, 74001 Haabneeme</li>'
         '<li>Эл. почта: <a href="mailto:info@mvtherapy.ee" style="color:var(--brand);">info@mvtherapy.ee</a></li>'
         '<li>Тел.: <a href="tel:+37258189561" style="color:var(--brand);">+372 5818 9561</a></li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Если вы считаете, что ваши данные обрабатываются незаконно, вы вправе подать жалобу в Инспекцию по защите данных (AKI): <a href="https://www.aki.ee" target="_blank" rel="noopener noreferrer" style="color:var(--brand);">www.aki.ee</a>.</p>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Политика конфиденциальности обновляется по мере необходимости. Последнее обновление: июнь 2026 г.</p>'),
    ],
    'en': [
        ('1. What personal data we collect',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Contact data:</strong> name, phone number, email address.</li>'
         '<li><strong>Health data:</strong> medical history, health condition, contraindications, session notes and other health-related information.</li>'
         '<li><strong>Booking data:</strong> date and time of booking, type of service, payment information (invoice number, payment confirmation).</li>'
         '<li><strong>Communication data:</strong> content of emails, SMS messages and other communications you share with us.</li>'
         '<li><strong>Technical data:</strong> cookies, IP address, browser type and page visit statistics (in anonymous/pseudonymous form only).</li>'
         '</ul>'),
        ('2. Legal bases for processing personal data',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Performance of a contract (GDPR Art. 6(1)(b)):</strong> Contact and booking data are processed to manage bookings and provide services.</li>'
         '<li><strong>Consent (GDPR Art. 6(1)(a) and Art. 9(2)(a)):</strong> Health data (special category data) are processed only on the basis of your explicit consent given when confirming a booking.</li>'
         '<li><strong>Legal obligation (GDPR Art. 6(1)(c)):</strong> Certain data (e.g. invoices) are retained to comply with statutory accounting requirements.</li>'
         '<li><strong>Legitimate interests (GDPR Art. 6(1)(f)):</strong> Anonymous visit statistics are used to improve the website and marketing.</li>'
         '</ul>'),
        ('3. How we collect data',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li>Directly from you (booking form, email, SMS, phone, on-site questionnaire).</li>'
         '<li>Through the SalonLife booking system (a third-party software service).</li>'
         '<li>Through Stebby, Kingituste Saar or other intermediary platforms when you use their vouchers or gift cards.</li>'
         '<li>Through website cookies and analytics (Matomo) — anonymously only.</li>'
         '</ul>'),
        ('4. Transfer of data to third parties',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">We do not sell or share your personal data with third parties for marketing purposes. Data may be transferred only in the following cases:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Service providers:</strong> SalonLife OÜ (booking system) — only to the extent necessary for contract performance.</li>'
         '<li><strong>Payment processors:</strong> banks and payment companies for settlement transactions.</li>'
         '<li><strong>Public authorities:</strong> to fulfil legal obligations (e.g. tax authority).</li>'
         '<li>Third-party platforms (Stebby, Kingituste Saar, etc.) process only the data necessary for their intermediary service — under their own privacy policies.</li>'
         '</ul>'),
        ('5. Data retention periods',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Health data and session notes:</strong> retained for up to 3 years from the last visit or until consent is withdrawn (whichever comes first).</li>'
         '<li><strong>Invoices and payment data:</strong> retained for 7 years in accordance with accounting legislation.</li>'
         '<li><strong>Contact and communication data:</strong> retained for up to 2 years from the last contact.</li>'
         '<li><strong>Anonymous statistics:</strong> retained indefinitely.</li>'
         '</ul>'),
        ('6. Data subject rights',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Under the GDPR you have the following rights:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Right of access:</strong> the right to know what personal data we process about you.</li>'
         '<li><strong>Right to rectification:</strong> the right to request correction of inaccurate data.</li>'
         '<li><strong>Right to erasure ("right to be forgotten"):</strong> the right to request deletion of data when there is no lawful basis for processing.</li>'
         '<li><strong>Right to restriction of processing:</strong> the right to request that processing be restricted under certain conditions.</li>'
         '<li><strong>Right to data portability:</strong> the right to receive your data in machine-readable format.</li>'
         '<li><strong>Right to object:</strong> the right to object to processing based on legitimate interests.</li>'
         '<li><strong>Withdrawal of consent:</strong> you may stop consent-based processing at any time by contacting info@mvtherapy.ee. This does not affect the lawfulness of processing before withdrawal.</li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">To exercise your rights, please contact: <a href="mailto:info@mvtherapy.ee" style="color:var(--brand);">info@mvtherapy.ee</a>. We will respond within 30 days.</p>'),
        ('7. Cookies',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">We use the following types of cookies on our website:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Essential cookies:</strong> necessary for the website to function (e.g. session cookies). Their use does not require consent.</li>'
         '<li><strong>Analytical cookies (Matomo):</strong> to measure website usage. We use a self-hosted Matomo solution that does not share data with third parties. Data are anonymised.</li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">You can disable cookies at any time in your browser settings.</p>'),
        ('8. Data security',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">We implement appropriate technical and organisational measures to protect your personal data against unauthorised access, alteration, disclosure or destruction:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li>Data transmission takes place over encrypted HTTPS connections.</li>'
         '<li>Physical documents are stored in locked premises.</li>'
         '<li>Digital data are protected by access controls.</li>'
         '<li>Data processing agreements are in place with all third-party service providers.</li>'
         '</ul>'),
        ('9. Contact and dispute resolution',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">For questions, requests or complaints, please contact:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>MV Therapy OÜ</strong>, Viimsi Haigla, Ravi tee 4, 74001 Haabneeme</li>'
         '<li>Email: <a href="mailto:info@mvtherapy.ee" style="color:var(--brand);">info@mvtherapy.ee</a></li>'
         '<li>Tel: <a href="tel:+37258189561" style="color:var(--brand);">+372 5818 9561</a></li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">If you believe your data are being processed unlawfully, you have the right to lodge a complaint with the Estonian Data Protection Inspectorate (AKI): <a href="https://www.aki.ee" target="_blank" rel="noopener noreferrer" style="color:var(--brand);">www.aki.ee</a>.</p>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">This privacy policy is updated as necessary. Last updated: June 2026.</p>'),
    ],
    'fi': [
        ('1. Mitä henkilötietoja keräämme',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Yhteystiedot:</strong> nimi, puhelinnumero, sähköpostiosoite.</li>'
         '<li><strong>Terveystiedot:</strong> esitiedot, terveydentila, vasta-aiheet, istuntomuistiinpanot ja muut terveydentilaa kuvaavat tiedot.</li>'
         '<li><strong>Varaustieto:</strong> varauksen päivämäärä ja aika, palvelun tyyppi, maksutiedot (laskun numero, maksuvahvistus).</li>'
         '<li><strong>Viestintätiedot:</strong> sähköpostien, tekstiviestien ja muun viestinnän sisältö, jota jaat kanssamme.</li>'
         '<li><strong>Tekniset tiedot:</strong> evästeet, IP-osoite, selaintyyppi ja sivuvierailujen tilastot (vain anonyymissä/pseudonyymissä muodossa).</li>'
         '</ul>'),
        ('2. Henkilötietojen käsittelyn oikeusperusteet',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Sopimuksen täyttäminen (GDPR 6 art. 1 kohta b):</strong> Yhteystietoja ja varaustietoja käsitellään varausten hallintaan ja palveluiden tarjoamiseen.</li>'
         '<li><strong>Suostumus (GDPR 6 art. 1 kohta a ja 9 art. 2 kohta a):</strong> Terveystietoja (erityisiä henkilötietoja) käsitellään vain nimenomaisen suostumuksesi perusteella, jonka annat varauksen vahvistamisen yhteydessä.</li>'
         '<li><strong>Lakisääteinen velvollisuus (GDPR 6 art. 1 kohta c):</strong> Tiettyjä tietoja (esim. laskut) säilytetään lakisääteisen kirjanpitovelvollisuuden täyttämiseksi.</li>'
         '<li><strong>Oikeutettu etu (GDPR 6 art. 1 kohta f):</strong> Anonyymiä kävijätilastoa käytetään verkkosivuston ja markkinoinnin parantamiseen.</li>'
         '</ul>'),
        ('3. Miten keräämme tietoja',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li>Suoraan sinulta (varauslomake, sähköposti, tekstiviesti, puhelin, paikan päällä täytettävä lomake).</li>'
         '<li>SalonLife-varausjärjestelmän kautta (kolmannen osapuolen ohjelmistopalvelu).</li>'
         '<li>Stebbyn, Kingituste Saaren tai muiden välitysalustojen kautta, kun käytät niiden kuponkeja tai lahjakortteja.</li>'
         '<li>Verkkosivuston evästeiden ja analytiikan (Matomo) kautta — vain anonyymisti.</li>'
         '</ul>'),
        ('4. Tietojen siirtäminen kolmansille osapuolille',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Emme myy tai jaa henkilötietojasi kolmansille osapuolille markkinointitarkoituksiin. Tietoja voidaan siirtää vain seuraavissa tapauksissa:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Palveluntarjoajat:</strong> SalonLife OÜ (varausjärjestelmä) — vain sopimuksen täyttämiseen tarvittavassa laajuudessa.</li>'
         '<li><strong>Maksunkäsittelijät:</strong> pankit ja maksuyhtiöt maksutapahtumien suorittamiseen.</li>'
         '<li><strong>Viranomaiset:</strong> lakisääteisten velvollisuuksien täyttämiseksi (esim. veroviranomainen).</li>'
         '<li>Kolmansien osapuolten alustat (Stebby, Kingituste Saar jne.) käsittelevät vain välityspalvelunsa tarjoamiseen tarvittavia tietoja — oman tietosuojakäytäntönsä mukaisesti.</li>'
         '</ul>'),
        ('5. Tietojen säilytysajat',
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Terveystiedot ja istuntomuistiinpanot:</strong> säilytetään enintään 3 vuotta viimeisestä käynnistä tai suostumuksen peruuttamiseen asti (kumpi tahansa tulee ensin).</li>'
         '<li><strong>Laskut ja maksutiedot:</strong> säilytetään 7 vuotta kirjanpitolainsäädännön mukaisesti.</li>'
         '<li><strong>Yhteystiedot ja viestintätiedot:</strong> säilytetään enintään 2 vuotta viimeisestä yhteydestä.</li>'
         '<li><strong>Anonyymi tilasto:</strong> säilytetään toistaiseksi.</li>'
         '</ul>'),
        ('6. Rekisteröidyn oikeudet',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">GDPR:n nojalla sinulla on seuraavat oikeudet:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Oikeus tutustua tietoihin:</strong> oikeus saada tietää, mitä henkilötietoja käsittelemme sinusta.</li>'
         '<li><strong>Oikeus tietojen oikaisemiseen:</strong> oikeus vaatia virheellisten tietojen korjaamista.</li>'
         '<li><strong>Oikeus tietojen poistamiseen ("oikeus tulla unohdetuksi"):</strong> oikeus vaatia tietojen poistamista, kun käsittelylle ei ole oikeusperustetta.</li>'
         '<li><strong>Oikeus käsittelyn rajoittamiseen:</strong> oikeus vaatia käsittelyn rajoittamista tietyissä tilanteissa.</li>'
         '<li><strong>Oikeus tietojen siirrettävyyteen:</strong> oikeus saada tietosi koneluettavassa muodossa.</li>'
         '<li><strong>Vastustamisoikeus:</strong> oikeus vastustaa oikeutettuun etuun perustuvaa käsittelyä.</li>'
         '<li><strong>Suostumuksen peruuttaminen:</strong> voit milloin tahansa lopettaa suostumukseen perustuvan käsittelyn ottamalla yhteyttä osoitteeseen info@mvtherapy.ee. Tämä ei vaikuta ennen peruuttamista tapahtuneen käsittelyn lainmukaisuuteen.</li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Oikeuksiesi käyttämiseksi ota yhteyttä: <a href="mailto:info@mvtherapy.ee" style="color:var(--brand);">info@mvtherapy.ee</a>. Vastaamme 30 päivän kuluessa.</p>'),
        ('7. Evästeet (cookies)',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Käytämme verkkosivustollamme seuraavia evästetyyppejä:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>Välttämättömät evästeet:</strong> tarvitaan verkkosivuston toimintaan (esim. istuntoevästeet). Niiden käyttö ei edellytä suostumusta.</li>'
         '<li><strong>Analyyttiset evästeet (Matomo):</strong> sivuston käytön mittaamiseen. Käytämme itse ylläpidettävää Matomo-ratkaisua, joka ei jaa tietoja kolmansille osapuolille. Tiedot on anonymisoitu.</li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Voit poistaa evästeet käytöstä milloin tahansa selaimesi asetuksista.</p>'),
        ('8. Tietoturva',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Toteutamme asianmukaisia teknisiä ja organisatorisia toimenpiteitä henkilötietojesi suojaamiseksi luvattomalta käytöltä, muuttamiselta, paljastamiselta tai tuhoamiselta:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li>Tiedonsiirto tapahtuu salatun HTTPS-yhteyden kautta.</li>'
         '<li>Fyysiset asiakirjat säilytetään lukituissa tiloissa.</li>'
         '<li>Digitaaliset tiedot on suojattu käyttöoikeusrajoituksilla.</li>'
         '<li>Kaikkien kolmansien osapuolten palveluntarjoajien kanssa on tehty tietojenkäsittelysopimukset.</li>'
         '</ul>'),
        ('9. Yhteystiedot ja riitojen ratkaisu',
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Kysymyksiä, pyyntöjä tai valituksia varten ota yhteyttä:</p>'
         '<ul style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;padding-left:1.4rem;">'
         '<li><strong>MV Therapy OÜ</strong>, Viimsi Haigla, Ravi tee 4, 74001 Haabneeme</li>'
         '<li>Sähköposti: <a href="mailto:info@mvtherapy.ee" style="color:var(--brand);">info@mvtherapy.ee</a></li>'
         '<li>Puh.: <a href="tel:+37258189561" style="color:var(--brand);">+372 5818 9561</a></li>'
         '</ul>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Jos uskot, että tietojasi käsitellään laittomasti, sinulla on oikeus tehdä valitus Viron tietosuojaviranomaiselle (AKI): <a href="https://www.aki.ee" target="_blank" rel="noopener noreferrer" style="color:var(--brand);">www.aki.ee</a>.</p>'
         '<p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;margin-bottom:.6rem;">Tietosuojakäytäntöä päivitetään tarvittaessa. Viimeksi päivitetty: kesäkuu 2026.</p>'),
    ],
}

H2_STYLE = "font-family:'DM Serif Display',serif;font-size:clamp(1.1rem,2vw,1.5rem);font-weight:400;color:var(--text);margin-bottom:.8rem;"

def build_nav_links(links):
    parts = []
    for href, text in links:
        parts.append('        <a href="{}">{}</a>'.format(href, text))
    return '\n'.join(parts)

def build_lang_links(links):
    parts = []
    for href, text, active in links:
        cls = ' class="active"' if active else ''
        parts.append('          <a href="{}"{}>{}</a>'.format(href, cls, text))
    return '\n'.join(parts)

def build_footer_pages(links):
    parts = []
    for href, text in links:
        parts.append('          <div><a href="{}">{}</a></div>'.format(href, text))
    return '\n'.join(parts)

def build_sections(lang):
    parts = []
    for title, body in SECTIONS[lang]:
        section = (
            '\n      <section style="margin-bottom:2rem;">\n'
            '        <h2 style="{}">{}</h2>\n'
            '        {}\n'
            '      </section>'
        ).format(H2_STYLE, title, body)
        parts.append(section)
    return '\n'.join(parts)

def build_page(lang):
    c = META[lang]
    nav_desktop = build_nav_links(c['nav'])
    nav_mobile = build_nav_links(c['nav'])
    lang_links_desktop = build_lang_links(c['lang_links'])
    lang_links_mobile = build_lang_links(c['lang_links'])
    footer_pages = build_footer_pages(c['footer_pages_links'])
    sections = build_sections(lang)

    html = '''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5.0, user-scalable=yes, shrink-to-fit=no">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="theme-color" content="#44437d">
  <!-- Geo Location Meta Tags -->
  <meta name="geo.region" content="EE-37">
  <meta name="geo.placename" content="Tallinn, Estonia">
  <meta name="geo.position" content="59.5093;24.8283">
  <meta name="ICBM" content="59.5093, 24.8283">
  <!-- Open Graph Meta Tags -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{og_url}">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:image" content="https://mvtherapy.ee/public/img/mvsubheader.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="{og_locale}">

  <!-- Twitter Card Meta Tags -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="{tw_url}">
  <meta property="twitter:title" content="{tw_title}">
  <meta property="twitter:description" content="{tw_desc}">
  <meta property="twitter:image" content="https://mvtherapy.ee/public/img/mvsubheader.png">

  <!-- Canonical URL -->
  <link rel="canonical" href="{canonical}">

  <!-- Alternate languages -->
  <link rel="alternate" hreflang="et" href="https://mvtherapy.ee/et/privaatsuspoliitika.html">
  <link rel="alternate" hreflang="ru" href="https://mvtherapy.ee/ru/privaatsuspoliitika.html">
  <link rel="alternate" hreflang="en" href="https://mvtherapy.ee/en/privaatsuspoliitika.html">
  <link rel="alternate" hreflang="fi" href="https://mvtherapy.ee/fi/privaatsuspoliitika.html">
  <link rel="alternate" hreflang="x-default" href="https://mvtherapy.ee/et/privaatsuspoliitika.html">

  <!-- Favicons -->
  <link rel="apple-touch-icon" sizes="180x180" href="/icons/apple-icon-180x180.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/icons/favicon-16x16.png">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=DM+Serif+Display&display=swap" onload="this.onload=null;this.rel=\'stylesheet\'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=DM+Serif+Display&display=swap"></noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0">

  <style>
    :root {{
      --bg: #f5f4fa; --surface: rgba(255,255,255,.78); --surface-solid: #ffffff;
      --text: #1a1832; --text-secondary: #5e5977;
      --line: rgba(68,67,125,.10); --brand: #44437d; --brand-light: #5c5b9e;
      --brand-accent: #6c6bb5; --brand-bg: #eeedf8; --brand-glow: rgba(68,67,125,.12);
      --shadow: 0 8px 32px rgba(26,24,50,.08); --shadow-lg: 0 16px 56px rgba(26,24,50,.13);
      --shadow-card: 0 4px 20px rgba(26,24,50,.06);
      --radius: 20px; --radius-sm: 14px; --radius-xs: 10px;
      --container: 1240px; --header-h: 72px;
    }}
    *,*::before,*::after {{ box-sizing: border-box; margin: 0; }}
    html {{ scroll-behavior: smooth; -webkit-text-size-adjust: 100%; overflow-x: hidden; }}
    body {{
      font-family: \'DM Sans\', system-ui, -apple-system, sans-serif;
      color: var(--text); background: var(--bg); line-height: 1.6;
      text-rendering: optimizeLegibility; -webkit-font-smoothing: antialiased; overflow-x: hidden;
    }}
    img {{ max-width: 100%; display: block; height: auto; }}
    a {{ color: inherit; }}
    .container {{ width: min(100% - 28px, var(--container)); margin-inline: auto; }}
    .skip-link {{ position: absolute; left: -9999px; top: 0; }}
    .skip-link:focus {{ left: 16px; top: 16px; z-index: 1000; background: #fff; padding: 12px 16px; border-radius: 12px; }}
    .site-header {{
      position: sticky; top: 0; z-index: 100;
      backdrop-filter: blur(20px) saturate(1.4); -webkit-backdrop-filter: blur(20px) saturate(1.4);
      background: rgba(245,244,250,.82); border-bottom: 1px solid var(--line); height: var(--header-h);
    }}
    .topbar {{ display: flex; align-items: center; justify-content: space-between; gap: 8px; height: var(--header-h); }}
    .brand {{ display: flex; align-items: center; gap: 8px; text-decoration: none; min-width: 0; flex-shrink: 1; }}
    .brand-logo {{ width: 38px; height: 38px; border-radius: 10px; background: linear-gradient(135deg, var(--brand), var(--brand-accent)); box-shadow: inset 0 1px 0 rgba(255,255,255,.25), 0 4px 12px rgba(68,67,125,.2); flex-shrink: 0; }}
    .brand-text {{ min-width: 0; overflow: hidden; }}
    .brand-text strong {{ display: block; font-size: .88rem; font-weight: 700; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; }}
    .brand-text span {{ display: block; font-size: .68rem; color: var(--text-secondary); white-space: nowrap; text-overflow: ellipsis; overflow: hidden; }}
    .desktop-nav {{ display: none; gap: 4px; align-items: center; }}
    .desktop-nav a {{ text-decoration: none; padding: 8px 14px; border-radius: 999px; font-weight: 600; font-size: .9rem; color: var(--text-secondary); transition: all .2s; }}
    .desktop-nav a:hover, .desktop-nav a[aria-current="page"] {{ background: var(--surface-solid); color: var(--brand); box-shadow: var(--shadow-card); }}
    .header-actions {{ display: flex; align-items: center; gap: 6px; flex-shrink: 0; }}
    .mobile-lang-header {{ display: flex; gap: 1px; align-items: center; }}
    .mobile-lang-header a {{ text-decoration: none; padding: 4px 6px; border-radius: 999px; font-weight: 700; font-size: .7rem; color: var(--text-secondary); transition: all .2s; }}
    .mobile-lang-header a.active {{ background: var(--brand-bg); color: var(--brand); }}
    .lang-switch {{ display: none; gap: 2px; }}
    .lang-switch a {{ text-decoration: none; padding: 6px 10px; border-radius: 999px; font-weight: 700; font-size: .8rem; color: var(--text-secondary); transition: all .2s; }}
    .lang-switch a:hover, .lang-switch a.active {{ background: var(--brand-bg); color: var(--brand); }}
    .btn {{ display: inline-flex; align-items: center; justify-content: center; gap: 8px; border: 0; border-radius: 999px; padding: 12px 20px; font-weight: 700; font-size: .9rem; text-decoration: none; cursor: pointer; transition: transform .2s, box-shadow .2s; font-family: inherit; }}
    .btn-primary {{ color: #fff; background: linear-gradient(135deg, var(--brand), var(--brand-accent)); box-shadow: 0 8px 24px rgba(68,67,125,.22); }}
    .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 12px 32px rgba(68,67,125,.3); }}
    .mobile-toggle {{ width: 40px; height: 40px; border-radius: 10px; border: 1px solid var(--line); background: #fff; box-shadow: var(--shadow-card); display: inline-grid; place-items: center; cursor: pointer; font-size: 1.1rem; -webkit-tap-highlight-color: transparent; }}
    .mobile-panel {{ display: none; position: absolute; top: var(--header-h); left: 0; right: 0; background: rgba(245,244,250,.96); backdrop-filter: blur(20px); border-bottom: 1px solid var(--line); padding: 16px; box-shadow: 0 12px 40px rgba(0,0,0,.1); z-index: 99; }}
    .mobile-panel.open {{ display: block; }}
    .mobile-panel nav {{ display: grid; gap: 6px; }}
    .mobile-panel nav a {{ text-decoration: none; background: #fff; padding: 14px 16px; border-radius: var(--radius-sm); box-shadow: var(--shadow-card); font-weight: 600; display: block; }}
    .terms-content {{ background: var(--surface); border: 1px solid rgba(255,255,255,.7); backdrop-filter: blur(16px); border-radius: 28px; box-shadow: var(--shadow-lg); padding: 32px 24px; margin: 28px 0; }}
    .terms-content h1 {{ font-family: \'DM Serif Display\', Georgia, serif; font-size: clamp(1.6rem, 4vw, 2.8rem); line-height: 1.12; margin: 0 0 24px; letter-spacing: -.02em; font-weight: 400; }}
    .site-footer {{ background: #1a1832; color: rgba(255,255,255,.7); padding: 36px 0 56px; margin-top: 28px; }}
    .footer-grid {{ display: grid; gap: 24px; grid-template-columns: 1fr; }}
    .footer-grid strong {{ color: #fff; display: block; margin-bottom: 6px; font-size: .9rem; }}
    .footer-grid a {{ color: rgba(255,255,255,.7); text-decoration: none; transition: color .2s; }}
    .footer-grid a:hover {{ color: #fff; }}
    .footer-locations {{ display: flex; flex-direction: column; gap: 10px; }}
    .footer-location {{ display: flex; flex-direction: column; gap: 2px; }}
    .footer-location span {{ color: rgba(255,255,255,.7); font-size: .85rem; }}
    .footer-social {{ display: flex; gap: 10px; align-items: center; margin-top: 10px; }}
    .footer-social a {{ width: 36px; height: 36px; border-radius: 8px; background: rgba(255,255,255,.08); display: inline-grid; place-items: center; transition: background .2s, transform .2s; }}
    .footer-social a:hover {{ background: rgba(255,255,255,.16); transform: translateY(-2px); }}
    .footer-social svg {{ width: 18px; height: 18px; fill: rgba(255,255,255,.85); }}
    .go-top {{ position: fixed; bottom: 20px; right: 20px; z-index: 90; width: 48px; height: 48px; border-radius: 50%; background: var(--brand); color: #fff; border: 0; box-shadow: 0 4px 16px rgba(68,67,125,.3); cursor: pointer; display: none; place-items: center; font-size: 1.3rem; transition: transform .2s; }}
    .go-top:hover {{ transform: translateY(-3px); }}
    .mobile-book-bar {{ position: fixed; bottom: 0; left: 0; right: 0; z-index: 95; background: rgba(245,244,250,.92); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-top: 1px solid var(--line); padding: 10px 16px; padding-bottom: calc(10px + env(safe-area-inset-bottom)); display: flex; align-items: center; justify-content: space-between; gap: 10px; box-shadow: 0 -4px 20px rgba(0,0,0,.08);
      pointer-events: none;
    }}
    .mobile-book-bar .btn, .mobile-book-bar .book-info {{ pointer-events: auto; }}
    .mobile-book-bar .book-info {{ font-size: .82rem; color: var(--text-secondary); line-height: 1.3; }}
    .mobile-book-bar .book-info strong {{ display: block; font-size: .9rem; color: var(--text); }}
    .mobile-book-bar .btn {{ flex-shrink: 0; padding: 12px 22px; }}
    #cookieNotice {{ position: fixed; bottom: 20px; left: 20px; background: #fff; border: 1px solid #ddd; border-radius: 16px; padding: 18px; max-width: 320px; box-shadow: 0 8px 32px rgba(0,0,0,.15); z-index: 9999; font-size: .88rem; line-height: 1.5; }}
    #cookieNotice .cookie-btn {{ background: var(--brand); color: #fff; border: 0; padding: 8px 18px; border-radius: 999px; cursor: pointer; font-weight: 700; font-size: .85rem; margin-top: 10px; font-family: inherit; }}
    .partner-bar {{ display:flex; gap:28px; margin:0 0 14px; justify-content:center; align-items:center; }}
    .partner-bar-header {{ display:none; }}
    .partner-icon {{ display:flex; flex-direction:column; align-items:center; gap:3px; text-decoration:none; color:var(--text-secondary); font-size:.65rem; font-weight:700; transition:all .2s; padding:4px 8px; }}
    .partner-icon:hover {{ color:var(--brand); transform:translateY(-2px); }}
    .partner-icon img {{ width:28px; height:28px; object-fit:contain; border-radius:4px; display:block; }}
    @media (max-width: 899px) {{ .site-footer {{ padding-bottom: 90px; }} .go-top {{ bottom: 80px; }} #cookieNotice {{ bottom: 80px; }} }}
    @media (min-width: 900px) {{
      .desktop-nav, .lang-switch {{ display: flex; }}
      .mobile-toggle, .mobile-lang-header {{ display: none; }}
      .brand-text span {{ font-size: .78rem; }} .brand-logo {{ width: 42px; height: 42px; border-radius: 12px; }}
      .brand-text strong {{ font-size: .95rem; }}
      .footer-grid {{ grid-template-columns: 1.4fr 1fr 1fr .8fr; }}
      .mobile-book-bar {{ display: none !important; }}
      .terms-content {{ padding: 48px 40px; }}
    }}
    @media(min-width:900px) {{ .partner-bar {{ display:none; }} .partner-bar-header {{ display:flex; gap:6px; align-items:center; flex-shrink:0; }} .partner-bar-header .partner-icon {{ flex-direction:column; gap:2px; padding:2px 6px; font-size:.6rem; }} .partner-bar-header .partner-icon img {{ width:26px; height:26px; }} }}
  </style>
</head>
<body>
  <a class="skip-link" href="#content">{skip_link}</a>

  <header class="site-header">
    <div class="container topbar">
      <a class="brand" href="{brand_home}" aria-label="MV Therapy">
        <div class="brand-logo" aria-hidden="true"></div>
        <div class="brand-text">
          <strong>MV Therapy</strong>
          <span>{brand_sub}</span>
        </div>
      </a>
      <div class="partner-bar-header" aria-label="Partners">
        <a href="https://app.stebby.eu/pos/mv.therapy.massaazi.ja.vaimse.teraapia.keskus/services" target="_blank" rel="noopener noreferrer" class="partner-icon" aria-label="{stebby_label}">
          <img src="/public/img/stebby.png" alt="Stebby" width="32" height="32">
          <span>Stebby</span>
        </a>
        <a href="{arve_href}" class="partner-icon" aria-label="{arve_label}">
          <img src="/public/img/tsek.png" alt="Tsekk" width="32" height="32">
          <span>Arve</span>
        </a>
        <a href="{partner_href}" class="partner-icon" aria-label="{partner_label}">
          <img src="/public/img/partner.png" alt="Partner" width="32" height="32">
          <span>Partner</span>
        </a>
      </div>

      <nav class="desktop-nav" aria-label="Main">
{nav_desktop}
      </nav>
      <div class="header-actions">
        <div class="mobile-lang-header" aria-label="Languages">
{lang_links_mobile}
        </div>
        <div class="lang-switch" aria-label="Languages">
{lang_links_desktop}
        </div>
        <button class="mobile-toggle" id="mobileToggle" aria-expanded="false" aria-controls="mobilePanel" aria-label="{menu_label}">
          <span class="material-symbols-outlined">menu</span>
        </button>
      </div>
    </div>
    <div class="mobile-panel" id="mobilePanel">
      <div class="container">
        <nav aria-label="Mobile">
{nav_mobile}
        </nav>
      </div>
    </div>
  </header>
<div style="background:rgba(245,244,250,0.95);border-bottom:1px solid rgba(68,67,125,0.1);padding:8px 0;"><div class="container" style="display:flex;align-items:center;gap:8px;"><span style="font-size:.8rem;color:#5e5977;font-weight:500;">{location_label}</span><div style="display:inline-flex;align-items:center;gap:4px;background:#fff;border:1px solid rgba(68,67,125,0.15);border-radius:999px;padding:3px;"><span style="background:#44437d;color:#fff;font-weight:700;font-size:.8rem;padding:5px 16px;border-radius:999px;">{city_active}</span><a href="{city_other_href}" style="color:#2563eb;font-weight:700;font-size:.8rem;padding:5px 16px;border-radius:999px;text-decoration:none;">{city_other}</a></div></div></div>

  <main id="content">
    <div class="container">
      <div class="partner-bar">
        <a href="https://app.stebby.eu/pos/mv.therapy.massaazi.ja.vaimse.teraapia.keskus/services" target="_blank" rel="noopener noreferrer" class="partner-icon" aria-label="{stebby_label}">
          <img src="/public/img/stebby.png" alt="Stebby" width="28" height="28">
          <span>Stebby</span>
        </a>
        <a href="{arve_href}" class="partner-icon" aria-label="{arve_label}">
          <img src="/public/img/tsek.png" alt="Tsekk" width="28" height="28">
          <span>Arve</span>
        </a>
        <a href="{partner_href}" class="partner-icon" aria-label="{partner_label}">
          <img src="/public/img/partner.png" alt="Partner" width="28" height="28">
          <span>Partner</span>
        </a>
      </div>

      <div class="terms-content">
        <h1>{h1}</h1>

        <p style="font-size:.92rem;color:var(--text-secondary);line-height:1.7;font-style:italic;margin-bottom:2rem;">{intro}</p>
{sections}

      </div>

      <div id="broneeri-container"></div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <strong>MV Therapy</strong>
          <div>Medical Verified Therapy</div>
          <div style="margin-top:6px;font-size:.82rem;">{footer_copy}</div>
          <div class="footer-social">
            <a href="https://www.facebook.com/profile.php?id=100090837369433" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M9.198 21.5h4v-8.01h3.604l.396-3.98h-4V7.5a1 1 0 0 1 1-1h3v-4h-3a5 5 0 0 0-5 5v2.01h-2l-.396 3.98h2.396v8.01Z"/></svg>
            </a>
            <a href="https://www.instagram.com/medmassaaz/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.7 3.7 0 0 1-1.38-.9 3.7 3.7 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16Zm0 1.8c-3.15 0-3.5.01-4.74.07-1.07.05-1.65.23-2.04.38-.51.2-.88.44-1.26.82-.38.38-.62.75-.82 1.26-.15.39-.33.97-.38 2.04-.06 1.24-.07 1.59-.07 4.74s.01 3.5.07 4.74c.05 1.07.23 1.65.38 2.04.2.51.44.88.82 1.26.38.38.75.62 1.26.82.39.15.97.33 2.04.38 1.24.06 1.59.07 4.74.07s3.5-.01 4.74-.07c1.07-.05 1.65-.23 2.04-.38.51-.2.88-.44 1.26-.82.38-.38.62-.75.82-1.26.15-.39.33-.97.38-2.04.06-1.24.07-1.59.07-4.74s-.01-3.5-.07-4.74c-.05-1.07-.23-1.65-.38-2.04a3.27 3.27 0 0 0-.82-1.26 3.27 3.27 0 0 0-1.26-.82c-.39-.15-.97-.33-2.04-.38-1.24-.06-1.59-.07-4.74-.07Zm0 3.06a4.98 4.98 0 1 1 0 9.96 4.98 4.98 0 0 1 0-9.96Zm0 1.8a3.18 3.18 0 1 0 0 6.36 3.18 3.18 0 0 0 0-6.36Zm5.18-3.04a1.16 1.16 0 1 1 0 2.32 1.16 1.16 0 0 1 0-2.32Z"/></svg>
            </a>
            <a href="https://www.tiktok.com/@medmassaaz" target="_blank" rel="noopener noreferrer" aria-label="TikTok">
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-.88-.05A6.33 6.33 0 0 0 5.8 20.1a6.34 6.34 0 0 0 10.86-4.43V8.84a8.16 8.16 0 0 0 4.77 1.52V6.92a4.85 4.85 0 0 1-1.84-.23Z"/></svg>
            </a>
          </div>
        </div>
        <div>
          <strong>{footer_addr}</strong>
          <div class="footer-locations">
            <div class="footer-location">
              <strong>Tallinn / Viimsi</strong>
              <span>Viimsi Haigla, Ravi tee 4</span>
              <span>74001 Haabneeme</span>
            </div>
            <div class="footer-location">
              <strong>P&#228;rnu</strong>
              <span>R&#252;&#252;tli 47 II korrus</span>
              <span>80010 P&#228;rnu</span>
            </div>
          </div>
        </div>
        <div>
          <strong>{footer_contact}</strong>
          <div><a href="tel:+37258189561">+372 5818 9561</a></div>
          <div><a href="mailto:info@mvtherapy.ee">info@mvtherapy.ee</a></div>
        </div>
        <div>
          <strong>{footer_pages}</strong>
{footer_pages_html}
        </div>
      </div>
    </div>
  </footer>

  <button class="go-top" id="goTop" aria-label="{go_top_label}">
    <span class="material-symbols-outlined">expand_less</span>
  </button>

  <div class="mobile-book-bar" id="mobileBookBar">
    <div class="book-info">
      <strong>{book_info_strong}</strong>
      {book_info_addr}
    </div>
    <button class="btn btn-primary book-trigger">{book_btn}</button>
  </div>

  <div id="cookieNotice" style="display:none;" role="dialog" aria-label="{cookie_label}">
    <p>{cookie_text}</p>
    <button class="cookie-btn" id="cookieAccept">{cookie_btn}</button>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      var toggle = document.getElementById('mobileToggle');
      var panel = document.getElementById('mobilePanel');
      if (toggle && panel) {{
        toggle.addEventListener('click', function() {{
          var open = panel.classList.toggle('open');
          toggle.setAttribute('aria-expanded', String(open));
        }});
        panel.querySelectorAll('a').forEach(function(a) {{
          a.addEventListener('click', function() {{ panel.classList.remove('open'); toggle.setAttribute('aria-expanded','false'); }});
        }});
        document.addEventListener('click', function(e) {{
          if (!toggle.contains(e.target) && !panel.contains(e.target)) {{
            panel.classList.remove('open'); toggle.setAttribute('aria-expanded','false');
          }}
        }});
      }}
      document.querySelectorAll('.book-trigger').forEach(function(btn) {{
        btn.addEventListener('click', function(e) {{
          e.preventDefault();
          var container = document.getElementById('broneeri-container');
          if (!container) return;
          container.style.cssText = 'height:auto;overflow:visible;';
          var slBtn = container.querySelector('.button-cta, button, [class*="button"], [class*="btn"]');
          if (slBtn) {{
            slBtn.click();
            setTimeout(function() {{ container.style.cssText = 'height:0;overflow:hidden;margin:0;padding:0;'; }}, 300);
          }} else {{
            setTimeout(function() {{
              var retry = container.querySelector('.button-cta, button, [class*="button"], [class*="btn"]');
              if (retry) retry.click();
              setTimeout(function() {{ container.style.cssText = 'height:0;overflow:hidden;margin:0;padding:0;'; }}, 300);
            }}, 1000);
          }}
        }});
      }});
      var goTop = document.getElementById('goTop');
      var scrollTimer;
      window.addEventListener('scroll', function() {{
        if (scrollTimer) return;
        scrollTimer = setTimeout(function() {{
          scrollTimer = null;
          if (goTop) goTop.style.display = window.scrollY > 300 ? 'grid' : 'none';
        }}, 100);
      }}, {{ passive: true }});
      if (goTop) goTop.addEventListener('click', function() {{ window.scrollTo({{ top: 0, behavior: 'smooth' }}); }});
      var notice = document.getElementById('cookieNotice');
      var accept = document.getElementById('cookieAccept');
      if (notice && accept) {{
        if (!localStorage.getItem('cookieAccepted')) {{
          setTimeout(function() {{ notice.style.display = 'block'; }}, 1200);
        }}
        accept.addEventListener('click', function() {{
          localStorage.setItem('cookieAccepted','true'); notice.style.display = 'none';
        }});
      }}
    }});
  </script>

  <script src="https://static.elfsight.com/platform/platform.js" async></script>

  <script>
    var book_texts = {{ et: 'Broneeri aeg', ru: 'Записаться на приём', en: 'Book appointment', fi: 'Varaa aika' }};
    !function(e,n,t){{
      var i=document,o="script",a=i.createElement(o),d=i.getElementsByTagName(o)[0];
      a.async=!0;a.defer=!0;
      a.src="//widget.salon.life/static/js/widget.js?t="+(new Date).getTime();
      n&&a.addEventListener("load",function(){{t.SalonLifeCb=n}},!1);
      d.parentNode.insertBefore(a,d)
    }}(0,function(){{
      window.SalonLifeWidget.mount({{
        identifier:3986,button_text:book_texts.{sl_lang},language:'{sl_lang}',color:'#44437d',container:'#broneeri-container'
      }})
    }},window);
  </script>

  <script>
    var _paq=window._paq=window._paq||[];
    _paq.push(['trackPageView']);_paq.push(['enableLinkTracking']);
    (function(){{var u="//mvtherapy.ee/matomo/";
    _paq.push(['setTrackerUrl',u+'matomo.php']);_paq.push(['setSiteId','1']);
    var d=document,g=d.createElement('script'),s=d.getElementsByTagName('script')[0];
    g.async=true;g.src=u+'matomo.js';s.parentNode.insertBefore(g,s);}})();
  </script>
</body>
</html>'''

    return html.format(
        lang=c['lang'],
        title=c['title'],
        desc=c['desc'],
        og_url=c['og_url'],
        og_title=c['og_title'],
        og_desc=c['og_desc'],
        og_locale=c['og_locale'],
        tw_url=c['tw_url'],
        tw_title=c['tw_title'],
        tw_desc=c['tw_desc'],
        canonical=c['canonical'],
        skip_link=c['skip_link'],
        brand_home=c['brand_home'],
        brand_sub=c['brand_sub'],
        stebby_label=c['stebby_label'],
        arve_href=c['arve_href'],
        arve_label=c['arve_label'],
        partner_href=c['partner_href'],
        partner_label=c['partner_label'],
        nav_desktop=nav_desktop,
        nav_mobile=nav_mobile,
        lang_links_mobile=lang_links_mobile,
        lang_links_desktop=lang_links_desktop,
        menu_label=c['menu_label'],
        location_label=c['location_label'],
        city_active=c['city_active'],
        city_other_href=c['city_other_href'],
        city_other=c['city_other'],
        h1=c['h1'],
        intro=c['intro'],
        sections=sections,
        footer_copy=c['footer_copy'],
        footer_addr=c['footer_addr'],
        footer_contact=c['footer_contact'],
        footer_pages=c['footer_pages'],
        footer_pages_html=footer_pages,
        go_top_label=c['go_top_label'],
        book_info_strong=c['book_info_strong'],
        book_info_addr=c['book_info_addr'],
        book_btn=c['book_btn'],
        cookie_text=c['cookie_text'],
        cookie_btn=c['cookie_btn'],
        cookie_label=c['cookie_label'],
        sl_lang=c['sl_lang'],
    )


for lang in LANGS:
    path = '/home/user/static/{}/privaatsuspoliitika.html'.format(lang)
    content = build_page(lang)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Written: {}'.format(path))

print('Done.')
