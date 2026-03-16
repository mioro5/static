#!/usr/bin/env python3
"""Create Finnish (fin) language version of MV Therapy website.

Reads English pages, translates content to Finnish, adds Finnish notice banner,
removes workshop section, updates navigation, and writes to fin/ directory.
"""

import os
import re
import shutil

SOURCE_DIR = '/home/user/static/en'
TARGET_DIR = '/home/user/static/fin'

# ── Finnish notice banner CSS (inserted before </style>) ──────────────────────
NOTICE_CSS = """
    /* ===== FINNISH LANGUAGE NOTICE BANNER ===== */
    .fin-notice {
      background: linear-gradient(135deg, #fff8e1, #fff3cd);
      border-bottom: 2px solid #f5a623;
      padding: 12px 0;
      text-align: center;
      font-size: .9rem;
      color: #5d4037;
      font-weight: 500;
      position: relative;
      z-index: 99;
    }
    .fin-notice .container {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .fin-notice-flag { font-size: 1.3rem; flex-shrink: 0; }
    .fin-notice-text { line-height: 1.4; }
    .fin-notice-text strong { color: #3e2723; }
"""

# Finnish notice banner HTML (inserted after </header>)
NOTICE_HTML = """
  <!-- Suomenkielinen kieli-ilmoitus -->
  <div class="fin-notice" role="note">
    <div class="container">
      <span class="fin-notice-flag">🇫🇮</span>
      <span class="fin-notice-text"><strong>Kielitiedote:</strong> En puhu suomea, mutta loin tämän sivun, jotta sinun olisi mukavampi tutustua palveluihimme.</span>
    </div>
  </div>
"""

# ── Common text replacements (applied to every page) ─────────────────────────
# Order matters — more specific patterns first
COMMON_REPLACEMENTS = [
    # HTML lang attribute
    ('lang="en"', 'lang="fi"'),

    # Meta charset / locale
    ('content="en_US"', 'content="fi_FI"'),

    # Skip link
    ('>Skip to main content<', '>Siirry pääsisältöön<'),

    # Brand subtitle
    ('Medical Verified Therapy', 'Lääketieteellisesti varmennettu terapia'),

    # aria labels
    ('aria-label="MV Therapy home page"', 'aria-label="MV Therapy etusivu"'),
    ('aria-label="Main menu"', 'aria-label="Päävalikko"'),
    ('aria-label="Mobile menu"', 'aria-label="Mobiilivalikko"'),
    ('aria-label="Language"', 'aria-label="Kieli"'),
    ('aria-label="Open menu"', 'aria-label="Avaa valikko"'),
    ('aria-label="Scroll to top of page"', 'aria-label="Vieritä sivun alkuun"'),
    ('aria-label="Cookie notice"', 'aria-label="Evästeilmoitus"'),
    ('aria-label="Scroll left"', 'aria-label="Vieritä vasemmalle"'),
    ('aria-label="Scroll right"', 'aria-label="Vieritä oikealle"'),
    ('aria-label="Breadcrumb"', 'aria-label="Navigointipolku"'),

    # Footer
    ('<strong>Address</strong>', '<strong>Osoite</strong>'),
    ('<strong>Contact</strong>', '<strong>Yhteystiedot</strong>'),
    ('<strong>Pages</strong>', '<strong>Sivut</strong>'),
    ('>Massage services<', '>Hierontapalvelut<'),
    ('📍 View on map', '📍 Näytä kartalla'),
    ('© 2025 MV Therapy – Massage in Pärnu', '© 2025 MV Therapy – Hieronta Pärnussa'),
    ('<div>2nd floor</div>', '<div>2. kerros</div>'),
    ('Rüütli 47, 2nd floor', 'Rüütli 47, 2. kerros'),

    # Mobile booking bar
    ('>Book appointment<', '>Varaa aika<'),
    ('Book appointment', 'Varaa aika'),

    # Cookie notice
    ('We use cookies to enhance your experience, personalize content and analyze traffic.',
     'Käytämme evästeitä parantaaksemme käyttökokemustasi, personoidaksemme sisältöä ja analysoidaksemme liikennettä.'),
    ('OK, accept', 'OK, hyväksy'),

    # Footer page links text
    ('>Massage in Pärnu<', '>Hieronta Pärnussa<'),
    ('>Diagnoses<', '>Diagnoosit<'),
    ('>Blog<', '>Blogi<'),
    ('>FAQ<', '>UKK<'),

    # Common content phrases
    ('Pärnu city centre', 'Pärnun kaupunkikeskusta'),
    ('Pärnu city center', 'Pärnun kaupunkikeskusta'),
    ('Pärnu massage centre', 'Pärnun hierontakeskus'),
    ('in Pärnu', 'Pärnussa'),
    ('at Rüütli 47', 'osoitteessa Rüütli 47'),
    ('Rüütli 47, Pärnu', 'Rüütli 47, Pärnu'),

    # Common button/link text
    ('All services →', 'Kaikki palvelut →'),
    ('All diagnoses →', 'Kaikki diagnoosit →'),
    ('All articles →', 'Kaikki artikkelit →'),
    ('More questions →', 'Lisää kysymyksiä →'),
    ('See all services →', 'Katso kaikki palvelut →'),
    ('Book now →', 'Varaa nyt →'),
    ('Read more →', 'Lue lisää →'),
    ('Learn more →', 'Lue lisää →'),

    # Breadcrumb common items
    ('>Home<', '>Etusivu<'),
    ('>Massages<', '>Hieronnat<'),
    ('>Blog<', '>Blogi<'),
    ('>Campaigns<', '>Kampanjat<'),

    # Scroll nav arrows
    ('aria-label="Scroll left"', 'aria-label="Vieritä vasemmalle"'),
    ('aria-label="Scroll right"', 'aria-label="Vieritä oikealle"'),
]

# ── Per-page content translation dictionaries ─────────────────────────────────

HOME_REPLACEMENTS = [
    # Title/meta
    ('Massage in Pärnu | MV Therapy',
     'Hieronta Pärnussa | MV Therapy'),
    ('Professional massage therapist in Pärnu',
     'Ammatillinen hieroja Pärnussa'),

    # Hero
    ('5.0★ Google rating · 5,000+ clients · Pärnu city centre',
     '5.0★ Google-arvosana · 5 000+ asiakasta · Pärnun keskusta'),
    ('Massage in Pärnu&nbsp;&mdash;&nbsp;MV&nbsp;Therapy',
     'Hieronta Pärnussa&nbsp;&mdash;&nbsp;MV&nbsp;Therapy'),
    ('Therapy centre specialised in <strong>medical massage at Rüütli 47, Pärnu city centre</strong>. We offer trigger point therapy, high-intensity magnetic therapy, shockwave therapy, deep tissue massage, sports massage, classical and relaxation massage &ndash; over 14 different services. All performed by a <strong>Level 6 certified massage therapist</strong>.',
     'Erikoistunut hoitokeskus <strong>lääketieteelliseen hierontaan osoitteessa Rüütli 47, Pärnun kaupunkikeskustassa</strong>. Tarjoamme triggerpiste-terapiaa, voimakasta magneettiterapiaa, iskuaaltoterapiaa, syväkudoshierontaa, urheiluhierontaa, klassista ja rentoutushierontaa – yli 14 eri palvelua. Kaikki suorittaa <strong>tason 6 sertifioitu hieroja</strong>.'),
    ('Level 6 certificate ↗', 'Tason 6 todistus ↗'),
    ('Medical &amp; relaxation', 'Lääketieteellinen &amp; rentoutus'),

    # Trustbar
    ('happy clients', 'tyytyväistä asiakasta'),
    ('serving Pärnu', 'palvelua Pärnussa'),
    ('Google rating', 'Google-arvosana'),
    ('3 languages', '4 kieltä'),
    ('ET, RU, EN', 'ET, RU, EN, FI'),

    # Location callout
    ('📍 Our location in the heart of Pärnu:',
     '📍 Sijaintimme Pärnun sydämessä:'),
    ('Located on Pärnu\'s main pedestrian street at <strong>Rüütli 47, 2nd floor</strong> – in the heart of the historic Old Town. Near the Red Tower (15th century landmark) and Independence Square. Pärnu beach is a 15-minute walk away. <strong>Serving Pärnu residents and visitors since 2020</strong> – over 5,000 happy clients from Pärnu and across Estonia!',
     'Sijaitsemme Pärnun pääkävelykadulla osoitteessa <strong>Rüütli 47, 2. kerros</strong> – historiallisen vanhan kaupungin sydämessä. Lähellä Punaista Tornia (1400-luvun maamerkki) ja Itsenäisyysaukiota. Pärnun ranta on 15 minuutin kävelymatkan päässä. <strong>Palvelemme Pärnun asukkaita ja vierailijoita vuodesta 2020</strong> – yli 5 000 tyytyväistä asiakasta Pärnusta ja kaikkialta Virosta!'),

    # Services section
    ('Our Massage Services in Pärnu', 'Hierontapalvelumme Pärnussa'),
    ('Classical massage', 'Klassinen hieronta'),
    ('Stroking, rubbing and caressing to improve circulation', 'Sively, hangaus ja vaivaaminen verenkierron parantamiseksi'),
    ('Medical massage', 'Lääketieteellinen hieronta'),
    ('Therapeutic approach for treating chronic muscle pain', 'Terapeuttinen lähestymistapa kroonisen lihaskivun hoitoon'),
    ('High-intensity magnetic therapy', 'Voimakas magneettiterapia'),
    ('Revolutionary pain treatment method without medication', 'Vallankumouksellinen kivunhoitomenetelmä ilman lääkkeitä'),
    ('Shockwave therapy', 'Iskuaaltoterapia'),
    ('Sound waves for chronic pain and inflammation relief', 'Ääniaallot kroonisen kivun ja tulehduksen lievitykseen'),
    ('Trigger point therapy', 'Triggerpiste-terapia'),
    ('Releasing painful muscle knots and tension points', 'Kivuliaiden lihaspisteiden ja jännityskohtien vapauttaminen'),
    ('Sports massage', 'Urheiluhieronta'),
    ('For athletes before and after training', 'Urheilijoille ennen ja jälkeen harjoittelun'),
    ('Deep tissue massage', 'Syväkudoshieronta'),
    ('Treatment of chronic pain in deeper muscle layers', 'Kroonisen kivun hoito syvemmissä lihaskerroksissa'),
    ('Cupping massage', 'Kuppihieronta'),
    ('Vacuum improves lymphatic and blood circulation', 'Alipainehoito parantaa lymfa- ja verenkiertoa'),
    ('Gua Sha therapy', 'Gua Sha -terapia'),
    ('Traditional Chinese skin scraping technique for circulation stimulation', 'Perinteinen kiinalainen ihonkaapimistekniikka verenkierron stimuloimiseksi'),
    ('Biocurrent massage', 'Biosähköinen hieronta'),
    ('Microcurrents and bioelectric stimulation to increase skin elasticity', 'Mikrovirrat ja biosähköinen stimulaatio ihon elastisuuden lisäämiseksi'),
    ('Lymphatic massage', 'Lymfahieronta'),
    ('Increasing lymphatic fluid flow and reducing swelling', 'Lymfanesteen virtauksen lisääminen ja turvotuksen vähentäminen'),
    ('Foot sole massage', 'Jalkapohjan refleksologia'),
    ('Improving foot circulation and functionality', 'Jalkojen verenkierron ja toiminnallisuuden parantaminen'),
    ('Ultrasound therapy', 'Ultraääniterapia'),
    ('Microvibration warms tissues and improves metabolism', 'Mikrovibräätio lämmittää kudoksia ja parantaa aineenvaihduntaa'),
    ('Manual muscle testing', 'Manuaalinen lihastestaus'),
    ('Posture and movement pattern analysis for a personalised massage plan', 'Asento- ja liikemallianalyysi yksilöllisen hierontasuunnitelman luomiseksi'),
    ('Kinesio taping', 'Kinesioteippaus'),
    ('Supporting muscle and joint recovery and the treatment process', 'Lihasten ja nivelten toipumisen ja hoitoprosessin tukeminen'),

    # Diagnoses section
    ('Diagnosis-Based Treatment in Pärnu', 'Diagnoosipohjainen hoito Pärnussa'),
    ('Protrusion, herniation and extrusion treatment', 'Pullistuman, tyrän ja ulosvirtauksen hoito'),
    ('Effective treatment of intervertebral disc problems without surgery', 'Tehokas välilevyongelmien hoito ilman leikkausta'),
    ('Plantar fasciitis (heel spur) treatment', 'Plantaarifaskiitti (kantapiikki) -hoito'),
    ('Stop morning heel pain! Shockwave therapy accelerates healing', 'Lopeta aamuinen kantakipu! Iskuaaltoterapia nopeuttaa paranemista'),
    ('Lateral and medial epicondylitis', 'Lateraalinen ja mediaalinen epikondyliitti'),
    ('Rapid treatment for tennis and golfer\'s elbow with combined therapies', 'Nopea hoito tenniskyynärpäähän ja golfkyynärpäähän yhdistelmähoidoilla'),
    ('Piriformis syndrome treatment', 'Piriformis-oireyhtymän hoito'),
    ('Effective treatment for sciatic nerve pain and buttock pain with magnetic therapy', 'Tehokas hoito iskiashermokipuun ja pakarakipuun magneettiterapialla'),
    ('Deep Reset – Depression, anxiety treatment', 'Deep Reset – Masennuksen ja ahdistuksen hoito'),
    ('Deep brain reset without medication. Magnetic therapy balances neurotransmitters', 'Syvä aivojen nollaus ilman lääkkeitä. Magneettiterapia tasapainottaa välittäjäaineita'),
    ('Migraine (chronic headache) treatment', 'Migreeni (krooninen päänsärky) -hoito'),
    ('Manual therapy and magnetic therapy combination breaks the pain cycle', 'Manuaaliterapian ja magneettiterapian yhdistelmä katkaisee kiputyklin'),
    ('Erectile dysfunction (ED) treatment', 'Erektiohäiriöiden (ED) hoito'),
    ('Magnetic intensive therapy strengthens pelvic floor muscles and improves circulation', 'Magneettinen intensiiviterapia vahvistaa lantionpohjan lihaksia ja parantaa verenkiertoa'),
    ('Adhesive capsulitis treatment', 'Adhesiiviisen kapsuliitti -hoito'),
    ('Rapid frozen shoulder treatment. Shockwave and magnetic therapy restores mobility', 'Nopea jäätyneen olkapään hoito. Iskuaalto- ja magneettiterapia palauttaa liikkuvuuden'),

    # Blog section
    ('Blog Articles', 'Blogiartikkelit'),
    ('High-intensity magnetic therapy', 'Voimakas magneettiterapia'),
    ('When the body constantly sends signals – the pain doesn\'t subside...', 'Kun keho lähettää jatkuvasti signaaleja – kipu ei lievity...'),
    ('Chronic heel spur: Shockwave therapy effectiveness', 'Krooninen kantapiikki: iskuaaltoterapian tehokkuus'),
    ('When getting out of bed in the morning sends a shock of pain through your heel...', 'Kun aamuinen vuoteesta nousu lähettää kipupiikin kantapäähäsi...'),
    ('A modern and non-invasive treatment method using high-frequency sound waves...', 'Moderni ja ei-invasiivinen hoitomenetelmä, joka käyttää korkeataajuisia ääniaaltoja...'),
    ('Certified therapist versus quick courses', 'Sertifioitu hieroja vs. pikakurssit'),
    ('Understanding the difference in qualifications when choosing a massage therapist.', 'Pätevyyserojen ymmärtäminen hierojaa valittaessa.'),
    ('Massage for runners: through a specialist\'s eyes', 'Hieronta juoksijoille: asiantuntijan silmin'),
    ('A professional guide on the benefits of massage for runners\' recovery.', 'Ammatillinen opas hieronnan hyödyistä juoksijoiden palautumisessa.'),
    ('Deep tissue massage and nerve receptors', 'Syväkudoshieronta ja hermoreseptorit'),
    ('Discover the scientific background of deep tissue massage and its effects.', 'Tutustu syväkudoshieronnan tieteelliseen taustaan ja sen vaikutuksiin.'),
    ('Lymphatic massage: promoting health and wellbeing', 'Lymfahieronta: terveyden ja hyvinvoinnin edistäminen'),
    ('Benefits of lymphatic massage for detoxification and immune support.', 'Lymfahieronnan hyödyt detoksifikaatiolle ja immuunituelle.'),
    ('Relieving carpal tunnel syndrome', 'Rannekanavaoireyhtymän lievittäminen'),
    ('How massage therapy offers a natural way to relieve symptoms.', 'Miten hierontaterapia tarjoaa luonnollisen tavan lievittää oireita.'),
    ('Importance of massage for combat athletes', 'Hieronnan tärkeys kamppailuurheilijoille'),
    ('Massage plays a key role in recovery and performance improvement.', 'Hieronta on keskeisessä roolissa palautumisessa ja suorituskyvyn parantamisessa.'),
    ('Massage therapist\'s role in preventive medicine', 'Hierontaterapeutin rooli ennaltaehkäisevässä lääketieteessä'),
    ('How regular massage helps prevent health problems.', 'Miten säännöllinen hieronta auttaa ehkäisemään terveysongelmia.'),
    ('Massage in modern medicine', 'Hieronta modernissa lääketieteessä'),
    ('Why massage is increasingly recognised as an important part of healthcare.', 'Miksi hieronta tunnustetaan yhä enemmän tärkeäksi osaksi terveydenhuoltoa.'),
    ('Physiotherapy and therapeutic massage synergy', 'Fysioterapia ja terapeuttinen hieronta synergiassa'),
    ('Combining with massage leads to more complete and effective recovery.', 'Yhdistäminen hierontaan johtaa täydellisempään ja tehokkaampaan palautumiseen.'),
    ('Functional anatomy and kinesiology', 'Toiminnallinen anatomia ja kinesiologia'),
    ('Understanding body structure and movement for effective therapy.', 'Kehon rakenteen ja liikkeen ymmärtäminen tehokkaaseen terapiaan.'),

    # FAQ section
    ('Frequently Asked Questions', 'Usein kysytyt kysymykset'),
    ('What problems is medical massage intended for?',
     'Mihin ongelmiin lääketieteellinen hieronta on tarkoitettu?'),
    ('Medical massage helps with chronic muscle pain, nerve impingement, migraines and joint mobility restrictions. It focuses on treating a specific problem rather than just relaxation.',
     'Lääketieteellinen hieronta auttaa krooniseen lihaskipuun, hermon pinnistymiseen, migreeniin ja nivelten liikkuvuusrajoituksiin. Se keskittyy tietyn ongelman hoitamiseen eikä pelkkään rentoutumiseen.'),
    ('How does medical massage differ from regular massage?',
     'Miten lääketieteellinen hieronta eroaa tavallisesta hieronnasta?'),
    ('Medical massage is targeted therapy using deep tissue techniques and anatomical knowledge to address specific health issues. Regular massage focuses on general relaxation.',
     'Lääketieteellinen hieronta on kohdennettua terapiaa, jossa käytetään syväkudostekniikoita ja anatomista tietämystä tiettyjen terveysongelmien käsittelyyn. Tavallinen hieronta keskittyy yleiseen rentoutumiseen.'),
    ('How often should I get medical massage?',
     'Kuinka usein minun pitäisi käydä lääketieteellisessä hieronnassa?'),
    ('During active treatment, we recommend sessions at 4–7 day intervals. After achieving results, monthly maintenance sessions are sufficient. Your therapist will create a personalised plan.',
     'Aktiivisen hoidon aikana suosittelemme istuntoja 4–7 päivän välein. Tulosten saavuttamisen jälkeen kuukausittaiset ylläpitoistunnot riittävät. Terapeuttisi luo yksilöllisen suunnitelman.'),
    ('Can medical massage be painful?',
     'Voiko lääketieteellinen hieronta olla kivulias?'),
    ('Medical massage is more intensive than regular massage but should never cause excessive pain. The therapist adjusts pressure based on your feedback – open communication during the session is essential.',
     'Lääketieteellinen hieronta on voimakkaampaa kuin tavallinen hieronta, mutta ei koskaan pidä aiheuttaa liiallista kipua. Terapeutti säätää painetta palautteesi perusteella – avoin viestintä istunnon aikana on välttämätöntä.'),

    # SEO section
    ('Professional Massage in Pärnu', 'Ammatillinen hieronta Pärnussa'),
    ('Professional Massage Therapist in Pärnu', 'Ammatillinen hieroja Pärnussa'),
    ('MV Therapy is a professional massage centre', 'MV Therapy on ammatillinen hierontakeskus'),
    ('Located at Rüütli 47', 'Sijaitsee osoitteessa Rüütli 47'),
    ('certified massage therapist', 'sertifioitu hieroja'),
    ('Level 6 certified', 'tason 6 sertifioitu'),
    ('over 5,000 clients', 'yli 5 000 asiakasta'),
]

SERVICES_REPLACEMENTS = [
    ('Massage Services in Parnu', 'Hierontapalvelut Pärnussa'),
    ('Massage Services in Pärnu', 'Hierontapalvelut Pärnussa'),
    ('15 Different Massage Types', '15 erilaista hierontatyyppiä'),
    ('Classical Massage in Parnu', 'Klassinen hieronta Pärnussa'),
    ('Medical Massage in Parnu', 'Lääketieteellinen hieronta Pärnussa'),
    ('High-Intensity Magnetic Therapy in Parnu', 'Voimakas magneettiterapia Pärnussa'),
    ('Shockwave Therapy in Parnu', 'Iskuaaltoterapia Pärnussa'),
    ('Trigger Point Therapy in Parnu', 'Triggerpiste-terapia Pärnussa'),
    ('Sports Massage in Parnu', 'Urheiluhieronta Pärnussa'),
    ('Deep Tissue Massage in Parnu', 'Syväkudoshieronta Pärnussa'),
    ('Cupping Massage in Parnu', 'Kuppihieronta Pärnussa'),
    ('Gua Sha Therapy in Parnu', 'Gua Sha -terapia Pärnussa'),
    ('Bio-Electric Massage in Parnu', 'Biosähköinen hieronta Pärnussa'),
    ('Lymphatic Massage in Parnu', 'Lymfahieronta Pärnussa'),
    ('Foot Reflexology in Parnu', 'Jalkapohjan refleksologia Pärnussa'),
    ('Ultrasound Therapy in Parnu', 'Ultraääniterapia Pärnussa'),
    ('Manual Muscle Testing in Parnu', 'Manuaalinen lihastestaus Pärnussa'),
    ('Kinesio Taping in Parnu', 'Kinesioteippaus Pärnussa'),
    ('Stroking, rubbing and kneading to improve blood circulation', 'Sively, hangaus ja vaivaaminen verenkierron parantamiseksi'),
    ('Therapeutic approach for treating chronic muscle pain', 'Terapeuttinen lähestymistapa kroonisen lihaskivun hoitoon'),
    ('This is a revolutionary pain treatment method without medications', 'Tämä on vallankumouksellinen kivunhoitomenetelmä ilman lääkkeitä'),
    ('Sound waves for relieving chronic pain and inflammation', 'Ääniaallot kroonisen kivun ja tulehduksen lievitykseen'),
    ('Release of painful muscle knots and tension points', 'Kivuliaiden lihaspisteiden ja jännityskohtien vapauttaminen'),
    ('For athletes before and after training', 'Urheilijoille ennen ja jälkeen harjoittelun'),
    ('Treatment of chronic pain in deeper muscle layers', 'Kroonisen kivun hoito syvemmissä lihaskerroksissa'),
    ('Vacuum therapy improves lymphatic and blood circulation', 'Alipaineterapia parantaa lymfa- ja verenkiertoa'),
    ('Traditional Chinese skin scraping technique to stimulate blood circulation', 'Perinteinen kiinalainen ihonkaapimistekniikka verenkierron stimuloimiseksi'),
    ('Micro-currents and bio-electric stimulation to increase skin elasticity', 'Mikrovirrat ja biosähköinen stimulaatio ihon elastisuuden lisäämiseksi'),
    ('Increase lymphatic fluid flow and reduce swelling', 'Lymfanesteen virtauksen lisääminen ja turvotuksen vähentäminen'),
    ('Improve foot circulation and functionality', 'Jalkojen verenkierron ja toiminnallisuuden parantaminen'),
    ('Micro-vibration warms tissues and improves metabolism', 'Mikrovibräätio lämmittää kudoksia ja parantaa aineenvaihduntaa'),
    ('Posture and movement pattern analysis for personalized massage plan', 'Asento- ja liikemallianalyysi yksilöllisen hierontasuunnitelman luomiseksi'),
    ('Support muscle and joint recovery and healing process', 'Lihasten ja nivelten toipumisen ja paranemisprosessin tukeminen'),
    ('Professional Massage Therapist in Parnu - MV Therapy', 'Ammatillinen hieroja Pärnussa - MV Therapy'),
    ('MV Therapy is a professional massage center located in Parnu city center', 'MV Therapy on ammatillinen hierontakeskus Pärnun kaupunkikeskustassa'),
    ('Our experienced massage therapist specializes in', 'Kokenut hierojamme on erikoistunut'),
    ('medical massage in Parnu', 'lääketieteelliseen hierontaan Pärnussa'),
    ('quality massage in Parnu', 'laadukasta hierontaa Pärnussa'),
    ('If you are looking for', 'Jos etsit'),
    ('then MV Therapy is the right choice', 'MV Therapy on oikea valinta'),
    ('We offer both classical relaxing massage and specialized treatment services', 'Tarjoamme sekä klassista rentoutushierontaa että erikoistuneita hoitopalveluja'),
    ('Our massage center is located in Parnu city center and is easily accessible', 'Hierontakeskuksemme sijaitsee Pärnun kaupunkikeskustassa ja on helposti saavutettavissa'),
    ('Massage services in Parnu:', 'Hierontapalvelut Pärnussa:'),
]

DIAGNOSIS_REPLACEMENTS = [
    ('Diagnoses - Conditions We Treat in Pärnu', 'Diagnoosit - hoidamme Pärnussa'),
    ('Diagnoses - Health Conditions Treated', 'Diagnoosit - hoidettavat terveystilat'),
    ('Protrusion, herniation and extrusion treatment', 'Pullistuman, tyrän ja ulosvirtauksen hoito'),
    ('Plantar fasciitis (heel spur)', 'Plantaarifaskiitti (kantapiikki)'),
    ('Plantar fasciitis (heel spur) treatment', 'Plantaarifaskiitti (kantapiikki) -hoito'),
    ('Lateral and medial epicondylitis', 'Lateraalinen ja mediaalinen epikondyliitti'),
    ('Piriformis syndrome', 'Piriformis-oireyhtymä'),
    ('Piriformis syndrome treatment', 'Piriformis-oireyhtymän hoito'),
    ('Deep Reset - Depression, anxiety', 'Deep Reset - Masennus, ahdistus'),
    ('Deep Reset – Depression, anxiety treatment', 'Deep Reset – Masennuksen ja ahdistuksen hoito'),
    ('Migraine (chronic headache)', 'Migreeni (krooninen päänsärky)'),
    ('Migraine (chronic headache) treatment', 'Migreeni (krooninen päänsärky) -hoito'),
    ('Erectile dysfunction (ED)', 'Erektiohäiriö (ED)'),
    ('Erectile dysfunction (ED) treatment', 'Erektiohäiriön (ED) hoito'),
    ('Adhesive capsulitis', 'Adhesiiviinen kapsuliitti (jäätynyt olkapää)'),
    ('Adhesive capsulitis treatment', 'Adhesiiviisen kapsuliitti -hoito'),
    ('Effective treatment of intervertebral disc problems', 'Tehokas välilevyongelmien hoito'),
    ('without surgery', 'ilman leikkausta'),
    ('Stop morning heel pain', 'Lopeta aamuinen kantakipu'),
    ('Rapid treatment for tennis and golfer\'s elbow', 'Nopea hoito tenniskyynärpäähän ja golfkyynärpäähän'),
    ('with combined therapies', 'yhdistelmähoidoilla'),
    ('sciatic nerve pain and buttock pain', 'iskiashermokipu ja pakarakipu'),
    ('with magnetic therapy', 'magneettiterapialla'),
    ('Deep brain reset without medication', 'Syvä aivojen nollaus ilman lääkkeitä'),
    ('Magnetic therapy balances neurotransmitters', 'Magneettiterapia tasapainottaa välittäjäaineita'),
    ('breaks the pain cycle', 'katkaisee kiputyklin'),
    ('strengthens pelvic floor muscles and improves circulation', 'vahvistaa lantionpohjan lihaksia ja parantaa verenkiertoa'),
    ('Rapid frozen shoulder treatment', 'Nopea jäätyneen olkapään hoito'),
    ('restores mobility', 'palauttaa liikkuvuuden'),
    ('Diagnoses in Pärnu', 'Diagnoosit Pärnussa'),
    ('Our Approach to Treatment', 'Hoitolähestymistapamme'),
    ('Treatment Phases', 'Hoitovaiheet'),
]

TEAM_REPLACEMENTS = [
    ('MV Therapy Team', 'MV Therapy tiimi'),
    ('Licensed Massage Therapist', 'Lisensioitu hieroja'),
    ('Massage Therapist', 'Hieroja'),
    ('6+ years of experience', 'Yli 6 vuoden kokemus'),
    ('years of experience', 'vuoden kokemus'),
    ('Qualifications', 'Pätevyydet'),
    ('Level 6 professional certificate', 'Tason 6 ammatillinen todistus'),
    ('Nursing qualification', 'Hoitoalan pätevyys'),
    ('Specializations:', 'Erikoisalat:'),
    ('Specializations', 'Erikoisalat'),
    ('shockwave therapy', 'iskuaaltoterapia'),
    ('magnetic therapy', 'magneettiterapia'),
    ('trigger point therapy', 'triggerpiste-terapia'),
    ('Medical massage', 'Lääketieteellinen hieronta'),
    ('Sports massage', 'Urheiluhieronta'),
    ('Deep tissue massage', 'Syväkudoshieronta'),
    ('Experience', 'Kokemus'),
    ('Certifications', 'Sertifikaatit'),
    ('Education', 'Koulutus'),
    ('About Roman', 'Tietoa Romanista'),
    ('Roman Gussev', 'Roman Gussev'),
    ('Professional massage therapist with', 'Ammatillinen hieroja, jolla on'),
    ('Over 5,000 clients helped', 'Yli 5 000 autettua asiakasta'),
    ('since 2020', 'vuodesta 2020'),
]

BLOG_REPLACEMENTS = [
    ('Our Massage Blog Articles', 'Hierontablogimme artikkelit'),
    ('High-intensity magnetic therapy', 'Voimakas magneettiterapia'),
    ('When the body constantly sends signals – pain doesn\'t subside, then we need to look for revolutionary methods that can break this vicious cycle.',
     'Kun keho lähettää jatkuvasti signaaleja – kipu ei lievity, meidän on etsittävä vallankumouksellisia menetelmiä, jotka voivat katkaista tämän noidankehän.'),
    ('Chronic heel spur: Effectiveness of shockwave therapy in treating chronic plantar fasciitis',
     'Krooninen kantapiikki: Iskuaaltoterapian tehokkuus kroonisen plantaarifaskiitin hoidossa'),
    ('When getting out of bed in the morning, a sharp pain shoots through your heel, making you stand on tiptoes for a moment.',
     'Kun nouset aamulla sängystä, terävä kipu ampuu kantapäähäsi, saaden sinut seisomaan varpaillasi hetken.'),
    ('Shockwave therapy', 'Iskuaaltoterapia'),
    ('Shockwave therapy is a modern and non-invasive treatment method that uses high-frequency sound waves to stimulate healing and reduce pain.',
     'Iskuaaltoterapia on moderni ja ei-invasiivinen hoitomenetelmä, joka käyttää korkeataajuisia ääniaaltoja paranemisen stimuloimiseen ja kivun vähentämiseen.'),
    ('Certified massage therapist versus quick courses',
     'Sertifioitu hieroja vs. pikakurssit'),
    ('Understanding the difference in qualifications when choosing a massage therapist.',
     'Pätevyyserojen ymmärtäminen hierojaa valittaessa.'),
    ('Massage for runners: through a specialist\'s eyes',
     'Hieronta juoksijoille: asiantuntijan silmin'),
    ('Professional guide on the benefits of massage for runners\' performance and recovery.',
     'Ammatillinen opas hieronnan hyödyistä juoksijoiden suorituskykyyn ja palautumiseen.'),
    ('Deep tissue massage and nerve receptors: How it helps relieve muscle tension',
     'Syväkudoshieronta ja hermoreseptorit: Miten se auttaa lievittämään lihasjännitystä'),
    ('Learn about the scientific background of deep tissue massage and its effect on muscle tension.',
     'Tutustu syväkudoshieronnan tieteelliseen taustaan ja sen vaikutukseen lihasjännitykseen.'),
    ('Lymphatic massage: promoting health and wellbeing',
     'Lymfahieronta: terveyden ja hyvinvoinnin edistäminen'),
    ('Understand the benefits of lymphatic massage for detoxification and immune system support.',
     'Ymmärrä lymfahieronnan hyödyt detoksifikaatiolle ja immuunijärjestelmän tukemiselle.'),
    ('Relieving carpal tunnel syndrome with massage therapy: a natural and effective alternative',
     'Rannekanavaoireyhtymän lievittäminen hierontaterapialla: luonnollinen ja tehokas vaihtoehto'),
    ('Explore how massage therapy offers a natural way to relieve carpal tunnel syndrome symptoms.',
     'Tutustu siihen, miten hierontaterapia tarjoaa luonnollisen tavan lievittää rannekanavaoireyhtymän oireita.'),
    ('The importance of massage for martial artists',
     'Hieronnan tärkeys kampaurheilijoille'),
    ('Massage plays a key role in martial artists\' recovery and performance improvement.',
     'Hieronta on keskeisessä roolissa kampaurheilijoiden palautumisessa ja suorituskyvyn parantamisessa.'),
    ('The role of massage therapists in preventive medicine practice',
     'Hierontaterapeutit ennaltaehkäisevässä lääketieteessä'),
    ('Learn how regular massage helps prevent health problems and maintain wellbeing.',
     'Tutustu siihen, miten säännöllinen hieronta auttaa ehkäisemään terveysongelmia ja ylläpitämään hyvinvointia.'),
    ('Massage in modern medicine', 'Hieronta modernissa lääketieteessä'),
    ('Physiotherapy and therapeutic massage synergy', 'Fysioterapia ja terapeuttinen hieronta synergiassa'),
    ('Functional anatomy and kinesiology', 'Toiminnallinen anatomia ja kinesiologia'),
]

KKK_REPLACEMENTS = [
    ('FAQ', 'UKK'),
    ('Frequently Asked Questions', 'Usein kysytyt kysymykset'),
    ('Question: Can you feel pain during a therapeutic massage?',
     'Kysymys: Voiko terapeuttisen hieronnan aikana tuntea kipua?'),
    ('Answer: Pain can occur since we often work with tense or painful muscles. However, it\'s important to be honest with the masseur because the more honest you are, the better he can do his job and adjust the procedure accordingly.',
     'Vastaus: Kipua voi esiintyä, koska työskentelemme usein jännittyneiden tai kivuliaiden lihasten kanssa. On kuitenkin tärkeää olla rehellinen hierojalle, koska mitä rehellisempi olet, sitä paremmin hän voi tehdä työnsä ja säätää toimenpidettä sen mukaisesti.'),
    ('Question: If I come for a massage for the first time, should I immediately lie down on the massage table?',
     'Kysymys: Jos tulen hierontaan ensimmäistä kertaa, pitääkö minun heti käydä hierontapöydälle?'),
    ('Answer: No, before the massage, we take time for a conversation and to check the muscles, even with a classic massage, to exclude medical contraindications.',
     'Vastaus: Ei, ennen hierontaa otamme aikaa keskusteluun ja lihasten tarkistamiseen, myös klassisessa hieronnassa, lääketieteellisten vasta-aiheiden sulkemiseksi pois.'),
    ('Question: How many sessions are required to alleviate my problems? 5, 10, or 15 times?',
     'Kysymys: Kuinka monta istuntoa tarvitaan ongelmieni lievittämiseen? 5, 10 vai 15 kertaa?'),
    ('Answer: The number of sessions depends on individual needs.',
     'Vastaus: Istuntojen määrä riippuu yksilöllisistä tarpeista.'),
    ('Question: Should I eat or drink something special before the massage?',
     'Kysymys: Pitäisikö minun syödä tai juoda jotain erityistä ennen hierontaa?'),
    ('Answer: We recommend avoiding heavy food immediately before the massage. It\'s also good to consume enough water to help the muscles relax.',
     'Vastaus: Suosittelemme välttämään raskasta ruokaa juuri ennen hierontaa. On myös hyvä juoda riittävästi vettä lihasten rentoutumisen helpottamiseksi.'),
    ('Question: How often should I attend massage to maintain well-being?',
     'Kysymys: Kuinka usein minun pitäisi käydä hieronnassa hyvinvoinnin ylläpitämiseksi?'),
    ('Answer: During the treatment process, it\'s important to return every 4-7 days.',
     'Vastaus: Hoitoprosessin aikana on tärkeää palata 4–7 päivän välein.'),
    ('Question: Does massage help with headaches or migraines?',
     'Kysymys: Auttaako hieronta päänsärkyyn tai migreeniin?'),
    ('Answer: Yes, massage can successfully reduce the symptoms of a headache or migraine by improving circulation and relaxing tense muscles.',
     'Vastaus: Kyllä, hieronta voi onnistuneesti vähentää päänsäryn tai migreenikohtauksen oireita parantamalla verenkiertoa ja rentouttamalla jännittyneitä lihaksia.'),
    ('Question: What\'s the difference between a relaxing and therapeutic massage?',
     'Kysymys: Mikä on ero rentoutus- ja terapeuttisen hieronnan välillä?'),
    ('Answer: Relaxing massage primarily aims to relieve tension and general well-being, avoiding the feeling of pain, using softer methods. Therapeutic massage is aimed at addressing specific problems or pain points, often using deeper and more targeted methods.',
     'Vastaus: Rentoutushieronta tähtää ensisijaisesti jännityksen lievittämiseen ja yleiseen hyvinvointiin, välttäen kivun tunnetta, käyttäen pehmeämpiä menetelmiä. Terapeuttinen hieronta tähtää tiettyjen ongelmien tai kipukohtien käsittelyyn, usein käyttäen syvempiä ja kohdennetumpia menetelmiä.'),
    ('Question: What should I do after the massage session?',
     'Kysymys: Mitä minun pitäisi tehdä hierontaistunnon jälkeen?'),
    ('Answer: After the massage, it\'s important to drink plenty of water to help the body remove toxins.',
     'Vastaus: Hieronnan jälkeen on tärkeää juoda runsaasti vettä kehon myrkkyjen poistamiseksi.'),
    ('Question: How quickly can I expect to see the positive effects of massage?',
     'Kysymys: Kuinka nopeasti voin odottaa näkeväni hieronnan positiiviset vaikutukset?'),
    ('Answer: In most cases, clients feel the positive effects of massage immediately after the session.',
     'Vastaus: Useimmissa tapauksissa asiakkaat tuntevat hieronnan positiiviset vaikutukset heti istunnon jälkeen.'),
]

CAMPAIGN_REPLACEMENTS = [
    ('Campaigns', 'Kampanjat'),
    ('Special Offers', 'Erikoistarjoukset'),
    ('Valid until', 'Voimassa'),
    ('WOMEN\'S DAY SPECIAL OFFER', 'NAISTENPÄIVÄN ERIKOISTARJOUS'),
    ('A gift that brings real relief.', 'Lahja, joka tuo todellista helpotusta.'),
    ('Health. Recovery. Relaxation.', 'Terveys. Palautuminen. Rentoutus.'),
    ('60 Minute Massage', '60 minuutin hieronta'),
    ('90 Minute Massage', '90 minuutin hieronta'),
    ('5×60 Minute Package', '5×60 minuutin paketti'),
    ('Before €', 'Ennen €'),
    ('Save €', 'Säästä €'),
    ('BEST OFFER', 'PARAS TARJOUS'),
    ('Gift Card', 'Lahjakortti'),
    ('Gift card', 'Lahjakortti'),
    ('gift card', 'lahjakortti'),
    ('Special offer', 'Erikoistarjous'),
    ('special offer', 'erikoistarjous'),
    ('Package', 'Paketti'),
    ('package', 'paketti'),
    ('Offer', 'Tarjous'),
    ('minute', 'minuutin'),
    ('minutes', 'minuuttia'),
    ('Original price', 'Alkuperäinen hinta'),
    ('Discounted', 'Alennettu'),
]

MAP_REPLACEMENTS = [
    ('Location - MV Therapy Massage in Pärnu', 'Sijainti - MV Therapy Hieronta Pärnussa'),
    ('Find Us', 'Löydä meidät'),
    ('Our Location', 'Sijaintimme'),
    ('How to find us', 'Miten löytää meidät'),
    ('Directions', 'Ajo-ohjeet'),
    ('Open in Google Maps', 'Avaa Google Mapsissa'),
    ('Located at', 'Sijaitsee osoitteessa'),
    ('Rüütli street', 'Rüütli-katu'),
    ('Old Town', 'Vanha kaupunki'),
    ('Pärnu, Estonia', 'Pärnu, Viro'),
    ('By car', 'Autolla'),
    ('By foot', 'Jalan'),
    ('Parking', 'Pysäköinti'),
    ('Bus stop', 'Bussipysäkki'),
    ('Near', 'Lähellä'),
    ('15-minute walk to', '15 minuutin kävelymatka'),
]

# ── Service sub-page translations ─────────────────────────────────────────────
SERVICE_SUBPAGE_REPLACEMENTS = [
    # Breadcrumbs
    ('Home &gt;', 'Etusivu &gt;'),
    ('Massages &gt;', 'Hieronnat &gt;'),
    ('Home >', 'Etusivu >'),
    ('Massages >', 'Hieronnat >'),

    # Service names
    ('Classical Massage', 'Klassinen hieronta'),
    ('Medical Massage', 'Lääketieteellinen hieronta'),
    ('High-Intensity Magnetic Therapy', 'Voimakas magneettiterapia'),
    ('Shockwave Therapy', 'Iskuaaltoterapia'),
    ('Trigger Point Therapy', 'Triggerpiste-terapia'),
    ('Sports Massage', 'Urheiluhieronta'),
    ('Deep Tissue Massage', 'Syväkudoshieronta'),
    ('Cupping Massage', 'Kuppihieronta'),
    ('Gua Sha Therapy', 'Gua Sha -terapia'),
    ('Bio-Electric Massage', 'Biosähköinen hieronta'),
    ('Lymphatic Massage', 'Lymfahieronta'),
    ('Foot Reflexology', 'Jalkapohjan refleksologia'),
    ('Ultrasound Therapy', 'Ultraääniterapia'),
    ('Manual Muscle Testing', 'Manuaalinen lihastestaus'),
    ('Kinesio Taping', 'Kinesioteippaus'),

    # Price table
    ('aria-label="Medical massage prices"', 'aria-label="Lääketieteellinen hierontahinnat"'),
    ('aria-label="Classical massage prices"', 'aria-label="Klassinen hierontahinnat"'),

    # Common section headings
    ('Which Conditions is', 'Mihin tiloihin'),
    ('Which Conditions is Medical Massage Suitable For?', 'Mihin tiloihin lääketieteellinen hieronta sopii?'),
    ('Suitable For?', 'sopii?'),
    ('Our Approach to Medical Massage', 'Lähestymistapamme lääketieteelliseen hierontaan'),
    ('Our Approach to', 'Lähestymistapamme'),
    ('Benefits of Medical Massage', 'Lääketieteellisen hieronnan hyödyt'),
    ('Benefits of', 'Hyödyt:'),
    ('Benefits', 'Hyödyt'),
    ('Frequently Asked Questions', 'Usein kysytyt kysymykset'),
    ('Let\'s Start Your Health Recovery', 'Aloitetaan terveytesi palautuminen'),
    ('Medical massage is the first step towards a more pain-free and active life.',
     'Lääketieteellinen hieronta on ensimmäinen askel kohti kivuttomampaa ja aktiivisempaa elämää.'),

    # Conditions
    ('Chronic Muscle Pain', 'Krooninen lihaskipu'),
    ('Persistent muscle tension and pain that interferes with daily life.',
     'Jatkuva lihasjännitys ja kipu, joka häiritsee jokapäiväistä elämää.'),
    ('Nerve Compression', 'Hermopuristus'),
    ('Migraines and Headaches', 'Migreeni ja päänsärky'),
    ('Mobility Limitations', 'Liikkuvuusrajoitukset'),
    ('Muscle Dysfunction', 'Lihasdysktoimia'),
    ('Fasciitis and Post-Trauma Recovery', 'Faskiitti ja post-trauma-toipuminen'),

    # Benefits list
    ('Individual approach for each client', 'Yksilöllinen lähestymistapa jokaiselle asiakkaalle'),
    ('Application of anatomical knowledge', 'Anatomisen tietämyksen soveltaminen'),
    ('Use of nervous system action mechanisms', 'Hermostojärjestelmän toimintamekanismien käyttö'),
    ('Restoration of body\'s normal functionality', 'Kehon normaalin toiminnallisuuden palauttaminen'),
    ('Long-term health improvement', 'Pitkäaikainen terveyden parantaminen'),
    ('Evidence-based massage techniques', 'Näyttöön perustuvat hierontatekniikat'),

    # FAQ answers for service pages
    ('How does medical massage differ from regular massage?',
     'Miten lääketieteellinen hieronta eroaa tavallisesta hieronnasta?'),
    ('Is medical massage suitable for me?', 'Sopiiko lääketieteellinen hieronta minulle?'),
    ('How often should I have medical massage?', 'Kuinka usein minun pitäisi käydä lääketieteellisessä hieronnassa?'),
    ('Can medical massage be painful?', 'Voiko lääketieteellinen hieronta olla kivulias?'),
    ('What should I bring to the massage?', 'Mitä minun pitäisi tuoda hierontaan?'),
    ('What results can I expect?', 'Mitä tuloksia voin odottaa?'),

    # Benefits
    ('<strong>Pain Relief:</strong>', '<strong>Kivunlievitys:</strong>'),
    ('<strong>Improved Mobility:</strong>', '<strong>Parantunut liikkuvuus:</strong>'),
    ('<strong>Reduced Inflammation:</strong>', '<strong>Vähentynyt tulehdus:</strong>'),
    ('<strong>Better Stress Management:</strong>', '<strong>Parempi stressinhallinta:</strong>'),
    ('<strong>Accelerated Post-Trauma Recovery:</strong>', '<strong>Nopeutunut vamman jälkeinen toipuminen:</strong>'),
    ('<strong>Enhanced Quality of Life:</strong>', '<strong>Parantunut elämänlaatu:</strong>'),
    ('Reduces chronic and acute pain', 'Vähentää kroonista ja akuuttia kipua'),
    ('Restores normal joint and muscle function', 'Palauttaa nivelten ja lihasten normaalin toiminnan'),
    ('Stimulates lymphatic system and reduces tissue swelling', 'Stimuloi lymfajärjestelmää ja vähentää kudosturvotusta'),
    ('Reduces nervous system overactivity', 'Vähentää hermostojärjestelmän yliaktiivisuutta'),
    ('Promotes tissue healing', 'Edistää kudosten paranemista'),
    ('Enables return to normal activity', 'Mahdollistaa palaamisen normaaliin toimintaan'),

    # CTA section
    ('Book Your Appointment', 'Varaa aikasi'),
    ('Book an Appointment', 'Varaa aika'),
    ('Ready to Start?', 'Valmis aloittamaan?'),
    ('Contact us to book', 'Ota yhteyttä ja varaa'),
    ('Our experienced therapist', 'Kokenut terapeuttimme'),
    ('will help you find the best solution', 'auttaa sinua löytämään parhaan ratkaisun'),
]

# ── Diagnosis sub-page translations ───────────────────────────────────────────
DIAGNOSIS_SUBPAGE_REPLACEMENTS = [
    ('Home &gt;', 'Etusivu &gt;'),
    ('Diagnoses &gt;', 'Diagnoosit &gt;'),
    ('Home >', 'Etusivu >'),
    ('Diagnoses >', 'Diagnoosit >'),
    ('Treatment Method', 'Hoitomenetelmä'),
    ('Treatment Phases', 'Hoitovaiheet'),
    ('Phase', 'Vaihe'),
    ('Symptoms', 'Oireet'),
    ('Causes', 'Syyt'),
    ('Who is Affected?', 'Ketä se koskee?'),
    ('How We Treat', 'Miten hoidamme'),
    ('Expected Results', 'Odotetut tulokset'),
    ('Treatment Duration', 'Hoitokesto'),
    ('Number of Sessions', 'Istuntojen määrä'),
    ('Session Duration', 'Istunnon kesto'),
    ('Warning Signs', 'Varoitusmerkit'),
    ('Contraindications', 'Vasta-aiheet'),
    ('When to Consult a Doctor', 'Milloin konsultoida lääkäriä'),
    ('Book Appointment', 'Varaa aika'),
    ('minutes', 'minuuttia'),
    ('sessions', 'istuntoa'),
    ('weeks', 'viikkoa'),
    ('months', 'kuukautta'),
    ('Shockwave therapy', 'Iskuaaltoterapia'),
    ('Magnetic therapy', 'Magneettiterapia'),
    ('Manual therapy', 'Manuaaliterapia'),
    ('Trigger point therapy', 'Triggerpiste-terapia'),
    ('Deep tissue massage', 'Syväkudoshieronta'),
    ('inflammatory process', 'tulehdusprosessi'),
    ('pain relief', 'kivunlievitys'),
    ('tissue healing', 'kudosten paraneminen'),
    ('blood circulation', 'verenkierto'),
    ('muscle tension', 'lihasjännitys'),
    ('nerve compression', 'hermopuristus'),
    ('chronic pain', 'krooninen kipu'),
    ('acute pain', 'akuutti kipu'),
    ('without surgery', 'ilman leikkausta'),
    ('without medication', 'ilman lääkkeitä'),
    ('non-invasive', 'ei-invasiivinen'),
    ('effective treatment', 'tehokas hoito'),
]

# ── Blog sub-page translations ────────────────────────────────────────────────
BLOG_SUBPAGE_REPLACEMENTS = [
    ('Home &gt;', 'Etusivu &gt;'),
    ('Blog &gt;', 'Blogi &gt;'),
    ('Home >', 'Etusivu >'),
    ('Blog >', 'Blogi >'),
    ('Published', 'Julkaistu'),
    ('Author', 'Tekijä'),
    ('Reading time', 'Lukuaika'),
    ('minutes read', 'min lukuaika'),
    ('Share article', 'Jaa artikkeli'),
    ('Related articles', 'Aiheeseen liittyvät artikkelit'),
    ('Back to blog', 'Takaisin blogiin'),
    ('Tags', 'Tagit'),
    ('Category', 'Kategoria'),
    ('massage', 'hieronta'),
    ('therapy', 'terapia'),
    ('health', 'terveys'),
    ('pain', 'kipu'),
    ('muscles', 'lihakset'),
    ('treatment', 'hoito'),
    ('benefits', 'hyödyt'),
    ('recovery', 'palautuminen'),
    ('conclusion', 'yhteenveto'),
    ('Conclusion', 'Yhteenveto'),
    ('Summary', 'Yhteenveto'),
    ('Introduction', 'Johdanto'),
    ('Results', 'Tulokset'),
    ('Research', 'Tutkimus'),
    ('Scientific background', 'Tieteellinen tausta'),
    ('In conclusion', 'Yhteenvetona'),
    ('To summarize', 'Yhteenvetona'),
    ('Furthermore', 'Lisäksi'),
    ('However', 'Kuitenkin'),
    ('Therefore', 'Siksi'),
    ('In addition', 'Lisäksi'),
]

# ── Campaign sub-page translations ────────────────────────────────────────────
CAMPAIGN_SUBPAGE_REPLACEMENTS = [
    ('Home &gt;', 'Etusivu &gt;'),
    ('Campaigns &gt;', 'Kampanjat &gt;'),
    ('Home >', 'Etusivu >'),
    ('Campaigns >', 'Kampanjat >'),
    ('Special Offer', 'Erikoistarjous'),
    ('Gift Card', 'Lahjakortti'),
    ('Valid', 'Voimassa'),
    ('until', 'saakka'),
    ('Package', 'Paketti'),
    ('Minute Massage', 'Minuutin hieronta'),
    ('Minute', 'Minuutti'),
    ('Minutes', 'Minuuttia'),
    ('Best offer', 'Paras tarjous'),
    ('Best Offer', 'Paras tarjous'),
    ('Save', 'Säästä'),
    ('Before', 'Ennen'),
    ('Original price', 'Alkuperäinen hinta'),
    ('Discount', 'Alennus'),
    ('discount', 'alennus'),
    ('Book now', 'Varaa nyt'),
    ('Order now', 'Tilaa nyt'),
    ('Buy now', 'Osta nyt'),
    ('Health. Recovery. Relaxation.', 'Terveys. Palautuminen. Rentoutus.'),
    ('A gift that brings real relief.', 'Lahja, joka tuo todellista helpotusta.'),
    ('WOMEN\'S DAY SPECIAL OFFER', 'NAISTENPÄIVÄN ERIKOISTARJOUS'),
    ('WOMEN\'S DAY', 'NAISTENPÄIVÄ'),
    ('Spring offer', 'Kevättarjous'),
    ('Summer offer', 'Kesätarjous'),
    ('Autumn offer', 'Syystarjous'),
    ('Winter offer', 'Talvitarjous'),
    ('Christmas offer', 'Joulutarjous'),
    ('New Year offer', 'Uudenvuoden tarjous'),
    ('Birthday', 'Syntymäpäivä'),
    ('Corporate', 'Yritys'),
    ('wellness', 'hyvinvointi'),
    ('Wellness', 'Hyvinvointi'),
    ('relaxation', 'rentoutus'),
    ('Relaxation', 'Rentoutus'),
    ('health', 'terveys'),
    ('Health', 'Terveys'),
    ('recovery', 'palautuminen'),
    ('Recovery', 'Palautuminen'),
]


def get_page_replacements(rel_path):
    """Return page-specific replacements based on file path."""
    replacements = []
    rel_lower = rel_path.lower()

    if rel_path in ('home.html', 'index.html'):
        replacements += HOME_REPLACEMENTS
    if 'services.html' in rel_path and '/' not in rel_path:
        replacements += SERVICES_REPLACEMENTS
    if 'diagnosis.html' in rel_lower and '/' not in rel_path:
        replacements += DIAGNOSIS_REPLACEMENTS
    if 'team.html' in rel_path:
        replacements += TEAM_REPLACEMENTS
    if 'blog.html' in rel_path and '/' not in rel_path:
        replacements += BLOG_REPLACEMENTS
    if 'kkk.html' in rel_path:
        replacements += KKK_REPLACEMENTS
    if 'campaign.html' in rel_path and '/' not in rel_path:
        replacements += CAMPAIGN_REPLACEMENTS
    if 'map.html' in rel_path:
        replacements += MAP_REPLACEMENTS
    if rel_path.startswith('services/'):
        replacements += SERVICE_SUBPAGE_REPLACEMENTS
    if rel_path.lower().startswith('diagnosis/'):
        replacements += DIAGNOSIS_SUBPAGE_REPLACEMENTS
    if rel_path.startswith('blog/'):
        replacements += BLOG_SUBPAGE_REPLACEMENTS
    if rel_path.startswith('campaign/'):
        replacements += CAMPAIGN_SUBPAGE_REPLACEMENTS

    return replacements


def update_navigation(content, rel_path):
    """
    Update header navigation:
    - Remove workshop link
    - Translate nav items
    - Add FIN to language switchers (both mobile and desktop)
    - Update brand href to /fin/
    """
    # Determine current page filename for lang switcher
    filename = os.path.basename(rel_path)
    subdir = os.path.dirname(rel_path)
    if subdir:
        lang_page = subdir + '/' + filename
    else:
        lang_page = filename

    # Remove Training/Workshops nav links (any nav variant, any language prefix)
    content = re.sub(
        r'\s*<a href="/(?:en|fin|et|ru)/workshops\.html"[^>]*>[^<]*</a>',
        '',
        content
    )

    # Translate nav items (desktop + mobile)
    nav_map = [
        (r'>Home</a>', '>Etusivu</a>'),
        (r'>Massages</a>', '>Hieronnat</a>'),
        (r'>Diagnoses</a>', '>Diagnoosit</a>'),
        (r'>Campaigns</a>', '>Kampanjat</a>'),
        (r'>Team</a>', '>Tiimi</a>'),
        (r'>FAQ</a>', '>UKK</a>'),
        (r'>Blog</a>', '>Blogi</a>'),
    ]
    for old, new in nav_map:
        content = re.sub(old, new, content)

    # Update brand link to /fin/
    content = content.replace(
        'href="/en/home.html" aria-label="MV Therapy etusivu"',
        'href="/fin/home.html" aria-label="MV Therapy etusivu"'
    )

    # Replace language switchers — build new switcher with FIN active
    def make_mobile_switcher(m):
        return (
            '<div class="mobile-lang-header" aria-label="Kieli">\n'
            f'          <a href="/et/{lang_page}">EST</a>\n'
            f'          <a href="/ru/{lang_page}">RUS</a>\n'
            f'          <a href="/en/{lang_page}">ENG</a>\n'
            f'          <a href="/fin/{lang_page}" class="active">FIN</a>\n'
            '        </div>'
        )

    def make_desktop_switcher(m):
        return (
            '<div class="lang-switch" aria-label="Kieli">\n'
            f'          <a href="/et/{lang_page}">EST</a>\n'
            f'          <a href="/ru/{lang_page}">RUS</a>\n'
            f'          <a href="/en/{lang_page}">ENG</a>\n'
            f'          <a href="/fin/{lang_page}" class="active">FIN</a>\n'
            '        </div>'
        )

    content = re.sub(
        r'<div class="mobile-lang-header"[^>]*>.*?</div>',
        make_mobile_switcher,
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="lang-switch"[^>]*>.*?</div>',
        make_desktop_switcher,
        content,
        flags=re.DOTALL
    )

    return content


def update_footer_links(content):
    """Update all internal /en/ links to /fin/ in footer and body."""
    # Replace /en/ links → /fin/ (but keep external links unchanged)
    content = re.sub(r'href="/en/', 'href="/fin/', content)
    return content


def add_notice_banner_css(content):
    """Insert Finnish banner CSS before last </style>."""
    # Find the last </style> before </head> and insert CSS before it
    idx = content.rfind('</style>\n</head>')
    if idx == -1:
        idx = content.rfind('</style>')
    if idx != -1:
        content = content[:idx] + NOTICE_CSS + '\n' + content[idx:]
    return content


def add_notice_banner_html(content):
    """Insert Finnish banner HTML after </header>."""
    content = content.replace('</header>\n\n  <!-- ===== MAIN =====',
                              '</header>\n' + NOTICE_HTML + '\n  <!-- ===== MAIN =====')
    # fallback if exact string not found
    if NOTICE_HTML not in content:
        content = re.sub(
            r'</header>\s*\n',
            '</header>\n' + NOTICE_HTML + '\n',
            content,
            count=1
        )
    return content


def process_file(src_path, dst_path, rel_path):
    """Process a single HTML file: translate and write Finnish version."""
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Common replacements
    for old, new in COMMON_REPLACEMENTS:
        content = content.replace(old, new)

    # 2. Page-specific replacements
    for old, new in get_page_replacements(rel_path):
        content = content.replace(old, new)

    # 3. Update all internal /en/ links → /fin/ (do BEFORE nav update so
    #    the lang-switcher ENG link we add later keeps /en/)
    content = update_footer_links(content)

    # 4. Update navigation (remove workshops, translate, add FIN with ENG→/en/).
    #    update_navigation rebuilds the lang-switcher from scratch, so the
    #    ENG link will correctly stay as /en/ regardless of step 3.
    content = update_navigation(content, rel_path)

    # 5. Add Finnish notice CSS
    content = add_notice_banner_css(content)

    # 6. Add Finnish notice HTML after </header>
    content = add_notice_banner_html(content)

    # 7. Write output
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    # Pages to include at root level (NO workshops.html)
    root_pages = [
        'home.html',
        'index.html',
        'services.html',
        'Diagnosis.html',
        'campaign.html',
        'team.html',
        'kkk.html',
        'blog.html',
        'map.html',
    ]

    # Subdirectories to process (NO workshops/)
    sub_dirs = ['services', 'blog', 'Diagnosis', 'campaign']

    total = 0

    # Process root pages
    for page in root_pages:
        src = os.path.join(SOURCE_DIR, page)
        dst = os.path.join(TARGET_DIR, page)
        if os.path.exists(src):
            process_file(src, dst, page)
            print(f'  ✓  {page}')
            total += 1
        else:
            print(f'  ✗  {page} (NOT FOUND – skipped)')

    # Process sub-pages
    for subdir in sub_dirs:
        src_dir = os.path.join(SOURCE_DIR, subdir)
        dst_dir = os.path.join(TARGET_DIR, subdir)
        if not os.path.isdir(src_dir):
            print(f'  ✗  {subdir}/ (directory not found – skipped)')
            continue
        for fname in sorted(os.listdir(src_dir)):
            if not fname.endswith('.html'):
                continue
            rel = subdir + '/' + fname
            src = os.path.join(src_dir, fname)
            dst = os.path.join(dst_dir, fname)
            process_file(src, dst, rel)
            print(f'  ✓  {rel}')
            total += 1

    print(f'\n✅ Done – {total} Finnish pages created in {TARGET_DIR}/')


if __name__ == '__main__':
    main()
