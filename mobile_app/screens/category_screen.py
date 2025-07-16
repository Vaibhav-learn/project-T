from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.lang import Builder
from widgets.product_card import ProductCard
from kivy.app import App
from functools import partial
from screens.product_list_screen import ProductListScreen

# Your original data structure - UNCHANGED as requested.
categories = {
    # ... (Your huge categories dictionary is here) ...
    # (Name, Image Path, Description, Old Price, New Price)
    "SALE": [("Kayakalpa/Kaayakalpaa Kit 225g Each" , "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
        ("Karisalankanni/Karisilankanni Oil[For Hair]90g" , "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/2.png","""Description
This oil comes from a plant known in English as “false daisy.” The herb is in the sunflower family and grows best in moist places including Thailand, India, and Brazil.

Preparation:
STEP-1: Equal quantities of nallennai, cow’s milk and the powder are taken.

STEP-2: The leaves of Karisalankanni plant are grinded in a mixer.

STEP-3: Nallennai and cow’s milk are added to the powder acheived.

STEP-4: Boiling the three((Karisalankanni),(Nallennai),(Cow’s milk)) for 20 minutes in a stove. Thus, Karisalankanni oil is prepared.

As there will be a bad smell coming from the oil, we mix some amount of carrier oil to it.

Benefits:
Hair growth:

Karisalankanni contains vitamin E, which is known to fight free radicals that can impede hair growth.

Dandruff reduction:

Karisalankanni oil has antimicrobial and antifungal properties that can help reduce dandruff. The oil also has anti-inflammatory properties, which can help psoriasis or other skin irritations on the scalp. It is also said to improve circulation to the scalp.

Slows graying:

Karisalankanni oil slows the graying process. Gray hair is also commonly understood as a loss of pigment. The darkening properties of Karisalankanni may help hair appear less gray.

Application:
Gently, apply the oil on your hair. Applying the oil directly on the scalps is recommended for quick effectiveness.

Frequency of usage:

You may use it 3 days once as the product will be very pure. Apply it deep on the scalps at night, and morning wash your hair!""",350.00,300.00),
        ("Eucalyptus Oil 60ml", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/3.jpg","""Description
Benefits of Eucalyptus Oil:
It is super-effective for COVID-19. You shall mix this Oil in hot water, close yourself with a blanket and inhale the steam that arises from it.
NOTE: Add Manjal Powder for increasing the effectiveness

1. Silence a cough:

For many years, eucalyptus oil has been used to relieve coughing. Today, some over-the-counter cough medications have eucalyptus oil as one of their active ingredients. Vicks VapoRub, for example, contains about 1.2 percent eucalyptus oil along with other cough suppressant ingredients.

The popular rub is applied to the chest and throat to relieve cough symptoms from the common cold or flu.

2. Clear your chest:

Are you coughing but nothing is coming up? Eucalyptus oil can not only silence a cough, it can also help you get the mucus out of your chest.

Inhaling vapor made with the essential oil can loosen mucus so that when you do cough, it’s expelled. Using a rub containing eucalyptus oil will produce the same effect.

3. Keep the bugs away:

Mosquitoes and other biting insects carry diseases that can be dangerous to our health. Avoiding their bites is our best defense.

4. Disinfect wounds:

The Australian aborigines used eucalyptus leaves to treat wounds and prevent infection. Today the diluted oil may still be used on the skin to fight inflammation and promote healing. You can purchase creams or ointments that contain eucalyptus oil. These products may be used on minor burns or other injuries that can be treated at home.

5. Breathe easy:

Respiratory conditions such as asthma and sinusitis may be helped by inhaling steam with added eucalyptus oil. The oil reacts with mucous membranes, not only reducing mucus but helping loosen it so that you can cough it up.

It’s also possible that eucalyptus blocks asthma symptoms. On the other hand, for people who are allergic to eucalyptus, it may worsen their asthma. More research is needed to determine how eucalyptus affects people with asthma.

6. Control blood sugar:

Eucalyptus oil has potential as a treatment for diabetes. Although we don’t know much at this time, experts believe that it may play a role in lowering blood sugar in people with diabetes.

7. Soothe cold sores:

The anti-inflammatory properties of eucalyptus can ease symptoms of herpes. Applying eucalyptus oil to a cold sore may reduce pain and speed up the healing process.

You can buy over-the-counter balms and ointments for cold sores that use a blend of essential oils, including eucalyptus, as part of their active ingredient list.

9. Ease joint pain:

Research suggests that eucalyptus oil eases joint pain. In fact, many popular over-the- counter creams and ointments used to soothe pain from conditions like osteoarthritis and rheumatoid arthritis contain this essential oil.

Eucalyptus oil helps to reduce pain and inflammation associated with many conditions. It may also be helpful to people experiencing back pain or those recovering from a joint or muscle injury. Talk to your doctor about if it may be right for you.""",200.00,150.00),
        ("Sathuragiri/Sadhuragiri Joint Pain Thailam" , "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/4.jpg","""Description
Benefits of Sathuragiri Mootu Vali(Joint Pain) Thailam:
Our fast-paced lifestyle tends to overwhelm our joints and muscle cells, rendering them dysfunctional. Orthoherb Oil easily penetrates the skin, delivering its medicinal properties to the muscle cells and joints in the body, making it flexible, strong and healthy.

Benefits:

Anti-inflammatory and analgesic
Lubricates joints
Imparts muscle tone and strengthens the Dhatus
Imparts firmness to limbs
Stimulates circulation
Helps the lymphatic functioning for detoxification
Joint Pain
Inflammations
Cervical & Lumbar Spondylosis
Sciatica & all types of inflammatory joint conditions
This oil provides excellent relief from joint pain.
It not only alleviates pain but also helps remove excess fluids that may be trapped within the joints.
Ideal for elders, aging individuals, and mothers at home.
✅ Absolutely no side effects.

Usage Instructions:
Step 1:
Slightly warm the oil and apply it to the affected/painful areas.

Step 2:
Gently massage the area for a few minutes to ensure absorption.

Step 3:
In the morning, rinse the area with bearably hot water for best results.""",350.00,300.00),
        ("Nalangu Maavu Powder 50g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/5.jpg","""Description
Nalangu Maavu is a herbal body wash or face wash popular in South India. It is an Ayurvedic formulation, made with natural ingredients like Indian sarsaparilla, White turmeric, Champak, Flagroot, and others. This bath powder is also used in Ayurveda as medicine, to treat skin conditions like eczema. The benefits it offers are immense, and it was everyone’s choice of a good cleanser before chemical soaps and gels came into the picture.

Benefits of using Nalangu Maavu:
• Nalangu Maavu absorbs excess oil from the skin without drying it
• It helps to restore the natural pH balance of skin
• Turmeric in the bath powder works wonders for inflammation
• Turmeric also promotes the body’s synthesis of antioxidants and slows down visible signs of aging
• Regular usage of herbal bath powder can help people with acne or pimples, by reducing oil secretion
• Using Nalangu Maavu Herbal Bath Powder on a daily basis can help reduce body odor and excessive sweating
• It acts like a toner, minimizing pores on the skin
• Nalangu Maavu Herbal Bath Powder is antifungal, anti-bacterial and anti-microbial

This product can be used for infants(babies) also!""",50.00,40.00),
        ("Aadutheendapalai Powder 50g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/6.jpg","""Description
Benefits of Aadu Theenda Paalai:
• Aadu theenda palai is a good remedy for Diarrhea & fever.
• It cures inflammation.
• Treat for respiratory disorders & asthma.
• It controls Blood pressure.
• It used for gas problems.
• Snake bites""",70.00,60.00),
        ("Pure K.Oil/Karisalankanni Oil 225Ml", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/7.png","""Description
HOW TO USE?
Internal Consumption:
When taken orally, this oil can significantly enhance overall organ health, especially the liver and lungs.

For Hair Application:
When applied directly to the roots of the hair, it helps prevent greying, reduces hair fall, and promotes thicker hair growth.

For Skin Application:
When applied to the face, hands, legs, and skin in general, it gives a natural golden glow, making you appear significantly younger.

For Eye Care:
In cases of blurred vision, applying a small amount of this oil gently on the eyelids can help improve eyesight.

Dosage:
Internal Consumption: 1 Spoon

External Application: 2 Spoons (once every 3 days)
✅ Free spoon included

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Bhringraj Extract	Eclipta prostrata	85%
Gingelly Oil	Sesamum indicum	15%

Method of Preparation:
This oil is prepared by processing high-quality, edible-grade gingelly oil with Bhringraj juice (Karisilankanni).
Notably, Karisilankanni is one of the main ingredients used in the ancient formulation “Thangapashpam” (Golden Elixir).""",3000.00,2120.00),
        ("Manjal/Turmeric Powder 50g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/8.jpg","""Description
Benefits of Manjal Podi(Virali Manjal Powder):
• Manjal Podi is used as blood purifier and it is used in the treatment of atherosclerosis, it is used to remove accumulation in the blood vessels and used to remove toxins from the body.

• It is used in the treatment of diabetes. Turmeric herb is very effective herb that is used in the treatment of diabetes.

• Being anti-inflammatory this herb is used to reduce inflammation and used in the treatment of bone related disorders.

• Being a stimulant it is used to stimulate digestive fire and it is used as stomach tonic and used in various ailments associated with digestive system.

• Externally its paste is used for wound healing and it is also helpful to rejuvenate skin tone. It is used to heal sores and also used in various cosmetics.

• It is anti-bacterial and anti-oxidant in nature and used to cure various body disorders.

• Externally its paste is used in the treatment of acne and pimples. It is also beneficial to treat anaemia.

• It is main home remedy to cure common cold and cough.""",40.00,30.00),
        ("SPL. Arokiya Podi/Powder 225G", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/9.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
        ("Sukku Powder 25g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/10.jpg","""Description
Benefits of Sukku:
• Digestive disorders: This extremely useful herb is used to relieve patients suffering from dyspepsia, flatulence, vomiting, spasms, colic and other stomach problems.
• Cough and Cold: The herb is used to relieve cough.
• Respiratory Disorder: It reducing fever in patients suffering from influenza. It is known to act as an expectorant in relieving asthma, cough and tuberculosis.
• Impotency: The herb is known to be an effective aphrodisiac. It relieve impotency, premature ejaculation, involuntary seminal discharge and also spermatorrhoea.
• Menstrual Disorders: A piece of ginger with a cup of boiled water must be used to relieve menstrual problems.""",33.00,30.00),
        ("Scool Rice/Sool Arisi 50g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/11.jpg","""Description
Benefits of Scool Arisi
Very effective in case you want a NORMAL DELIVERY!
It is a good remedy for women during the time of  (leucorrhoea).
Method of INTAKE:

Step-1: In tender coconut water add some school arisi at night before going to sleep.

Step-2: Drink the tender coconut with school arisi early in the morning.""",100.00,80.00),
        ("Naaval Seed Powder 50g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/12.jpg","""Description
Benefits of Naaval Seed:
• Regulates Blood Sugar Level: Jamun fruit is very good remedy for the people suffering from diabetes because of its anti-diabetic properties which helps keeping blood sugar level under control by converting starch and sugar into the energy. Another study showed that jamun seeds could lower blood sugar levels by 30%.

• Good For Diabetics: The low glycaemic index, in Jamun, makes it a good option for diabetics. A study conducted on the anti-diabetic effects of Jamun, suggests that it holds significant potential to produce safer drugs for diabetes treatment. The fruit is associated with lowered risk of secondary complications of diabetes. The leaves, barks, and seeds are the most useful parts among which the seeds are popular for their anti-diabetic properties.

• Good for heart health: Jamun is loaded with nutrients like ellagic acid / ellagitannins, anthocyanins and anthocyanidins which has the anti-inflammatory property and these compounds are also powerful antioxidants that prevent oxidation of cholesterol and plaque formation that contributes to heart disease.

• Acts as a Blood Purifier: Black Plum has adequate amount of iron and vitamin C. The presence of iron in the black plum is good to increase the hemoglobin count. The fruits iron content acts as blood purifying agent.

• Improves Bone Strength: The fruit also has healthy amount of nutrients like calcium, iron, potassium and Vitamin C, which makes it great for boosting immunity and bone strength.

• Treats Infections: The fruit as well as the other parts of the plant has compounds like malic acid, gallic acid, oxalic acid and tannins which makes the fruit as a anti-malarial, anti-bacterial, anti-infective and gastro protective properties.

• Cures Digestive Disorders: Jamun has cooling property thus very beneficial for curing digestive disorders.

• Fights Anemia: The Jamun fruit is rich in Iron content and daily eating of this fruit, cures anemia and jaundice and also good for ladies who suffers for menstrual problems.

• Increases Immunity: Its high level of vitamin C availability makes body immunity system strong to fight with common seasonal problems.""",50.00,40.00),
        ("Multhani Mitty Powder 100g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/13.jpg","""Description
About Multhani Mitty:

Multhani Mitty is a clay substance that is hugely popular for its healing property against acne and blemishes. It is very rich in magnesium chloride which helps to reduce acne. Originally used as an absorbent in the wool industry this ingredient is now greatly used in many skin care products. Multhani Mitty also helps to enhance the color and tone of the skin. But this can only be caused by the continued use of Multhani Mitty.

Multhani Mitty for hair:

As a hydrating agent, Multhani Mitty helps moisturize your scalp and reduces dryness and unevenness.With the anti-bacterial and hydrating properties of Multhani Mitty regularly is effective in reducing and preventing dandruff.It brings in more antibody cells to improve the growth of skin mushrooms in your scalp and improves blood flow. Multhani Mitty absorbs all the oil that is in addition to it, giving it the hydration and nutrition it needs. Reduces the burden of bacteria on your scalp and makes you feel light.
Dry and uneven scalp is a natural skin condition for some people. Factors such as pollution and climate can worsen this. These factors may also play a role in scalp dryness. In addition, some shampoos have also been linked to dryness. From time to time, Multhani Mitty has been in the making of Hair Care Products. The hydrating nature of Multhani Mitty Powder helps moisturize your scalp and hair. It also ensures that your scalp gets enough blood flow.So it will get extra nutrients and regain the natural glow.

NOTE: If you like straight hair, you can create a hair pack with Multhani Mitty, yoghurt, white egg and some drop lemon juice.

Benefits of Multhani Mitty :
• Multhani Mitty for Oily skin: Multhani Mitty works wonders for oily skin. Oily skin easily attracts dust and other impurities from surrounding. These particles clog the skin pores and may cause pimples and eruptions on face. Multhani Mitty Powder is a blessing for such individuals. It absorbs excess oil from the skin surface and makes it soft and smooth. It avoids the occurrence of pimples caused due to excess oil secretion.

• Multhani Mitty for dry skin: Those who have dry to normal skin can use Multhani Mitty face packs by adding some milk and almond paste. Dry skins needs extra care.

• Multhani Mitty for Scrubbing: When in hurry, and no time for applying a face pack, you can use Multhani Mitty for scrubbing purpose. It will give equally glowing skin. To make this scrub use roughly grounded almonds or walnuts. if you do not wish to use these nuts, you can use some sugar granules with Multhani Mitty and scrub your face softly with this mix. Wash it off and you will see a clean, glowing skin in minutes.

• Multhani Mitty for cleaning: Multhani Mitty is a very good cleanser. It cleanses on the surface as well as deeper action. It removes all the dead cells and cleanses the pores from impurities.

• Multhani Mitty for Toning: It helps in improving the skin tone and gives a bright glow and radiance on the face. Multhani Mitty’s bleaching effect helps in lightening the blemishes and acne marks too.

• Multhani Mitty for blemishes and pimple/ Acne marks: Multhani Mitty can be used for removing pimple marks and blemishes to have an even tone. To make an anti blemish and anti mark pack, mix Multhani Mitty with tomato juice or lemon juice and add a pinch of turmeric to it.

• Multhani Mitty for Acne and pimples: Pimple and acne problems can be relieved by applying Multhani Mitty Powder and Neem leaves paste on face. You can keep it for some time and then wash it off. If you have scars, you can add lemon juice to this paste. Applying it for a week will have noticeable effects on your face.

• Multhani Mitty for pigmentation: Multhani Mitty has anti tan properties and helps in getting rid of sun tan and ill effects of pollution on your skin.

• Multhani Mitty for skin irritation: If you have skin irritation due to acidity, allergic reaction to any cosmetic products or bleach, or red skin due to excess sun exposure, Multhani Mitty has cooling effect and will give you instant relief from skin irritation.

• Multhani Mitty as Body Wash: Multhani Mitty can be used in your natural body wash.""",60.00,50.00),
        ("Kalarchikai/Klachikai Powder 25g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/14.jpg","""Description
Benefits of Kalarchikai:
• It has been used for treating intestinal worms, fever, tumors, cough, amenorrhea, and to remove the placenta after childbirth.
• Kalarchikai is used for eliminating piles, wounds, leucorrhea, and urinary disorders.
• It can be used for gargling to relieve a sore throat.
• It is used in controlling elephantiasis and smallpox.
• It is good for Hernia patients.

• It may be roasted in castor oil and be applied to reduce piles, inflammatory swellings, orchitis, and hydrocele.
• A paste made from the leaves and twigs is useful in reducing toothache.

Way of Consumption:
You have to consume Kalarchikai Podi in the morning(empty stomach)!

You can take a banana with our powder as it will be very bitter or you may mix the powder with water and drink for effectiveness!""",55.00,50.00),
        ("Arugampul Podi/Bermuda Grass Powder 50g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/15.jpg","""Description
Health Benefits Of Arugampul:
• Arugampul juice is highly praised for its potent alkaline property. It works well by increasing the alkaline level and lowers acidity. To get instant relief from acidity take 3 teaspoons of Arugampul powder and mix it with a glass of water and consume.
• Arugampul juice is revered for its powerful detoxifying properties. The natural detoxify agent cleanses the liver and flushes out the toxins from the body. Arugampul is naturally high in chlorophyll and facilitates blood purification by removing harmful toxins.
• The goodness of Arugampul juice is beneficial to heal various skin ailments like eczema, psoriasis, treat wounds and fungal infections. Drinking Arugampul juice regularly on an empty stomach detoxifies the system and enhances the skin glow and radiance.
• Arugampul juice contains Cynodon Dactylon Protein Fractions or CDPF, a protein element responsible for triggering the immune system. In addition, it is also heaped with powerful antioxidants, vitamins A and C which scavenges free radical damages, avert chronic inflammation and keep diseases away.
• Also consumption of Arugampul juice regularly, keeps Blood Sugar level in check.
• Arugampul juice is an effective natural remedy to treat kidney stones and urinary tract infections. It functions well as a good diuretic by flushing out the toxins, getting rid of excess water and clears out kidney stones.""",18.00,15.00),
        ("SPL. Amukkara Powder(SPL. Ashwagandha) 225G", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sales/16.png","""Description
Benefits of Ashwagandha:
• It helps to reduce level of stress and tension.
• It improves energy level.
• It supports better sleep.
• It helps to lower blood pressure and is highly effective in stopping the formation of stress induced ulcers.
• It increases haemoglobin and hair melanin.
• It stabilizes blood sugar and lowers cholesterol.
• It helps to reduce stress during a weight loss diet. When a person is stressed more Cortisol hormone is produced by the adrenal glands. Cortisol stimulates glucose production and triggers a hunger response in the brain. Ashwagandha can naturally lower cortisol levels up to 26%. It also helps to lose weight by reducing swelling in body and improving haemoglobin level.
• It is useful for any imbalance in the muscles as it reduces inflammation and strengthens muscles. It is an anabolic muscle builder. As it benefits all muscle tissue it is used as a heart tonic, uterine tonic, and lung tonic.
• It improves body immunity and strengthen body defense system. This makes this herb suitable for treating Auto-immune conditions such as neutropenia, rheumatoid and osteo arthritis, cancer and chronic connective tissue disorders.
• It gives good results in nerves related conditions such as Multiple sclerosis, Neurosis, insomnia, anxiety, and stress.
• It is used to enhance memory and lesson age-related cognitive deficits.

Benefits for Men:
• For males, Ashwagandha promotes sexual health by uplifting the mood, reducing anxiety, improving energy levels and fertility, thus supporting sexual performance.
• It has direct spermatogenic effect and helps to improve sperm count.
• It helps to alleviate asthenospermia (increasing sperm motility), oligospermia (increasing sperm count) and other sperm disorders.
• It exerts something like testosterone, influencing the seminiferous tubules.
• It promotes better sexual performance.
• It reduces impotence and promotes potency.

Benefits for Women:
• It contains phytoestrogen.
• It relieves females from menstrual imbalance.
• It stimulates secretion of breast milk in lactating mothers.
• It gives strength and cures debility when consumed post – delivery.
• It supports female reproductive system, and increases ovarian weight and folliculogenesis.""",1260.00,630),
        ],
   
 
    "Baby Care":[ ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/Kaayakalpaa-Kit-Intro-300x300.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
                 ("Kasi/Kaasi Katti 10g", "C:/Users/shiv shanker/OneDrive\Desktop/all image paths/baby care images/Kaasi-Katti-scaled-1-1-300x300.jpg","""Description
Kasi Katti is a resin or extract which is manufactured from Acacia catechu heartwood. Acacia catechu possesses various medicinal properties, therefore it is used in Ayurvedic medicines that treat many diseases.

Kaasi Katti is generally used in the treatment of asthma, cough, colitis, diarrhea, dysentery, skin boils, and sores.

Medicinal Properties of Kasi Katti
Kasi Katti is enriched with catechin, epicatechin and also has a fewer amount of flavonoids. This antioxidant behavior of Acacia catechu heartwood resin manages inflammation, protects tissues, prevents the growth of tumors, and relieves pain. It also possesses antihyperglycemic, antinociceptive, and antipyretic properties.

Health Benefits

• It is used to reduce food stagnation which in turn improves the digestion system.
• Kasi Katti helps in preventing bleeding ( hemorrhage).
• Generates new tissues.
• Acacia catechu heartwood resin is also used in the treatment of cancer.
• Kasi Katti has bitter, astringent properties that treat and clear lungs.

How to Consume
The decoction can be prepared with Kaasi Katti and water for drinking purposes.""",40.00,30.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/Untitled-design-19-300x300.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("Vengai Paal Pottu/Black Bindi for Babies 1 piece","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/Vengai-Pal-Pottu-scaled-1-1-300x300.jpg","""Description
This pottu helps to protect the baby from bad vibrations and energy. Vengai Paal Pottu doesn’t cause any skin allergies to the baby. Moreover, you need not put any strain on removing this pottu from the baby’s forehead.

Benefits:
Vengai Paal Pottu comes from Vijaysar tree.
Promotes sleep in babies.
Doesn’t have any harmful effects on the babies.
Easy to remove from the baby’s skin.
Vengai Paal Pottu has a property to avoid Dhrishti in any form.""",120.00,100.00),
            ("Seer Pacchilai/Pillaivalathi Leaf 20g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/Pillavalathi-Elai-scaled-1-1-300x300.jpg","""Description
             Seer
Causes:

If a woman who is menstruating or has recently undergone an abortion comes near a baby, the child may be affected by “Seer” (a form of negative energy disturbance).

Even if a brooding hen flaps its wings near the baby, it is believed the child could be affected.

If the baby’s father or mother has had sexual relations and lifts or touches the child without bathing, it may lead to this disturbance.

When a baby already affected by “Seer” comes close to another child, the energy is believed to transfer—even between boys and girls. Cross-gender transfer is thought to be more intense.

Traditional Cure:
There exists a special herbal leaf known as Seer Pachilai (Seer Leaf).
Crushing and applying this leaf paste on the baby’s forehead is believed to cure the condition.

Reflection:
How do we describe these deeply rooted ancestral practices and traditional beliefs that even modern science and educated minds often cannot fully explain?

These are part of our cultural wisdom, passed down through generations—often beyond the grasp of textbooks or laboratories.""",120.00,100.00),
            ("Vasambu Bangle 1 piece","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/Vasambu-Valayal-scaled-1-1-300x300.jpg","""Description
Vasambu is an organic product; it is referred to as ‘child-rearing. It is also known as flagroot, bitter crinkle root, sweet cane, myrtle grass, Rat root, and sweet sedge. Vasambu plays the primary role in Tamil traditional medicine.
Babies frequently used to shake their hands and taking their hands to their mouth. When we wear a Vasambu bracelet to the baby, it gives a beautiful fragrance, and it will keep refreshing the brain and nervous system.

Vasambu Valayal for Babies
In the old days, people tie the vasambu valayal into the baby’s hand at the naming ceremony. They also tie this in babies’ neck and hip with the rope. It helps to filter impurities from the baby’s body. Moreover, it increases the baby’s sleeping time and also keeps their mind in peace state.

Benefits of Vasambu Valayal

• Babies used to drink milk as the main food. Milk takes a large time to get digest. Vaasambu protects babies from digestion issues.
• Vasambu Valayal protects the babies from microbes which try to enter into their body.
• It is not only concerning from evil eye; it also has a medical property which helps to improve their sleep and keep their mind calm.
• These herbs are mainly used for:

1)Throat soreness
2)Migraine
3)Stomach ache
4)Congestion and Colds
5)Asthma
6)Vomiting""",70.00,60.00),
            ("Mooligai Sambrani/Muligai Saampirani Set 100 g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/Sampirani-scaled-1-1-300x300.jpg","""Description
SAMBRANI HEALTH BENEFITS
• Sambrani has a unique beautiful fragrance that is different from the normal incense sticks. The smell of sambrani transports back in time and somehow fills a person with peace and happiness. Even Ayurveda advises to use sambrani, as it calms the nerves, and produces tranquility, thus making the person ready for prayers.
• Women after having their hair washed, light up sambrani to dry it very quickly and also leave a beautiful fragrant smell in their hair. During winter months, if we use sambrani, we will not get a headache, especially if we have long, thick hair.
• Sambrani is also used for babies, after children have their bath, sambrani is lit and brought in that room. This prevents them from catching a cold but make sure not to bring the smoke too near the babies, as it will make their lungs delicate. No auspicious day is complete without sambrani, sambrani is always lit during our prayers and rituals.
• Regularly light up sambrani every morning, take it to every room in the house. This wards off mosquitoes and cleanses the whole place.
• To remove stale and negative energy, calm down anxiety, depression, and for a fresh smelling home.
• Light up sambrani at least weekly once and fill the whole house with the smoke. It will make the whole house smell divine.
• Even for headaches, sambrani smoke is very good.
• Purification of the air
• No auspicious day is completed without sambrani; sambrani is always lit during prayers and rituals. Lighting up of sambrani once in a day, makes us feel that we have followed proper rituals and cultures.
• This Traditional way of Lighting of Sambrani keeps the rooms spiritually strong and produces positive vibrates and also keeps away from mosquitoes.
• Medicated smoke has an important role in Ayurveda. It can be used to fumigate a room or it can carry to an individual the essence of herbs. Incense thus has healing properties. The smoke with its gandha or aroma activates the nasal system and through it makes changes in the body and mind of the person.
• Manage pain
• Improve sleep quality
• Reduce stress, agitation, and anxiety
• Soothe sore joints
• Treat headaches and migraines
• Ease discomforts
• Fight bacteria, virus, or fungus
• Improve digestion
• Improve hospice and palliative care
• Boost immunity""",140.00,120.00),
            ("Spiked Ginger Lily 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/IMG_0599-scaled-e1646573249906-1-300x300.jpg","""Description
Benefits of Poolan Kizhangu:
• Poolan Kizhangu is helpful in treating liver complaints, indigestion and poor circulation due to thickening of the blood.
• It is used in treating nausea, halitosis, vomiting, diminished appetite, hiccups and local inflammation.
• The rhizomes of Poolan Kizhangu are used in treating asthma and internal injuries.
• The rhizomes are powdered and used as an antiseptic agent and as a poultice for various aches and pains.
• Its rootstalk is used in treating bronchitis and alleviating pain.
• It is good for skin.""",160,120),
            ("Urasu/Orasu Medicine(For Baby) 1 set","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/Orasu-Marunthu-scaled-1-1-300x300.jpg","""Description
CONTENTS:
Paalkayam
Kadukkai
Jathikkai
Maasakkai
Vasambu
When To Use?
When your Babies feel the slightest discomfort, you may rub the set as a whole and keep it in the tongue of the baby.""",70.00,60.00),
            ("Vasambu Sweetflag 2 piece","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/Vasambu-scaled-1-1-300x300.jpg","""Description
Benefits of Vasambu(Sweet Flag):
• Vasambu helps to get rid of all gastric problems.
• It stimulating aroma rejuvenates the brain and the nervous system.
• It is also effective against digestive disorders.
• Baby nutrition problems and baby sleep problems are the most common problems in newborns.
• Remedy for acid re-flux, loose motion, hair removal, and flatulence. The other stomach problems like indigestion, stomach, loss of appetite can also be cured with the herb extracts.""",30.00,20.00),
            ("Baby Care Combo 1 set","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/IMG_0532-scaled-2-1-300x300.jpg","""Description
INGREDIENTS:

1) Orasu Marundhu – 1 piece each
[Paalkayam, Kadukkai, Jathikkai, Maasakkai, Vasambu]
2) Kaadhola Karugamani – 1 piece
3) Vasambu Valayal – 1 piece
4) Pillavalathi Elai – 25 grams
5) Vasambu – 2 pieces
6) Kaasi Katti – 10 grams
7) Muligai Saampiraani – 100 grams
8) Kuliyal Podi – 50 grams
9) Vengai Paal Pottu – 1 piece
10) Javvaadhu – 6 grams
[Perfume for baby]""",800.00,550.00),
            ("Javvadu/Javathu Powder 6g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/Javvadhu-scaled-1-1-300x300.jpg","""Description
Javadhu was thus used during worships, yoga, pranayama & meditation to enhance spirituality of the mind. The Fragrance of Javadhu evokes mental harmony which makes our Aura more effective during our Yoga and Meditation sessions. It enhances deep breath and helps us during Yoga and Pranayama. The Fragrance of Javadhu is also a strong as mentioned in many ancient literatures of India With a perfect blend of nature gifted Sandal Oil, Sandal Powder and Indian ecstatic herbs and floral extracts, Javadhu Powder is so unique to fill your hearts with joy and romance. Javadhu Powder being in powder form it’s easy to apply and will not give any suffocation as sprays. Javadhu Powder, with its divine and spritual fragrance gives mental peace and relaxation from stress when used in worship place. Usage is quiet simple to mix with little drops of water or rose water to make a paste and apply directly to body. Unlike artificial perfumes Javadhu powder doesn’t cause any irritation. The Herbal nature of Javadhu powder resists body odor causing germs in the skin. Modern Deodorants mostly reduces the process of sweating which is very harmful to skin but Javadhu powder only prevents the cause of the body odor hence keeps the skin in its natural state and fills with fresh and pleasant fragrance. Artificial perfumes give a blast of fragrance when applied but they evaporate very soon to no effect, Javadhu powder being a powder perfume stays with the skin and lasts much long for a whole day. Javadhu powder is not only a Natural body perfume but a herbal remedy to body odor.

Benefits:

• Javadhu Powder, with its divine and spritual fragrance gives mental peace and relaxation from stress when used in worship place.
• Javadhu Powder is so unique to fill your hearts with joy and romance.
• The Herbal nature of Javadhu powder resists body odor causing germs in the skin.
• Keep Body Cool & Fragrant, Mix with little water and apply it on body to keep cool and fragrant through the day
• A traditional Indian Natural blended perfume powder, The Javadhu – the perfume from paradise""",160.00,120.00),
            ("Kaadhola/KaadholaiKarugamani  1 set","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/Kaadhola-Karugamani-scaled-1-1-600x600.jpg","""Description
A product extremely useful for babies.

Traditional Practice & Symbolism:
In ancient times, married women (Sowbhagyavathis) did not wear the modern Thirumangalyam (Mangalsutra).

Instead, they adorned themselves with:

Karugamani (black beads), and

Kaadhani (ear ornaments made from palm leaves).

Even today, during the Varalakshmi Puja, when decorating the deity Mahalakshmi, these traditional ornaments—Kaadhani and Karugamani—are included.

The Kaadhani consists of a rolled pale red palm leaf inserted through a small black bead, forming a simple yet culturally rich earring.""",80.00,60.00),
    ],
    "Bathing":[
             ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/bathing products/Kaayakalpaa-Kit-Intro-300x300.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
             ("Herbal Hairwash/Shikakai/Seeyakkai Powder 50g Each", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/bathing products/Herbal-Hairwash-50g-60-scaled-1-1-600x600.jpg","""Description
Benefits of Herbal Hairwash:
Imparts Shine and Softness To Hair:
The essential nutrients and natural ingredients present in the powder is extremely beneficial in improving the texture of hair in winter. Being a natural surfactant, it cleanses the hair follicles, removes greasiness and makes the hair softer and shinier.
Boil 2-3 tbsp of the powder in 2 cups of water, to make a semi-liquid paste. Add some more water. Apply this paste and rinse your hair with water. Try this remedy twice a week to flaunt gorgeous shiny hair.

Removes Hair Lice and Dandruff:
Much to our respite, the potent antifungal and anti-microbial property of the powder plays a key role in removing dandruff and lice from the scalp and hair respectively. It effectively removes dandruff but does not strip away the essential oils from the scalp, hence preventing dry scalp problems which ultimately causes flaking and dandruff.

Boil the powder in water. Filter and squeeze half a lemon in it. Wash your hair regularly with this water to get relief from dandruff and lice.

Provides Stronger and Thicker Hair:
All of us wish to have a healthy, lustrous and strong mane. The active ingredients of the powder provides the essential oils and vitamins necessary for hair growth. It holds high significance in regaining the lustre and length of hair. It strengthens the hair from roots, prevents split ends, breakage and hair fall.
Make a paste of the powder with fresh yoghurt and apply to your hair and scalp. Allow it to remain for 20-30 minutes and rinse with cold water. Regular usage provides stronger and thicker mane.

Heals Infections:
The Herbal Hairwash Powder has a calming and soothing effect due to its potent medicinal properties. Unlike chemical shampoos, which may cause irritation on the inflamed or sensitive scalp, Shikakai provides a cooling effect and subdues the pain.
Apply a paste of slightly air-roasted herbal hairwash powder, neem leaves and turmeric on cuts, wounds, scratches or throbbing headache to get relief from inflammation and pain.

Slows Greying:
Grey hairs are quite depressing as it gives away your age and these days, many youngsters are suffering from premature greying. This powder not only prevents premature greying but also retains the natural youthfulness of black hair.
Apply a hair pack containing this powder, amla powder and soap nut on your hair once a week to get marked results.""",80.00,60.00),
             ("Herbal Bath/Kuliyal Powder 50g Each", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/bathing products/Muligai-Kuliyal-Podi-60-scaled-1-1-600x600.jpg","""Description
INGREDIENTS:
Curcuma zedoaria.Rosc
Psoralea corylifolia.Linn
Hydnocarpus laurifolia sleumer
Wood of Tefranthra.Roxb
Alkanna Tinctoria (L)
Vetriveria Zizanioides.Linn
Crossandra intundibuliformis
Curcuma aromatica.salisb
Cyperus notundus,Linn.
Aquilaria agallocha Roxb
Cedrus deodara.G.Don
Parmotrema Perlatum
Santalum Album
Boswellia serrata.Roxb
Bergenia Ligulata
Salix caprea.Linn
Eradicates:

Scabies
Itching
Phrynoderma
Scar
Melanoderma
Fungal skin diseases
Pimples
Black spots
Bad odour
If used for babies:

Baby’s Skin Stays Clean
It Softens the Skin
It evens Out Skin Tone
It reduces Risk of Infection
It maintain the pH levels in your baby’s skin
It Gives You Time to Bond with your Baby
Better Hand Eye Coordination and Visual Tracking
It Helps your Baby Relax
It Develops Cognitive skills""",80.00,60.00),
        ],
    "Beauty & Face":[
             ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/bathing products/Kaayakalpaa-Kit-Intro-300x300.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/baby care images/Untitled-design-19-300x300.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
             ("Herbal Bath/Kuliyal Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/bathing products/Muligai-Kuliyal-Podi-60-scaled-1-1-600x600.jpg","""Description
INGREDIENTS:
Curcuma zedoaria.Rosc
Psoralea corylifolia.Linn
Hydnocarpus laurifolia sleumer
Wood of Tefranthra.Roxb
Alkanna Tinctoria (L)
Vetriveria Zizanioides.Linn
Crossandra intundibuliformis
Curcuma aromatica.salisb
Cyperus notundus,Linn.
Aquilaria agallocha Roxb
Cedrus deodara.G.Don
Parmotrema Perlatum
Santalum Album
Boswellia serrata.Roxb
Bergenia Ligulata
Salix caprea.Linn
Eradicates:

Scabies
Itching
Phrynoderma
Scar
Melanoderma
Fungal skin diseases
Pimples
Black spots
Bad odour
If used for babies:

Baby’s Skin Stays Clean
It Softens the Skin
It evens Out Skin Tone
It reduces Risk of Infection
It maintain the pH levels in your baby’s skin
It Gives You Time to Bond with your Baby
Better Hand Eye Coordination and Visual Tracking
It Helps your Baby Relax
It Develops Cognitive skills""",80.00,60.00),
             ("Aavaarampoo Powder/Avarampoo Podi 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/beauty & face/4.jpg","""Description
              Description
Benefits of Aavaaram poo:
Aavaarampoo for diabetes:
Aavaaram flowers have cooling and dehydrating effects. Aavaarampoo juice is also effective for diabetic people. The properties of this plant help to reduce the sugar level in the blood effectively.

Aavaarampoo for Urinal issues:
These amazing flowers leave amazing effects on bowel movements and works as the very effective, natural laxative. The plant extract cleanses urinary system. Aavaarampoo tea is a good source of antioxidant that is good for health.

Aavaarampoo beauty benefits:
People use Aavaarampoo as a beauty treatment.

Aavaarampoo for hair:
It is used for hair care to remove dandruff.

How to Consume Aavaarampoo:
Morning: Mix 5 gms of powder in 100 ml water and boil it for a few minutes. Once the water gets warm, filter the content and drink it before food. Repeat the same for Evening Dosage after dinner. For excessive urination, take 1-2 gm of this powder with cow’s milk twice a day.

Applying Aavaarampoo powder:
• Aavaarampoo beauty benefits:
If you wish to get fair complexion then mix the flower powder with Bengal gram and green gram flour. Add little water or rose water to make a paste. Use this paste while taking bath. The regular usage will give you fairer complexion easily. Flower powder is also available in the market.

• Aavaarampoo Powder for hair:
Aavaarampoo powder (podi) and aloe vera gel is mixed with fenugreek(vendhayam) powder and applied on the scalp to treat dandruff.""",33.00,30.00),
        ("Vengai Paal Pottu/Black Bindi for Babies 1 piece","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/beauty & face/5.jpg","""Description
This pottu helps to protect the baby from bad vibrations and energy. Vengai Paal Pottu doesn’t cause any skin allergies to the baby. 
Moreover, you need not put any strain on removing this pottu from the baby’s forehead.

Benefits:
Vengai Paal Pottu comes from Vijaysar tree.
Promotes sleep in babies.
Doesn’t have any harmful effects on the babies.
Easy to remove from the baby’s skin.
Vengai Paal Pottu has a property to avoid Dhrishti in any form.""",120.00,100.00),
             ("Kasthuri Manjal Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/beauty & face/6.jpg","""Description
Beauty Benefits of Kasturi Manjal:
Kasturi Manjal works a wonder for human skin and also treats the skin ailments.

1. Can get rid of facial hair
The daily use of Kasturi Manjal by making a paste on the face eliminates the hair growth. In many small villages, the paste of Kasturi Manjal is applied to the face during the daily bath.

2. Enhances your complexion and get rid of dark circles
The daily use of Kasturi Manjal face pack made by mixing with milk or yogurt helps to cleanse the skin deeply. It eliminates the skin blemishes and provides the bright and fairer skin. Kasturi Manjal assists in lightening the skin tone and reduces pigmentation under eyes.

3. Helps keep acne at bay
Kasturi Manjal possesses the antibacterial properties which is effective in dealing with acne. It has no side effects and effectively alleviates the acne scars.

4. Can banish oily skin
Blemishes, coarseness, blackheads and acne could be alleviated if Kasturi Manjal is used with sandal wood powder and orange juice. The face pack could be prepared with 3 tablespoons of orange juice, one tablespoon of sandalwood powder and a pinch of turmeric powder. It should be applied to the face and should be left for 15 minutes. The sandalwood powder helps to tighten the pores of the skin and prevents the oily substance from the skin which is called sebum. Kasturi Manjal and orange juice reduces the skin blemishes.

5. Makes your skin look younger
Kasturi Manjal provides the supple and soft skin by eliminating the fine lines and wrinkles. The daily use of Kasturi Manjal slows down the ageing process. It enhances the healthy and glowing face.

6. Scrub for exfoliating skin
The anti-oxidant property keeps the skin rash free and prevents the skin disorders. The turmeric paste should be made with the yogurt and it should be used as a scrub on the skin. Let it remain for 15-20 minutes and wash it.

7. Treats skin tanning
The exposed parts to the sun should be applied Kasturi turmeric which prevents from getting tanned. One can get rid of tanning within few days of application of Kasturi turmeric powder.""",60.00,40.00),
             ("Multhani Mitty Powder 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/beauty & face/7.jpg","""Description
About Multhani Mitty:

Multhani Mitty is a clay substance that is hugely popular for its healing property against acne and blemishes. It is very rich in magnesium chloride which helps to reduce acne. Originally used as an absorbent in the wool industry this ingredient is now greatly used in many skin care products. Multhani Mitty also helps to enhance the color and tone of the skin. But this can only be caused by the continued use of Multhani Mitty.

Multhani Mitty for hair:

As a hydrating agent, Multhani Mitty helps moisturize your scalp and reduces dryness and unevenness.With the anti-bacterial and hydrating properties of Multhani Mitty regularly is effective in reducing and preventing dandruff.It brings in more antibody cells to improve the growth of skin mushrooms in your scalp and improves blood flow. Multhani Mitty absorbs all the oil that is in addition to it, giving it the hydration and nutrition it needs. Reduces the burden of bacteria on your scalp and makes you feel light.
Dry and uneven scalp is a natural skin condition for some people. Factors such as pollution and climate can worsen this. These factors may also play a role in scalp dryness. In addition, some shampoos have also been linked to dryness. From time to time, Multhani Mitty has been in the making of Hair Care Products. The hydrating nature of Multhani Mitty Powder helps moisturize your scalp and hair. It also ensures that your scalp gets enough blood flow.So it will get extra nutrients and regain the natural glow.

NOTE: If you like straight hair, you can create a hair pack with Multhani Mitty, yoghurt, white egg and some drop lemon juice.

Benefits of Multhani Mitty :
• Multhani Mitty for Oily skin: Multhani Mitty works wonders for oily skin. Oily skin easily attracts dust and other impurities from surrounding. These particles clog the skin pores and may cause pimples and eruptions on face. Multhani Mitty Powder is a blessing for such individuals. It absorbs excess oil from the skin surface and makes it soft and smooth. It avoids the occurrence of pimples caused due to excess oil secretion.

• Multhani Mitty for dry skin: Those who have dry to normal skin can use Multhani Mitty face packs by adding some milk and almond paste. Dry skins needs extra care.

• Multhani Mitty for Scrubbing: When in hurry, and no time for applying a face pack, you can use Multhani Mitty for scrubbing purpose. It will give equally glowing skin. To make this scrub use roughly grounded almonds or walnuts. if you do not wish to use these nuts, you can use some sugar granules with Multhani Mitty and scrub your face softly with this mix. Wash it off and you will see a clean, glowing skin in minutes.

• Multhani Mitty for cleaning: Multhani Mitty is a very good cleanser. It cleanses on the surface as well as deeper action. It removes all the dead cells and cleanses the pores from impurities.

• Multhani Mitty for Toning: It helps in improving the skin tone and gives a bright glow and radiance on the face. Multhani Mitty’s bleaching effect helps in lightening the blemishes and acne marks too.

• Multhani Mitty for blemishes and pimple/ Acne marks: Multhani Mitty can be used for removing pimple marks and blemishes to have an even tone. To make an anti blemish and anti mark pack, mix Multhani Mitty with tomato juice or lemon juice and add a pinch of turmeric to it.

• Multhani Mitty for Acne and pimples: Pimple and acne problems can be relieved by applying Multhani Mitty Powder and Neem leaves paste on face. You can keep it for some time and then wash it off. If you have scars, you can add lemon juice to this paste. Applying it for a week will have noticeable effects on your face.

• Multhani Mitty for pigmentation: Multhani Mitty has anti tan properties and helps in getting rid of sun tan and ill effects of pollution on your skin.

• Multhani Mitty for skin irritation: If you have skin irritation due to acidity, allergic reaction to any cosmetic products or bleach, or red skin due to excess sun exposure, Multhani Mitty has cooling effect and will give you instant relief from skin irritation.

• Multhani Mitty as Body Wash: Multhani Mitty can be used in your natural body wash.""",60.00,50.00),
             ("Nalangu Maavu Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/beauty & face/8.jpg","""Description
              Nalangu Maavu is a herbal body wash or face wash popular in South India. It is an Ayurvedic formulation, made with natural ingredients like Indian sarsaparilla, White turmeric, Champak, Flagroot, and others. This bath powder is also used in Ayurveda as medicine, to treat skin conditions like eczema. The benefits it offers are immense, and it was everyone’s choice of a good cleanser before chemical soaps and gels came into the picture.

Benefits of using Nalangu Maavu:
• Nalangu Maavu absorbs excess oil from the skin without drying it
• It helps to restore the natural pH balance of skin
• Turmeric in the bath powder works wonders for inflammation
• Turmeric also promotes the body’s synthesis of antioxidants and slows down visible signs of aging
• Regular usage of herbal bath powder can help people with acne or pimples, by reducing oil secretion
• Using Nalangu Maavu Herbal Bath Powder on a daily basis can help reduce body odor and excessive sweating
• It acts like a toner, minimizing pores on the skin
• Nalangu Maavu Herbal Bath Powder is antifungal, anti-bacterial and anti-microbial

This product can be used for infants(babies) also!""",50.00,40.00),
              ("Orange Peel Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/beauty & face/9.jpg","""Description
Benefits of Orange Pazha Thol:
Orange Peel Tea is recommended for better digestion
This powder is a great solution for Dry Skin.
It can be used for Skin whitening & Body Odor.
It can be used on Dark Spots & Dark Circle.
It can be used for Acne, Acne Scars & Glowing skin.
It can improve your Breath if you have a bad breath.
This powder can be used as a Hair Mask.
This powder can be used for washing hair also.""",80.00,60.00),
              ("Manjistha Podi/Indian Madder Powder 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/beauty & face/10.jpg","""Description
Manjistha or Indian Madder is considered to be one of the best blood-purifying herbs. It is mainly used to break down blockages in the blood flow and remove stagnant blood.
Benefits of Manjistha Powder:
Manjistha herb can be used both internally and externally on skin for promoting skin whitening. Applying Manjistha powder along with honey or rose water (at least 2-3 times a week) helps manage acne and pimples by inhibiting the growth of acne-causing bacteria due to its antioxidant property.""",80.00,60.00),
              ],
    "Blood Purifier" : [
             ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/blood purifier/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/blood purifier/2.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/blood purifier/3.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("SPL. Amukkara Powder(SPL. Ashwagandha) 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/blood purifier/4.png","""Description
             Benefits of Ashwagandha:
• It helps to reduce level of stress and tension.
• It improves energy level.
• It supports better sleep.
• It helps to lower blood pressure and is highly effective in stopping the formation of stress induced ulcers.
• It increases haemoglobin and hair melanin.
• It stabilizes blood sugar and lowers cholesterol.
• It helps to reduce stress during a weight loss diet. When a person is stressed more Cortisol hormone is produced by the adrenal glands. Cortisol stimulates glucose production and triggers a hunger response in the brain. Ashwagandha can naturally lower cortisol levels up to 26%. It also helps to lose weight by reducing swelling in body and improving haemoglobin level.
• It is useful for any imbalance in the muscles as it reduces inflammation and strengthens muscles. It is an anabolic muscle builder. As it benefits all muscle tissue it is used as a heart tonic, uterine tonic, and lung tonic.
• It improves body immunity and strengthen body defense system. This makes this herb suitable for treating Auto-immune conditions such as neutropenia, rheumatoid and osteo arthritis, cancer and chronic connective tissue disorders.
• It gives good results in nerves related conditions such as Multiple sclerosis, Neurosis, insomnia, anxiety, and stress.
• It is used to enhance memory and lesson age-related cognitive deficits.

Benefits for Men:
• For males, Ashwagandha promotes sexual health by uplifting the mood, reducing anxiety, improving energy levels and fertility, thus supporting sexual performance.
• It has direct spermatogenic effect and helps to improve sperm count.
• It helps to alleviate asthenospermia (increasing sperm motility), oligospermia (increasing sperm count) and other sperm disorders.
• It exerts something like testosterone, influencing the seminiferous tubules.
• It promotes better sexual performance.
• It reduces impotence and promotes potency.

Benefits for Women:
• It contains phytoestrogen.
• It relieves females from menstrual imbalance.
• It stimulates secretion of breast milk in lactating mothers.
• It gives strength and cures debility when consumed post – delivery.
• It supports female reproductive system, and increases ovarian weight and folliculogenesis.""",1260.00,630),
    ],
    
    "Body building" : [
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/body building/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Amukkara Powder(SPL. Ashwagandha) 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/body building/2.png","""Description
             Benefits of Ashwagandha:
• It helps to reduce level of stress and tension.
• It improves energy level.
• It supports better sleep.
• It helps to lower blood pressure and is highly effective in stopping the formation of stress induced ulcers.
• It increases haemoglobin and hair melanin.
• It stabilizes blood sugar and lowers cholesterol.
• It helps to reduce stress during a weight loss diet. When a person is stressed more Cortisol hormone is produced by the adrenal glands. Cortisol stimulates glucose production and triggers a hunger response in the brain. Ashwagandha can naturally lower cortisol levels up to 26%. It also helps to lose weight by reducing swelling in body and improving haemoglobin level.
• It is useful for any imbalance in the muscles as it reduces inflammation and strengthens muscles. It is an anabolic muscle builder. As it benefits all muscle tissue it is used as a heart tonic, uterine tonic, and lung tonic.
• It improves body immunity and strengthen body defense system. This makes this herb suitable for treating Auto-immune conditions such as neutropenia, rheumatoid and osteo arthritis, cancer and chronic connective tissue disorders.
• It gives good results in nerves related conditions such as Multiple sclerosis, Neurosis, insomnia, anxiety, and stress.
• It is used to enhance memory and lesson age-related cognitive deficits.

Benefits for Men:
• For males, Ashwagandha promotes sexual health by uplifting the mood, reducing anxiety, improving energy levels and fertility, thus supporting sexual performance.
• It has direct spermatogenic effect and helps to improve sperm count.
• It helps to alleviate asthenospermia (increasing sperm motility), oligospermia (increasing sperm count) and other sperm disorders.
• It exerts something like testosterone, influencing the seminiferous tubules.
• It promotes better sexual performance.
• It reduces impotence and promotes potency.

Benefits for Women:
• It contains phytoestrogen.
• It relieves females from menstrual imbalance.
• It stimulates secretion of breast milk in lactating mothers.
• It gives strength and cures debility when consumed post – delivery.
• It supports female reproductive system, and increases ovarian weight and folliculogenesis.""",1260.00,630),
    ],
   "Body Heat" : [
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/body heat/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/body heat/3.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/blood purifier/3.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/body heat/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Vendhayam/Fenugreek Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/body heat/4.jpg","""Description
Benefits of Venthayam (Fenugreek):
Lowers Cholesterol

Fenugreek Seeds helps in reducing the body’s production of cholesterol, especially low-density lipo protein (LDL or bad cholesterol). The University of Michigan Health System discusses the relationship between Fenugreek Seeds and high cholesterol.

Herbal Medicine to control Diabetes and Lowers Blood Sugar Levels

4HO-Ile, an unusual amino acid, which is found only in Fenugreek Seeds, has possible anti-diabetic qualities, such as enhancing insulin secretion and increasing insulin sensitivity

One of Herbal Remedies to Aids Digestion

For those suffering from stomach ailments, eating Fenugreek Seeds can be really helpful. As it is rich in fiber and antioxidants, it helps in flushing out harmful toxins from the body and thus, aids digestion. It is an effective treatment for gastritis and indigestion. It helps prevent constipation as well as digestive problems created by stomach ulcers.

• Fenugreek Seeds is known to be an effective natural remedy for heartburn or acid reflux because the mucilage in Fenugreek Seeds assist in soothing gastrointestinal inflammation, and coats the stomach and intestinal lining.""",32.00,30.00),
            ("Kadal Paasi(Badham Pisin) 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/body heat/5.jpg","""Description
Benefits of Kadal Paasi(Badham Pisin):
It is extensively used to reduce body heat.
It is useful in reviving the menstruation cycle to its original format.
Also, it’s said that if taken with milk and sugar, Badham Pisin can help increase weight and immunity.
Way of Consumption:
Before going to bed, mix KADAL PAASI in a glass of water and allow it to change into a jelly-like substance overnight. Then in the morning, before breakfast, consume the perfectly jelly-like Badham Pisin.""",60.00,50.00),
            ("Vettiver Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/body heat/6.jpg","""Description
Benefits of Vettiver:
Vetiver water is very cooling. It helps to cure painful urination, ulcers and bad breath.

This aromatic water has a calming effect on the nerves and regular intake of this water helps in general well being and it acts as a blood purifier.

Eye burning, head ache, fever, hair care & used for bath powder.""",80.00,60.00),
            
            ],
   "Child-Birth Disorders": [
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/child disordder/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/child disordder/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Karunjeeragam Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/child disordder/3.jpg","""Description
Benefits of Karunjeeragam:
• Weight Loss diet tips: Consuming Karunjeeragam is an easy way to shed extra calories. It may be considered as one of the weight loss diet plans. It helps to make you slim without visiting to gym.

• Type 2 diabetes: Just two grams of Karunjeeragam daily could result in reduced fasting blood sugar levels, along with decreased insulin resistance, and increased beta-cell function in the pancreas.

• Epilepsy: Karunjeeragam will be effective at reducing the frequency of seizures in children who resisted conventional treatment. Karunjeeragam indeed has anti-convulsive properties.

• Protection Against Heart Attack: An extract from Karunjeeragam has been shown to possess heart-protective qualities, dampening damages associated with heart attacks and boosting overall heart health.

• Sinus problems: Karunjeeragam is effective in giving you relief from the frequent occurrence of sinusitis.

• Joint pain home remedies: It is useful in relieving of joint pains, knee pains and arthritis.

• Neck pain remedy: Solve your neck pain and cervical related pains by using Karunjeeragam.

• Sexual problems: Karunjeeragam have effective solution to get rid off from sexual weakness.

• Karunjeeragam for gynecological issues: Karunjeeragam is helpful in treating and curing of many gynecological problems such as Menstrual, Leucorrhoea, White discharge, back pain, stomach pain, etc.""",33.00,30.00),
            ("Atthi Pattai Podi/Atthi Bark Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/child disordder/4.jpg","""Description
Benefits of Atthi Bark Powder / Atthi Pattai Powder:
Atthi Pattai Powder is very good for women as it cures problems in Menstruation.

Atthi Pattai Powder is used for Swelling & Boils.

Atthi Pattai Powder cures mouth ulcers and other mouth infections.

Atthi Pattai Powder is a good remedy for Pimples and freckles.""",65.00,60.00),
            
        ],
   "Cold and Cough": [
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/child disordder/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/cold & cough/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Eucalyptus Oil 60ml","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/cold & cough/3.jpg","""Description
Benefits of Eucalyptus Oil:
It is super-effective for COVID-19. You shall mix this Oil in hot water, close yourself with a blanket and inhale the steam that arises from it.
NOTE: Add Manjal Powder for increasing the effectiveness

1. Silence a cough:

For many years, eucalyptus oil has been used to relieve coughing. Today, some over-the-counter cough medications have eucalyptus oil as one of their active ingredients. Vicks VapoRub, for example, contains about 1.2 percent eucalyptus oil along with other cough suppressant ingredients.

The popular rub is applied to the chest and throat to relieve cough symptoms from the common cold or flu.

2. Clear your chest:

Are you coughing but nothing is coming up? Eucalyptus oil can not only silence a cough, it can also help you get the mucus out of your chest.

Inhaling vapor made with the essential oil can loosen mucus so that when you do cough, it’s expelled. Using a rub containing eucalyptus oil will produce the same effect.

3. Keep the bugs away:

Mosquitoes and other biting insects carry diseases that can be dangerous to our health. Avoiding their bites is our best defense.

4. Disinfect wounds:

The Australian aborigines used eucalyptus leaves to treat wounds and prevent infection. Today the diluted oil may still be used on the skin to fight inflammation and promote healing. You can purchase creams or ointments that contain eucalyptus oil. These products may be used on minor burns or other injuries that can be treated at home.

5. Breathe easy:

Respiratory conditions such as asthma and sinusitis may be helped by inhaling steam with added eucalyptus oil. The oil reacts with mucous membranes, not only reducing mucus but helping loosen it so that you can cough it up.

It’s also possible that eucalyptus blocks asthma symptoms. On the other hand, for people who are allergic to eucalyptus, it may worsen their asthma. More research is needed to determine how eucalyptus affects people with asthma.

6. Control blood sugar:

Eucalyptus oil has potential as a treatment for diabetes. Although we don’t know much at this time, experts believe that it may play a role in lowering blood sugar in people with diabetes.

7. Soothe cold sores:

The anti-inflammatory properties of eucalyptus can ease symptoms of herpes. Applying eucalyptus oil to a cold sore may reduce pain and speed up the healing process.

You can buy over-the-counter balms and ointments for cold sores that use a blend of essential oils, including eucalyptus, as part of their active ingredient list.

9. Ease joint pain:

Research suggests that eucalyptus oil eases joint pain. In fact, many popular over-the- counter creams and ointments used to soothe pain from conditions like osteoarthritis and rheumatoid arthritis contain this essential oil.

Eucalyptus oil helps to reduce pain and inflammation associated with many conditions. It may also be helpful to people experiencing back pain or those recovering from a joint or muscle injury. Talk to your doctor about if it may be right for you.""",200.00,150.00),
            ("Trikadugu Powder/Thirikadugu Podi 100g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/cold & cough/4.jpg","""Description
About Thirikadugu Powder:
Sukku (Dry ginger), Milagu (Peppercorns) and Thippili (Long pepper) is called Thirikadugam in Tamil. The combination of these three ingredients is so very effective that it is used to treat many diseases and it is popularly known as the best Herbs combination to improve health in all aspects. In Tamilnadu, Thirikadugam is an ultimate medicine that treats a wide variety of diseases depending on how it is used. This powder can be stored in an airtight box for long use. In India, we have a very few herbal powders that are marketed for removing phlegm cough and Thirikadugu Powdaer is quite effective in it actually.

Benefits of Thirikadugu Powder:
• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Cures Indigestion
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Thirikadugu Powder:
FOR CHILDREN: Mix 3gms of Thirikadugu Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Thirikadugu Powder in either water or honey or a mixture of both and drink.""",350.00,300.00),
            ],
   "Combos":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/combo/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("Baby Care Combo 1[SET]","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/combo/2.jpg","""Description
INGREDIENTS:

1) Orasu Marundhu – 1 piece each
[Paalkayam, Kadukkai, Jathikkai, Maasakkai, Vasambu]
2) Kaadhola Karugamani – 1 piece
3) Vasambu Valayal – 1 piece
4) Pillavalathi Elai – 25 grams
5) Vasambu – 2 pieces
6) Kaasi Katti – 10 grams
7) Muligai Saampiraani – 100 grams
8) Kuliyal Podi – 50 grams
9) Vengai Paal Pottu – 1 piece
10) Javvaadhu – 6 grams
[Perfume for baby]""",800.00,550.00),
            
        ],
   "COVID-19":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/COVID-19/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/COVID-19/3.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Herbal Tea Powder/Mooligai/Muligai Thenir Podi 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/COVID-19/2.jpg","""Description
INGREDIENTS:
1.Sukku
2.Adhimadhuram
3.Sitharathai
4.Kadukkaithol
5.Manjal
6.Thippili
7.Omam
8.Krambhu
9.Milagu
The above mentioned products are completely blended in a ratio fixed by Dr.Veerababu from Chennai. It enhances your immunity levels manifold. Also, this product is found to be effective against all types of viruses. We are not telling that this is a cure for the so called “CORONA” or “COVID-19”, but this can be your first step in preventing the spread of it.

Way of Consumption:
Step-1: Mix 2 spoons of Powder in a whole glass of water.

Step-2: Boil the glass of water mixed with powder till the glass of water reduces from 300ml to 100ml. Now the decoction is ready to consume.

Let’s make INDIA a CORONA-free nation!!""",300.00,200.00),
            ("Eucalyptus Oil 60ml","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/COVID-19/5.jpg","""Description
Benefits of Eucalyptus Oil:
It is super-effective for COVID-19. You shall mix this Oil in hot water, close yourself with a blanket and inhale the steam that arises from it.
NOTE: Add Manjal Powder for increasing the effectiveness

1. Silence a cough:

For many years, eucalyptus oil has been used to relieve coughing. Today, some over-the-counter cough medications have eucalyptus oil as one of their active ingredients. Vicks VapoRub, for example, contains about 1.2 percent eucalyptus oil along with other cough suppressant ingredients.

The popular rub is applied to the chest and throat to relieve cough symptoms from the common cold or flu.

2. Clear your chest:

Are you coughing but nothing is coming up? Eucalyptus oil can not only silence a cough, it can also help you get the mucus out of your chest.

Inhaling vapor made with the essential oil can loosen mucus so that when you do cough, it’s expelled. Using a rub containing eucalyptus oil will produce the same effect.

3. Keep the bugs away:

Mosquitoes and other biting insects carry diseases that can be dangerous to our health. Avoiding their bites is our best defense.

4. Disinfect wounds:

The Australian aborigines used eucalyptus leaves to treat wounds and prevent infection. Today the diluted oil may still be used on the skin to fight inflammation and promote healing. You can purchase creams or ointments that contain eucalyptus oil. These products may be used on minor burns or other injuries that can be treated at home.

5. Breathe easy:

Respiratory conditions such as asthma and sinusitis may be helped by inhaling steam with added eucalyptus oil. The oil reacts with mucous membranes, not only reducing mucus but helping loosen it so that you can cough it up.

It’s also possible that eucalyptus blocks asthma symptoms. On the other hand, for people who are allergic to eucalyptus, it may worsen their asthma. More research is needed to determine how eucalyptus affects people with asthma.

6. Control blood sugar:

Eucalyptus oil has potential as a treatment for diabetes. Although we don’t know much at this time, experts believe that it may play a role in lowering blood sugar in people with diabetes.

7. Soothe cold sores:

The anti-inflammatory properties of eucalyptus can ease symptoms of herpes. Applying eucalyptus oil to a cold sore may reduce pain and speed up the healing process.

You can buy over-the-counter balms and ointments for cold sores that use a blend of essential oils, including eucalyptus, as part of their active ingredient list.

9. Ease joint pain:

Research suggests that eucalyptus oil eases joint pain. In fact, many popular over-the- counter creams and ointments used to soothe pain from conditions like osteoarthritis and rheumatoid arthritis contain this essential oil.

Eucalyptus oil helps to reduce pain and inflammation associated with many conditions. It may also be helpful to people experiencing back pain or those recovering from a joint or muscle injury. Talk to your doctor about if it may be right for you.""",200.00,150.00),
            ("Kabasura Kudineer Powder 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/COVID-19/4.jpg","""Description
INGREDIENTS:
• PEPPUDAL 
• NILAVEMBU 
• SEENDHILKODI 
• MALLI 
• ADHIMATHURAM 
• SUKKU (சுக்கு)
• ARATTHAI
• PERARATTHAI 
• NARUKKUMOOLAM 
• NELLI VATTHAL 
• THIPPILI 
• MARAMANJAL 
• VAALMILAGU 
The above mentioned products are completely blended in a ratio fixed by our ancestors. This product is found to be effective against all types of viruses. We are not telling that, this is a cure for the so called “CORONA” or “COVID-19”, but this can be your first step in preventing the spread of it.

Consuming Kabasura Kashaaya Podi:

Step-1: Mix 1 spoon of Powder in a whole glass of water.

Step-2: Boil the glass of water mixed with powder till the glass of water reduces as half. Now the decoction is ready to consume.

Children must drink 50 ml before going to bed, for effectiveness.
Adults must drink 100ml before going to bed, for effectiveness.

Let’s make INDIA a CORONA-free nation!!""",300.00,240),   
        ],
   "Essentials":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/3.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Herbal Tea Powder/Mooligai/Muligai Thenir Podi","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/2.jpg","""Description
INGREDIENTS:
1.Sukku
2.Adhimadhuram
3.Sitharathai
4.Kadukkaithol
5.Manjal
6.Thippili
7.Omam
8.Krambhu
9.Milagu
The above mentioned products are completely blended in a ratio fixed by Dr.Veerababu from Chennai. It enhances your immunity levels manifold. Also, this product is found to be effective against all types of viruses. We are not telling that this is a cure for the so called “CORONA” or “COVID-19”, but this can be your first step in preventing the spread of it.

Way of Consumption:
Step-1: Mix 2 spoons of Powder in a whole glass of water.

Step-2: Boil the glass of water mixed with powder till the glass of water reduces from 300ml to 100ml. Now the decoction is ready to consume.

Let’s make INDIA a CORONA-free nation!!""",300.00,200.00),
            ("Eucalyptus Oil 60ml","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/6.jpg","""Description
Benefits of Eucalyptus Oil:
It is super-effective for COVID-19. You shall mix this Oil in hot water, close yourself with a blanket and inhale the steam that arises from it.
NOTE: Add Manjal Powder for increasing the effectiveness

1. Silence a cough:

For many years, eucalyptus oil has been used to relieve coughing. Today, some over-the-counter cough medications have eucalyptus oil as one of their active ingredients. Vicks VapoRub, for example, contains about 1.2 percent eucalyptus oil along with other cough suppressant ingredients.

The popular rub is applied to the chest and throat to relieve cough symptoms from the common cold or flu.

2. Clear your chest:

Are you coughing but nothing is coming up? Eucalyptus oil can not only silence a cough, it can also help you get the mucus out of your chest.

Inhaling vapor made with the essential oil can loosen mucus so that when you do cough, it’s expelled. Using a rub containing eucalyptus oil will produce the same effect.

3. Keep the bugs away:

Mosquitoes and other biting insects carry diseases that can be dangerous to our health. Avoiding their bites is our best defense.

4. Disinfect wounds:

The Australian aborigines used eucalyptus leaves to treat wounds and prevent infection. Today the diluted oil may still be used on the skin to fight inflammation and promote healing. You can purchase creams or ointments that contain eucalyptus oil. These products may be used on minor burns or other injuries that can be treated at home.

5. Breathe easy:

Respiratory conditions such as asthma and sinusitis may be helped by inhaling steam with added eucalyptus oil. The oil reacts with mucous membranes, not only reducing mucus but helping loosen it so that you can cough it up.

It’s also possible that eucalyptus blocks asthma symptoms. On the other hand, for people who are allergic to eucalyptus, it may worsen their asthma. More research is needed to determine how eucalyptus affects people with asthma.

6. Control blood sugar:

Eucalyptus oil has potential as a treatment for diabetes. Although we don’t know much at this time, experts believe that it may play a role in lowering blood sugar in people with diabetes.

7. Soothe cold sores:

The anti-inflammatory properties of eucalyptus can ease symptoms of herpes. Applying eucalyptus oil to a cold sore may reduce pain and speed up the healing process.

You can buy over-the-counter balms and ointments for cold sores that use a blend of essential oils, including eucalyptus, as part of their active ingredient list.

9. Ease joint pain:

Research suggests that eucalyptus oil eases joint pain. In fact, many popular over-the- counter creams and ointments used to soothe pain from conditions like osteoarthritis and rheumatoid arthritis contain this essential oil.

Eucalyptus oil helps to reduce pain and inflammation associated with many conditions. It may also be helpful to people experiencing back pain or those recovering from a joint or muscle injury. Talk to your doctor about if it may be right for you.""",200.00,150.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/4.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("Herbal Hairwash/Shikakai/Seeyakkai Powder 50g Each","C:/Users/shiv shanker/OneDrive\Desktop/all image paths/essential/7.jpg","""Description
             Description
Benefits of Herbal Hairwash:
Imparts Shine and Softness To Hair:
The essential nutrients and natural ingredients present in the powder is extremely beneficial in improving the texture of hair in winter. Being a natural surfactant, it cleanses the hair follicles, removes greasiness and makes the hair softer and shinier.
Boil 2-3 tbsp of the powder in 2 cups of water, to make a semi-liquid paste. Add some more water. Apply this paste and rinse your hair with water. Try this remedy twice a week to flaunt gorgeous shiny hair.

Removes Hair Lice and Dandruff:
Much to our respite, the potent antifungal and anti-microbial property of the powder plays a key role in removing dandruff and lice from the scalp and hair respectively. It effectively removes dandruff but does not strip away the essential oils from the scalp, hence preventing dry scalp problems which ultimately causes flaking and dandruff.

Boil the powder in water. Filter and squeeze half a lemon in it. Wash your hair regularly with this water to get relief from dandruff and lice.

Provides Stronger and Thicker Hair:
All of us wish to have a healthy, lustrous and strong mane. The active ingredients of the powder provides the essential oils and vitamins necessary for hair growth. It holds high significance in regaining the lustre and length of hair. It strengthens the hair from roots, prevents split ends, breakage and hair fall.
Make a paste of the powder with fresh yoghurt and apply to your hair and scalp. Allow it to remain for 20-30 minutes and rinse with cold water. Regular usage provides stronger and thicker mane.

Heals Infections:
The Herbal Hairwash Powder has a calming and soothing effect due to its potent medicinal properties. Unlike chemical shampoos, which may cause irritation on the inflamed or sensitive scalp, Shikakai provides a cooling effect and subdues the pain.
Apply a paste of slightly air-roasted herbal hairwash powder, neem leaves and turmeric on cuts, wounds, scratches or throbbing headache to get relief from inflammation and pain.

Slows Greying:
Grey hairs are quite depressing as it gives away your age and these days, many youngsters are suffering from premature greying. This powder not only prevents premature greying but also retains the natural youthfulness of black hair.
Apply a hair pack containing this powder, amla powder and soap nut on your hair once a week to get marked results.""",80.00,60.00),
            ("SPL. Amukkara Powder(SPL. Ashwagandha) 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/5.png","""Description
             Benefits of Ashwagandha:
• It helps to reduce level of stress and tension.
• It improves energy level.
• It supports better sleep.
• It helps to lower blood pressure and is highly effective in stopping the formation of stress induced ulcers.
• It increases haemoglobin and hair melanin.
• It stabilizes blood sugar and lowers cholesterol.
• It helps to reduce stress during a weight loss diet. When a person is stressed more Cortisol hormone is produced by the adrenal glands. Cortisol stimulates glucose production and triggers a hunger response in the brain. Ashwagandha can naturally lower cortisol levels up to 26%. It also helps to lose weight by reducing swelling in body and improving haemoglobin level.
• It is useful for any imbalance in the muscles as it reduces inflammation and strengthens muscles. It is an anabolic muscle builder. As it benefits all muscle tissue it is used as a heart tonic, uterine tonic, and lung tonic.
• It improves body immunity and strengthen body defense system. This makes this herb suitable for treating Auto-immune conditions such as neutropenia, rheumatoid and osteo arthritis, cancer and chronic connective tissue disorders.
• It gives good results in nerves related conditions such as Multiple sclerosis, Neurosis, insomnia, anxiety, and stress.
• It is used to enhance memory and lesson age-related cognitive deficits.

Benefits for Men:
• For males, Ashwagandha promotes sexual health by uplifting the mood, reducing anxiety, improving energy levels and fertility, thus supporting sexual performance.
• It has direct spermatogenic effect and helps to improve sperm count.
• It helps to alleviate asthenospermia (increasing sperm motility), oligospermia (increasing sperm count) and other sperm disorders.
• It exerts something like testosterone, influencing the seminiferous tubules.
• It promotes better sexual performance.
• It reduces impotence and promotes potency.

Benefits for Women:
• It contains phytoestrogen.
• It relieves females from menstrual imbalance.
• It stimulates secretion of breast milk in lactating mothers.
• It gives strength and cures debility when consumed post – delivery.
• It supports female reproductive system, and increases ovarian weight and folliculogenesis.""",1260.00,630.00),
            ("Multhani Mitty Powder 100g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/8.jpg","""Description
About Multhani Mitty:

Multhani Mitty is a clay substance that is hugely popular for its healing property against acne and blemishes. It is very rich in magnesium chloride which helps to reduce acne. Originally used as an absorbent in the wool industry this ingredient is now greatly used in many skin care products. Multhani Mitty also helps to enhance the color and tone of the skin. But this can only be caused by the continued use of Multhani Mitty.

Multhani Mitty for hair:

As a hydrating agent, Multhani Mitty helps moisturize your scalp and reduces dryness and unevenness.With the anti-bacterial and hydrating properties of Multhani Mitty regularly is effective in reducing and preventing dandruff.It brings in more antibody cells to improve the growth of skin mushrooms in your scalp and improves blood flow. Multhani Mitty absorbs all the oil that is in addition to it, giving it the hydration and nutrition it needs. Reduces the burden of bacteria on your scalp and makes you feel light.
Dry and uneven scalp is a natural skin condition for some people. Factors such as pollution and climate can worsen this. These factors may also play a role in scalp dryness. In addition, some shampoos have also been linked to dryness. From time to time, Multhani Mitty has been in the making of Hair Care Products. The hydrating nature of Multhani Mitty Powder helps moisturize your scalp and hair. It also ensures that your scalp gets enough blood flow.So it will get extra nutrients and regain the natural glow.

NOTE: If you like straight hair, you can create a hair pack with Multhani Mitty, yoghurt, white egg and some drop lemon juice.

Benefits of Multhani Mitty :
• Multhani Mitty for Oily skin: Multhani Mitty works wonders for oily skin. Oily skin easily attracts dust and other impurities from surrounding. These particles clog the skin pores and may cause pimples and eruptions on face. Multhani Mitty Powder is a blessing for such individuals. It absorbs excess oil from the skin surface and makes it soft and smooth. It avoids the occurrence of pimples caused due to excess oil secretion.

• Multhani Mitty for dry skin: Those who have dry to normal skin can use Multhani Mitty face packs by adding some milk and almond paste. Dry skins needs extra care.

• Multhani Mitty for Scrubbing: When in hurry, and no time for applying a face pack, you can use Multhani Mitty for scrubbing purpose. It will give equally glowing skin. To make this scrub use roughly grounded almonds or walnuts. if you do not wish to use these nuts, you can use some sugar granules with Multhani Mitty and scrub your face softly with this mix. Wash it off and you will see a clean, glowing skin in minutes.

• Multhani Mitty for cleaning: Multhani Mitty is a very good cleanser. It cleanses on the surface as well as deeper action. It removes all the dead cells and cleanses the pores from impurities.

• Multhani Mitty for Toning: It helps in improving the skin tone and gives a bright glow and radiance on the face. Multhani Mitty’s bleaching effect helps in lightening the blemishes and acne marks too.

• Multhani Mitty for blemishes and pimple/ Acne marks: Multhani Mitty can be used for removing pimple marks and blemishes to have an even tone. To make an anti blemish and anti mark pack, mix Multhani Mitty with tomato juice or lemon juice and add a pinch of turmeric to it.

• Multhani Mitty for Acne and pimples: Pimple and acne problems can be relieved by applying Multhani Mitty Powder and Neem leaves paste on face. You can keep it for some time and then wash it off. If you have scars, you can add lemon juice to this paste. Applying it for a week will have noticeable effects on your face.

• Multhani Mitty for pigmentation: Multhani Mitty has anti tan properties and helps in getting rid of sun tan and ill effects of pollution on your skin.

• Multhani Mitty for skin irritation: If you have skin irritation due to acidity, allergic reaction to any cosmetic products or bleach, or red skin due to excess sun exposure, Multhani Mitty has cooling effect and will give you instant relief from skin irritation.

• Multhani Mitty as Body Wash: Multhani Mitty can be used in your natural body wash.""",60.00,50.00),
            ("Manjal/Turmeric Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/9.jpg","""Description
Benefits of Manjal Podi(Virali Manjal Powder):
• Manjal Podi is used as blood purifier and it is used in the treatment of atherosclerosis, it is used to remove accumulation in the blood vessels and used to remove toxins from the body.

• It is used in the treatment of diabetes. Turmeric herb is very effective herb that is used in the treatment of diabetes.

• Being anti-inflammatory this herb is used to reduce inflammation and used in the treatment of bone related disorders.

• Being a stimulant it is used to stimulate digestive fire and it is used as stomach tonic and used in various ailments associated with digestive system.

• Externally its paste is used for wound healing and it is also helpful to rejuvenate skin tone. It is used to heal sores and also used in various cosmetics.

• It is anti-bacterial and anti-oxidant in nature and used to cure various body disorders.

• Externally its paste is used in the treatment of acne and pimples. It is also beneficial to treat anaemia.

• It is main home remedy to cure common cold and cough.""",40.00,30.00),
            ("Kadukkai Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/10.jpg","""Description
Benefits of Kadukkai:
Weight loss: Kadukkai is known to remove toxins from the body and keeps the digestive system in peak order. It prevents bloating sensation, acidity and helps in proper assimilation of food. Kadukkai is a natural blood purifier and it helps to remove the toxins in the body. Consuming Kadukkai will regulate hunger and combined together with a sensible diet and exercise will aid in weight loss naturally.

Cough in infants and adults: Kadukkai is amazing for treating cough in both adults and infants.

Constipation: Kadukkai powder is a natural laxative that is available to us. Many suffer from constipation and take medicines for it continuously. Having a traditional diet that is rich in fiber and using natural laxatives like Kadukkai podi / powder will keep our bowels in good health.

Acidity: Kadukkai is known to cure all stomach related problems from acidity and indigestion to constipation very effectively. Kadukkai increases the mucus production in the stomach forming a protective barrier thus preventing acidity and ulcer.

Diabetes: Kadukkai decreases insulin sensitivity and helps to regulate the blood sugar levels in the body effectively. The interesting thing was many of the diabetic medicines had some side effects along with regulating the blood sugar levels whereas Kadukkai did not have any side effects at all. But diabetic patients should consult a medical professional before taking kadukkai daily on a regular basis.

Hair loss: In certain parts of India, Kadukkai oil is used on the hair to prevent lice infection and dandruff. They use it as a daily application hair oil.

Skin allergies: Kadukkai effectively treats skin allergies in the ears caused by earrings. Gold and silver earrings doesn’t produce any allergies. if we wear these earrings for longer duration, the earlobes turn itchy, red and swollen. Usually it gives good relief from pain and swellings due to allergies.

Mouth ulcers: Kadukkai has anti cariogenic properties and can be used for most of the dental problems especially mouth ulcers and bleeding gums.

Consuming Kadukkai Podi:
Mix a teaspoon of Kadukkai powder in either hot water or honey and consume before going to bed.""",65.00,50.00),
            ("Karisalankanni/Karisilankanni Oil [For Hair]90g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/11.png","""Description
This oil comes from a plant known in English as “false daisy.” The herb is in the sunflower family and grows best in moist places including Thailand, India, and Brazil.

Preparation:
STEP-1: Equal quantities of nallennai, cow’s milk and the powder are taken.

STEP-2: The leaves of Karisalankanni plant are grinded in a mixer.

STEP-3: Nallennai and cow’s milk are added to the powder acheived.

STEP-4: Boiling the three(கரிசிலாங்கண்ணி(Karisalankanni), நல்லெண்ணெய்(Nallennai), பசும்பால்(Cow’s milk)) for 20 minutes in a stove. Thus, Karisalankanni oil is prepared.

As there will be a bad smell coming from the oil, we mix some amount of carrier oil to it.

Benefits:
Hair growth:

Karisalankanni contains vitamin E, which is known to fight free radicals that can impede hair growth.

Dandruff reduction:

Karisalankanni oil has antimicrobial and antifungal properties that can help reduce dandruff. The oil also has anti-inflammatory properties, which can help psoriasis or other skin irritations on the scalp. It is also said to improve circulation to the scalp.

Slows graying:

Karisalankanni oil slows the graying process. Gray hair is also commonly understood as a loss of pigment. The darkening properties of Karisalankanni may help hair appear less gray.

Application:
Gently, apply the oil on your hair. Applying the oil directly on the scalps is recommended for quick effectiveness.

Frequency of usage:

You may use it 3 days once as the product will be very pure. Apply it deep on the scalps at night, and morning wash your hair!""",350.00,300),
            ("Trikadugu Powder/Thirikadugu Podi","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/12.jpg","""Description
About Thirikadugu Powder:
Sukku (Dry ginger), Milagu (Peppercorns) and Thippili (Long pepper) is called Thirikadugam in Tamil. The combination of these three ingredients is so very effective that it is used to treat many diseases and it is popularly known as the best Herbs combination to improve health in all aspects. In Tamilnadu, Thirikadugam is an ultimate medicine that treats a wide variety of diseases depending on how it is used. This powder can be stored in an airtight box for long use. In India, we have a very few herbal powders that are marketed for removing phlegm cough and Thirikadugu Powdaer is quite effective in it actually.

Benefits of Thirikadugu Powder:
• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Cures Indigestion
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Thirikadugu Powder:
FOR CHILDREN: Mix 3gms of Thirikadugu Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Thirikadugu Powder in either water or honey or a mixture of both and drink.""",350.00,300.00),
            ("Kadal Paasi(Badham Pisin) 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/13.jpg","""Description
Benefits of Kadal Paasi(Badham Pisin):
It is extensively used to reduce body heat.
It is useful in reviving the menstruation cycle to its original format.
Also, it’s said that if taken with milk and sugar, Badham Pisin can help increase weight and immunity.
Way of Consumption:
Before going to bed, mix KADAL PAASI in a glass of water and allow it to change into a jelly-like substance overnight. Then in the morning, before breakfast, consume the perfectly jelly-like Badham Pisin.""",60.00,50.00),
            ("Vettiver Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/body heat/6.jpg","""Description
Benefits of Vettiver:
Vetiver water is very cooling. It helps to cure painful urination, ulcers and bad breath.

This aromatic water has a calming effect on the nerves and regular intake of this water helps in general well being and it acts as a blood purifier.

Eye burning, head ache, fever, hair care & used for bath powder.""",80.00,60.00),
            ("Herbal Bath/Kuliyal Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/14.jpg","""Description
INGREDIENTS:
Curcuma zedoaria.Rosc
Psoralea corylifolia.Linn
Hydnocarpus laurifolia sleumer
Wood of Tefranthra.Roxb
Alkanna Tinctoria (L)
Vetriveria Zizanioides.Linn
Crossandra intundibuliformis
Curcuma aromatica.salisb
Cyperus notundus,Linn.
Aquilaria agallocha Roxb
Cedrus deodara.G.Don
Parmotrema Perlatum
Santalum Album
Boswellia serrata.Roxb
Bergenia Ligulata
Salix caprea.Linn
Eradicates:

Scabies
Itching
Phrynoderma
Scar
Melanoderma
Fungal skin diseases
Pimples
Black spots
Bad odour
If used for babies:

Baby’s Skin Stays Clean
It Softens the Skin
It evens Out Skin Tone
It reduces Risk of Infection
It maintain the pH levels in your baby’s skin
It Gives You Time to Bond with your Baby
Better Hand Eye Coordination and Visual Tracking
It Helps your Baby Relax
It Develops Cognitive skills""",80.00,60.00),
            ("Nilavembu Powder 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/15.jpg","""Description
Benefits of Nilavembu
Looking for natural ways to boost immunity? Nilavembu is a herbal remedy that will do you good. It is a medicinal herb that treats all diseases.  Here are some benefits that its medicine offers.

• Reduces Risks of Diabetes, Arthritis, Liver Diseases and Cancer
• Reduces Risks of all kinds of fever
• Treats Arthritis
• Treats Skin Problems
• Good For Digestion
• Prevents ulcers
• Reduces risks of heart problems
• Reduces risks of respiratory problems
• Natural Immunity booster

NOTE: The Tamil Nadu government had distributed Nilavembu(Kashayam) to treat people infected with dengue during the outbreak in 2017.""",55.00,50.00),
            ("Mooligai Sambrani/Muligai Saampirani Set 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/16.jpg","""Description
SAMBRANI HEALTH BENEFITS
• Sambrani has a unique beautiful fragrance that is different from the normal incense sticks. The smell of sambrani transports back in time and somehow fills a person with peace and happiness. Even Ayurveda advises to use sambrani, as it calms the nerves, and produces tranquility, thus making the person ready for prayers.
• Women after having their hair washed, light up sambrani to dry it very quickly and also leave a beautiful fragrant smell in their hair. During winter months, if we use sambrani, we will not get a headache, especially if we have long, thick hair.
• Sambrani is also used for babies, after children have their bath, sambrani is lit and brought in that room. This prevents them from catching a cold but make sure not to bring the smoke too near the babies, as it will make their lungs delicate. No auspicious day is complete without sambrani, sambrani is always lit during our prayers and rituals.
• Regularly light up sambrani every morning, take it to every room in the house. This wards off mosquitoes and cleanses the whole place.
• To remove stale and negative energy, calm down anxiety, depression, and for a fresh smelling home.
• Light up sambrani at least weekly once and fill the whole house with the smoke. It will make the whole house smell divine.
• Even for headaches, sambrani smoke is very good.
• Purification of the air
• No auspicious day is completed without sambrani; sambrani is always lit during prayers and rituals. Lighting up of sambrani once in a day, makes us feel that we have followed proper rituals and cultures.
• This Traditional way of Lighting of Sambrani keeps the rooms spiritually strong and produces positive vibrates and also keeps away from mosquitoes.
• Medicated smoke has an important role in Ayurveda. It can be used to fumigate a room or it can carry to an individual the essence of herbs. Incense thus has healing properties. The smoke with its gandha or aroma activates the nasal system and through it makes changes in the body and mind of the person.
• Manage pain
• Improve sleep quality
• Reduce stress, agitation, and anxiety
• Soothe sore joints
• Treat headaches and migraines
• Ease discomforts
• Fight bacteria, virus, or fungus
• Improve digestion
• Improve hospice and palliative care
• Boost immunity""",140.00,120.00),
            ("Luffa/Ridge Gourd Scrub 1 piece","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/essential/17.jpg","""Description
Usage:
The sponge becomes more pliant when it is soaked in water. As such, it is considered a natural way to exfoliate dead skin cells. Its fibrous texture gently exfoliates the skin without scratching it or causing chemical-induced irritation, removing dead skin cells that can build up on the surface of the skin and make it look dull or rough and letting the healthy skin underneath breathe and absorb any moisturizers you apply to it.""",60.00,50.00),
            ],
    "Fever":[
             ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/fever/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/fever/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Trikadugu Powder/Thirikadugu Podi","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/fever/4.jpg","""Description
About Thirikadugu Powder:
Sukku (Dry ginger), Milagu (Peppercorns) and Thippili (Long pepper) is called Thirikadugam in Tamil. The combination of these three ingredients is so very effective that it is used to treat many diseases and it is popularly known as the best Herbs combination to improve health in all aspects. In Tamilnadu, Thirikadugam is an ultimate medicine that treats a wide variety of diseases depending on how it is used. This powder can be stored in an airtight box for long use. In India, we have a very few herbal powders that are marketed for removing phlegm cough and Thirikadugu Powdaer is quite effective in it actually.

Benefits of Thirikadugu Powder:
• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Cures Indigestion
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Thirikadugu Powder:
FOR CHILDREN: Mix 3gms of Thirikadugu Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Thirikadugu Powder in either water or honey or a mixture of both and drink.""",350.00,300.00),
            ("Kabasura Kudineer Powder","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/fever/3.jpg","""Description
INGREDIENTS:
• PEPPUDAL 
• NILAVEMBU 
• SEENDHILKODI 
• MALLI 
• ADHIMATHURAM 
• SUKKU (சுக்கு)
• ARATTHAI
• PERARATTHAI 
• NARUKKUMOOLAM 
• NELLI VATTHAL 
• THIPPILI 
• MARAMANJAL 
• VAALMILAGU 
The above mentioned products are completely blended in a ratio fixed by our ancestors. This product is found to be effective against all types of viruses. We are not telling that, this is a cure for the so called “CORONA” or “COVID-19”, but this can be your first step in preventing the spread of it.

Consuming Kabasura Kashaaya Podi:

Step-1: Mix 1 spoon of Powder in a whole glass of water.

Step-2: Boil the glass of water mixed with powder till the glass of water reduces as half. Now the decoction is ready to consume.

Children must drink 50 ml before going to bed, for effectiveness.
Adults must drink 100ml before going to bed, for effectiveness.

Let’s make INDIA a CORONA-free nation!!""",300.00,240),
        ],
    "Hair Problems":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/hair problems/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/hair problems/3.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("Karisalankanni/Karisilankanni Oil [For Hair]90g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/hair problems/6.png","""Description
This oil comes from a plant known in English as “false daisy.” The herb is in the sunflower family and grows best in moist places including Thailand, India, and Brazil.

Preparation:
STEP-1: Equal quantities of nallennai, cow’s milk and the powder are taken.

STEP-2: The leaves of Karisalankanni plant are grinded in a mixer.

STEP-3: Nallennai and cow’s milk are added to the powder acheived.

STEP-4: Boiling the three(கரிசிலாங்கண்ணி(Karisalankanni), நல்லெண்ணெய்(Nallennai), பசும்பால்(Cow’s milk)) for 20 minutes in a stove. Thus, Karisalankanni oil is prepared.

As there will be a bad smell coming from the oil, we mix some amount of carrier oil to it.

Benefits:
Hair growth:

Karisalankanni contains vitamin E, which is known to fight free radicals that can impede hair growth.

Dandruff reduction:

Karisalankanni oil has antimicrobial and antifungal properties that can help reduce dandruff. The oil also has anti-inflammatory properties, which can help psoriasis or other skin irritations on the scalp. It is also said to improve circulation to the scalp.

Slows graying:

Karisalankanni oil slows the graying process. Gray hair is also commonly understood as a loss of pigment. The darkening properties of Karisalankanni may help hair appear less gray.

Application:
Gently, apply the oil on your hair. Applying the oil directly on the scalps is recommended for quick effectiveness.

Frequency of usage:

You may use it 3 days once as the product will be very pure. Apply it deep on the scalps at night, and morning wash your hair!""",350.00,300),
            ("Herbal Hairwash/Shikakai/Seeyakkai Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/hair problems/7.jpg","""Description
             Description
Benefits of Herbal Hairwash:
Imparts Shine and Softness To Hair:
The essential nutrients and natural ingredients present in the powder is extremely beneficial in improving the texture of hair in winter. Being a natural surfactant, it cleanses the hair follicles, removes greasiness and makes the hair softer and shinier.
Boil 2-3 tbsp of the powder in 2 cups of water, to make a semi-liquid paste. Add some more water. Apply this paste and rinse your hair with water. Try this remedy twice a week to flaunt gorgeous shiny hair.

Removes Hair Lice and Dandruff:
Much to our respite, the potent antifungal and anti-microbial property of the powder plays a key role in removing dandruff and lice from the scalp and hair respectively. It effectively removes dandruff but does not strip away the essential oils from the scalp, hence preventing dry scalp problems which ultimately causes flaking and dandruff.

Boil the powder in water. Filter and squeeze half a lemon in it. Wash your hair regularly with this water to get relief from dandruff and lice.

Provides Stronger and Thicker Hair:
All of us wish to have a healthy, lustrous and strong mane. The active ingredients of the powder provides the essential oils and vitamins necessary for hair growth. It holds high significance in regaining the lustre and length of hair. It strengthens the hair from roots, prevents split ends, breakage and hair fall.
Make a paste of the powder with fresh yoghurt and apply to your hair and scalp. Allow it to remain for 20-30 minutes and rinse with cold water. Regular usage provides stronger and thicker mane.

Heals Infections:
The Herbal Hairwash Powder has a calming and soothing effect due to its potent medicinal properties. Unlike chemical shampoos, which may cause irritation on the inflamed or sensitive scalp, Shikakai provides a cooling effect and subdues the pain.
Apply a paste of slightly air-roasted herbal hairwash powder, neem leaves and turmeric on cuts, wounds, scratches or throbbing headache to get relief from inflammation and pain.

Slows Greying:
Grey hairs are quite depressing as it gives away your age and these days, many youngsters are suffering from premature greying. This powder not only prevents premature greying but also retains the natural youthfulness of black hair.
Apply a hair pack containing this powder, amla powder and soap nut on your hair once a week to get marked results.""",80.00,60.00),
            ("Bitter Apple/Kumattikkaai 1 PIECE","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/hair problems/2.png","""Description
Benefits of Bitter Apple/Kumattikkaai:
Good for Hair.
Kills all intestinal worms.
Some people experience premature greying of hair at a very young age, giving them an aged appearance and causing emotional distress.

For some, side effects of medications taken for other health conditions can lead to hair turning grey or white.

Others, in the name of fashion and modern trends, apply artificial colors like red or green to their hair. These chemical dyes damage the natural black pigment of the hair, causing it to lose its original color and become grey.

To protect the hair from such damage, to restore its natural black color, and to reduce hair fall, Thummatti Kaaygal (fruit of the Thummatti plant) is highly beneficial.""",80.00,60.00),
            ("Karisalankanni/Karisilankanni Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/hair problems/4.jpg","""Description
Benefits of Karisalankanni:
•It is used for lowers Cholesterol and Trigs, Cardiovascular Disease.
•Karisalankanni also increases blood flow to the coronary arteries, Antimicrobial.
•Karisalankanni is a great antibacterial agent that kills E Coli and Staph infections.
•It helps people with Lower Blood Glucose level in blood.
•It is used widely for treating liver disorders.
•It used for Cold, Cough, Asthma, Jaundice and Sinus Infection.

Karisalanganni for Hair:
If you want Black hair for a long time. We suggest this product to you . If the oil made with this powder is applied on your scalps regularly your hair won’t be turning white, there will be no hairfall problems and your hair will be way stronger than before.

Making oil with Karisalankanni Powder:

STEP-1: Take equal quantities of nallennai, cow’s milk and the powder.

STEP-2: Grind the powder in a Mixer and add nallennai and cow’s milk.

STEP-3: Now, boil the three(Karisalankanni, Nallennai, Cow’s milk) for 20 minutes. Thus, Karisalankanni oil is prepared.""",27.00,25.00),
            ("Avuri Ilai Podi/Avuri Leaves Powder 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/hair problems/5.jpg","""Description
Benefits of Avuri:
• Digestive system:
It relieves constipation, useful in rheumatoid arthritis, ascites, splenomegaly, liver disorders. It is a very good liver tonic.

• Respiratory system:
It is useful in cough, cold, bronchitis, rhinitis, asthma.

• Musculo-skeletal system:
Useful in gout, rheumatoid arthritis, osteo-arthritis. Relieves pain and inflammation of joints, improves flexibility.

• Hair care:
Used to relieve grey hairs and to promote hair growth. The dry powder doesn ‘t turn blue since it is from dry extracts of plant and free from coloring agents.

• Insect bites and skin disorders:
Leaf paste is applied externally to heal wound quickly, also useful in case of insect bites and skin disorders with itching. It is also used in treating scorpion bite.

• Use in rabies:
The leaf paste is applied over the dog bite site.""",25.00,20.00),
            ("Usila Leaves Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/hair problems/8.jpg","""Description
Benefits of Usilai Podi:
Usilai Podi makes hair grow black, shiny and silky and it serves to cool down the body. Its aroma stays in the hair for 4-5 days and there is therapeutic by keeping the body and mind stress-free, cool and relaxed.

Usilai Podi prevents hair problems, controls hair loss and controls body heat""",50.00,40.00),
            ("Boondhikottai/Soapnut 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/hair problems/9.png","""Description
Benefits of Soapnut:
The fruit is collected during winter months for seed and or sale in the market as soap nut. 
Dried fruit is most valuable part of the plant. Its fleshy portion consists of saponin, which is actually a good replacement for washing soap and is also used in making quality shampoos, detergents, etc. 
In fact the skin of the fruit is extremely appreciated by the rural folks as a natural produced shampoo for washing their hair. They also use these for cleaning woolen clothes.""",140.00,120.00),
    ],
    "Hair Removal":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/hair removal/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("Mirtharsing/Mirdharsing 10g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/hair removal/2.jpeg","""Description
Benefits:
Very useful for ladies of all age groups to remove unwanted hair at undesirable/unwanted places. 
Ensures your skin is soft and shiny with absolutely no hair. 
Steps of usage: 

Step-1: Take a brush. 

Step-2: Dip the brush in water. 

Step-3: Rub the brush on Mirdarsing stone. 

Step-4: Apply(rub) it at the parts where there is unwanted hair. 

Apply this with caution, it may cause irritation if applied to sensitive parts such as eyes, mouth etc..

And never consume it, internal consumption of the product may cause other problems!""",100.00,80.00),
        ],
    "Head Ache":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/head ache/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/head ache/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Eucalyptus Oil 60ml","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/head ache/4.jpg","""Description
Benefits of Eucalyptus Oil:
It is super-effective for COVID-19. You shall mix this Oil in hot water, close yourself with a blanket and inhale the steam that arises from it.
NOTE: Add Manjal Powder for increasing the effectiveness

1. Silence a cough:

For many years, eucalyptus oil has been used to relieve coughing. Today, some over-the-counter cough medications have eucalyptus oil as one of their active ingredients. Vicks VapoRub, for example, contains about 1.2 percent eucalyptus oil along with other cough suppressant ingredients.

The popular rub is applied to the chest and throat to relieve cough symptoms from the common cold or flu.

2. Clear your chest:

Are you coughing but nothing is coming up? Eucalyptus oil can not only silence a cough, it can also help you get the mucus out of your chest.

Inhaling vapor made with the essential oil can loosen mucus so that when you do cough, it’s expelled. Using a rub containing eucalyptus oil will produce the same effect.

3. Keep the bugs away:

Mosquitoes and other biting insects carry diseases that can be dangerous to our health. Avoiding their bites is our best defense.

4. Disinfect wounds:

The Australian aborigines used eucalyptus leaves to treat wounds and prevent infection. Today the diluted oil may still be used on the skin to fight inflammation and promote healing. You can purchase creams or ointments that contain eucalyptus oil. These products may be used on minor burns or other injuries that can be treated at home.

5. Breathe easy:

Respiratory conditions such as asthma and sinusitis may be helped by inhaling steam with added eucalyptus oil. The oil reacts with mucous membranes, not only reducing mucus but helping loosen it so that you can cough it up.

It’s also possible that eucalyptus blocks asthma symptoms. On the other hand, for people who are allergic to eucalyptus, it may worsen their asthma. More research is needed to determine how eucalyptus affects people with asthma.

6. Control blood sugar:

Eucalyptus oil has potential as a treatment for diabetes. Although we don’t know much at this time, experts believe that it may play a role in lowering blood sugar in people with diabetes.

7. Soothe cold sores:

The anti-inflammatory properties of eucalyptus can ease symptoms of herpes. Applying eucalyptus oil to a cold sore may reduce pain and speed up the healing process.

You can buy over-the-counter balms and ointments for cold sores that use a blend of essential oils, including eucalyptus, as part of their active ingredient list.

9. Ease joint pain:

Research suggests that eucalyptus oil eases joint pain. In fact, many popular over-the- counter creams and ointments used to soothe pain from conditions like osteoarthritis and rheumatoid arthritis contain this essential oil.

Eucalyptus oil helps to reduce pain and inflammation associated with many conditions. It may also be helpful to people experiencing back pain or those recovering from a joint or muscle injury. Talk to your doctor about if it may be right for you.""",200.00,150.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/head ache/3.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("Trikadugu Powder/Thirikadugu Podi","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/head ache/6.jpg","""Description
About Thirikadugu Powder:
Sukku (Dry ginger), Milagu (Peppercorns) and Thippili (Long pepper) is called Thirikadugam in Tamil. The combination of these three ingredients is so very effective that it is used to treat many diseases and it is popularly known as the best Herbs combination to improve health in all aspects. In Tamilnadu, Thirikadugam is an ultimate medicine that treats a wide variety of diseases depending on how it is used. This powder can be stored in an airtight box for long use. In India, we have a very few herbal powders that are marketed for removing phlegm cough and Thirikadugu Powdaer is quite effective in it actually.

Benefits of Thirikadugu Powder:
• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Cures Indigestion
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Thirikadugu Powder:
FOR CHILDREN: Mix 3gms of Thirikadugu Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Thirikadugu Powder in either water or honey or a mixture of both and drink.""",350.00,300.00),
            ("Paatti’s Pain Relief Thailam 10g(each)","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/head ache/5.jpg","""Description
Method of Usage:
Mix these 3 in a GLASS BOTTLE at your home:

1) Omam Salt(ஓம உப்பு)
2) Raw Soodam(பச்ச சூடம்)
3) Pudhina Salt(புதினா உப்பு) you will achieve the Thailam(Liquid) magically in 2-3 hours, which you can apply on the painful and affected areas.

It not only cures the pain, but also makes you way active.""",350.00,300.00),
            ("Pachai KarpooramRaw Camphor 10g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/head ache/7.jpg","""Description
             Raw Camphor""",80.00,60.00),
    ],
    "Heart Problems":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/heart problems/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/heart problems/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/heart problems/3.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("SPL. Amukkara Powder(SPL. Ashwagandha) 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/heart problems/4.png","""Description
             Benefits of Ashwagandha:
• It helps to reduce level of stress and tension.
• It improves energy level.
• It supports better sleep.
• It helps to lower blood pressure and is highly effective in stopping the formation of stress induced ulcers.
• It increases haemoglobin and hair melanin.
• It stabilizes blood sugar and lowers cholesterol.
• It helps to reduce stress during a weight loss diet. When a person is stressed more Cortisol hormone is produced by the adrenal glands. Cortisol stimulates glucose production and triggers a hunger response in the brain. Ashwagandha can naturally lower cortisol levels up to 26%. It also helps to lose weight by reducing swelling in body and improving haemoglobin level.
• It is useful for any imbalance in the muscles as it reduces inflammation and strengthens muscles. It is an anabolic muscle builder. As it benefits all muscle tissue it is used as a heart tonic, uterine tonic, and lung tonic.
• It improves body immunity and strengthen body defense system. This makes this herb suitable for treating Auto-immune conditions such as neutropenia, rheumatoid and osteo arthritis, cancer and chronic connective tissue disorders.
• It gives good results in nerves related conditions such as Multiple sclerosis, Neurosis, insomnia, anxiety, and stress.
• It is used to enhance memory and lesson age-related cognitive deficits.

Benefits for Men:
• For males, Ashwagandha promotes sexual health by uplifting the mood, reducing anxiety, improving energy levels and fertility, thus supporting sexual performance.
• It has direct spermatogenic effect and helps to improve sperm count.
• It helps to alleviate asthenospermia (increasing sperm motility), oligospermia (increasing sperm count) and other sperm disorders.
• It exerts something like testosterone, influencing the seminiferous tubules.
• It promotes better sexual performance.
• It reduces impotence and promotes potency.

Benefits for Women:
• It contains phytoestrogen.
• It relieves females from menstrual imbalance.
• It stimulates secretion of breast milk in lactating mothers.
• It gives strength and cures debility when consumed post – delivery.
• It supports female reproductive system, and increases ovarian weight and folliculogenesis.""",1260.00,630.00),
            ("Oridhazh Thamarai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/heart problems/5.jpg","""Description
Benefits of Oridhazh Thamarai:
• For Men: Oridhazh Thamarai has shown increase in the testosterone level in males and also has aphrodisiac properties.
• Hypolipidemic Activity: Oridhazh thamarai has cholesterol lowering properties, regular intake of Oridhazh thamarai will result in reduction of cholesterol significantly.
• Antioxidant & Anti Diabetic activity: Oridhazh thamarai has amazing anti oxidant properties which helps reduce oxidative stress very effectively. It also reduces blood sugar levels.
• For Treating Anaemia: Another important use of Oridhazh thamarai is its amazing ability to treat anaemia as the extract of Oridhazh thamarai has high amounts of iron.
• For Reducing Body Heat: The decoction of the plant is used for reducing body heat, this use is quite famous and is followed in villages. The extract also has anti allergic and pain reducing properties.""",44.00,40.00),
            ("Semparuthipoo/Sembaruthi Podi Hibiscus Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/heart problems/6.jpg","""Description
Benefits of Semparuthipoo(Hibiscus):
Controls High Blood Pressure & Cholesterol Levels

Cures Cold : Hibiscus is rich in Vitamin C and thus it has the capacity to cure cure minor cold related infections like sore throat, cough and headache.

Boosts Energy : As the antioxidants in hibiscus help to repair free radical damage, your energy levels naturally go up.

Calms Hot Flashes : Women who are going through the tough hormonal period of menopause might use the health benefits of hibiscus. Hibiscus can help soothe hot flashes.

Slows Ageing : The antioxidants in hibiscus not only help to fight cancer but also also slow down the ageing of your cells. As a result, it may be the secret to eternal youth.

Boost Immunity : One of the main health benefits of hibiscus flower is that it helps to boost the level of immunity in your body.

Maintains Fluid Balance : According to ancient sources, having hibiscus flower extracts can help to maintain the fluid balance in your body. It was once used as a cure for oedema or excess water retention in the body.

Speeds Up Metabolism : Vitamin C has a very essential place in the digestive system. And as hibiscus is rich in Vitamin C, it helps to increase the rate of metabolism.

Maintains Body Temperature : According to ancient African medicine, having hibiscus flower extracts regulates the body temperature. It helps to flush out excess body heat in summers.

Hair care : It is also used for hair growth.

Cures Acne : Hibiscus has many natural anti-inflammatory substances and also Vitamin C that can stop the growth of acne and even clear the marks left by it.""",43.00,40.00),
            ("Marutham Pattai Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/heart problems/7.jpg","""Description
Benefits of Marutham Pattai:
• Regular use this powder improves the pumping activity of heart, which makes it very useful for heart weakness and congestive heart failure.

• Marutham Pattai improves cardiac muscle strength.

• It decreases LDL cholesterol levels.

• Marutham Pattai’s ability to suppress the blood’s absorption of lipids indicates that it has cholesterol-regulating properties. Its principle constituents are sitosterol, ellagic acid and arjunic acid.

• This plant’s bark is rich in Co-enzyme Q-10 which prevents incident of heart attacks.

• This also has a tonic and diuretic effects that benefit cirrhosis of the liver.

• It induces a drug-dependent decrease in blood pressure and heart rate.

• The bark of this plant is useful as an anti-ischemic and cardioprotective agent in hypertension and in ischemic heart disease, especially in disturbed cardiac rhythm, angina or myocardial infarction.

•This helps maintain a healthy heart and reduces the effects of stress and nervousness.

• This enhances prostaglandins and lowers risk of coronary heart trouble.

• This can relieve symptomatic complaints of essential hypertension such as giddiness, insomnia, lassitude, headache and the inability to concentrate.

• In a study on the efficacy of the bark powder in treating congestive cardiac failure (CCF), over 40% of the cases showed marked improvement. CCF due to congenital anomaly of heart and valve disease was also brought under control. 4 out of 9 cases of CCF due to chronic bronchitis were also relieved by the treatment.""",60.00,50.00),
    ],
    "Herbal oils & Legiyams":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/herbal oils/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("Eucalyptus Oil 60ml","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/herbal oils/4.jpg","""Description
Benefits of Eucalyptus Oil:
It is super-effective for COVID-19. You shall mix this Oil in hot water, close yourself with a blanket and inhale the steam that arises from it.
NOTE: Add Manjal Powder for increasing the effectiveness

1. Silence a cough:

For many years, eucalyptus oil has been used to relieve coughing. Today, some over-the-counter cough medications have eucalyptus oil as one of their active ingredients. Vicks VapoRub, for example, contains about 1.2 percent eucalyptus oil along with other cough suppressant ingredients.

The popular rub is applied to the chest and throat to relieve cough symptoms from the common cold or flu.

2. Clear your chest:

Are you coughing but nothing is coming up? Eucalyptus oil can not only silence a cough, it can also help you get the mucus out of your chest.

Inhaling vapor made with the essential oil can loosen mucus so that when you do cough, it’s expelled. Using a rub containing eucalyptus oil will produce the same effect.

3. Keep the bugs away:

Mosquitoes and other biting insects carry diseases that can be dangerous to our health. Avoiding their bites is our best defense.

4. Disinfect wounds:

The Australian aborigines used eucalyptus leaves to treat wounds and prevent infection. Today the diluted oil may still be used on the skin to fight inflammation and promote healing. You can purchase creams or ointments that contain eucalyptus oil. These products may be used on minor burns or other injuries that can be treated at home.

5. Breathe easy:

Respiratory conditions such as asthma and sinusitis may be helped by inhaling steam with added eucalyptus oil. The oil reacts with mucous membranes, not only reducing mucus but helping loosen it so that you can cough it up.

It’s also possible that eucalyptus blocks asthma symptoms. On the other hand, for people who are allergic to eucalyptus, it may worsen their asthma. More research is needed to determine how eucalyptus affects people with asthma.

6. Control blood sugar:

Eucalyptus oil has potential as a treatment for diabetes. Although we don’t know much at this time, experts believe that it may play a role in lowering blood sugar in people with diabetes.

7. Soothe cold sores:

The anti-inflammatory properties of eucalyptus can ease symptoms of herpes. Applying eucalyptus oil to a cold sore may reduce pain and speed up the healing process.

You can buy over-the-counter balms and ointments for cold sores that use a blend of essential oils, including eucalyptus, as part of their active ingredient list.

9. Ease joint pain:

Research suggests that eucalyptus oil eases joint pain. In fact, many popular over-the- counter creams and ointments used to soothe pain from conditions like osteoarthritis and rheumatoid arthritis contain this essential oil.

Eucalyptus oil helps to reduce pain and inflammation associated with many conditions. It may also be helpful to people experiencing back pain or those recovering from a joint or muscle injury. Talk to your doctor about if it may be right for you.""",200.00,150.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/herbal oils/3.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("Karisalankanni/Karisilankanni Oil [For Hair]90g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/herbal oils/7.png","""Description
This oil comes from a plant known in English as “false daisy.” The herb is in the sunflower family and grows best in moist places including Thailand, India, and Brazil.

Preparation:
STEP-1: Equal quantities of nallennai, cow’s milk and the powder are taken.

STEP-2: The leaves of Karisalankanni plant are grinded in a mixer.

STEP-3: Nallennai and cow’s milk are added to the powder acheived.

STEP-4: Boiling the three(கரிசிலாங்கண்ணி(Karisalankanni), நல்லெண்ணெய்(Nallennai), பசும்பால்(Cow’s milk)) for 20 minutes in a stove. Thus, Karisalankanni oil is prepared.

As there will be a bad smell coming from the oil, we mix some amount of carrier oil to it.

Benefits:
Hair growth:

Karisalankanni contains vitamin E, which is known to fight free radicals that can impede hair growth.

Dandruff reduction:

Karisalankanni oil has antimicrobial and antifungal properties that can help reduce dandruff. The oil also has anti-inflammatory properties, which can help psoriasis or other skin irritations on the scalp. It is also said to improve circulation to the scalp.

Slows graying:

Karisalankanni oil slows the graying process. Gray hair is also commonly understood as a loss of pigment. The darkening properties of Karisalankanni may help hair appear less gray.

Application:
Gently, apply the oil on your hair. Applying the oil directly on the scalps is recommended for quick effectiveness.

Frequency of usage:

You may use it 3 days once as the product will be very pure. Apply it deep on the scalps at night, and morning wash your hair!""",350.00,300),
            ("Paatti’s Pain Relief Thailam 10g(each)","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/herbal oils/5.jpg","""Description
Method of Usage:
Mix these 3 in a GLASS BOTTLE at your home:

1) Omam Salt(ஓம உப்பு)
2) Raw Soodam(பச்ச சூடம்)
3) Pudhina Salt(புதினா உப்பு) you will achieve the Thailam(Liquid) magically in 2-3 hours, which you can apply on the painful and affected areas.

It not only cures the pain, but also makes you way active.""",350.00,300.00),
            ("Sathuragiri/Sadhuragiri Joint Pain Thailam 60g(each)","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/herbal oils/2.jpg","""Description
Benefits of Sathuragiri Mootu Vali(Joint Pain) Thailam:
Our fast-paced lifestyle tends to overwhelm our joints and muscle cells, rendering them dysfunctional. Orthoherb Oil easily penetrates the skin, delivering its medicinal properties to the muscle cells and joints in the body, making it flexible, strong and healthy.

Benefits:

Anti-inflammatory and analgesic
Lubricates joints
Imparts muscle tone and strengthens the Dhatus
Imparts firmness to limbs
Stimulates circulation
Helps the lymphatic functioning for detoxification
Joint Pain
Inflammations
Cervical & Lumbar Spondylosis
Sciatica & all types of inflammatory joint conditions
This oil provides excellent relief from joint pain. It doesn’t just stop at reducing pain — it also removes excess fluid retained in the joints that causes swelling or stiffness.

It is safe for elderly people, aged individuals, and mothers at home.
(No side effects whatsoever.)
Usage:

Step-1: Slightly HEAT this ‘THAILAM’ and apply it on the painful areas.

Step-2: Massage it a bit.

Step-3: Wash it with BEARABLE HOT WATER in the morning.""",350.00,300),
            ("Karunjeeragam Oil 50ml","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/herbal oils/6.jpg","""DescriptionDescription
Benefits of Karunjeeragam Oil:
Primarily used for massaging the penis. It is said to increase size and girth.
Reducing high blood pressure: Taking black cumin seed extract for two months has been shown to reduce high blood pressure in people whose blood pressure is mildly elevated.
Reducing high cholesterol: Taking black seed oil has been shown to reduce high cholesterol. It’s high in healthy fatty acids that can help you maintain healthier cholesterol levels. Examples of these fatty acids include linoleic acids and oleic acid. The levels of the oils can vary depending on where the black seeds are grown. People may also see results when consuming the crushed seeds.
Improving rheumatoid arthritis symptoms: Taking oral black seed oil may help to reduce inflammatory rheumatoid arthritis symptoms.
Decreasing asthma symptoms: The anti-inflammatory effects of black seed oil may extend to improving asthma symptoms. Its effect in reducing inflammation in the airways may also help with bronchitis symptoms.
Reducing stomach upset: Eating black seeds or taking black seed oil is associated with relieving stomach pain and cramps. The oil can help to reduce gas, stomach bloating, and the incidence of ulcers as well.
Black seed oil is also thought to have anticancer properties. It may help fight against skin cancers when applied topically.
Portions of black seed oil known as thymoquinone and other seed potions were able to reduce the growth of tumors in lab rats. The oil also may help to reduce the tissue damaging effects of radiation that is used to kill cancer cells. But these results haven’t been studied in humans. Black seed oil shouldn’t be used as a substitute for conventional cancer treatments.
Black seed oil beauty benefits

Black seed oil has several applications and benefits for problematic skin conditions. The oil is found in many health foods stores and pharmacies. Examples of applications for beauty and skin include:

• Acne: According to the Journal of Dermatology & Dermatologic Surgery, applying a lotion prepared with 10 percent black seed oil significantly reduced the incidence of acne after two months. Those who participated in the study reported 67 percent satisfaction.
• Hydrating hair: Black seed oil can be applied to human hair to soften it and promote shine.
• Psoriasis: Applying black seed oil has been shown to reduce the incidence of psoriasis plaques.
• Softening skin: Black seed oil has been added to oils and moisturizers to improve skin moisture and hydration.
• Wound healing: Application of black seed oil has been shown to reduce inflammation and the presence of bacteria to aid in wound healing. While it doesn’t seem to be helpful in growing new collagen fibers, it does stimulate other growth factors to help the body create new, healthy skin.""",200.00,180.00),
            ("Prasava Legiyam/Mother-Care Product 500g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/herbal oils/8.jpg","""Description
For New Moms and Pregnant Ladies, it is a tradition in Southern India to prepare a marundhu called Prasava Legiyum. This legiyam has lots of nutrition packed ingredients that helps the New Mom’s in digesting their food.

Ingredients:

1) Hiptage Madablota

2) Zingiber Officinalis

3) Aplotaxis Auriculata

4) Coriandrum Sativum

5) Abrus Precatorious

6) Phyllanthus Embelia

7) Embelia Ribes

8) Terminalia Chebula

9) Plumbago Capensis

10) Ferula Asafoetida

11) Veppalarisy

12) Cinnamomum Zeylancium

13) Caryophyllum

14) Elettaria Cardomomum

15) Zingiber Officianale

16) Piper Nigrum

17) Nigella Sativa

18) Carum Coticum

19) Sinapis Nigrae Semina

20) Piper Cubeba

21) Trigonella Foenum

22) Chevviyam

Benefits:

• Treats anemia, edema and vomiting.
• Removes Prasava alukku [removes the unwanted contents of the delivery]
• Good cure for weakness
• Cures poor secretion of mother’s milk
• Works great for disorders of vaginal tract
• Can be given for digestive disorders
• Strengthens the uterus.
• Can be used for 6 months to 1 year after delivery""",300.00,220.00),
            ("Prasava Legiyam/Mother-Care Product 200g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/herbal oils/9.jpg","""Description
For New Moms and Pregnant Ladies, it is a tradition in Southern India to prepare a marundhu called Prasava Legiyum. This legiyam has lots of nutrition packed ingredients that helps the New Mom’s in digesting their food.

Ingredients:

1) Hiptage Madablota

2) Zingiber Officinalis

3) Aplotaxis Auriculata

4) Coriandrum Sativum

5) Abrus Precatorious

6) Phyllanthus Embelia

7) Embelia Ribes

8) Terminalia Chebula

9) Plumbago Capensis

10) Ferula Asafoetida

11) Veppalarisy

12) Cinnamomum Zeylancium

13) Caryophyllum

14) Elettaria Cardomomum

15) Zingiber Officianale

16) Piper Nigrum

17) Nigella Sativa

18) Carum Coticum

19) Sinapis Nigrae Semina

20) Piper Cubeba

21) Trigonella Foenum

22) Chevviyam

Benefits:

• Treats anemia, edema and vomiting.
• Removes Prasava alukku [removes the unwanted contents of the delivery]
• Good cure for weakness
• Cures poor secretion of mother’s milk
• Works great for disorders of vaginal tract
• Can be given for digestive disorders
• Strengthens the uterus.
• Can be used for 6 months to 1 year after delivery.""",200.00,140.00),
            ("Maruthani Oil 40ml", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/herbal oils/10.jpg","""Description
Benefits of Marudhani Oil:
• It is used in aromatherapy.
• It is used to soothe soul, mind and body.
• It detoxifies and cools the body.
• It prevents dandruff, premature greying, hair loss and nourishes the hair.
• It lowers confusion and mental fatigue.
• It enhances blood circulation of scalp.
• It is used in aromatherapy for providing relief from stress and depress.
• The addition of mehndi oil to the bath water provides relaxation and soothing effect.
• The use of mehndi oil to the scalp alleviates dryness and itchiness of scalp.
• It promotes sleep, cure bruises and headaches.
• It helps to treat eczema, fungal infections, scabies and burns.""",200.00,150.00),
        ],
     "Joint Pain":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/joint pain/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("Sathuragiri/Sadhuragiri Joint Pain Thailam 60g(each)","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/joint pain/2.jpg","""Description
Benefits of Sathuragiri Mootu Vali(Joint Pain) Thailam:
Our fast-paced lifestyle tends to overwhelm our joints and muscle cells, rendering them dysfunctional. Orthoherb Oil easily penetrates the skin, delivering its medicinal properties to the muscle cells and joints in the body, making it flexible, strong and healthy.

Benefits:

Anti-inflammatory and analgesic
Lubricates joints
Imparts muscle tone and strengthens the Dhatus
Imparts firmness to limbs
Stimulates circulation
Helps the lymphatic functioning for detoxification
Joint Pain
Inflammations
Cervical & Lumbar Spondylosis
Sciatica & all types of inflammatory joint conditions
This oil provides excellent relief from joint pain. It doesn’t just stop at reducing pain — it also removes excess fluid retained in the joints that causes swelling or stiffness.

It is safe for elderly people, aged individuals, and mothers at home.
(No side effects whatsoever.)
Usage:

Step-1: Slightly HEAT this ‘THAILAM’ and apply it on the painful areas.

Step-2: Massage it a bit.

Step-3: Wash it with BEARABLE HOT WATER in the morning.""",350.00,300),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/joint pain/3.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/joint pain/4.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("SPL. Amukkara Powder(SPL. Ashwagandha) 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/joint pain/5.png","""Description
             Benefits of Ashwagandha:
• It helps to reduce level of stress and tension.
• It improves energy level.
• It supports better sleep.
• It helps to lower blood pressure and is highly effective in stopping the formation of stress induced ulcers.
• It increases haemoglobin and hair melanin.
• It stabilizes blood sugar and lowers cholesterol.
• It helps to reduce stress during a weight loss diet. When a person is stressed more Cortisol hormone is produced by the adrenal glands. Cortisol stimulates glucose production and triggers a hunger response in the brain. Ashwagandha can naturally lower cortisol levels up to 26%. It also helps to lose weight by reducing swelling in body and improving haemoglobin level.
• It is useful for any imbalance in the muscles as it reduces inflammation and strengthens muscles. It is an anabolic muscle builder. As it benefits all muscle tissue it is used as a heart tonic, uterine tonic, and lung tonic.
• It improves body immunity and strengthen body defense system. This makes this herb suitable for treating Auto-immune conditions such as neutropenia, rheumatoid and osteo arthritis, cancer and chronic connective tissue disorders.
• It gives good results in nerves related conditions such as Multiple sclerosis, Neurosis, insomnia, anxiety, and stress.
• It is used to enhance memory and lesson age-related cognitive deficits.

Benefits for Men:
• For males, Ashwagandha promotes sexual health by uplifting the mood, reducing anxiety, improving energy levels and fertility, thus supporting sexual performance.
• It has direct spermatogenic effect and helps to improve sperm count.
• It helps to alleviate asthenospermia (increasing sperm motility), oligospermia (increasing sperm count) and other sperm disorders.
• It exerts something like testosterone, influencing the seminiferous tubules.
• It promotes better sexual performance.
• It reduces impotence and promotes potency.

Benefits for Women:
• It contains phytoestrogen.
• It relieves females from menstrual imbalance.
• It stimulates secretion of breast milk in lactating mothers.
• It gives strength and cures debility when consumed post – delivery.
• It supports female reproductive system, and increases ovarian weight and folliculogenesis.""",1260.00,630.00),
            ("Eucalyptus Oil 60ml","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/joint pain/6.jpg","""Description
Benefits of Eucalyptus Oil:
It is super-effective for COVID-19. You shall mix this Oil in hot water, close yourself with a blanket and inhale the steam that arises from it.
NOTE: Add Manjal Powder for increasing the effectiveness

1. Silence a cough:

For many years, eucalyptus oil has been used to relieve coughing. Today, some over-the-counter cough medications have eucalyptus oil as one of their active ingredients. Vicks VapoRub, for example, contains about 1.2 percent eucalyptus oil along with other cough suppressant ingredients.

The popular rub is applied to the chest and throat to relieve cough symptoms from the common cold or flu.

2. Clear your chest:

Are you coughing but nothing is coming up? Eucalyptus oil can not only silence a cough, it can also help you get the mucus out of your chest.

Inhaling vapor made with the essential oil can loosen mucus so that when you do cough, it’s expelled. Using a rub containing eucalyptus oil will produce the same effect.

3. Keep the bugs away:

Mosquitoes and other biting insects carry diseases that can be dangerous to our health. Avoiding their bites is our best defense.

4. Disinfect wounds:

The Australian aborigines used eucalyptus leaves to treat wounds and prevent infection. Today the diluted oil may still be used on the skin to fight inflammation and promote healing. You can purchase creams or ointments that contain eucalyptus oil. These products may be used on minor burns or other injuries that can be treated at home.

5. Breathe easy:

Respiratory conditions such as asthma and sinusitis may be helped by inhaling steam with added eucalyptus oil. The oil reacts with mucous membranes, not only reducing mucus but helping loosen it so that you can cough it up.

It’s also possible that eucalyptus blocks asthma symptoms. On the other hand, for people who are allergic to eucalyptus, it may worsen their asthma. More research is needed to determine how eucalyptus affects people with asthma.

6. Control blood sugar:

Eucalyptus oil has potential as a treatment for diabetes. Although we don’t know much at this time, experts believe that it may play a role in lowering blood sugar in people with diabetes.

7. Soothe cold sores:

The anti-inflammatory properties of eucalyptus can ease symptoms of herpes. Applying eucalyptus oil to a cold sore may reduce pain and speed up the healing process.

You can buy over-the-counter balms and ointments for cold sores that use a blend of essential oils, including eucalyptus, as part of their active ingredient list.

9. Ease joint pain:

Research suggests that eucalyptus oil eases joint pain. In fact, many popular over-the- counter creams and ointments used to soothe pain from conditions like osteoarthritis and rheumatoid arthritis contain this essential oil.

Eucalyptus oil helps to reduce pain and inflammation associated with many conditions. It may also be helpful to people experiencing back pain or those recovering from a joint or muscle injury. Talk to your doctor about if it may be right for you.""",200.00,150.00),
            ("Paatti’s Pain Relief Thailam 10g(each)", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/joint pain/7.jpg","""Description
Method of Usage:
Mix these 3 in a GLASS BOTTLE at your home:

1) Omam Salt(ஓம உப்பு)
2) Raw Soodam(பச்ச சூடம்)
3) Pudhina Salt(புதினா உப்பு) you will achieve the Thailam(Liquid) magically in 2-3 hours, which you can apply on the painful and affected areas.

It not only cures the pain, but also makes you way active.""",350.00,300.00),
            ("Seemakilangu Podi/Seemakizhangu Powder 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/joint pain/8.jpg","""Description
Benefits:
This is a wonder herb that takes out the extra waste water from your joints!

Steps to apply externally:

Step – 1: Squeeze the juice of a Lemon in this Seemakilangu Powder and make it as a paste.

Step – 2: Then apply it on the painful and affected joint part at night.

It then gets dried by morning which you have to wash and remove with warm water.""",120.00,100.00),
            ("Seemakilangu 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/joint pain/9.png","""Description
This wonder herb’s powder takes out the extra waste water(தேவையற்ற நீர்) from your joints!

Steps to apply externally:
Step – 1: Squeeze the juice of a Lemon in this Seemakilangu Powder and make it as a paste.
Step – 2: Then apply it on the painful and affected joint part at night.
It then gets dried by morning which you have to wash and remove with warm water.""",160.00,100.00),
     ],
     "Kidney Problems":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/kidney problem/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/kidney problem/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/kidney problem/3.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("Nerunjil Powder 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/kidney problem/4.jpg","""Description
Benefits of Nerunjil Podi:
Reduction in kidney problems:

When consumed in the form of a water-based decoction for twice a day, it is said to break and eliminate kidney stones. It also further prevents kidney stone formation in the future.

Reduction of Urinary Problems:

Urinary problems such as blood in urine, urinary infection, frequent urination, painful urination and urine blockage can be resolved to a great extent by usage of this powder.

Aids in muscle building:

We’ve seen above that the saponins in this powder increase the secretion of hormones like testosterone. This helps in resolving weakness by helping improve the immune system, and further helps in muscle building and increase in body strength.

For muscle building:

Grind Nerunjil powder along with Karisalankanni powder and Adhimathuram powder(all in equal quantities), and consume it twice a day to notice benefits in a few days.

Blood Pressure reduction:

The hypotensive properties of Nerunjil help in controlling high blood pressure. Regular consumption of this powder also helps to reduce cholesterol levels in the body.

Boosts sexual performance:

Nerunjil powder, when consumed along with Ashwagandha(Amukkara) powder, can help reduce sexual weakness in men, including treating issues of erectile dysfunction and low sperm count. The saponins contained in Nerunjil stimulates testosterone secretion in men and promotes spermatogenesis. 
It should be consumed twice a day for up to 10 days before any difference can be noticed.""",35.00,30.00),
            ("Neermulli Seed Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/kidney problem/5.jpg","""Description
Benefits of Neermulli Leaf:
Tonic, diuretic and blood purifier, gingivitis, stomatitis, burns, dental caries,stone breaker, edema, nocturnal ejaculation and cracking heel.
It is used to treat wounds.""",80.00,60.00),
            ("Sirupeelai Podi 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/kidney problem/6.jpg","""Description
Benefits of Sirupeelai:
• In Tamil Maruthuvam: For Urinal Problems; It is diuretic which helps in promoting the production of urine, effective in urethral problems, lithiasis, and gonorrhea.

• In Ayurveda: It acts as a demulcent which helps in getting relief from pain and inflammation.

• As per Paatti Vaithiyam: It acts as an astringent thereby helping in reducing bleeding in piles. It is also used as a treatment for diarrhea and hemorrhages.

• As a Natural Remedy: Sirupeelai’s stem acts as an antioxidant which helps in balancing the free radicals.

• As Great Natural relief for Kidney Stone: It is lithontriptic and antilithic which gives the plant the power to destroy stones in kidneys and bladder.

• As a Herbal booster: It is also known for increasing memory power and used to treat a headache, abdomen and digestion problems.

• In Siddha Maruthuvam for Back pain: It is effective for neck and back pain, fever, urine problems and also regulates body metabolism.

• As a Herb for Liver disease: Aerva Lanata is considered to be effective for hepatitis and inflammation of the liver.

• Natural way for fat burning: Aerva Lanata is also used for the treatment of many health problems like Anemia, Alzheimer, Arthritis, Cholesterol, lung problems, bone problems and also blood circulation.

• Helps to fight against pathogens: It protects both the skin and the body from pathogens and it is anthelmintic which helps in destroying parasitic worms and reducing sores and injuries on the skin.""",60.00,50.00),
     ],
     "Liver Problems":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/liver problems/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/liver problems/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/liver problems/3.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
        ],
     "Menstruation":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/menstruation/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/menstruation/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Kalarchikai/Klachikai Powder 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/menstruation/3.jpg","""Description
Benefits of Kalarchikai:
• It has been used for treating intestinal worms, fever, tumors, cough, amenorrhea, and to remove the placenta after childbirth.
• Kalarchikai is used for eliminating piles, wounds, leucorrhea, and urinary disorders.
• It can be used for gargling to relieve a sore throat.
• It is used in controlling elephantiasis and smallpox.
• It is good for Hernia patients.

• It may be roasted in castor oil and be applied to reduce piles, inflammatory swellings, orchitis, and hydrocele.
• A paste made from the leaves and twigs is useful in reducing toothache.

Way of Consumption:
You have to consume Kalarchikai Podi in the morning(empty stomach)!

You can take a banana with our powder as it will be very bitter or you may mix the powder with water and drink for effectiveness!""",55.00,50.00),
            ("Karunjeeragam Powder 25g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/menstruation/4.jpg","""Description
Benefits of Karunjeeragam:
• Weight Loss diet tips: Consuming Karunjeeragam is an easy way to shed extra calories. It may be considered as one of the weight loss diet plans. It helps to make you slim without visiting to gym.

• Type 2 diabetes: Just two grams of Karunjeeragam daily could result in reduced fasting blood sugar levels, along with decreased insulin resistance, and increased beta-cell function in the pancreas.

• Epilepsy: Karunjeeragam will be effective at reducing the frequency of seizures in children who resisted conventional treatment. Karunjeeragam indeed has anti-convulsive properties.

• Protection Against Heart Attack: An extract from Karunjeeragam has been shown to possess heart-protective qualities, dampening damages associated with heart attacks and boosting overall heart health.

• Sinus problems: Karunjeeragam is effective in giving you relief from the frequent occurrence of sinusitis.

• Joint pain home remedies: It is useful in relieving of joint pains, knee pains and arthritis.

• Neck pain remedy: Solve your neck pain and cervical related pains by using Karunjeeragam.

• Sexual problems: Karunjeeragam have effective solution to get rid off from sexual weakness.

• Karunjeeragam for gynecological issues: Karunjeeragam is helpful in treating and curing of many gynecological problems such as Menstrual, Leucorrhoea, White discharge, back pain, stomach pain, etc.""",33.00,30.00),
            ("Atthi Pattai Podi/Atthi Bark Powder 25g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/menstruation/5.jpg","""Description
Benefits of Atthi Bark Powder / Atthi Pattai Powder:
Atthi Pattai Powder is very good for women as it cures problems in Menstruation.

Atthi Pattai Powder is used for Swelling & Boils.

Atthi Pattai Powder cures mouth ulcers and other mouth infections.

Atthi Pattai Powder is a good remedy for Pimples and freckles.""",65.00,60.00),
            
        ],
     "Piles":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/piles/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/piles/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/piles/3.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("Kilangu Podi/Kizhangu Powder 25g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/piles/4.jpg",""""Description
Ingredients:
1) Kaattukkaranai
2) Kaaraakaranai
3) Naattukaranai

Benefits:
Good for patients suffering from internal as well as external(வெளிமூலம்) hemorrhoids(piles).""",45.00,40.00),
            
        ],
     "Pooja Products":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/pooja/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("Mooligai Sambrani/Muligai Saampirani Set 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/pooja/2.jpg","""Description
SAMBRANI HEALTH BENEFITS
• Sambrani has a unique beautiful fragrance that is different from the normal incense sticks. The smell of sambrani transports back in time and somehow fills a person with peace and happiness. Even Ayurveda advises to use sambrani, as it calms the nerves, and produces tranquility, thus making the person ready for prayers.
• Women after having their hair washed, light up sambrani to dry it very quickly and also leave a beautiful fragrant smell in their hair. During winter months, if we use sambrani, we will not get a headache, especially if we have long, thick hair.
• Sambrani is also used for babies, after children have their bath, sambrani is lit and brought in that room. This prevents them from catching a cold but make sure not to bring the smoke too near the babies, as it will make their lungs delicate. No auspicious day is complete without sambrani, sambrani is always lit during our prayers and rituals.
• Regularly light up sambrani every morning, take it to every room in the house. This wards off mosquitoes and cleanses the whole place.
• To remove stale and negative energy, calm down anxiety, depression, and for a fresh smelling home.
• Light up sambrani at least weekly once and fill the whole house with the smoke. It will make the whole house smell divine.
• Even for headaches, sambrani smoke is very good.
• Purification of the air
• No auspicious day is completed without sambrani; sambrani is always lit during prayers and rituals. Lighting up of sambrani once in a day, makes us feel that we have followed proper rituals and cultures.
• This Traditional way of Lighting of Sambrani keeps the rooms spiritually strong and produces positive vibrates and also keeps away from mosquitoes.
• Medicated smoke has an important role in Ayurveda. It can be used to fumigate a room or it can carry to an individual the essence of herbs. Incense thus has healing properties. The smoke with its gandha or aroma activates the nasal system and through it makes changes in the body and mind of the person.
• Manage pain
• Improve sleep quality
• Reduce stress, agitation, and anxiety
• Soothe sore joints
• Treat headaches and migraines
• Ease discomforts
• Fight bacteria, virus, or fungus
• Improve digestion
• Improve hospice and palliative care
• Boost immunity""",140.00,120.00),
            ("Pure Sambrani 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/pooja/3.jpg","""Description
SAMBRANI HEALTH BENEFITS
• Sambrani has a unique beautiful fragrance that is different from the normal incense sticks. The smell of sambrani transports back in time and somehow fills a person with peace and happiness. Even Ayurveda advises to use sambrani, as it calms the nerves, and produces tranquility, thus making the person ready for prayers.
• Women after having their hair washed, light up sambrani to dry it very quickly and also leave a beautiful fragrant smell in their hair. During winter months, if we use sambrani, we will not get a headache, especially if we have long, thick hair.
• Sambrani is also used for babies, after children have their bath, sambrani is lit and brought in that room. This prevents them from catching a cold but make sure not to bring the smoke too near the babies, as it will make their lungs delicate. No auspicious day is complete without sambrani, sambrani is always lit during our prayers and rituals.
• Regularly light up sambrani every morning, take it to every room in the house. This wards off mosquitoes and cleanses the whole place.
• To remove stale and negative energy, calm down anxiety, depression, and for a fresh smelling home.
• Light up sambrani at least weekly once and fill the whole house with the smoke. It will make the whole house smell divine.
• Even for headaches, sambrani smoke is very good.
• Purification of the air
• No auspicious day is completed without sambrani; sambrani is always lit during prayers and rituals. Lighting up of sambrani once in a day, makes us feel that we have followed proper rituals and cultures.
• This Traditional way of Lighting of Sambrani keeps the rooms spiritually strong and produces positive vibrates and also keeps away from mosquitoes.
• Medicated smoke has an important role in Ayurveda. It can be used to fumigate a room or it can carry to an individual the essence of herbs. Incense thus has healing properties. The smoke with its gandha or aroma activates the nasal system and through it makes changes in the body and mind of the person.
• Manage pain
• Improve sleep quality
• Reduce stress, agitation, and anxiety
• Soothe sore joints
• Treat headaches and migraines
• Ease discomforts
• Fight bacteria, virus, or fungus
• Improve digestion
• Improve hospice and palliative care
• Boost immunity""",120.00,100.00),
            ("Carrom SeedsAjwain/Omam","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/pooja/4.jpg","""Description
Benefits of Omam/Carrom Seeds:
1. Fights bacteria and fungi:

Carom seeds have powerful antibacterial and antifungal properties.
This is likely attributed to two of its active compounds, thymol and carvacrol, which have been shown to inhibit the growth of bacteria and fungi.

2. Improve cholesterol levels:

Animal research indicates that carom seeds may lower cholesterol and triglyceride levels. High cholesterol and triglyceride levels are risk factors for heart disease.
In one rabbit study, carom seed powder reduced total cholesterol, LDL (bad) cholesterol, and triglyceride levels.

3. Lowers blood pressure:

High blood pressure, or hypertension, is a common condition that increases your risk of heart disease

4. Combats peptic ulcers and relieves indigestion:

Carom seeds are commonly used as a household remedy for digestive issues in Ayurvedic medicine. Carom seed extract also helps prevent and treat gas and chronic indigestion. Indigestion is categorized as persistent pain and discomfort in the upper part of your stomach. Delayed stomach emptying is one of the perceived causes of indigestion.

5. May prevent coughing and improve airflow:

Some evidence suggests that carom seeds may provide relief from coughing. Carom seeds also improves airflow to the lungs.

6. Has anti-inflammatory effects:

Inflammation can be good or bad. Short-term inflammation is your body’s natural way of protecting against illness or injury.
On the other hand, chronic inflammation can have negative effects on your body and increase your risk of certain diseases.""",60.00,40.00),
            ("Venkunguliyam/Venkungulingam White Kunguliyam 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/pooja/5.jpg","""Description
Benefits:
White Kungiliam is also used in Ayurveda, Siddha and Unani because of its miraculous medicinal power like the ordinary one.
It is good for curing chronic skin disorders, musculoskeletal disorder, tumors, diseases of oral cavity, rheumatism, fever, cough, asthma, epilepsy, ear and hair ailments etc.
It is also used to produced germ killers and perfumes""",80.00,60.00),
            ("Pachai Karpooram Raw Camphor","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/pooja/6.jpg","""Description
Raw Camphor""",80.00,60.00),
            ("Kunguliyam/Kungulingam 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/pooja/7.jpg","""Description
Kungiliam, a medicinal tree is a rare and precious specious found all over India. This species is commonly known as Sal tree or Shala. It’s scientific name is Shorea Robusta Gaertn.

Benefits:

Kungiliam is used in Ayurveda, Siddha and Unani because of its miraculous medicinal power.
It is good for curing chronic skin disorders, musculoskeletal disorder, tumors, diseases of oral cavity, rheumatism, fever, cough, asthma, epilepsy, ear and hair ailments etc.
It is also used to produced germ killers and perfumes.""",100.00,80.00),
            ],
     "PREGNANCY":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/preganancy/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/preganancy/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Prasava Legiyam/Mother-Care Product 500g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/preganancy/3.jpg","""Description
For New Moms and Pregnant Ladies, it is a tradition in Southern India to prepare a marundhu called Prasava Legiyum. This legiyam has lots of nutrition packed ingredients that helps the New Mom’s in digesting their food.

Ingredients:

1) Hiptage Madablota

2) Zingiber Officinalis

3) Aplotaxis Auriculata

4) Coriandrum Sativum

5) Abrus Precatorious

6) Phyllanthus Embelia

7) Embelia Ribes

8) Terminalia Chebula

9) Plumbago Capensis

10) Ferula Asafoetida

11) Veppalarisy

12) Cinnamomum Zeylancium

13) Caryophyllum

14) Elettaria Cardomomum

15) Zingiber Officianale

16) Piper Nigrum

17) Nigella Sativa

18) Carum Coticum

19) Sinapis Nigrae Semina

20) Piper Cubeba

21) Trigonella Foenum

22) Chevviyam

Benefits:

• Treats anemia, edema and vomiting.
• Removes Prasava alukku [removes the unwanted contents of the delivery]
• Good cure for weakness
• Cures poor secretion of mother’s milk
• Works great for disorders of vaginal tract
• Can be given for digestive disorders
• Strengthens the uterus.
• Can be used for 6 months to 1 year after delivery""",300.00,220.00),
            ("Prasava Legiyam/Mother-Care Product 200g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/preganancy/4.jpg","""Description
For New Moms and Pregnant Ladies, it is a tradition in Southern India to prepare a marundhu called Prasava Legiyum. This legiyam has lots of nutrition packed ingredients that helps the New Mom’s in digesting their food.

Ingredients:

1) Hiptage Madablota

2) Zingiber Officinalis

3) Aplotaxis Auriculata

4) Coriandrum Sativum

5) Abrus Precatorious

6) Phyllanthus Embelia

7) Embelia Ribes

8) Terminalia Chebula

9) Plumbago Capensis

10) Ferula Asafoetida

11) Veppalarisy

12) Cinnamomum Zeylancium

13) Caryophyllum

14) Elettaria Cardomomum

15) Zingiber Officianale

16) Piper Nigrum

17) Nigella Sativa

18) Carum Coticum

19) Sinapis Nigrae Semina

20) Piper Cubeba

21) Trigonella Foenum

22) Chevviyam

Benefits:

• Treats anemia, edema and vomiting.
• Removes Prasava alukku [removes the unwanted contents of the delivery]
• Good cure for weakness
• Cures poor secretion of mother’s milk
• Works great for disorders of vaginal tract
• Can be given for digestive disorders
• Strengthens the uterus.
• Can be used for 6 months to 1 year after delivery.""",200.00,140.00),
            ("Scool Rice/Sool Arisi 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/preganancy/1.jpg","""Description
Benefits of Scool Arisi
Very effective in case you want a NORMAL DELIVERY!
It is a good remedy for women during the time of ‘வெள்ளை படுதல்’ (leucorrhoea).
Method of INTAKE:

Step-1: In tender coconut water(இளநீர்) add some school arisi at night before going to sleep.

Step-2: Drink the tender coconut with school arisi early in the morning.""",100.00,80.00),
        ],
     "Pressure":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/pressure/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/pressure/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/pressure/3.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            
        ],
     "Rice & Millets":[
            
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("Scool Rice/Sool Arisi 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/2.jpg","""Description
Benefits of Scool Arisi
Very effective in case you want a NORMAL DELIVERY!
It is a good remedy for women during the time of ‘வெள்ளை படுதல்’ (leucorrhoea).
Method of INTAKE:

Step-1: In tender coconut water(இளநீர்) add some school arisi at night before going to sleep.

Step-2: Drink the tender coconut with school arisi early in the morning.""",100.00,80.00),
            ("Popcorn Sorghum 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/3.jpg","""Description
Health Benefits of Popcorn Sorghum:
Jowar popcorns are a healthy snack which tastes and looks like mini popcorn but is made instead from the wholesome grain Jowar called as Sorghum in English.
Popped Jowar is a very popular treat in India also called as Jowar Dhani. Sorghum’s flavor is earthy and mild. When popped, it tastes like a nuttier version of popcorn. 
These are different than machine made Jowar puffs available in the market. Our Jowar popcorns are made manually.

Jowar is a gluten-free member of the grass family and is incredibly nutritious. Jowar is one of the best millets for diabetics.

Jowar is packed with good quality fibre which can help facilitate your digestion, manage obesity and regulate blood sugar levels.
It contains high amount of protein and calcium. Jowar is a powerhouse of essential vitamins, antioxidants and minerals. 
It is loaded with good amounts of copper, zinc, phosphorous, potassium and cell-building B vitamins.""",20.00,12.00),
            ("Aali Rice/Flax Seeds 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/4.jpg","""Description
Benefits of Aali Rice(Flax Seeds):
• Flax seed works well against constipation.
• Improves digestive health.
• It helps to get healthy skin and hair
• It helps in weight loss and lowers cholesterol.
• It is used to control levels of cholesterol and blood sugar in the body.""",30.00,25.00),
            ("Mappillai/MaapillaiSamba Rice 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/5.jpg","""Description
Mapillai Samba Rice:
• The high fibre content present in the rice eases digestion.
• The vitamin B1 present in the rice aids in healing stomach and mouth ulcers.
• Improves immunity and stamina
• Strengthens muscles and nerves
• Makes the blood flow faster so that our body gets instant energy
• Increases hemoglobin content
• Good for diabetics since it is has a low Glycemic Index.
• Little ones will achieve better growth

Health Benefits Of Mapillai Samba Rice
• Mappillai Samba rice is a loaded source of carbohydrates. Carbohydrates is a fuel for our central nervous system and provides energy to the muscles. Carbohydrates are the body’s main source of energy.
• The fibre content plays an important role in digestion and prevents gastrointestinal issues like constipation, diarrhoea and gastritis.
• It has wholesome amount of micronutrients which also absorbs other nutrients.
• It is a good source of iron and Zinc and promotes hemoglobin in our body. It also strengthens all the blood vessels in our body. Furthermore,it helps in reducing cholesterol and hyperglycemia level.
• It is an indigenous rice which is rich in magnesium and vitamin B6. Magnesium in our body helps to maintain a steady heart rate, adjust blood glucose levels and supports immune system""",20.00,12.00),
            ("Little Millet/Saamai Arisi 100g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/6.jpg","""Description
Benefits:
The Little Millet (samai) is believed to have originated in India. It is grown and used for food almost exclusively in our country. It belongs to the group of small millets (other members being Proso, Kodo, Barnyard and Finger millets), which are said to be nutritionally superior to rice and wheat. The name Samai is actually a Tamil word for this lesser known member of the millet family. It is known as Kutki or Shavan in Hindi, Gajro or Kuri in Gujarati, and Sava in Marathi. One of the few cereal crops that does not demand much from the soil, Samai can grow well in the poorest of soils and with little rainfall. Yet, while it does not take much, Samai gives back tremendously in terms of health benefits.

Health Benefits of Samai:
1. Among cereals, Samai has been found to have the highest amount of fiber. Its crude fiber content is nearly twice that of other cereals.

2. Samai is rich in phenolic compounds that show antioxidant activity.

3. This millet is an excellent source of Iron. One serving (30 g) can provide 16% of the daily iron needs for an adult man.

4. Like other millets, Samai is also gluten free. It makes up for the lack of wholegrain fiber in Celiac (gluten free) diets.

5. Samai has a low to medium glycaemic index thus is diabetic friendly.

6. It is a rich source of the essential amino acids Histidine, Methionine and Phenylalanine.""",20.00,15.00),
            ("Kaikutthal Arisi/Brown Rice 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/7.jpg","""Description
Benefits of Brown Rice/Kaikutthal Arisi:
Great Source of Energy:

Kaikuthal rice is abundant in carbohydrates it acts as fuel for the body and aids in the normal functioning of the brain. Carbohydrates are essential to be metabolized by the body and turned into functional, usable energy. The vitamins, minerals, and various organic components increase the functioning and metabolic activity of all your organ systems, which further increases energy levels.

Cholesterol Free:

Kaikuthal rice is extremely beneficial for health, simply because it does not contain harmful fats, cholesterol or sodium. It forms an integral part of balanced diet. It has low levels of fat, cholesterol, and sodium which will help in reducing obesity and the health conditions associated with being overweight.

Blood Pressure Management:

Kaikuthal Rice is low in sodium, so it is considered one of the best foods for those suffering from high blood pressure and hypertension. Sodium can cause veins and arteries to constrict, increasing the stress and strain on the cardiovascular system as the blood pressure increases. 
This is also associated with heart conditions like atherosclerosis, heart attacks, and strokes, so avoiding excess sodium is always a good idea.""",20.00,12.00),
            ("Barnyard Millet/Kudhiraivali Arisi 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/8.jpg","""Description
Benefits:
1. Low in Calories

Barnyard millet is a good source of highly digestible protein and at the same time is least caloric dense compared to all other cereals. It is a grain which makes one feel light and energetic after consumption. A serving of barnyard millets (25g, raw) gives 75 calories and 1.5g of protein.

2. Rich in Fiber

It is an excellent source of dietary fiber with a good amount of both soluble and insoluble fractions. The grain encompasses the highest amount of fiber in comparison to other grains and millets with a serve providing 2.4 grams of fiber. According to a study published in the Journal of Food Science and Technology, the dietary fiber content of barnyard millet was high (12.6%) including soluble (4.2%) and insoluble (8.4%) fractions. The high fiber content helps in preventing constipation, excess gas, bloating and cramping.

3. Low Glycemic Index

The carbohydrate content of barnyard millet is low and slowly digestible, making the barnyard millet a low glycemic index food.
The carbohydrates in millet show a high degree of retrogradation of amylase, which facilitate the formation of higher amounts of resistant starch. Hence, it can be potentially recommended for patients with cardiovascular disease and diabetes mellitus. In today’s scenario, this millet becomes one of the ideal foods for diabetics.

4. Gluten-Free Food

Like all millets, the barnyard millet is gluten-free. It is an appropriate food for patients who are intolerant to gluten (those with celiac disease) or looking to follow a gluten free lifestyle which eliminates wheat, barley, rye-based foods. The millet being easily available, quick to cook and good to taste proves to be an ideal wholesome alternative to rice, wheat and other less easily available millets.

5. Good Source of Iron

According to research on nutrient content on millets, some varieties of barnyard millet have shown to contain high amounts of iron (18.6 mg in 100g of raw millet) which was the richest amongst all millets and cereal grains. Barnyard millet could be a good source of iron for vegetarians.""",20.00,16.00),
            ("Kodo Millet/Varagu Arisi", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/9.jpg","""Description
Nutritional Benefits of Varagu

This cereal also known as ‘Varagu’ forms the main stay of the dietary nutritional requirements. It has a high protein content (11%), low fat (4.2%), 65 g of carbohydrates, 5.2g of fibre, B Vitamins especially niacin, B6 and 23.1g of folic acid and minerals such as calcium, iron, potassium, magnesium, and zinc.
Varagu is also rich in anti-oxidants polyphenols, an antioxidant compound, tannins, phosphorous and phytic acids. Its antioxidant potential is much higher than any other millet and major cereals. The phosphorus content is lower in Kodo millet in comparison to other millets.

Varagu is a good substitute to rice or wheat. The protein, fibre, and mineral content are much higher than the major cereals like rice. It can be cooked just like rice or ground into flour. It provides balanced nutrition, unlike polished white rice.

Health Benefits of Varagu
It is easy to digest, contains a high amount of lecithin and is excellent for strengthening the nervous system. It is rich in photo chemicals, phytate that helps in reduction of cancer risks. It helps to reduce the body weight and beneficial for postmenopausal women. It is good for those suffering from signs of cardiovascular disease, like high blood pressure and high cholesterol levels. Also, it is good for diabetics, its anti–diabetic compounds like quercetin, ferulic acid, p – hydroxybenzoic acid, vanillic acid and syringic acid from Varagu prevents obesity. 
Kodo millets contain no gluten and are good for people who are gluten intolerant.""",20.00,12.00),
            ("Foxtail Millet/Thinai Arisi 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/10.jpg","""Description
Benefits:
1. Anti Aging Properties
Due to the presence of lycine and methionine (amino acids) present in foxtail millets, they help in the formation of collagen which helps in slowing the appearance of wrinkles.
Cross linking of collagen reduces elasticity and increases stiffness. Foxtail millets are known to inhibit the crosslinking of collagen. Cross-linking of collagen will reduce elasticity and increases stiffness.

2. Energy Booster
Thinai is a rich source of phosphorus which is an important mineral for energy production and is an essential component of ATP- an energy store in our body.

3. Fights With Diabetes
People suffering with diabetes who switch over to foxtail millet have low triglyceride levels. Low triglyceride levels lower the amount of bad cholesterol levels.
Foxtail Millets has a low glycemic index and is a fantastic substitute for food and other grains. It increases the blood sugar levels slowly as energy is produced to perform functional activities.

4. Reduces The Risk Of Cancer
Add fibre to your food slowly and take plenty of water. This is a important tip for every women. In India, one women is diagnosed with breast cancer every four minutes and one women with breast cancer dies for every 13 minutes.

5. Boost Brain Development And IQ
Iron is directly associated with brain functions. It supplies oxygen to the brain as it uses 20% of the brain oxygen. The sufficient amount of blood received by the brain helps to promote cognitive functions and prevents alziemer’s disease and dementia.""",20.00,12.00),
            ("Black/Forbidden Rice 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/11.jpg","""Description
Benefits of Black Rice:
1. Rich in Antioxidants

The deep black or the purple hue of the black rice is a marker of its high antioxidant properties. Similar to blackberries and blueberries, that appear deeper in colour because of their high content of anti-oxidants. The outermost layer of the grain (the bran and the hull), contains immense amounts of the antioxidant-anthocyanin. In fact the amount of anthocyanin contained in black rice is higher than any other grain, including brown rice, red rice, red quinoa, or other colored whole grain varieties.

Anthocyanin can help prevent cardiovascular disease, restricting free radical movements which can cause variety of diseases like diabetes and even cancer. It can also help improve brain function and reduce inflammation.

White rice and other refined grains are stripped of their high nutrient content and beneficial properties in the milling process. Majority of the nutrients of rice are present in the outer layer, the hull and the bran, which are only retained in whole grains. Since black rice doesn’t undergo any refining or processing, it is able to retain its antioxidants, vitamins, minerals, and fiber. Black rice also contains important antioxidant- Vitamin E, which is useful in maintaining eye, skin, and immune health.

2. Natural Detoxifier

The phytonutrients present in black rice help cleanse the body of disease causing toxins (caused by free radicals). Black rice helps the liver (one of the most significant detoxifiers of the body) eliminate unwanted substances through its antioxidant activity.

3. Good Source of Fiber

The black rice has about 3 grams of fiber per half cup serving. This rich fibre content helps regulate the bowel movements, prevent constipation, diarrhea and bloating. The fibre helps bind the toxins and waste within the digestive tract, and flush it all out of the system on completion of the cycle of digestion. Fibre also gives your body a satiated feeling after consumption which prevents you from binging into other fatty food, thus aiding weight loss.

4. Preventing Risk of Diabetes

To ward off the risk of diabetes and obesity, it is advised to consume whole grains instead of just refined carbohydrates. The entire bran of the grain is where the all the fiber is stored in the black rice. The fibre is able to help glucose (sugar) from the grain to be absorbed by the body over a longer duration of time, (Since fibre take the longest to digest), thereby maintaining consistent sugar levels. Read A diabetic’s guide to eating rice too.

5. Preventing Risk of Obesity

For people battling obesity, black rice is the best variant of rice to consume. Full of fibre, black rice not only gives you the feeling of being full, thus preventing overeating; studies show that the rice variant can also help prevent insulin resistance, which is often linked to the risk of developing diabetes and obesity.

6. Richer Protein Content

The reason your nutritionist has been asking you to cut down on your rice consumption is because of its high carbohydrate versus very less protein content. Proteins are very essential in building muscles, and cutting down on excess weight. Black rice also offers a minutely increased amount of protein content over other ‘healthier variants‘. It contains 8.5gms of protein in a 100gms serving, while brown and red rice contains 8gms and 7gms of protein respectively for the same serving. On the other hand, polished white rice contains only 6.8gms of protein.

7. Better Heart Health

Eating black rice may have a positive impact on your healthy cholesterol levels too. The anthocyanins phytochemicals found in black rice, reduces the Low Density Lipo-protein (LDL) cholesterol also known as the bad cholesterol, which is a common contributor to cardiovascular diseases. It also brings down the total cholesterol levels.""",30.00,25.00),
            ("Pumpkin Seeds/Poosani Vidhai 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/12.jpg","""Description
Pumpkin seeds may be small, but they’re packed full of valuable nutrients.
Eating only a small amount of them can provide you with a substantial quantity of healthy fats, magnesium and zinc.
Because of this, pumpkin seeds have been associated with several health benefits.
These include improved heart health, prostate health and protection against certain cancers.

1. Full of Valuable Nutrients
Pumpkin seeds are also known as “pepita” — a Mexican Spanish term.
Unlike the hard white seeds from a carving pumpkin, most pumpkin seeds bought at the supermarket don’t have a shell.
These shell-free seeds are green, flat and oval.

2. High in Antioxidants
Pumpkin seeds contain antioxidants like carotenoids and vitamin E.
Antioxidants can reduce inflammation and protect your cells from harmful free radicals. That’s why consuming foods rich in antioxidants can help protect against many diseases.
It’s thought that the high levels of antioxidants in pumpkins seeds are partly responsible for their positive effects on health.
In one study, pumpkin seed oil reduced inflammation in rats with arthritis without side effects, whereas animals given an anti-inflammatory drug experienced adverse effects.

3. Linked to a Reduced Risk of Certain Cancers
Diets rich in pumpkin seeds have been associated with a reduced risk of stomach, breast, lung, prostate and colon cancers
A large observational study found that eating them was associated with a reduced risk of breast cancer in postmenopausal women
Others studies suggest that the lignans in pumpkin seeds may play a key role in preventing and treating breast cancer
Further test-tube studies found that a supplement containing pumpkin seeds had the potential to slow down the growth of prostate cancer cells

4. Improve Prostate and Bladder Health
Pumpkin seeds may help relieve symptoms of benign prostatic hyperplasia (BPH), a condition in which the prostate gland enlarges, causing problems with urination.
Several studies in humans found that eating these seeds reduced symptoms associated with BPH.
In a one-year study in over 1,400 men with BPH, pumpkin seed consumption reduced symptoms and improved quality of life.
Further research suggests that taking pumpkin seeds or their products as supplements can help treat symptoms of an overactive bladder.
One study in 45 men and women with overactive bladders found that 10 grams of pumpkin seed extract daily improved urinary function.

5. Very High in Magnesium
Pumpkin seeds are one of the best natural sources of magnesium  — a mineral that is often lacking in the diets of many Western populations.
In the US, around 79% of adults have a magnesium intake below the recommended daily amount
Magnesium is needed for more than 600 chemical reactions in your body. For example, adequate levels of magnesium are important for:
• Controlling blood pressure
• Reducing heart disease risk
• Forming and maintaining healthy bones
• Regulating blood sugar levels""",120.00,100.00),
            ("Red Rice/Sivappu Arisi 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/13.jpg","""Description
Health benefits of Red Rice
Red rice is a kind of unpolished rice which has higher nutritional value compared to white rice or even polished rice. Cooking time is comparatively more than white rice and it has a nutty taste and more gratifying flavor. It is fiber rich content, Vitamin B1 & B2, iron and calcium. Because of higher nutritive content and health advantages of red rice, it is strongly advised for heart patients as well as diabetics. Additionally it is loved by health gurus as well as fitness fanatics since it’s high fiber content helps gain less weight. By consuming red rice, you can get the following nutrition and also health advantages.

1. Contains antioxidants to counteract free radicals
Red/brown rice is a great source of iron or manganese. Mangan, who was simply instrumental in producing energy for the body is a vital element of the enzyme and is also an anti-oxidant that may safeguard the body from free-radicals which are formed once the energy produced. Additionally, red/brown rice is full of zinc, a mineral that can help accelerate wound healing and maintain the body’s defense mechanisms to function effectively. Just like iron or manganese, zinc is additionally full of anti-oxidants that safeguard the body from free-radicals that may damage tissues and cells within the body.

2. Containing Vitamin B6
By consuming only one serving of red/brown rice, can meet 23 percent of vitamin B6, the quantity required for the functioning of the organ. This particular vitamin is required to help balance the development of serotonin, red blood cells helping the creation of DNA cells.

3. Can Lower High Cholesterol
In 1970, human studies reported red rice’s effect on reducing the blood levels of total cholesterol. The active component in red rice is monacolin K. It’s just like lovastatin within the prescription drug cholesterol-lowering drug, Mevacor. In accordance with EMedtv, the United States Food and Drug Administration has ruled that simply because lovastatin is really a prescription drug, any red yeast rice supplement with a substantial dosage of lovastatin is surely an unapproved drug and not a dietary supplement. Do not take red rice in case you have liver disease, are pregnant, or are younger than 18. Side effects consist of gas, heartburn and dizziness.

4. Can Help Prevent Heart Disease
Higher amounts of low-density lipoprotein or LDL in the blood cause plaque build-up in the walls of the arteries. This particular narrows the size of the arteries and could block the coronary artery, causing a heart attack. Reducing LDL cholesterol levels reduces the chance of heart disease. A 2009 study carried out by David Becker and Ram Gordon, cardiologists at Chestnut Hill Hospital reported that LDL cholesterol levels reduced more in patients receiving red yeast rice compared to patients getting a placebo.

When your LDL or bad cholesterol levels are controlled, your heart health also improves. Your chances of contracting cardiovascular problems become slim. This is a very good thing since heart-related problems can be fatal.

5. Can Lower Blood Glucose
Uncontrolled blood glucose levels in diabetics can ruin the eyes, kidneys and also the coronary heart. Controlling blood sugar levels reduces these dangers. In a animal research carried out at the Department of Food Science at the National Pingtung University of Science and Technology, Hon-Qi–a form of red yeast rice–was administered to induced-diabetic rats and also to rats with normal blood glucose levels. This was a try to create a new replacement for dealing with diabetes. The results claim that oral administration of Hon-Qi may reduce blood glucose in diabetic rats inadequate insulin.

6. It lowers the risk of obesity
Red rice will help you decrease the desire to eat and may cause you to feel fuller for the really long time. Moreover, red rice provides energy in your body and helps the digestion. Red rice is completely fat-free. Most likely you know that high-fat consumption boost the chance of obesity. It’s been shown that individuals who eat red rice on a daily basis, have got a reduce chance of obesity. In case you are attempting to drop a few unwanted pounds, eating red rice could make the method simpler.

7. It helps in fighting asthma
Since red rice is a superb source of magnesium, which will help to manage your normal breathing pattern, consuming red rice regularly will assist you to avoid the issue of asthma. This really is among the best advantages of eating red rice. If you suffer from asthma, talk to your doctor and discover whether you can consume red rice or not.

8. It’s fortified with powerful antioxidants
Red rice is additionally loaded with effective anti-oxidants which are extremely therapeutic for the skin. Consuming red rice frequently might help avoid the appearance of fine lines and wrinkles on the skin. Plus, red rice may help firm and tighten the skin and minimize the damage brought on by UV rays that may result in wrinkles.

9. Red rice is good for your bone health
As we mentioned above, red rice is a superb source of magnesium, that is ideal for your bone health. Magnesium is a crucial nutrient needed to build healthy bones and magnesium deficiency can result in osteoporosis and low bone density later in life. It has been verified that regular consumption of red rice will help avoid and relieve joint problems.

10. It’s rich in fiber
Red rice is really a whole grain to help you meet your daily fiber requirements. One-quarter cup of red rice consists of about 2 grams of fiber, and it’s 8 percent of your daily fiber requirements.For adults, the recommended fiber intake is at 14 grams per 1,000 calories.

Fiber is renowned for its capability to assist in preventing and alleviate constipation, and enhance bowel function. While white rice is full of carbs, red rice is loaded with fiber. Additionally, it offers energy to your body required for regular body functioning.

Even better yet, if you’re on the pursuit of losing weight healthily and becoming more fit, red rice works for this purpose since it’s effective in controlling your hunger. Thereby, digestion is slowed down, and weight control is better managed.

11. It’s Rich In Iron
This benefit is particularly advantageous to those of you that have iron deficiency or are anemic. In addition to the supplements that you take, you may want to add red rice in your diet since it’s a rich source of iron. Healthy men need at least 8mg of iron a day, while women need 18mg. With even just ¼ cup serving of red, you’re already able to meet 2% of your daily iron requirement.

Note that iron is very important in your body for you to function well. Oxygen is needed by your body to flow through, else you’re going to feel weak the entire day. More importantly, iron also helps ward off any infection that may attack your body.""",15.00,10.00),
            ("Poongar/Poongaar Rice 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/14.jpg","""Description
Poongar Rice – The Women’s Rice:

This rice is rich in anthocyanin( an antioxidant). Anthocyanin gives it colour (reddish brown) and flavour (nutty). Poongar rice also contain mineral like Iron, Zinc, Magnesium and Molebidinum. Its husk is also nutritious and tasty. This rice generally comes in boiled and semi-polished form.
Poongar rice is one of the most wonderful option for making soft idlis, dosas(especially Neer Dosa) and porridge.

HEALTH BENEFITS:
A) Helpful for pregnant women:

Its kanji(usually called Pez, water extracted out of boiled rice) is said to induce normal delivery in pregnant women.

B) Removes bad sweat from body:

It contains anthocyanin(antioxidant)which helps to kick out the bad sweat out of the body and provide a healthy living.

C) Boost immune system:

It increases haemoglobin content in blood and thus boost immunity system.

D) Contain vitamin B1:

It contains vitamin B1 which is specially helpful in case of mouth and stomach ulcer and stomach related problem.

E) Memory:

It is also helpful for headache and is said to boost memory.

F) Diabetes:

It generally prevents the glucose from mixing in the blood stream thus preventing ‘diabetes insipidus’.

Though there are modern methods and variety with faster productivity but they cause many harmful effects on our body. Traditional methods are chemical free and harmless, also traditional variety of crops have higher content of nutrients thus even if they are produced in small scale they can be beneficial for consumers and can be harmless at greater scale. 
So organic farming can bring greater yield but there is need to select the best possible method.""",20.00,12.00),
            ("Cucumber Seeds/Vellari Vidhai 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/15.jpg","""Description
Cucumber plants are tendril bearing vines, rooting at the nodes, with triangular prickly hairy leaves and yellow flowers which are either male or female. The female flowers are recognized by the swollen ovary at the base which will become the edible fruit. The fruit is roughly cylindrical, elongated, with tapered ends, and may be as large as 60 cm long and 10 cm in diameter. Cucumber originated in south Asia, but is now cultivated throughout the world.

Benefits of Vellari vithai(Cucumber Seeds):
Hair Benefits:
If you are suffering from hair problems like hair fall and weak hair then cucumber seeds is the key to treat all your problems. The sulphur content of cucumber seeds helps in stimulating the growth of hair and makes them thick and healthy. Regular consumption of cucumber juice (with seeds) helps in preventing the problem of hair fall effectively.

Digestive Health Benefits:
Regular consumption of cucumber seeds is highly recommended as it helps in stimulating the overall digestive health. Cucumber seeds help in preventing a number of digestive problems like acidity, ulcers, gastritis, indigestion etc. The water, fibre and mineral content of cucumber helps in the smooth functioning of the digestive organs and helps in flushing out the toxic materials from the body.

Aids in weight loss:
It helps to shed theextra weight from the body when cucumber seeds are added in diet chart. Cucumber seeds contain less calorie and the water and mineral content of it help in losing weight more efficiently.

Promotes Gum and Teeth Health:
Regular consumption of cucumber seeds helps in improving the overall gum and teeth health. The photo chemical content of cucumber seeds is very useful in fighting off the harmful bacteria from the mouth and thus helps in getting rid of the problem of bad breath and cavities. cucumber seeds also help in increasing the salivation process too.

Promotes Brain Health:
The copper content of cucumber seeds helps in stimulating the process of neurotransmission which in turn improves the overall brain coordination. Regular consumption of cucumber seeds is recommended as it provides all the essential minerals that are required for improving the brain’s health. Regular consumption of cucumber seeds is linked with lower stress level if you have high stress then add cucumber to your daily routine in order to keep yourself up and charged.

Anti Inflammation:
Cucumber seeds possess anti inflammatory properties that help in reducing the inflammation. Regular consumption of cucumber seeds is also helpful in treating the problem of head ache.

Skin Benefits:
Cucumber seeds are very useful in treating a number of sin problems like sunburn, dry skin, tanning, wrinkles etc. The use of these seeds helps in providing a youthful look to your skin. The anti oxidants present in cucumber helps in revitalizing the skin and add a natural glow to it.""",80.00,60.00),
            ("Sunflower Seeds 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/16.jpg","""Description
Sunflower seeds are harvested from the flower head of the sunflower plant. While the seed itself is encased in a black and white striped shell, sunflower seeds are white and have a tender texture. Known for their distinct nutty flavor and high nutritional value, you can eat the seeds raw, roasted, or incorporated into other dishes.

Health Benefits
Studies link the consumption of sunflower seeds to a number of health benefits, including lowering your risk of developing diseases like high blood pressure or heart disease. They also contain nutrients that can support your immune system and boost your energy levels.

Here are some of the health benefits of sunflower seeds:

Reducing Inflammation:

For those with short-term or chronic inflammation, sunflower seeds can offer anti-inflammatory benefits. Sunflower seeds contain vitamin E, flavonoids, and other plant compounds that can reduce inflammation. A study found that consuming sunflower seeds and other seeds five times or more each week resulted in lower levels of inflammation, which also lowered risk factors for several chronic diseases.

Improving Heart Health:

Sunflower seeds are rich in ‘healthy’ fats, including polyunsaturated fat and monounsaturated fat. A three-fourths cup serving of sunflower seeds contains 14 grams of fat. Studies found that consumption of seeds — including sunflower seeds — was linked to lower rates of cardiovascular disease, high cholesterol, and high blood pressure.

Supporting the Immune System:

Sunflower seeds are a source of many vitamins and minerals that can support your immune system and increase your ability to fight off viruses. These include both zinc and selenium. Zinc plays a vital role in the immune system, helping the body maintain and develop immune cells. Selenium also plays a role in reducing inflammation, fighting infection, and boosting immunity.

Boosting Energy Levels:

While the high levels of protein in sunflower seeds already help boost your energy levels, other nutrients like vitamin B and selenium can help keep you energized. The vitamin B1 (also known as thiamin) present in sunflower seeds can help you convert food to energy, which can keep you active throughout the day. Selenium can increase blood flow and deliver more oxygen to your body.""",60.00,50.00),
            ("Naattu Kambu/Pearl Millet 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/17.jpg","""Description
Nutritional Value of Kambu:
• It is a high energy food which is packed with Iron. Kambu has 8 times Iron content higher than in Rice. The rich Iron content in Kambu aids in improving the hemoglobin level in the blood and prevents anemia.
• It is also rich in fiber, protein, minerals such as magnesium, zinc, manganese, folic acid, amino acids, lecithin, potassium, B complex vitamins, and calcium. Niacin in B complex vitamins reduces cholesterol, phosphorus plays an important part in the structure of body cells and magnesium is essential for maintaining heart health. Potassium and Magnesium help to prevent blood pressure.
• The phytonutrients in Kambu called lignin help to fight cancer and reduce the risk of cardiac arrests.
• Eating Kambu regularly helps in the prevention of gallstones in women. The abundant source of insoluble fiber in Kambu increases movement of food and decreases bile secretion that may result in gallstones. The rich concentration of fiber helps in the easy movement of food and prevents constipation.""",15.00,10.00),
            ("Bamboo Rice/Moongil Arisi 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/18.jpg","""Description
Health Benefits:
Bamboo Rice is nutrient rich and replace paddy in many tribal villages of western ghats and the north east. In fact the protein content of Bamboo seed is higher than that of rice and wheat.

Other than protein the rice also has carbohydrates, vitamins A, B1, B2, B3 and B6, minerals calcium, iron and phosphorus, and fibre. This makes the rice highly nutritive especially to small children because of the immediate release of energy it gives.

1. Enhances Fertility

The health benefit of bamboo rice is studied extensively in the Kani tribes of Kanyakumari. The study has reported that consumption of the rice is beneficial in the reproductive ability and fertility of the tribe.

2. Controls rheumatic pain and joint pain

Since bamboo rice is rich in calcium, bone health is maintained and pains related to joins, rheumatism, arthritis and backbone are controlled.

3. Controls Diabetes

The glycemic index of the rice is low and hence diabetes is controlled. It also is a rich source of phosphorus and iron, which makes sure that your heart is healthy and controls heart enlargement.

3. Lowers Cholesterol Level

There is no fat in bamboo seeds. The carbohydrates that is present also increase the blood glucose level in a slow pace, this helps in reducing cholesterol accumulation. Burning fat that is already accumulated is also possible because of this low glycemic index.

4. High Phosphorus content

Bamboo seeds contain about 218 mg % of phosphorus in them which is quite a commendable amount for any rice.
Phosphorus plays a vital role in
• formation of bones and teeth.
• also determines how the body uses carbohydrates and fats
• helps body to accumulate more protein for growth maintenance and repair of vital organs and tissues.
• Combines with B vitamins to make sure, kidney function, muscle contraction, heart beat and nerve signaling are normal.

5. Regulates Blood Pressure

Consuming the rice regularly keeps your blood pressure in the normal range by maintaining the mineral constituents in the body. Iron, calcium and phosphorus act simultaneously in keeping the heart and brain coordination working in unison.""",100.00,80.00),
            ("White Sorghum/Vellai Solam 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/19.jpg","""Description
Health Benefits of Vellai Solam/White Sorghum:
Improves digestion

Jowar contains a good amount of fibre, around 48 per cent of what is required by our body on daily basis. Fibre adds bulk to the stool and thus helps it pass smoothly through the digestive tract. As jowar helps in digestion it prevents problems like gas, bloating, constipation and diarrhoea.

It fights against free radicals

Jowar (sorghum) has a layer which contains anti-cancer properties and also fights the free radicals which are responsible for pre-mature ageing.

Boosts immunity

Jowar contains magnesium, copper and calcium which helps in making bone and tissues strong. Jowar also contains iron which helps to increase the red blood cells. All this in turn improves our immunity.
Improves heart health

As we have already mentioned jowar is rich in fibre, it helps to lower the LDL (bad cholesterol) and in turn reduces the chance of heart diseases including stroke. It is gluten free

Gluten is found in wheat and barley-based foods. Gluten can cause digestive problems in people who have gluten intolerance. So jowar being a gluten free food can be an excellent alternative for the ones suffering from gluten intolerance. Gluten intolerance can cause digestive problems like bloating, pain, cramps etc.

Rich source of protein

One cup of jowar contains 22 grams of protein. Protein not only gives energy to your body but it also helps in regeneration of cells. Controls blood sugar level

Being a complex carbohydrate, jowar gets digested slowly and thus promotes gradual rise in blood sugar. This is why it is a great choice for people who suffer from diabetes and for the ones those who want to lose weight.""",15.00,10.00),
            ("Solam/Sorghum 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/20.jpg","""Description
Health Benefits of Sorghum/Solam:
A healthy alternative to the all-purpose flour is Jowar or Sorghum. Rich, Bitter-y and fibrous in texture, this millet is grown abundantly across India.

Our obsession with all-purpose flour or Maida is often a cause for concern amongst health experts across the country. No doubt that piping hot maida pooris and bhaturas are delicious and decadent, but the truth is that the consequences of loading up on maida may outnumber its benefits. Maida is processed, refined and bleached wheat flour and has been associated with many health woes including weight gain and constipation. Luckily, there are some healthy, and equally tasty, grains out there we could look at as alternatives to maida. One such millet that is a healthy alternative to the all-purpose flour is Jowar or Sorghum. Rich, Bitter-y and fibrous in texture, this millet is grown abundantly across India but often loses out owing to the wheat fixation that runs in our country. Macrobiotic Nutritionist and Health Practitioner Shilpa Arora says, “rich in protein iron and copper, this gluten free grain has been known to play a crucial role in cellular function and repair.The rich quantity of potassium and phosphorous helps lower cholesterol and manage high blood pressure. Most importantly, the grain is incredibly rich in fibre and hence should be part of your daily diet.”

1. High of fibre

All millets are high in fibre, and jowar is no different. It can help facilitate your digestion, manage obesity, regulate blood sugar levels and curb the risk of high blood pressure and strokes. It is said that a single serving of jowar contains more than 12 grams. It makes for one of the best millets for diabetics.

2. Helps weight loss

The high fibre content in Jowar can help you shed a pound or two too. According to Dr. Anju, “Fibre takes the longest time to digest, which helps induce a feeling of being full for a longer spell. This prevents you from bingeing into other fattening foods, thereby saving you quite a few unwanted calories.” Moreover, fibre stimulates your digestive system, which help you stay an optimal weight.

3. Rich source of protein

A cup of jowar has a whopping 22 grams of protein. Protein helps build muscles, cell regeneration, and induce a feeling of satiety- which can further help in your weight reduction diet. If you are looking to lose weight, add jowar instead of wheat in your diet and see it work wonders on your health and weight.

4. Packed with essential Minerals and Vitamins

Jowar is a powerhouse of essential vitamins, antioxidants and minerals. It is loaded with good amounts of calcium, copper, zinc, phosphorous, potassium and cell-building B vitamins. The presence of these essential nutrients help keep the body healthy and keep all the ailments at bay.

5. Good for Diabetics

Dr. Anju says that Jowar is one of the best flours for those with a diabetic condition as it is a complex carbohydrate source. She says, “A diabetic needs to be very careful of his/her carb intake. Simple carbs are loaded in sugar which upon ingestion can trigger abnormal sugar spikes. But that doesn’t mean they need to rule out carbs completely. Carbohydrates are one of the three macronutrients which are essential for sustenance and good health. They should maximize on complex carbs and try to eliminate as many sources of simple carbs as possible. Jowar, a complex carbohydrate, is digested slowly, prompting a more gradual rise in blood sugar.”

6. It is Gluten-free

For those who are suffering from gluten intolerance, gluten allergies or are diagnosed with celiac disease, Jowar makes for a brilliant wheat alternative. Gluten refers to a mixture of proteins found in wheat, rye, oats and barley, it may cause digestive problems such as bloating, pain and stomach cramps for those who are allergic to this protein. Jowar, a gluten-free whole grain, is considered an excellent alternative for people who suffer from gluten intolerance’, the nutritional benefits are an added bonus.""",15.00,10.00),
            ("Samba Wheat 100g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/21.jpg","""Description
Controls Obesity (especially in women):

Wheat has a natural ability to control weight in everyone, but this ability is more pronounced among women. The American Journal of Clinical Nutrition has shown through research that whole wheat, rather than refined form, is a good choice for obese patients. Women who consumed whole wheat products over long periods showed considerably more weight loss than the others subjects.

Improves body metabolism:

Saturated and trans fats increase the chances of cardiovascular diseases, while omega-3 fats decrease cardiovascular disease risk. Whole grains like wheat are immensely effective on patients with metabolic disorders. Common types of metabolic syndromes include visceral obesity, also known as the “pear shaped” body, high triglycerides, low levels of protective HDL cholesterol, and high blood pressure. It protects against all of these conditions. Research has shown that foods made from refined grains not only tend to increase weight but they also increase the hazards of insulin resistance. Doctors recommend eating whole wheat bread and other fiber-rich foods. The majority of fiber works to help the digestive process in the body and improve the overall metabolism. Having a whole wheat diet is probably the most effective, quick, and enjoyable way to reduce metabolic syndrome, but also to stay slim and healthy throughout your life.

Prevents Type 2 Diabetes:

Wheat is rich in magnesium, which is a mineral that acts as a co-factor for more than 300 enzymes. These enzymes are involved in the body’s functional use of insulin and glucose secretion. The FDA permits foods that contain whole grain by at least 51% weight and are also low in saturated fat and cholesterol, which means a lower risk of coronary ailments and certain types of cancer. Moreover, regular consumption of whole grain wheat promotes healthy blood sugar control. People who suffer from diabetes are able to keep their sugar levels under control by replacing rice with wheat in their diet.

Reduces Chronic Inflammation:

The betaine content of wheat is what aids in the prevention of chronic inflammation. Betaine is usually found in whole wheat, beets and spinach. Inflammation is a key constituent in most types of rheumatic pains and also some rheumatic diseases. Thus, it is a good idea to eat a healthy amount of whole wheat food products that will actively reduce inflammation. Consumption of betaine affects a number of aspects in our body chemistry that assures a lower risk of chronic inflammation and other ailments like osteoporosis, heart disease, Alzheimer’s disease, cognitive decline, and type-2 diabetes.

Prevents Gallstones:

In various surveys by the American Journal of Gastroenterology, it has been proven that breads and cereals made from whole wheat help women to avoid gallstones. Since whole wheat is rich in insoluble fiber, it assures a quick and smooth intestinal transit time and lowers the secretion of bile acids. Excessive bile acids are a major cause of gallstone formation. Moreover, a high intake of wheat increases insulin sensitivity and thereby lowers triglycerides or fat in the blood. Besides wheat, you also get insoluble fiber from the edible skins of fruits and certain vegetables like cucumbers, tomatoes and squash, berries, apples, and pears. Beans also provide both insoluble and soluble fiber.

Whole Grain Wheat Assures a Healthy Lifestyle:

Wheat is the most popular and easily available bulk laxative. Three cups of wheat consumption per day is enough for an individual to live a long, healthy and disease-free life. When you maintain a fiber-rich diet comprised of wheat breads and cereals that are high in bran, you can be confident that problems such as pain, flatulence, nausea, constipation, and distension will be alleviated in no time. Diverticulitis often occurs due to inflammation and lower intestinal pains. This can also lead to chronic constipation and unnecessary straining, which can result in a sac or a pouch in the wall of the colon.""",25.00,20.00),
            ("Karboga/Babchi Arisi/Rice 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/22.jpg","""Description
Benefits of Karboga Arisi:

Used for treating:
• Skin Care
• Constipation""",120.00,90.00),
            ("Herbal Country SugarNaattu Sarkarai 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/rice/23.jpg","""Description
Benefits
1. Prevention Of Breathing Troubles
For those who have common respiratory tract problems, jaggery can be one of the maximum useful answers. You’ll save your allergies, bronchitis, and so forth.
By means of along with the same of their diet. It is better if one consumes jaggery at the side of sesame seeds. This mixture is ideal for treating respiration troubles.

2. Helps With Weight Reduction
Weight benefit is an issue most of the people should deal with. A depended on remedy to foster weight reduction is a mild consumption of jaggery.
It is a great supply of potassium that helps balance electrolytes, boosting metabolism as well as constructing muscle groups.
Furthermore, potassium also can assist lessen water retention in one’s body. As a result, playing a main function in weight loss.

3. Controls Blood Pressure
The presence of potassium and sodium in jaggery helps preserve acid degrees within the body. This, in turn, keeps normal blood pressure levels.

4. Blood Circulation
Unlike sugar that gives short-lived electricity raise, jaggery affords slow power that lasts for an extended time.
This is because it’s Unrefined, which guarantees that blood sugar ranges aren’t altered right away and rises slowly as a substitute.
This, in flip, can assist save your fatigue as properly.

5. Relieves Menstrual Pain
Jaggery is a natural treatment to ease pain going on rom menstrual cramps.
Individuals who enjoy temper swings or frustration before their periods must devour the identical in small amounts. It helps to launch endorphins that loosen up one’s body.

6. Prevents Anemia
To save your anemia, it is required that good enough stages of RBCs are maintained inside the frame at the side of iron and folate.
aggery is wealthy in each iron and folate, subsequently, a terrific manner to save anemia. Doctors often advise its intake to adolescents and pregnant women.

7. Purifies The Body
Human beings commonly consume jaggery after food due to the fact that it is one of the great herbal cleansing retailers for the body.
Eating this food can help take away all forms of undesirable particles from the body. Such as intestines, belly, meals pipe, lungs, and the respiration tract effectively.

8. Cleansing The Liver
Jaggery is a natural cleansing agent, specifically for the liver. The herbal sweetener helps flush out dangerous pollution from the body.
This further allows to detoxify the liver. Therefore, the ones stricken by illnesses related to the liver must begin eating jaggery.

9. Prevents Constipation
Consumption of the nutrient-packed sweetener facilitates to stimulate bowel actions and activation of digestive enzymes in one’s body.
After eaten a heavy meal, simply devour a number of this nutritious natural sweetener. It reduce the hazard of constipation.

10. Remedy Of Cold And Cough
Jaggery additionally enables cure flu-like signs consisting of cold and cough. It leads to the production of warmness in one’s body.
Result higher benefits, do mix jaggery in warm milk or use it as a sweetener to your tea.

11. Reduces Joint Ache
For people tormented by arthritis or any form of pain inside the joints, the consumption of jaggery can provide significant ache relief.
When eaten with ginger, the effectiveness most effective improves.

12. Purifies Blood
Intake of jaggery on a normal basis in slight amounts can useful resource in blood purification. That is also the motive why it’s powerful in treating zits or acne as cleanser blood also manner healthier skin. Moreover, the whole hemoglobin count in blood additionally will increase with the consumption of the right quantity of it.

13. Boosts Immunity
Antioxidants and minerals like selenium and zinc are found in considerable portions in jaggery.
his allows in stopping free radical damage along with constructing resistance in opposition to various infections. That is why it is eaten often in winters.

14. Treatments Urinary Tract Issues
Sugarcane is a herbal diuretic, so jaggery too possesses this property. Decreasing inflammation of the bladder, stimulating urination and improving the easy float of urine.
These some issues that regular intake of this nutritious meals object can easily assist with.

15. Maintains Intestinal Fitness
Jaggery is wealthy in magnesium. Each 10 g of the meals includes 16 mg of the mineral. So, if one consumes even 10 grams of it, they would’ve fulfilled 4% each day requirement of this mineral in our lives. Therefore, ingesting it on a every day basis can lead to properly intestinal fitness.""",100.00,78.00),    
            
        ],
     
     "Sex Life":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Amukkara Powder(SPL. Ashwagandha) 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/2.png","""Description
             Benefits of Ashwagandha:
• It helps to reduce level of stress and tension.
• It improves energy level.
• It supports better sleep.
• It helps to lower blood pressure and is highly effective in stopping the formation of stress induced ulcers.
• It increases haemoglobin and hair melanin.
• It stabilizes blood sugar and lowers cholesterol.
• It helps to reduce stress during a weight loss diet. When a person is stressed more Cortisol hormone is produced by the adrenal glands. Cortisol stimulates glucose production and triggers a hunger response in the brain. Ashwagandha can naturally lower cortisol levels up to 26%. It also helps to lose weight by reducing swelling in body and improving haemoglobin level.
• It is useful for any imbalance in the muscles as it reduces inflammation and strengthens muscles. It is an anabolic muscle builder. As it benefits all muscle tissue it is used as a heart tonic, uterine tonic, and lung tonic.
• It improves body immunity and strengthen body defense system. This makes this herb suitable for treating Auto-immune conditions such as neutropenia, rheumatoid and osteo arthritis, cancer and chronic connective tissue disorders.
• It gives good results in nerves related conditions such as Multiple sclerosis, Neurosis, insomnia, anxiety, and stress.
• It is used to enhance memory and lesson age-related cognitive deficits.

Benefits for Men:
• For males, Ashwagandha promotes sexual health by uplifting the mood, reducing anxiety, improving energy levels and fertility, thus supporting sexual performance.
• It has direct spermatogenic effect and helps to improve sperm count.
• It helps to alleviate asthenospermia (increasing sperm motility), oligospermia (increasing sperm count) and other sperm disorders.
• It exerts something like testosterone, influencing the seminiferous tubules.
• It promotes better sexual performance.
• It reduces impotence and promotes potency.

Benefits for Women:
• It contains phytoestrogen.
• It relieves females from menstrual imbalance.
• It stimulates secretion of breast milk in lactating mothers.
• It gives strength and cures debility when consumed post – delivery.
• It supports female reproductive system, and increases ovarian weight and folliculogenesis.""",1260.00,630.00),
            ("Drumstick Seed/Murungai Vithai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/3.jpg","""Description
Benefits of Murungai Vithai:
1. Ayurvedic Medicine to Lower Blood Pressure:High blood pressure is a serious cardiovascular issue that can lead to heart attacks and stroke if it isn’t managed. While studies have shown that moringa can lower blood pressure, these studies are preliminary and more research needs to be done on humans, so talk to your doctor before stopping any prescribed treatment for high blood pressure.

2. Siddha Medicine to Boost Energy:A single serving of moringa has almost three times the amount of iron as spinach. This is especially important for vegetarians/vegans and those who suffer from low iron issues, as the body needs iron to enrich the blood and carry oxygen to our muscles, organs, and tissues.

3. Paatti Vaithiyam to Lower Blood Sugar Levels: Moringa seeds can lower blood sugar levels, which would provide therapeutic management (or even prevention) of diabetes. However, the study was done on lab rats and research is needed on humans before any recommendations can be made.

4.Natural food with High Fiber: Moringa is high in fiber, and as a result it can do a great job of moving food along your digestive system. Fiber is also a key component in maintaining a healthy cardiovascular system.

5. Natural way to Lower Cholesterol:Too much cholesterol in the blood has been linked to heart disease. In traditional Tamil medicine, moringa is used as a Cardio tonic. Some plants have been known to reverse bad cholesterol and research is showing that moringa is among them.

6.Herb to Promote Healthy and Beautiful Skin:The oil extracted from the seeds contains almost 30 antioxidants. The skin absorbs the oil well and can receive these nourishing antioxidants easily. The oil can be used as a moisturizer and antiseptic.""",100.00,90.00),
            ("Oridhazh Thamarai Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/4.jpg","""Description
Benefits of Oridhazh Thamarai:
• For Men: Oridhazh Thamarai has shown increase in the testosterone level in males and also has aphrodisiac properties.
• Hypolipidemic Activity: Oridhazh thamarai has cholesterol lowering properties, regular intake of Oridhazh thamarai will result in reduction of cholesterol significantly.
• Antioxidant & Anti Diabetic activity: Oridhazh thamarai has amazing anti oxidant properties which helps reduce oxidative stress very effectively. It also reduces blood sugar levels.
• For Treating Anaemia: Another important use of Oridhazh thamarai is its amazing ability to treat anaemia as the extract of Oridhazh thamarai has high amounts of iron.
• For Reducing Body Heat: The decoction of the plant is used for reducing body heat, this use is quite famous and is followed in villages. The extract also has anti allergic and pain reducing properties.""",44.00,40.00),
            ("Karunjeeragam Oil 50ml","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/5.jpg","""Description
Benefits of Karunjeeragam Oil:
Primarily used for massaging the penis. It is said to increase size and girth.
Reducing high blood pressure: Taking black cumin seed extract for two months has been shown to reduce high blood pressure in people whose blood pressure is mildly elevated.
Reducing high cholesterol: Taking black seed oil has been shown to reduce high cholesterol. It’s high in healthy fatty acids that can help you maintain healthier cholesterol levels. Examples of these fatty acids include linoleic acids and oleic acid. The levels of the oils can vary depending on where the black seeds are grown. People may also see results when consuming the crushed seeds.
Improving rheumatoid arthritis symptoms: Taking oral black seed oil may help to reduce inflammatory rheumatoid arthritis symptoms.
Decreasing asthma symptoms: The anti-inflammatory effects of black seed oil may extend to improving asthma symptoms. Its effect in reducing inflammation in the airways may also help with bronchitis symptoms.
Reducing stomach upset: Eating black seeds or taking black seed oil is associated with relieving stomach pain and cramps. The oil can help to reduce gas, stomach bloating, and the incidence of ulcers as well.
Black seed oil is also thought to have anticancer properties. It may help fight against skin cancers when applied topically.
Portions of black seed oil known as thymoquinone and other seed potions were able to reduce the growth of tumors in lab rats. The oil also may help to reduce the tissue damaging effects of radiation that is used to kill cancer cells. But these results haven’t been studied in humans. Black seed oil shouldn’t be used as a substitute for conventional cancer treatments.
Black seed oil beauty benefits

Black seed oil has several applications and benefits for problematic skin conditions. The oil is found in many health foods stores and pharmacies. Examples of applications for beauty and skin include:

• Acne: According to the Journal of Dermatology & Dermatologic Surgery, applying a lotion prepared with 10 percent black seed oil significantly reduced the incidence of acne after two months. Those who participated in the study reported 67 percent satisfaction.
• Hydrating hair: Black seed oil can be applied to human hair to soften it and promote shine.
• Psoriasis: Applying black seed oil has been shown to reduce the incidence of psoriasis plaques.
• Softening skin: Black seed oil has been added to oils and moisturizers to improve skin moisture and hydration.
• Wound healing: Application of black seed oil has been shown to reduce inflammation and the presence of bacteria to aid in wound healing. While it doesn’t seem to be helpful in growing new collagen fibers, it does stimulate other growth factors to help the body create new, healthy skin.""",200.00,180.00),
            ("Moringa/Murungai/Drumstick Flower Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/6.jpg","""Description
Benefits of Murungai/Drumstick flowers:
Drumstick flowers are a rich source of amino acids, potassium and calcium, making them a vital supplement for nursing mothers.
Flowers are brewed as a medicinal tea and consumed as a health tonic to treat urinary tract infections.
Its flowers are the best supplement for breastfeeding women as it helps increase the flow of milk and its nutritional value.
It is beneficial in weight management due to its powerful diuretic content that helps reduce bloating and water retention.
It has potent antibiotic agents present in drumstick flowers help combat infection.
The Drumstick flower protects against tissue damage and strengthens the liver function.
Studies have found the Drumstick flower to be useful in the treatment of impotence and sexual dysfunctions.
Due to mild fragrance and antioxidant benefits for the skin, it is used in the preparation of cosmetics and perfumes including hair oils.""",100.00,90.00),
            ("Poonaikaali Seed Powder/Poonaikaali Vithai Podi 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/7.jpg","""Description
Benefits of Poonaikali:
• Increases libido.
• Increases sperm count in men and ovulation in women.
• Acts as a restorative nutrient for the nervous system.
• Increases blood circulation to the genitals.
• Decreases symptoms of stress and anxiety. Calms nerves.
• Reduces inflammation.
• Strengthens and tones the sexual glands.
• Increases stamina.
• Releases bound up testosterone, increasing the level of bio-available testosterone.
• Reduces fat and improves muscle tone. (By supporting healthy testosterone levels, Mucuna pruriens supports anabolic metabolism, increasing your tendency to burn fat and to build muscle.)""",100.00,80.00),
            ("Kadal Paasi(Badham Pisin) 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/8.jpg","""Description
Benefits of Kadal Paasi(Badham Pisin):
It is extensively used to reduce body heat.
It is useful in reviving the menstruation cycle to its original format.
Also, it’s said that if taken with milk and sugar, Badham Pisin can help increase weight and immunity.
Way of Consumption:
Before going to bed, mix KADAL PAASI in a glass of water and allow it to change into a jelly-like substance overnight. Then in the morning, before breakfast, consume the perfectly jelly-like Badham Pisin.""",60.00,50.00),
            ("Vettiver Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/body heat/6.jpg","""Description
Benefits of Vettiver:
Vetiver water is very cooling. It helps to cure painful urination, ulcers and bad breath.

This aromatic water has a calming effect on the nerves and regular intake of this water helps in general well being and it acts as a blood purifier.

Eye burning, head ache, fever, hair care & used for bath powder.""",80.00,60.00),
            ("Nilapanai Kizhangu/Black Musli Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/9.jpg","""Description
Benefits of Nilapanai Kilangu:
• Restorative tonic, to cure weakness, sexual debility.
• Aphrodisiac, Premature ejaculation, better performance, impotence.
• Low sperm count, impotence, general body weakness, loss of stamina and vigor, and to gain weight.
• For itches and skin diseases.
• The poultice of root is used, it cures Piles.
• Application of root paste on pile, gives relief in pain and burning sensation.
• Cough, cold and asthma.
• Black Musli acts as diuretic and boosts the resistance of urinary system against infections.

Search Terms: Nilappanai Kilangu Podi, Nilappanai Kilangu Powder, Nilapanai Kilangu Podi, Nilapanai Kilangu Powder""",80.00,60.00),
            ("Moringa/Murungai/Drumstick Seeds 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/10.jpg","""Description
Benefits of Murungai Vithai:
1. Ayurvedic Medicine to Lower Blood Pressure: High blood pressure is a serious cardiovascular issue that can lead to heart attacks and stroke if it isn’t managed. While studies have shown that moringa can lower blood pressure, these studies are preliminary and more research needs to be done on humans, so talk to your doctor before stopping any prescribed treatment for high blood pressure.
2. Siddha Medicine to Boost Energy: A single serving of moringa has almost three times the amount of iron as spinach. This is especially important for vegetarians/vegans and those who suffer from low iron issues, as the body needs iron to enrich the blood and carry oxygen to our muscles, organs, and tissues.
3. Paatti Vaithiyam to Lower Blood Sugar Levels: Moringa seeds can lower blood sugar levels, which would provide therapeutic management (or even prevention) of diabetes. However, the study was done on lab rats and research is needed on humans before any recommendations can be made.
4.Natural food with High Fiber: Moringa is high in fiber, and as a result it can do a great job of moving food along your digestive system. Fiber is also a key component in maintaining a healthy cardiovascular system.
5. Natural way to Lower Cholesterol: Too much cholesterol in the blood has been linked to heart disease. In traditional Tamil medicine, moringa is used as a Cardio tonic. Some plants have been known to reverse bad cholesterol and research is showing that moringa is among them.
6.Herb to Promote Healthy and Beautiful Skin: The oil extracted from the seeds contains almost 30 antioxidants. The skin absorbs the oil well and can receive these nourishing antioxidants easily. The oil can be used as a moisturizer and antiseptic.""",100.00,80.00),
            ("Velvet Bean/Poonaikaali Seeds 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/11.jpg","""Description
Health Benefits of Poonaikaali Seeds
Increases libido.

Increases sperm count in men and ovulation in women.

Acts as a restorative nutrient for the nervous system.

Increases blood circulation to the genitals.

Decreases symptoms of stress and anxiety.

Calms nerves.

Reduces inflammation.

Strengthens and tones the sexual glands.

Increases stamina.

Releases bound up testosterone, increasing the level of bio-available testosterone.

Reduces fat and improves muscle tone.(By supporting healthy testosterone levels, Poonaikali Seeds[Mucuna pruriens] supports anabolic metabolism increasing your sex and tendency to burn fat and to build muscle.)""",80.00,60.00),
            ("Fig/Atthipalam 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sex ife/12.png","""Description
Health Benefits of Figs/Atthi Fruits:
1: Helps Relieve Constipation:
Figs are well-thought-out to be an age-old remedy to cure constipation and thus help nourish the intestines. Figs act as a natural laxative due to their high soluble fibre content. Thus, eases out the strained bowel process. Try consuming 2 to 3 dry figs empty stomach to help relieve constipation.
2: May Aid Weight Loss:
Fibre-rich anjeer can be a perfect snack or mid-morning munchies, especially for weight watchers. Dried Anjeer makes a great nutritious snack. 2 or 3 dried figs can make you feel fuller for longer and this can help keep longer gaps between your two meals.
3: Might Control Blood Pressure:
Fast-food consumption has been increasing day by day and this can lead to high blood pressure problems. High blood pressure often leads to an imbalance of potassium levels in your body. Figs being a good source of potassium can naturally improve potassium levels and thus might control blood pressure.
4: Can Improve Digestive Wellness:
Figs are a great source of prebiotics. Prebiotics can support the function of probiotics which can help improve the digestion process and overall gut health. Being fibre-rich, also adds bulk to the stool, enabling normal bowel movement.
5: Figs for Fertility:
Figs were reflected as love fruit since ancient Greek times, where figs were considered a symbol of fertility. This was later researched and was termed true based on its high iron content. Iron plays an essential role in the entire ovulation process in females. For males, low iron may affect sperm quality and motility. It is very commonly consumed with milk even today to boost reproductive health.
7: Improves Heart Health:
Being high in fibre and potassium helps remove the excess fat from the body and pressure from the heart. This can drastically help improve the health of your heart. Along with these two functions, Figs are also a great source of antioxidants which not only reduces the free radicals but also helps reduce triglycerides and bad cholesterol. Therefore, making your heart stronger and letting it live for longer.""",120.00,100.00),
            
        ],
     "Stomach Pain":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/stomach pain/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/stomach pain/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/stomach pain/3.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("Thiribala Podi/Triphala Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/stomach pain/4.jpg","""Description
About Thiripala/Thiribala:
Thiripala is one of the most famous ayurvedic formulations that is popularly used all over the world. As the word Thiripala suggests, it is made of three famous ayurvedic ingredients, Kadukkai, Thanrikkai and Nelli. The botanical name of Kadukkai is Terminalia Chebula, Thanrikkai is Terminalia Bellirica and Nelli is Emblica officinalis. It has wonderful uses and benefits. Thiripala is an amazing medicine that has wide medicinal uses.

Benefits of Thiripala/Thiribala:
• Ayurvedic Medicine For Weight Loss: Thiripala is a very amazing colon cleanser and helps remove toxins from the body. A good and effective digestive system is the key to healthy weight loss and Thiripala helps to achieve it effortlessly. Thiripala also treats all digestive related problems. Thiripala also boosts metabolism and greatly aids weight loss when it is combined together with a good diet and exercise regimen.

• Siddha Medicine For Constipation: Kadukkai, one of the three ingredients that makes Thiripala is very very well known for its use in treating constipation. For treating constipation take Thiripala mixed with warm water before going to bed. Thiripala is one of the safest and best medicines for treating constipation.

• Tamil Medicine For Arthritis: People who are suffering from arthritis should consider taking Thiripala in proper dosage thus greatly prevents further bone and cartilage degradation.

• Natural Medicine For Diabetes: Thiripala is a boon for diabetic patients and has a significant effect in reducing the blood sugar levels. Within 4 hours of Consumption Thiripala reducing the blood sugar levels significantly.

• Herbal For Hair Care: Thiripala when applied as a hair pack treats dandruff and stimulates hair growth. It also greatly prevents hair loss due to scalp problems.

• Paatti Vaithiyam For Skin Care: Thiripala when applied as a face mask is great for treating and preventing acne. This is an amazing home remedy for treating acne.

• Triphala For Eyes: Thiripala is great for improving the eyesight both when taken internally and used as an eyewash.

How to Consume Thiripala/Thiribala Powder:
Morning – Mix 5 gms of powder in 100 ml of water or honey and drink it before eating food. Repeat the same for Evening Dosage after dinner.""",52.00,42.00),
            ("Paalkaayam 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/stomach pain/5.jpg","""Description
Benefits:
Asafoetida gum (Palkaayam) is often referred to as "original" Hing (Asafoetida).

Roll it into small balls and dry them in the shade at home using a large plate.

Using a ball about the size of three black peppercorns is enough for cooking.

Once dried properly (so that the balls don't stick together), store them in a spice box, and add one ball daily while cooking curry.

Make sure to add mustard seeds (kadugu) while tempering. If not, the ball may remain undissolved and be consumed whole by someone — leading to an overpowering flavor!

Until you grind your curry powder, you can also soak the Palkaayam ball in water, and once it dissolves, add that liquid into the curry.

Palkaayam has a very strong aroma, so a little goes a long way.

""",50.00,40.00),
            ("Ajeeranaa Powder 225g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/stomach pain/6.png","""Description
Ajirna Podi (Indigestion Relief Powder):

Helps flush out all accumulated waste and toxins from the body smoothly — just like a banana peel sliding effortlessly. Say GOODBYE to constipation from now on!""",800.00,650.00),
            ("Attathi Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/stomach pain/7.jpg","""Description
Ingredients:
1)Sukku
2)Thippili
3)Milagu
4)Seeragam
5)Karunjeeragam
6)Indhuppu
7)Omam
8)Perunkaayam

Benefits of Attathi Podi:
Indigestion 
Loss of Appetite
Quadraplegia""",90.00,80.00),
        ],
     "Sugar":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sugar/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sugar/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Puri K Oil/Karisalankanni Oil 225 ML","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sugar/4.png","""Description 
Karisalankanni Oil (Food Grade)
For Internal & External Use
FREE Spoon Included

How to Use
For Internal Consumption:
Dosage: 1 spoon daily (on an empty stomach)

Benefit: Greatly supports liver and lung health

“If consumed regularly, this oil can significantly enhance the function and strength of the liver and lungs.”

For External Application:
Dosage: 2 spoons every 3 days

Hair Care: Apply to the roots of the hair to reduce greying and hair fall while promoting thicker growth

Skin Care: Apply on face, hands, and legs for a natural golden glow and a more youthful appearance

Eye Care: Gently apply to eyelids to support better vision

Ingredients (per 100ml):
Common Name	Scientific Name	Percentage
Karisalankanni Juice	Eclipta prostrata	85%
Gingelly Oil (Sesame Oil)	Sesamum indicum	15%

Preparation Method
This oil is carefully processed by blending fresh Karisalankanni extract with first-quality, food-grade sesame (gingelly) oil.

It’s noteworthy that Karisalankanni is also a key ingredient in the making of “Thangapashpam”, a traditional rejuvenating formulation.""",3000.00,2120.00),
            ("Aavaarampoo Powder/Avarampoo Podi 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sugar/3.jpg","""Description
              Description
Benefits of Aavaaram poo:
Aavaarampoo for diabetes:
Aavaaram flowers have cooling and dehydrating effects. Aavaarampoo juice is also effective for diabetic people. The properties of this plant help to reduce the sugar level in the blood effectively.

Aavaarampoo for Urinal issues:
These amazing flowers leave amazing effects on bowel movements and works as the very effective, natural laxative. The plant extract cleanses urinary system. Aavaarampoo tea is a good source of antioxidant that is good for health.

Aavaarampoo beauty benefits:
People use Aavaarampoo as a beauty treatment.

Aavaarampoo for hair:
It is used for hair care to remove dandruff.

How to Consume Aavaarampoo:
Morning: Mix 5 gms of powder in 100 ml water and boil it for a few minutes. Once the water gets warm, filter the content and drink it before food. Repeat the same for Evening Dosage after dinner. For excessive urination, take 1-2 gm of this powder with cow’s milk twice a day.

Applying Aavaarampoo powder:
• Aavaarampoo beauty benefits:
If you wish to get fair complexion then mix the flower powder with Bengal gram and green gram flour. Add little water or rose water to make a paste. Use this paste while taking bath. The regular usage will give you fairer complexion easily. Flower powder is also available in the market.

• Aavaarampoo Powder for hair:
Aavaarampoo powder (podi) and aloe vera gel is mixed with fenugreek(vendhayam) powder and applied on the scalp to treat dandruff.""",33.00,30.00),
            ("Sirukurinjan/SirukurinjaanPowder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sugar/5.jpg","""Description
Benefits of Sirukurinjan Powder:
•Good remedy for Diabetes Mellitus: It is said that long administration of this medicine can even eliminate Sugar present in Urine. High doses of this medicine may help to regenerate Beta cells of Pancreas study and research says.

•Used for Sexual dysfunction and Pyurea and also for Obesity, Hypercholesterol.

•It cures wounds due to snake bite.

•It cures Cough, Rhinitis and Asthma.

•Leaves cure gastrointestinal disorders like Constipation and Gas trouble when given as powder or infusion.""",55.00,50.00),
            ("Naaval Seed Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sugar/6.jpg","""Description
Benefits of Naaval Seed:
• Regulates Blood Sugar Level: Jamun fruit is very good remedy for the people suffering from diabetes because of its anti-diabetic properties which helps keeping blood sugar level under control by converting starch and sugar into the energy. Another study showed that jamun seeds could lower blood sugar levels by 30%.

• Good For Diabetics: The low glycaemic index, in Jamun, makes it a good option for diabetics. A study conducted on the anti-diabetic effects of Jamun, suggests that it holds significant potential to produce safer drugs for diabetes treatment. The fruit is associated with lowered risk of secondary complications of diabetes. The leaves, barks, and seeds are the most useful parts among which the seeds are popular for their anti-diabetic properties.

• Good for heart health: Jamun is loaded with nutrients like ellagic acid / ellagitannins, anthocyanins and anthocyanidins which has the anti-inflammatory property and these compounds are also powerful antioxidants that prevent oxidation of cholesterol and plaque formation that contributes to heart disease.

• Acts as a Blood Purifier: Black Plum has adequate amount of iron and vitamin C. The presence of iron in the black plum is good to increase the hemoglobin count. The fruits iron content acts as blood purifying agent.

• Improves Bone Strength: The fruit also has healthy amount of nutrients like calcium, iron, potassium and Vitamin C, which makes it great for boosting immunity and bone strength.

• Treats Infections: The fruit as well as the other parts of the plant has compounds like malic acid, gallic acid, oxalic acid and tannins which makes the fruit as a anti-malarial, anti-bacterial, anti-infective and gastro protective properties.

• Cures Digestive Disorders: Jamun has cooling property thus very beneficial for curing digestive disorders.

• Fights Anemia: The Jamun fruit is rich in Iron content and daily eating of this fruit, cures anemia and jaundice and also good for ladies who suffers for menstrual problems.

• Increases Immunity: Its high level of vitamin C availability makes body immunity system strong to fight with common seasonal problems.""",50.00,40.00),
            ("Thean Kaai/Thaen Kai 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sugar/7.jpg","""Description
Benefits of Thean kai:
The seeds of this herbal medicinal plant are used to control Blood sugar levels or in the Treatment of Diabetes. The patient has to consume two seeds in the morning and two seeds in the evening for the first week. This dosage can be varied according to the individual’s body conditions. have little water after taking seeds.

In Indian Traditional Medicine this herbal plant is also used to promote Long life, Take care of skin complaints, Reduce fever, Treatment of asthma, Bronchitis treatment. It is very powerful against intestinal worms.""",100.00,80.00),
            ("Avarampoo/Aavaarampoo 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sugar/8.jpg","""Description
Benefits of Aavaaram poo:
Aavaarampoo for diabetes:
Aavaaram flowers have cooling and dehydrating effects. Aavaarampoo juice is also effective for diabetic people. The properties of this plant help to reduce the sugar level in the blood effectively.

Aavaarampoo for Urinal issues:
These amazing flowers leave amazing effects on bowel movements and works as the very effective, natural laxative. The plant extract cleanses urinary system. Aavaarampoo tea is a good source of antioxidant that is good for health.

Aavaarampoo beauty benefits:
People use Aavaarampoo as a beauty treatment.

Aavaarampoo for hair:
It is used for hair care to remove dandruff.""",40.00,30.00),
            ("Paneer/Panneer Poo 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sugar/9.jpg","""Description
Paneer poo is a flower that is native to India, Pakistan & Afghanistan. It is known to have medicinal properties and is great for diabetics. In addition, it not just utilizes the blood glucose but also repairs the beta cells of the pancreas. It promotes the secretion of insulin in the right amount. The herb promotes the depletion of blood sugar with improvement in glucose utilization and carbohydrate metabolism. It lowers the complication of hyperglycemia. The usage of anti-diabetic drugs and insulin is lowered on the regular use of Paneer Poo.

Benefits of Paneer Poo:
Best medicine for Diabetes.
Cures Asthma.
Purify the blood.
Teeth Cleaning.
Reduces Body aches.
Improves Physical Stamina.
Healing of wounds.
Nervous Exhaustion.
How to Use :
Soak about 10 – 15 pods of Paneer Poo in a glass of water overnight. Squeeze them to bring out their extract in the water. Filter it through a sieve and drink it in the morning(on empty stomach).
Take care if you are on a prescription medicine since it immediately gives results, your blood sugar may fall. Therefore, regularly test your blood sugar levels and adjust the dose of medicine with your physician’s advice.""",100.00,80.00),
            ("Sweet Basil Powder/Inippu(Seeni) Thulasi Podi 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/sugar/10.jpg","""Description
Inippu Thulasi Health Benefits:
• Stevia leaves do not contributes calories and carbohydrates to the dies.
• It can be used for people with diabetes, it helps to control the sugar level of the blood.
• Certain glycosides in stevia extract have been found to dilate blood vessels.
• Cardiotonic actions of this stevia leaves are normalizing blood pressure and regulate the heartbeat.
• Using these leaves is also helps to control the weight.
• Foods and beverages containing stevia can play an important role in decreasing calories from unwanted sweeteners in the diets of children.""",50.00,40.00),
        ],
     "Weight Loss":[
            ("Kayakalpa/Kaayakalpaa Kit 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/weight loss/1.png","""Description
KAAYAKALPAA KIT ✨
Contains:
SPL. Arokiya Podi, SPL. Ashwagandha Podi, Paarvai Podi, and Food-Grade Karisalankanni Oil.

1 – Karisalankanni Oil
Take one spoon of this oil on an empty stomach right after waking up in the morning.

It mainly supports vital organs like the lungs, liver, kidneys, and pancreas. When these organs function properly, there's a 99% chance your body won’t face most common health problems.

2 – SPL. Arokiya Podi (Health Mix)
Take one spoon of this powder morning and night after food, mixed in plain water.

This powder helps absorb good fat and eliminates bad fat effectively.

It’s made with age-old ingredients like dry ginger, pepper, long pepper, asafoetida, and carom seeds—what our grandparents used to keep in their kitchen remedies. Given today’s food habits, this has become very necessary!

3 – Paarvai Podi (Vision & Sugar Support)
Take one spoon of this powder in the afternoon.

It helps keep your blood sugar under control and ensures your vision stays sharp and consistent without decline.

4 – SPL. Ashwagandha Podi
Take one spoon of this powder at night before sleep, mixed in milk and boiled.

This helps improve blood quality, strengthens the nervous system, and is especially beneficial for the heart. It’s great for restful sleep and overall vitality.

Who Can Use This Kit?
This can be used by everyone—from 2-year-old children to elders over 80.

We do not use any chemicals or preservatives, so it’s completely safe with no side effects—we guarantee it.

Usage Advice
Eat wholesome, nutritious food.

If you're eating outside food, make sure you definitely use the Arokiya Podi, especially because most restaurants today add MSG (Ajinomoto) for taste, which is a major cause of health issues.

Avoiding that and taking this regularly can help you control conditions like:
Diabetes, Piles, High Blood Pressure, Hypertension, Heart Problems, Cholesterol, and more.""",4320.00,3376.00),
            ("SPL. Arokiya Podi/Powder 225g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/weight loss/2.png","""Description
Arokiya podi:
Sukku
Milagu
Thippili
Vaalmilagu
Paalkaayam
Narukkumoolam
Seendhilkodi
Peraratthai
Manjal
Omam
Aratthai

First and foremost benefit of Arokiya Powder is that it relieves you from indigestion due to heavy consumption of the following:

1.Food made from Maida(Wheat flour) such as Parotta, Pizza, Burger and Bajji
2.Almost all dishes made from Chicken
3.Almost all dishes made from Mutton
4.Almost all dishes made from Fishes

Very helpful in maintaining weight!

Other benefits of Arokiya Podi:

• To cure Common cold and cough
• Get rid of tiredness
• For body pain due to fever
• Regulates body function
• Treats headache due to cold & sinus problems
• Cures lack of appetite
• Cures Stomach ache
• Heals Fever and cough
• To heal ulcers
• Relieves constipation
• To remove toxins from the body
• To cure chronic lung problem

How to consume Arokiya Powder:
FOR CHILDREN: Mix 3gms of Arokiya Powder in either water or honey or a mixture of both and drink.
FOR ADULT: Mix 5gms of Arokiya Powder in either water or honey or a mixture of both and drink.""",2000.00,999.00),
            ("Thiribala Podi/Triphala Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/weight loss/3.jpg","""Description
About Thiripala/Thiribala:
Thiripala is one of the most famous ayurvedic formulations that is popularly used all over the world. As the word Thiripala suggests, it is made of three famous ayurvedic ingredients, Kadukkai, Thanrikkai and Nelli. The botanical name of Kadukkai is Terminalia Chebula, Thanrikkai is Terminalia Bellirica and Nelli is Emblica officinalis. It has wonderful uses and benefits. Thiripala is an amazing medicine that has wide medicinal uses.

Benefits of Thiripala/Thiribala:
• Ayurvedic Medicine For Weight Loss: Thiripala is a very amazing colon cleanser and helps remove toxins from the body. A good and effective digestive system is the key to healthy weight loss and Thiripala helps to achieve it effortlessly. Thiripala also treats all digestive related problems. Thiripala also boosts metabolism and greatly aids weight loss when it is combined together with a good diet and exercise regimen.

• Siddha Medicine For Constipation: Kadukkai, one of the three ingredients that makes Thiripala is very very well known for its use in treating constipation. For treating constipation take Thiripala mixed with warm water before going to bed. Thiripala is one of the safest and best medicines for treating constipation.

• Tamil Medicine For Arthritis: People who are suffering from arthritis should consider taking Thiripala in proper dosage thus greatly prevents further bone and cartilage degradation.

• Natural Medicine For Diabetes: Thiripala is a boon for diabetic patients and has a significant effect in reducing the blood sugar levels. Within 4 hours of Consumption Thiripala reducing the blood sugar levels significantly.

• Herbal For Hair Care: Thiripala when applied as a hair pack treats dandruff and stimulates hair growth. It also greatly prevents hair loss due to scalp problems.

• Paatti Vaithiyam For Skin Care: Thiripala when applied as a face mask is great for treating and preventing acne. This is an amazing home remedy for treating acne.

• Triphala For Eyes: Thiripala is great for improving the eyesight both when taken internally and used as an eyewash.

How to Consume Thiripala/Thiribala Powder:
Morning – Mix 5 gms of powder in 100 ml of water or honey and drink it before eating food. Repeat the same for Evening Dosage after dinner.""",62.00,42.00),
            ("Kadukkai Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/weight loss/4.jpg","""Description
Benefits of Kadukkai:
Weight loss: Kadukkai is known to remove toxins from the body and keeps the digestive system in peak order. It prevents bloating sensation, acidity and helps in proper assimilation of food. Kadukkai is a natural blood purifier and it helps to remove the toxins in the body. Consuming Kadukkai will regulate hunger and combined together with a sensible diet and exercise will aid in weight loss naturally.

Cough in infants and adults: Kadukkai is amazing for treating cough in both adults and infants.

Constipation: Kadukkai powder is a natural laxative that is available to us. Many suffer from constipation and take medicines for it continuously. Having a traditional diet that is rich in fiber and using natural laxatives like Kadukkai podi / powder will keep our bowels in good health.

Acidity: Kadukkai is known to cure all stomach related problems from acidity and indigestion to constipation very effectively. Kadukkai increases the mucus production in the stomach forming a protective barrier thus preventing acidity and ulcer.

Diabetes: Kadukkai decreases insulin sensitivity and helps to regulate the blood sugar levels in the body effectively. The interesting thing was many of the diabetic medicines had some side effects along with regulating the blood sugar levels whereas Kadukkai did not have any side effects at all. But diabetic patients should consult a medical professional before taking kadukkai daily on a regular basis.

Hair loss: In certain parts of India, Kadukkai oil is used on the hair to prevent lice infection and dandruff. They use it as a daily application hair oil.

Skin allergies: Kadukkai effectively treats skin allergies in the ears caused by earrings. Gold and silver earrings doesn’t produce any allergies. if we wear these earrings for longer duration, the earlobes turn itchy, red and swollen. Usually it gives good relief from pain and swellings due to allergies.

Mouth ulcers: Kadukkai has anti cariogenic properties and can be used for most of the dental problems especially mouth ulcers and bleeding gums.

Consuming Kadukkai Podi:
Mix a teaspoon of Kadukkai powder in either hot water or honey and consume before going to bed.""",65.00,50.00),
            
        ],
     "Powdered Products":[
            ("Vendhayam/Fenugreek Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/14.jpg","""Description
Benefits of Venthayam (Fenugreek):
Lowers Cholesterol

Fenugreek Seeds helps in reducing the body’s production of cholesterol, especially low-density lipo protein (LDL or bad cholesterol). The University of Michigan Health System discusses the relationship between Fenugreek Seeds and high cholesterol.

Herbal Medicine to control Diabetes and Lowers Blood Sugar Levels

4HO-Ile, an unusual amino acid, which is found only in Fenugreek Seeds, has possible anti-diabetic qualities, such as enhancing insulin secretion and increasing insulin sensitivity

One of Herbal Remedies to Aids Digestion

For those suffering from stomach ailments, eating Fenugreek Seeds can be really helpful. As it is rich in fiber and antioxidants, it helps in flushing out harmful toxins from the body and thus, aids digestion. It is an effective treatment for gastritis and indigestion. It helps prevent constipation as well as digestive problems created by stomach ulcers.

• Fenugreek Seeds is known to be an effective natural remedy for heartburn or acid reflux because the mucilage in Fenugreek Seeds assist in soothing gastrointestinal inflammation, and coats the stomach and intestinal lining.""",32.00,30.00),
            ("Drumstick Seed/Murungai Vithai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/15.jpg","""Description
Benefits of Murungai Vithai:
1. Ayurvedic Medicine to Lower Blood Pressure:High blood pressure is a serious cardiovascular issue that can lead to heart attacks and stroke if it isn’t managed. While studies have shown that moringa can lower blood pressure, these studies are preliminary and more research needs to be done on humans, so talk to your doctor before stopping any prescribed treatment for high blood pressure.

2. Siddha Medicine to Boost Energy:A single serving of moringa has almost three times the amount of iron as spinach. This is especially important for vegetarians/vegans and those who suffer from low iron issues, as the body needs iron to enrich the blood and carry oxygen to our muscles, organs, and tissues.

3. Paatti Vaithiyam to Lower Blood Sugar Levels: Moringa seeds can lower blood sugar levels, which would provide therapeutic management (or even prevention) of diabetes. However, the study was done on lab rats and research is needed on humans before any recommendations can be made.

4.Natural food with High Fiber: Moringa is high in fiber, and as a result it can do a great job of moving food along your digestive system. Fiber is also a key component in maintaining a healthy cardiovascular system.

5. Natural way to Lower Cholesterol:Too much cholesterol in the blood has been linked to heart disease. In traditional Tamil medicine, moringa is used as a Cardio tonic. Some plants have been known to reverse bad cholesterol and research is showing that moringa is among them.

6.Herb to Promote Healthy and Beautiful Skin:The oil extracted from the seeds contains almost 30 antioxidants. The skin absorbs the oil well and can receive these nourishing antioxidants easily. The oil can be used as a moisturizer and antiseptic.""",100.00,90.00),
            ("Maruthani Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/17.jpg","""Description
Benefits of Maruthani:
• Cooling agent: Maruthani is a great cooling agent. When applied to scrapes and burns it gives relief
• Cures Headaches: Maruthani is used as a medicine for headaches.
• Skin conditions: Maruthani can be used to treat skin conditions like athletes foot, rashes, and ringworm. It is also an effective sunblock.
• Nails: Maruthani is known for treating cracked nails. Mix Maruthani powder in water and drink to treat your cracked nails. Repeat for at least 10 days. You can mix butter with henna powder and use it as a poultice to treat sores filled with pus, manage, and scabies
• Arthritis: You can use Maruthani for arthritic and rheumatic pain.
• Hair: Maruthani contains natural ingredients important for hair nourishment. It shares a great bond with hair as it helps to penetrate, cleanse, and thicken the hair shafts which improve the quality of hair. Its also used to treat dandruff. It’s commonly used for coloring hair by mixing it into natural dyes. Maruthani leaves can be used to treat baldness.""",25.00,20.00),
            ("Thanneervittaan Kilangu Podi/Satavari Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/18.jpg","""Description
ABOUT:
Thaneervittan Kilangu / Satavari is also very good for the women in postnatal care procedures. It increases the lactation in mothers. It also adds nutrient in mothers milk in other words the child gets the milk which is filled with all nutrients required to have a balanced diet.

It can be consumed by women of almost all ages:

• It ensures right birth weight of the baby and birth defects during pregnancy period of time.
• It helps for the healthy growth of fetus.
• It can alter the hormone balance.
• It is also used for birth control and it regularizes the menstrual cycle. The form and dosage to address each requirement is decided only in consultation with the practitioners.
• It prevents and also cures premenstrual bloating.
• It functions as a rejuvenating tonic for women from the start of menstruation, throughout the cycle, ovulation, strength of the uterine during pregnancy,and also for smooth delivery.
• It is good for lactation.
• It helps to smoothed the transition of menopause stage because of its ability in balancing the hormones.

Benefits of Thaneervittan Kilangu (Satavari):
• Satavari for gastritis: Because of its bitter principles and coolant properties, it is very useful in treating gastritis.
• For Acne treatment: Because of its coolant nature and bitter principles, it is useful in blood imbalance disorders and skin conditions such as acne. Because it balances hormones, it is very useful against hormone imbalance induced acne.
• To enhance breast milk production: Almost all herbal lactation promoting medicines in the market contain Thaneervittan Kilangu as a very essential ingredient. It also helps in normal involution of uterus and helps to stop bleeding in the mother, in the initial few weeks after delivery. Hence, it is one of the ideal herbs to be used during lactation period. Apart from improving breast milk production, it also adds nutritive value to it, which helps the baby processing with milk. To treat many diseases such as gastritis, for aphrodisiac effect, anti aging effect, Satavari is often boiled with milk and administered.
• Satavari as gym supplement: Because of nutritive properties, coolant nature, anti aging effect, Asparagus Root Powder makes an excellent gym supplement. It helps to relieve tiredness quickly and also improves muscle mass. It is a very good nervine tonic. It is useful in epilepsy, schizophrenia and neurological disorders. Because of its coolant nature, it is very useful in relieving diabetic neuropathy. It is good for both diabetes and nerve irritation causing burning fingers and toes.
• Diabetic: Satavari when taken as a liquid contains healthy minerals that are essential for controlling blood sugar levels.""",44.00,40.00),
            ("Neem Leaves Powder/Veppilai Podi 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/19.jpg","""Description
Benefits of Veppilai( Neem leaves ):
• Antibacterial Potential:

One of the most widely recognized benefits of neem oil, leaves, tea, and every other derivative is its strong antibacterial and antimicrobial effects. This comes into play both internally and externally, which is why neem is considered to be such a general tonic for the immune system and as a simple way to keep your overall health better protected.

• Gastric Health:

Consuming neem has been directly connected with a reduction in inflammation in the gastrointestinal tract, which helps to reduce ulcers and a wide range of other intestinal issues, such as constipation, bloating, and cramping. It can also be used as a quick healing antidote for stomach flu and infections that can destroy beneficial bacteria in the gut.

• Diabetes Treatment:

The exact pathway of this beneficial effect of neem is somewhat unclear, but there is a connection between a lower deman for insulin in the body and the consumption of neem. Neem’s chemical components optimize insulin receptor function and ensure that the body is receiving appropriate amounts of insulin, which protects against the development of diabetes. Furthermore, for patients who have diabetes, neem can be used to minimize the dependence on insulin therapy.

• Malaria Treatment:

There has been some unconfirmed research that neem can effectively treat malaria symptoms and minimize the danger of the disease, but neem’s more common relationship to malaria is as a natural insect repellent that is nontoxic and highly effective in repelling mosquitoes, which are the main vectors of malaria.

• Reproductive Health:

Neem is widely used as a natural spermicide and birth control agent, as it is likely to reduce the chances of conception for both men and women without harming them in a toxic way. It lowers fertility levels without impacting libido and can even help treat or prevent certain sexually transmitted diseases.

• Neem for Dandruff:

The antifungal and antibacterial properties of neem make it very popular in shampoos and scalp cleansers, as it can help the skin remain hydrated and eliminate dandruff while strengthening your hair and improving the health of your hair follicles due to its antioxidant content. In fact, it is even used in traditional medicine to stimulate hair growth and prevent male-pattern baldness.

• Detoxifying Effects:

Whether you are using neem paste or leaves directly on the skin, consuming neem extracts in supplements or in some other form, the active ingredients in this one-stop pharmacy tree will help to rid the body of toxins. Neem has been known to stimulate the liver and kidneys, helping to eliminate toxins quickly and optimizing the body’s metabolic activities. A great deal of detritus accumulates on our skin every day, including germs, microbes, dust, and grime; neem paste can help neutralize those chemicals, pathogens, or dirt that can cause irritation or illness.

• Acne Treatment:

In terms of treating acne, which is one of the most widespread and challenging skin conditions to treat or eliminate, neem paste is recommended to eliminate much of grease and bacteria that can exacerbate the condition.

• Pore Size:

When neem paste is applied as a face mask, it works as an excellent exfoliant, and can also shrink pore size, which will help to prevent the development of blemishes and pimples.

• Fungal Infections:

You can apply neem paste or diluted neem oil directly onto infected areas of the body, including Athlete’s foot. The antifungal effects of neem’s active organic ingredients are rapid and highly efficient, leaving your immune system and skin intact""",25.00,20.00),
            ("Oridhazh Thamarai Powder 50g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/20.jpg","""Description
Benefits of Oridhazh Thamarai:
• For Men: Oridhazh Thamarai has shown increase in the testosterone level in males and also has aphrodisiac properties.
• Hypolipidemic Activity: Oridhazh thamarai has cholesterol lowering properties, regular intake of Oridhazh thamarai will result in reduction of cholesterol significantly.
• Antioxidant & Anti Diabetic activity: Oridhazh thamarai has amazing anti oxidant properties which helps reduce oxidative stress very effectively. It also reduces blood sugar levels.
• For Treating Anaemia: Another important use of Oridhazh thamarai is its amazing ability to treat anaemia as the extract of Oridhazh thamarai has high amounts of iron.
• For Reducing Body Heat: The decoction of the plant is used for reducing body heat, this use is quite famous and is followed in villages. The extract also has anti allergic and pain reducing properties.""",44.00,40.00),
            ("Arugampul Podi/Bermuda Grass Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/23.jpg","""Description
Health Benefits Of Arugampul:
• Arugampul juice is highly praised for its potent alkaline property. It works well by increasing the alkaline level and lowers acidity. To get instant relief from acidity take 3 teaspoons of Arugampul powder and mix it with a glass of water and consume.
• Arugampul juice is revered for its powerful detoxifying properties. The natural detoxify agent cleanses the liver and flushes out the toxins from the body. Arugampul is naturally high in chlorophyll and facilitates blood purification by removing harmful toxins.
• The goodness of Arugampul juice is beneficial to heal various skin ailments like eczema, psoriasis, treat wounds and fungal infections. Drinking Arugampul juice regularly on an empty stomach detoxifies the system and enhances the skin glow and radiance.
• Arugampul juice contains Cynodon Dactylon Protein Fractions or CDPF, a protein element responsible for triggering the immune system. In addition, it is also heaped with powerful antioxidants, vitamins A and C which scavenges free radical damages, avert chronic inflammation and keep diseases away.
• Also consumption of Arugampul juice regularly, keeps Blood Sugar level in check.
• Arugampul juice is an effective natural remedy to treat kidney stones and urinary tract infections. It functions well as a good diuretic by flushing out the toxins, getting rid of excess water and clears out kidney stones.""",18.00,15.00),
            ("Kuppaimeni Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/24.jpg","""Description
Benefits of Kuppaimeni:
• It is utilized for treating Brain related ailments namely, Alzheimer’s disease.
• It is helpful in combating Internal Bleeding such as uterine bleeding, nosebleeds, and bowel bleeding.
• It is useful in treating osteoarthritis.
• It cures Nerve related disorders like Amyotrophic Lateral Sclerosis, Neuralgia, Multiple Sclerosis and Sciatica.
• It alleviates Anemia and Tiredness.
• It is favorable in keeping away Cardiovascular disorders thus, promotes proper Blood Circulation. It detoxifies Blood.
• It treats enlarged spleen.
• It is helpful in treating dysentery.
• It relieves Allergic symptoms like Hay Fever, Hives.
• It is useful as a blood purification herb.
• It cures Throat Infections like Laryngitis.
• It relieves lung congestion.
• It is favorable in treating Hyperthyroidism.
• It alleviates Respiratory ailments like Cough, Bronchitis, Chest Congestion, Asthma, TB.
• It curbs High Blood Pressure and Blood Sugar Level.
• It efficiently works on strengthening the Immunity.
• It counters Bladder infections and formation of Kidney Stone.It helps in avoiding and dissolving the Kidney Stones.
• It is advantageous in getting rid of the invasion of Intestinal worms and parasites.
• It is a good herbal remedy for Women as it eases Labor Pains. It elevates the production of milk and nourishes the fetus.
• It is beneficial in curing Benign Prostatic Hyperplasia which may result in the enlargement of the Prostate Gland. It alleviates Prostatitis.
• It possesses Diuretic properties thus, it increases the Urine flow. It counters the problem of Bed Wetting in Children.
• It alleviates Muscle Pain and Joint Stiffness. Its leave relieve the condition of Gout, Rheumatism, Arthritis, Inflammation of the Tendons.
• The tea made from this is beneficial in countering Diarrhea.
• It curbs Edema as it shows diuretic like action.
• It eases out the Swollen Piles.
• It acts as a general health tonic.
• It is effective in getting rid of Hair troubles like Dandruff, Hair fall, Baldness. It adds shine and promotes growth of the Hair.
• It is a good herbal remedy for Skin problems like Acne, Eczema, Cuts, Scraps. It is effective in curing Burns and Wounds.
• It is utilized as a Mouth Wash to keep away Gingivitis, Mouth Sores and Plaque.""",50.00,40.00),
            ("Tulsi Powder/Thulasi Podi 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/26.jpg","""Description
Benefits of Thulasi:
• It has antibiotic, anti-viral, anti-bacterial and anti-carcinogenic properties.
• It helps in relieving from fever, headache, sore throat, cold, cough, flu and chest congestion.
• It is also beneficial in treating respiratory ailments like chronic bronchitis, asthma et cetera.
• Helps relieve stress, strengthen immunity, and facilitate proper digestion.
• It is loaded with phytonutrients, essential oils, Vitamin A and C
• Regular tulsi consumption can also aid in balancing various bodily processes.
• It counters elevated blood sugar levels and is therefore beneficial for diabetics.
• It helps in regulating uric acid levels in body, thereby elimination risks of developing kidney stones. It is also beneficial for those who have kidney stones.
• It can wards off harmful effects of free radicals.
• Is also beneficial in treating conditions like hepatitis, malaria, tuberculosis, dengue and swine flu.
• It acts as a detoxifying, cleansing and purifying agent – both from within and without.
• Therefore it is good for skin – both when consumed and applied topically.
• It is also effective in treating skin disorders, itching and issues like ringworms.
• Is great for dental health and for healthy gums
• Is an effective insect repellant and can aid in treating insect bite.""",18.00,15.00),
            ("Kalarchikai/Klachikai Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/28.jpg","""Description
Benefits of Kalarchikai:
• It has been used for treating intestinal worms, fever, tumors, cough, amenorrhea, and to remove the placenta after childbirth.
• Kalarchikai is used for eliminating piles, wounds, leucorrhea, and urinary disorders.
• It can be used for gargling to relieve a sore throat.
• It is used in controlling elephantiasis and smallpox.
• It is good for Hernia patients.

• It may be roasted in castor oil and be applied to reduce piles, inflammatory swellings, orchitis, and hydrocele.
• A paste made from the leaves and twigs is useful in reducing toothache.

Way of Consumption:
You have to consume Kalarchikai Podi in the morning(empty stomach)!

You can take a banana with our powder as it will be very bitter or you may mix the powder with water and drink for effectiveness!

""",55.00,50.00),
            ("Poonaikaali Seed Powder/Poonaikaali Vithai Podi 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/29.jpg","""Description
Benefits of Poonaikali:
• Increases libido.
• Increases sperm count in men and ovulation in women.
• Acts as a restorative nutrient for the nervous system.
• Increases blood circulation to the genitals.
• Decreases symptoms of stress and anxiety. Calms nerves.
• Reduces inflammation.
• Strengthens and tones the sexual glands.
• Increases stamina.
• Releases bound up testosterone, increasing the level of bio-available testosterone.
• Reduces fat and improves muscle tone. (By supporting healthy testosterone levels, Mucuna pruriens supports anabolic metabolism, increasing your tendency to burn fat and to build muscle.)""",100.00,80.00),
            ("Semparuthipoo/Sembaruthi Podi Hibiscus Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/30.jpg","""Description
Benefits of Semparuthipoo(Hibiscus):
Controls High Blood Pressure & Cholesterol Levels

Cures Cold : Hibiscus is rich in Vitamin C and thus it has the capacity to cure cure minor cold related infections like sore throat, cough and headache.

Boosts Energy : As the antioxidants in hibiscus help to repair free radical damage, your energy levels naturally go up.

Calms Hot Flashes : Women who are going through the tough hormonal period of menopause might use the health benefits of hibiscus. Hibiscus can help soothe hot flashes.

Slows Ageing : The antioxidants in hibiscus not only help to fight cancer but also also slow down the ageing of your cells. As a result, it may be the secret to eternal youth.

Boost Immunity : One of the main health benefits of hibiscus flower is that it helps to boost the level of immunity in your body.

Maintains Fluid Balance : According to ancient sources, having hibiscus flower extracts can help to maintain the fluid balance in your body. It was once used as a cure for oedema or excess water retention in the body.

Speeds Up Metabolism : Vitamin C has a very essential place in the digestive system. And as hibiscus is rich in Vitamin C, it helps to increase the rate of metabolism.

Maintains Body Temperature : According to ancient African medicine, having hibiscus flower extracts regulates the body temperature. It helps to flush out excess body heat in summers.

Hair care : It is also used for hair growth.

Cures Acne : Hibiscus has many natural anti-inflammatory substances and also Vitamin C that can stop the growth of acne and even clear the marks left by it.""",43.00,40.00),
            ("Vallarai Podi/Brahmi Leaves Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/31.jpg","""Description
Benefits of Vallarai (Brahmi Leaves):
• Memory power: When it comes to increasing memory power naturally, vallarai keerai is the first herb that comes in everyone’s mind. With its Nitric acid, it helps to increase the memory and concentration power as it is very beneficial for your brain. Including vallarai in your diet at least twice a week, you can realize the difference in your memory power.

• Hair and skin problems: Hair fall, premature greying, hair thinning are some of the problems which can be cured by regular intake of vallarai keerai. Regular intake of vallarai keerai can be helpful for treating skin disorders like eczema and psoriasis.

• Nervous Disorders: The calming effects of Vallarai that can reduce stress and stimulate healthy sleep can also calm the nervous system directly. For those who suffer from disorders like epilepsy or premature aging, Vallarai can have a powerful effect on the quality of life and the severity of the conditions if taken regularly.

• Stomach problems, stress and depression: Stomach upset, diarrhea and indigestion problems can be treated by consuming vallarai keerai. stress and other depression problems. Some depressions cannot be avoided like post natal depression. But you can handle it effectively by adding brahmi leaves in your diet. People also suggests it for controlling our own mind.

• Blood Pressure: Studies have linked Vallarai with a decrease in many diseases, including congestive heart failure, and one of the positive associations with the herb was blood pressure.""",50.00,40.00),
            ("Arasa Vithai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/33.jpg","""Description
Benefits of Arasa vithai:
Seeds are cooling and laxative. For neuralgia, inflammations and hemorrhages latex is used.

Asthma:

Asthma is a deadly disease as it blocks your breathing, preventing oxygen from getting into your lungs and to other organs in your body.

Due to the increasing amounts of harmful pollution and dust around us, asthma has become a very common ailment, particularly among young children.
Regular intake of the Arasa vithai powder can give you remarkable benefits and changes in your health, just mix the powder with milk and drink twice a day to help with your asthma.

Oral Health:

This powder is also extremely good for your oral health. You can also chew on the twigs of this tree. This prevents tooth decay.

Chewing on the twigs can help to remove any bacteria that are present in your mouth, thus preventing infections or diseases of any kind. It also removes the stain from your tooth.

Constipation:

It’s significant to keep your digestive system in a good condition. Clearing your digestive system regularly is very important as it ensures the smooth functioning of your body.
This powder can be mixed with jaggery and anise seed powder to relieve you from digestive problems. Have this mix before sleep, it will help clear out your system and provide relief from constipation.

Diabetes:

Diabetes is one of the deadly diseases but you don’t worry, because this powder can prevent it. It can help you lower the sugar level in your blood and keep you protected.

Skin problems:

This powder has healing and anti-irritation properties, as well as the health benefits of salicylic acid herbicide to relieve itchy skin.""",50.00,40.00),
            ("Roja Idhazh Podi/Rose Petal Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/39.jpg","""Description
Benefits of Roja Idhazh(Rose Petal):
• Rose Petal water is an effective astringent that reduces swelling of capillaries beneath the skin.
• Rose Petal tea is efficient in cleansing gall bladder and liver, and it helps improve bile secretion. Rose petals are dried and crushed and the powdered form is added in tea.
• Rose petal tea also helps in alleviating mild sore throats and bronchial infections. The tea cools the body and reduces fever-related rashes.
• Rose essential oil is used along with carrier oils such as almond or grape fruit to treat various illnesses like hemorrhage, liver problems, nausea, fatigue, ulcers, asthma, dehydration, and bacterial infections of the stomach, colon, and urinary tract.
• Rose petals are an important ingredient in eye washes as well, as it is antiseptic in nature.
• Rose Petal water benefits include nourishing the scalp and improving hair growth. It is medicinally used as an antibacterial, antiseptic, and anti-inflammatory product. It is also used to treat dry scaly skin and dermatitis.""",65.00,60.00),
            ("Vettiver Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/42.jpg","""Description
Benefits of Vettiver:
Vetiver water is very cooling. It helps to cure painful urination, ulcers and bad breath.

This aromatic water has a calming effect on the nerves and regular intake of this water helps in general well being and it acts as a blood purifier.

Eye burning, head ache, fever, hair care & used for bath powder.""",80.00,60.00),
            ("Karanthai Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/43.jpg","""Description
Benefits of Vettiver:
Vetiver water is very cooling. It helps to cure painful urination, ulcers and bad breath.

This aromatic water has a calming effect on the nerves and regular intake of this water helps in general well being and it acts as a blood purifier.

Eye burning, head ache, fever, hair care & used for bath powder.""",25.00,20.00),
            ("Nilapanai Kizhangu/Black Musli Powder 50g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/44.jpg","""Description
Benefits of Nilapanai Kilangu:
• Restorative tonic, to cure weakness, sexual debility.
• Aphrodisiac, Premature ejaculation, better performance, impotence.
• Low sperm count, impotence, general body weakness, loss of stamina and vigor, and to gain weight.
• For itches and skin diseases.
• The poultice of root is used, it cures Piles.
• Application of root paste on pile, gives relief in pain and burning sensation.
• Cough, cold and asthma.
• Black Musli acts as diuretic and boosts the resistance of urinary system against infections.""",80.00,60.00),
            ("Drumstick Leaves/Murungai Ilai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/45.jpg","""Description
Benefits of Murungai Ilai:
• Siddha Medicine to Lower Cholesterol: It is also effective in lowering LDL cholesterol levels and inhibiting the abnormal formation of blood clots.
• As Ayurvedic Medicine to Control Blood Pressure: Another benefit of moringa powder is its soothing ability which enables it to lower the blood pressure and promotes good sleep. It is a natural remedy for insomnia as it possesses certain properties that can treat sleeping disorders.
• Natural Herb which Detoxifies Body: It is often used to purify water due to its detoxifying effects. Being a coagulant agent, it can attach itself to hazardous bacteria and other agents. In a similar manner, when consumed, it helps in removing toxins from the body.
• Natural Way to Treat Depression: Moringa leaf powder is effective in treating depression and anxiety as well . You can make it a part of your diet and see the results within a couple of days.
• How to Boost Stamina: Being a complete package of vitamins, minerals, antioxidants and nutrients, this supplement is great for boosting your energy and stamina as well as increasing concentration.
Students can use it to improve concentration whereas athletes can benefit in the form of increased endurance during exercise. Moreover, it aids in weight loss because it provides enough energy and vitality to reduce the need for eating to increase energy levels.
•As Herbal Medicine for Diabetes: It is extremely beneficial for diabetic patients. Moringa Oliefera capsules or a drink made from moringa powder can be consumed for keeping the level of sugar normal. Thus, it is a cost effective home remedy for diabetic patients.
• Natural way to fight Cancer: Moringa powder is rich in catechin polyphenols, particularly epigallocatechin gallate (EGCG) which is a powerful antioxidant for inhibiting the growth of cancer cells.
•As Herbal Remedy for Sleep Disorders: For a good night’s rest, It will help you sleep soundly, which in turn will leave you energized to tackle the day.""",60.00,50.00),
            ("Aadathodai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/46.jpg","""Description
Benefits of Karuvepillai:
• Helps keep anaemia at bay If you suffer from anaemia, eat one dates with two curry leaves on an empty stomach every morning
• Protects your liver from damage , curry leaves help in curing liver damages due to alcohol.
• Maintains your blood sugar levels:- curry leaves lower your blood sugar levels by affecting the insulin activity.
• Protects you from heart disease:- curry leaves prevent the oxidation of cholesterol as it is packed with antioxidants. This in turn increases the amount of good cholesterol and protects you from heart disease and atherosclerosis.
• Helps with digestion Curry leaves are known to be carminative in nature and thus, is highly effective against indigestion.
• Relieves the symptoms of diarrhoea:- Even though curry leaves have mild laxative properties, it is a great remedy for diarrhoea.
• Reduces congestion in the chest and nose:- It cures from a wet cough, sinusitis or chest congestion. Curry leaves can help loosen up and release congested mucous
• Treats and prevents skin infections:- This makes it a great home remedy to deal with common skin infections like acne and fungal infections of the nail that are often difficult to treat.
• Accelerates hair growth:- it also very effective in treating damaged hair, adding bounce to limp hair, strengthening the shaft of thin hair, hair fall and treats dandruff.""",55.00,50.00),
            ("Karuveppilai Podi/Curry Leaves Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/47.jpg","""Description
Benefits of Karuvepillai:
• Helps keep anaemia at bay If you suffer from anaemia, eat one dates with two curry leaves on an empty stomach every morning
• Protects your liver from damage , curry leaves help in curing liver damages due to alcohol.
• Maintains your blood sugar levels:- curry leaves lower your blood sugar levels by affecting the insulin activity.
• Protects you from heart disease:- curry leaves prevent the oxidation of cholesterol as it is packed with antioxidants. This in turn increases the amount of good cholesterol and protects you from heart disease and atherosclerosis.
• Helps with digestion Curry leaves are known to be carminative in nature and thus, is highly effective against indigestion.
• Relieves the symptoms of diarrhoea:- Even though curry leaves have mild laxative properties, it is a great remedy for diarrhoea.
• Reduces congestion in the chest and nose:- It cures from a wet cough, sinusitis or chest congestion. Curry leaves can help loosen up and release congested mucous
• Treats and prevents skin infections:- This makes it a great home remedy to deal with common skin infections like acne and fungal infections of the nail that are often difficult to treat.
• Accelerates hair growth:- it also very effective in treating damaged hair, adding bounce to limp hair, strengthening the shaft of thin hair, hair fall and treats dandruff.""",55.00,50.00),
            ("Licorice/Athimathuram Powder[Adhimathuram Podi] 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/48.jpg","""Description
Benefits of Athimathuram:
• Medicine for Digestion: Athimathuram root has been used for centuries to treat various ailments that involves digestive tract, as it helps to protect the stomach lining.
• Medicine for Cough: Athimathuram tea is amazing home remedy for cough and since it is sweet by itself, it is easier to make the children drink it.
• Paatti Vaithiyam for Menstrual cramps: It also relieves menstrual cramps as it has antispasmodic and anti inflammatory proprieties.
• Medicine for Constipation: It is also a laxative and can relieve a person, who suffers from constipation. Consume this tea daily for 2 to 3 days to get good relief from constipation.
• Herbal remedy for Arthritis: Athimathuram has anti inflammatory properties, so it may help people who are suffering from arthritis.
• Natural Blood purifier: Blood purification and more – Athimathuram is known for its blood cleansing properties & used for blood circulation problem.
• Hair: It is good for your hair too.""",70.00,60.00),
            ("Mudakathan Podi/Powder 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/49.jpg","""Description
Benefits of Mudakathan:
• It is used in the treatment of rheumatism, nervous diseases, stiffness of the limbs.
• The leaves are rubefacient, they are applied as a poultice in the treatment of rheumatism.
• A tea made from them is used in the treatment of itchy skin.
• It is used in the treatment of Joint pains.
• The leaf juice has been used as a treatment for ear ache.
• The root is diaphoretic, diuretic, emmenagogue, laxative and rubefacient.
• It is occasionally used in the treatment of rheumatism, lumbago and nervous diseases.
• It is used in treating Anemia, Asthma, Urinary Incontinence.
• It is used in treating Arthritis, Backache, Baldness, Cough, Dandruff, Diarrhea, Dysentery, Earache, Eczema, Eye Diseases, Fracture, Gout, Headache, Menses Scanty, Menstrual Disorders, Piles, Rheumatism.
• It is used as Hair growth stimulation.
• It is used to treat for wounds & Swelling.""",50.00,40.00),
            ("Vilvam Leaves Powder/Vilva Ilai Podi 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/50.jpg","""Description
Benefits of Vilvam:
• Vilvam is helpful in increasing immunity and is effective against seasonal diseases like cough, cold and fever.
• Children often get sick during cold weather. Vilvam Powder is safe for children and can be given to them during such infections.
• Vilvam is rich in fibre which makes it a wonderful laxative. It has tannins which help relieve diarrhoea, cholera and other digestive disorders.
• Vilvam has anti oxidant properties as well due to which it helps remove toxins from body and improve overall metabolism.
• Vilvam is also known for its property to regulate thyroid secretion there by maintaining normal thyroid function and prevents hyperthyroidism.
• Vilvam protects liver from injuries and keeps it healthy. Because of this property it is highly recommended in case of liver infections like cirrhosis, jaundice and other liver disorders. Vilvam is also found to heal Ulcer.
• Vilvam has hypoglycaemic properties. It reduces oxidative stress on pancreas by reducing the free radicals and increases the level of antioxidants there by reducing the risk of diabetes. Regular use of Vilvam has shown good results in diabetic patients.
• Vilvam has phytochemicals which help maintain blood pressure. It has soothing effect on body and hence a fine paste of Vilvam Powder applied on forehead relieves headache.
• Vilvam is anti-inflammatory in nature and hence it is highly effective in both chronic and acute inflammation. Vilvam leaf paste applied on the swollen part provides quick relief from inflammation.""",45.00,40.00),
            ("Thoothuvalai Podi/Climbing Brinjal Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/51.jpg","""Description
Benefits of Thoothuvalai(Climbing Brinjal Powder):
• Thoothuvalai for cold and cough: The herb is considered as the best remedy for treating babies and adult cough and cold. It works effectively on throat irritation and itching. The consumption of the Thoothuvalai kashayam or legiyam reduces the congestion of nose and chest. The people who are suffering from chronic cough and cold can take advantage of the Thoothuvalai powder.

• Asthma and other respiratory problems: This medicinal plant is very effective in treatment of Asthma. Its best treatments for many types of respiratory problems like carcinoma and anorexia.

• Strength and energy: The herb is considered as the very good medicine for getting strength and energy in the body. The natural steroids present in the herb give strength and stamina to the human being.

• Sinus problem: In ayurveda this herb is popularly used for treating sinus, lung diseases and even for the treatment of tuberculosis.

• Production of blood: Thoothuvalai is very useful for increasing the production of blood in the body and it also increases the blood circulation effectively. The problem of indigestion and other gastric problems can be cured with the use of Thoothuvalai leaves extracts.

""",34.00,30.00),
            ("Jaadhikkaai/Jathikai Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/52.jpg","""Description
Benefits of Jathikai Powder:
1. Jathikai for sleep:

Jathikai helps to induce sleep. People with sleep disorders prefer Jathikai to get a good night sleep. Nutmeg helps to treat various sleep disorders. It has natural sedative properties and helps you to get sleep naturally without sleeping pills and other chemicals.

Mix jathikai powder in warm milk. 1/8 tsp of Nutmeg powder can be added to 1 cup of warm milk. Drink it before going to bed. You will get a deep sleep very soon.

Jathikai is a popular natural sleep aid. It provides relaxation and gives a sound sleep.

2. Jathikai for face, skin and hair:

Jathikai is good in treating pimples, blemishes, acne and acne scars. It has anti-inflammatory properties.

Just swipe the jathikai in a wet stone and apply the paste on the pimples. Repeat it daily till the pimple and scars goes off. Make sure that you clean and pat dry your face before applying.

If you have jathikai powder, mix it with water and make a thick paste. Clean and wipe the face gently. Apply the jathikai powder paste directly on the pimples.

You can use freshly ground nutmeg powder too.

After applying, wait for 20 minutes and wash it off with clean water. Pat dry your face.

You can also mix tumeric powder, sandalwood powder with the jathikai powder. Instead of water, you can use rose water or milk to make the paste.

Jathikka is also good for dry skin. You can massage the nutmeg oil before taking bath. Jathikkai thailam is available in market. Use it according to the instructions. Jathikkai oil is used for treating hair problems also like dandruff. Please look out for quality jathikkai oil for usage.

3. Jathikai for babies:

Jathikai is good for babies. But please limit the quantity you give to babies with just a swipe. It induces the sleep in babies. This is a very old home remedy. People give it as a part of Ura marundhu. People give vasambu, sukku, masikkai, kadukkai and few other ingredients also along with nutmeg.

4. Jathikai for Stomach problems:

Nutmeg is good to treat stomach problems like indigestion, diarrhea and flatulence. You can include nutmeg powder in your breakfast cereals or with warm milk.

5. Jathikai for dental problems:

Nutmeg has anti-bacterial properties. It is used in oral care and to treat problems like tooth pain, sore gums. Nutmeg oil is available in market. One drop of oil can be applied in the problematic area.

6. Jathikai for joint pains, massage and aromatherapy:

There are jathikai oil available in the market for joint and muscular pains associated with rheumatism or overexertion. Even nutmeg essential oil is available online and offline which can be used in massage and aromatherapy.""",85.00,80.00),
            ("Kilangu Podi/Kizhangu Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/53.jpg","""Description
Ingredients:
1) Kaattukkaranai
2) Kaaraakaranai
3) Naattukaranai

Benefits:
Good for patients suffering from internal as well as external hemorrhoids(piles).""",45.00,40.00),
            ("Katraalai Podi/Aloe Vera Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/55.jpg","""Description
Benefits of Katralai:
• It is an excellent natural antibiotic.
• It strengthens digestion, prevents the formation of gas and helps to improve large intestinal flora.
• It purifies the blood, aids digestion of protein and promotes proper metabolism in the body.
• It is also used in infection, arthritis, dysentery, jaundice and other liver problems.
• It is used to treat chest congestion, menstrual discomforts and many more ailments.
• It helps to Boosts weight loss and immunity.
• It is also extensively used in treating cough problem. Add a pinch or two of turmeric to warm milk to soothe respiratory.
• Skin Care.""",60.00,50.00),
            ("Vishnukiranthi Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/57.jpg","""Description
Benefits of Vishnu Kiranthi:
• Vishnukranthi Plant Decoction used for Fever, Reducing Stress & Enhancing Memory.
• It is one of the psychotropic drugs that cures nervous debility and dementia.
• It treats disorders of nervous system.
• It gives relief in anxiety, depression, pain, insomnia, epilepsy and fits.
• It reduces stress.
• It detoxifies body.
• It helps in digestive impairment due to nervousness.
• It has laxative action.
• It has aphrodisiac action and strengthens reproductive system.
• It is one of the best herbs used as a general tonic and rejuvenation.
• It cures Ulcers, Toothache, Hair care and also used to Improve Libido.""",50.00,40.00),
            ("Thutthi Leaves Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/58.jpg","""Description
Benefits of Thuthi Ilai:
• A Fantastic diuretic as it contains Gallic acid it acts as anti-inflammatory & analgesic.
• Very effective medicine for Piles (Bleeding Piles), Fistula.
• Extremely good Blood purifier and can cure bleeding piles.
• The mixture of root (Decoction) can be an effective cure for paralysis, renal failure and very good tonic for strengthening of nerves.
• It is used to treat for wounds & Good for children who get swelling due to a fall.
• Good cure for Lymph nodes – put the warm leaf mixture on the area. You will get good results.""",50.00,40.00),
            ("Aadutheendapalai Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/59.jpg","""Description
Benefits of Aadu Theenda Paalai:
• Aadu theenda palai is a good remedy for Diarrhea & fever.
• It cures inflammation.
• Treat for respiratory disorders & asthma.
• It controls Blood pressure.
• It used for gas problems.
• Snake bites""",70.00,60.00),
            ("Vadhanarayanan/White Gulmohar Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/60.jpg","""Description
Benefits of Vadhanarayanan(White Gulmohar):
Paralysis attack: There are many types of paralysis attacks and some can be curable by adding White Gulmohar in the diet with garlic and asafoetida.
Heart-related diseases: To cure heart-related diseases, add dry ginger, cumin seeds, and basil with this spinach variety and cook a delicious dish that tempts family members to have a bite for a healthy heart.
Gastric problems and stomach: White Gulmohar with garlic gives a big relief from all the gastric problems and stomach related diseases.
Knee pain, Joint pain and Neck pain: Those who are suffering from knee pain, joint pain, and neck pain, try the juice of Vadhanarayanan for once or twice a week.

How to Consume:

Morning – Mix 5 grams of powder in 100 ml water, Boil the content for a few minutes. once the water gets warm, filter the content and drink it before food. Repeat the same for the Evening Dosage after dinner.

External Benefits:
It is used to treat wounds.

How to Apply:

Apply the paste in the affected area.""",35.00,30.00),
            ("Orange Peel Powder 50g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/61.jpg","""Description
Benefits of Orange Pazha Thol:
Orange Peel Tea is recommended for better digestion
This powder is a great solution for Dry Skin.
It can be used for Skin whitening & Body Odor.
It can be used on Dark Spots & Dark Circle.
It can be used for Acne, Acne Scars & Glowing skin.
It can improve your Breath if you have a bad breath.
This powder can be used as a Hair Mask.
This powder can be used for washing hair also.""",80.00,60.00),
            ("Arathai Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/62.jpg","""Description
Benefits of Arathai:

• Arathai for Cough: For cough with sputum, a piece of rhizome of this plant is slowly chewed. This is also good for vomiting issues.
• Arathai for Infants and children: For all sorts of digestive and respiratory ailments in infants and children, this rhizome is baked or heated and given after mixing with honey and breast milk.
• Arathai for Rheumatic Ailments: 1 to 3 gram of powder of this rhizome is administered thrice daily for rheumatic ailments.
• Arathai for Digestive Problems: For digestive problems, 1 to 5 grams of powder of this rhizome can be administered twice daily before food.
• Arathai for Headache and Fever: Athimathuram, Thaleesapathri, Arathai and Thippili can be powdered, mixed in equal quantity and given along with honey for cough, headache, fever and indigestion.
• Arathai for Increase in Sperm Count: Recent research on this plant have proved that regular consumption of this powder or decoction increases sperm count and acts as an Aphrodisiac.""",50.00,40.00),
            ("Nilavaagai Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/64.jpg","""Description
Benefits of Nilavaagai Powder:
• This powder is used for diseases such as abdominal worm infestation, rheumatoid arthritis, gout.
• Ayurveda has suggested that in the conditions of Hepatomegaly, Splenomegaly and Jaundice to relive excessive Pitta from the body using this powder.
• Nilavaagai Powder stimulates the liver for production of Pitta.
• This powder is a good blood purifier and can be used for constipation.""",45.00,40.00),
            ("Sweet Basil Powder/Inippu(Seeni) Thulasi Podi 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/65.jpg","""Description
Inippu Thulasi Health Benefits:
• Stevia leaves do not contributes calories and carbohydrates to the dies.
• It can be used for people with diabetes, it helps to control the sugar level of the blood.
• Certain glycosides in stevia extract have been found to dilate blood vessels.
• Cardiotonic actions of this stevia leaves are normalizing blood pressure and regulate the heartbeat.
• Using these leaves is also helps to control the weight.
• Foods and beverages containing stevia can play an important role in decreasing calories from unwanted sweeteners in the diets of children.""",50.00,40.00),
            ("Nannari Ver Podi/Nannari Root Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/66.jpg","""Description
Benefits of Nannari Ver:
1. Body coolant: Nannari root is a natural body coolant and if had as a sherbet during summer, it keep us from becoming dehydrated.

2. Blood purifier: Nannari root is an excellent blood purifier and increases our energy levels

3. Urinary infection: This nannari is reported to be an excellent home remedy for urinary infection

4. Constipation: Consuming a glass of nannari drink also is a good and effective home remedy for constipation and it also relieves body pain.

5. For Digestion: This nannari root is an effective way to treat our stomach disorders without swallowing bitter pills. If you have a mild indigestion or if you are not hungry, take a cup of this nannari sherbet, you will feel better in no time.""",120.00,100.00),
            ("Indhu Uppu Powder 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/67.jpg","""Description
Benefits of Indu Uppu:
• Indhu Uppu cures Malaria.
• It cures Ear-ache.
• It can be used as a teeth whitener or mouth freshener. Gargling with rock salt provides relief against sore throat.""",40.00,32.00),
            ("Pirandai Powder 50g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/68.jpg","""Description
Benefits of Pirandai:
Pirandai for Gastritis, Indigestion & Lack of Appetite:

Pirandai treats all digestion related problems like gastritis, indigestion and lack of appetite.

Sprains:

Pirandai poultice is very good for treating sprains and swollen joints (suluku in Tamil). It is also one home remedy that many people in our village use often for minor injuries, as it heals the minor sprains and fractures very fast.

Pirandai helps stomach disorders for children:

Regularly including pirandai to children’s diet will prevent them from getting stomach disorders.

Pirandai for Bleeding Piles & Deworming:

This treatment for bleeding piles has to done continuously for at least 7 to 10 days to see results.
It’s used to treat blood Pressure, heart diseases, Fat increase, Gynecological problems.
It is a best worming medicine, menstrual problems and is also the best home remedy for ear pain.""",50.00,40.00),
            ("Marutham Pattai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/69.jpg","""Description
Benefits of Marutham Pattai:
• Regular use this powder improves the pumping activity of heart, which makes it very useful for heart weakness and congestive heart failure.

• Marutham Pattai improves cardiac muscle strength.

• It decreases LDL cholesterol levels.

• Marutham Pattai’s ability to suppress the blood’s absorption of lipids indicates that it has cholesterol-regulating properties. Its principle constituents are sitosterol, ellagic acid and arjunic acid.

• This plant’s bark is rich in Co-enzyme Q-10 which prevents incident of heart attacks.

• This also has a tonic and diuretic effects that benefit cirrhosis of the liver.

• It induces a drug-dependent decrease in blood pressure and heart rate.

• The bark of this plant is useful as an anti-ischemic and cardioprotective agent in hypertension and in ischemic heart disease, especially in disturbed cardiac rhythm, angina or myocardial infarction.

•This helps maintain a healthy heart and reduces the effects of stress and nervousness.

• This enhances prostaglandins and lowers risk of coronary heart trouble.

• This can relieve symptomatic complaints of essential hypertension such as giddiness, insomnia, lassitude, headache and the inability to concentrate.

• In a study on the efficacy of the bark powder in treating congestive cardiac failure (CCF), over 40% of the cases showed marked improvement. CCF due to congenital anomaly of heart and valve disease was also brought under control. 4 out of 9 cases of CCF due to chronic bronchitis were also relieved by the treatment.""",60.00,50.00),
            ("Goraikilangu Powder/Koraikilangu Podi 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/70.jpg","""Description
Benefits of Goraikilangu:
• The paste of Goraikilangu is used in treating skin related ailments like scabies and eczema and helps in relieving itching.
• The paste is used in increasing the size of the breasts. It also purifies the breast milk, improves eyesight and helps in eye related ailments.
• The extract from the roots is instilled into eyes in conjunctivitis, to reduce the pain, redness and ocular discharges.
• Goraikilangu, when taken in powdered form, improves digestive system, removes worms from the gastro-intestinal tract, curbs infection and purifies blood.
• The powder is massaged to reduce the subcutaneous fat deposition in case of obese people.
• It normalizes the menstrual disturbances and breast discomfort and maintains normal body temperature.
• Goraikilangu proves useful in diseases like psychosis and epilepsy and mental diseases.
• The herb helps, uterine contraction and provides strength to the body.
• It is used as a diuretic to treat ulcers and as an emmenagogue and an ingredient in warm plasters.
• The herb proves to be a keen stimulant in appetite.
• Goraikilangu is an effective remedy for distaste, vomiting, diarrhea, colitis and dyspepsia.
• It is considered the best herb for treating any type of fever.
• The Root is often used for developing High Memory.
• Goraikilangu is beneficial in treating cough and asthma, since it alleviates the Kapha.
• The herb harmonizes liver, spleen, and pancreas. It helps in curing thirst, bronchitis, dysuria and poisonous affections.
• Used for Skin Acne, Dandruff, Skin Wounds, and Skin Ulcers.""",50.00,40.00),
            ("Nilaavarai/Senna Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/71.jpg","""Description
Benefits of

Help With Constipation
The most common benefit of senna leaves is relief from constipation. Senna leaves contain compounds called sennosides, which stimulate muscle contractions in the intestines. These muscular contractions help move stool through the bowels and help relieve constipation. The sennosides also boost secretion of water in the colon, which softens the stool and increases its bulk, making it easier to pass.
When using senna leaves as a laxative, you should take 20 to 60 milligrams of sennosides daily for a maximum of 10 days.
Ad
Inflammation Reduction
According to the Journal of Medicinal Plant Studies, senna leaves contain a natural anti-inflammatory compound called resveratrol (the same compound that gives red wine its anti-inflammatory effects). Because of this, senna leaves may help reduce widespread, chronic inflammation in the body. However, because senna leaves are not approved for long-term use, it may not be the best choice for chronic care.
Common Side Effects
The most common side effects of senna leaves are abdominal pain, cramping and diarrhea, which occur as a result of senna’s laxative effect. Over time, senna can cause fluid loss and electrolyte imbalances, which may cause lightheadedness. When taking senna leaves, you may want to consider also taking an electrolyte supplement or drinking beverages fortified with electrolytes. You should also keep in mind that, if you use senna leaves too often, your bowels may become dependent on it, making it harder to have a bowel movement without it.

Search Terms: Nila avarai Podi, Nilavarai Powder""",60.00,40.00),
            ("Ponnaankanni Powder/Ponnaankanni Keerai Podi 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/72.jpg","""Description
Benefits of Ponnanganni:
• Enhances energy level.
• Cures piles.
• Liver care.
• Cures Asthma.
• Improves breast milk.
• Helps weight gain.
• Cures headache.

• Eye care: Ponnanganni keerai or leaves are one of the best sources for treatment of eye related problems.
• Body stings and spines: The paste is used to draw out from the body stings and spines.
• Snakebites: It used to remove the effect of poison due to snakebites. It can be applied along with other first-aids given for snake bites.
• Removes body heat: It reduces the body heat to the normal level and keeps the eyes cool.

Reviews""",50.00,40.00),
            ("Kandankathiri Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/73.jpg","""Description
Benefits of Kandankathiri:
• It is useful in treating worms, cough, hoarseness of voice, fever, painful urination, enlargement of the liver, muscular pain, and stone in the urinary bladder and used for curing bloody piles, asthma & skin allergies.
• It is used to treat Hair fall, Toothache, Migraine, Epilepsy.""",60.00,50.00),
            ("Thamarai/Lotus Petals Powder 25g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/74.jpg","""Description
Benefits:
• Lotus’ petals are helpful in controlling the burning sensation, due to its cold potency.

• It helps in improving the skin texture and complexion.

• It improves the mental condition and regularizes the peristaltic movements.

• It treats urine related problems and maintains the body’s normal temperature.

• It is taken with sugar to treat rectal prolapse.

• It is also used in treating sunstroke, diarrhea, dysentery, dizziness, and vomiting of blood.

• The stamens are mixed with jaggery and ghee to treat hemorrhoids.

• It is useful in treating many bleeding disorders.

• Lotus’ petals are prescribed to promote conception.

• The flower stalk, mixed with other herbs, is used to treat bleeding from the uterus.

• The petals alleviate thirst and inflammations while the seeds are powdered and mixed with honey to treat cough.

• Lotus, when taken with ghee, and milk is considered a general tonic to promote strength, virility, and intellect.

How to Consume:

Morning – Mix 5 gms of powder in 100 ml water, Boil the content for a few minutes. once the water gets warm, filter the content and drink it before food. Repeat the same for the Evening Dosage after dinner

External Benefits:
It is a wonder for skin-conscious people.

How to Apply:

• The leaf paste is applied to the body for regular skin care and also for inflammatory skin conditions.""",45.00,40.00),
            ("Musumusukkai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/75.jpg","""Description
Benefits of Musumusukai:
Sore throat due to cold: Blood sugar: A diabetic people are suggested to add these leaves to maintain a normal glycemic index.

Liver diseases: The health of the liver is maintained with the help of nutritional components.""",50.00,60.00),
            ("Lemon Peel Powder/Elumichai Thol Podi 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/76.jpg","""Description
Benefits of Elumichai Thol:
Fever:

This can treat a person who is suffering from a cold, flu or fever. It helps to break fevers by increasing perspiration.

Weight Loss:

If a person drinks this powder mixed with lukewarm water and honey, it can help reduce body weight.

Respiratory Disorders:

This assists in relieving respiratory problems and breathing problems, such as its ability to soothe a person suffering from an asthma attack. Being a rich source of vitamin C, it helps in dealing with more long-term respiratory disorders as well.

Cholera:

Diseases like cholera and malaria can be treated with this, because it acts as a blood purifier.

Foot Relaxation:

Lemon is an aromatic and antiseptic agent and is useful in foot relaxation. Add some its juice to warm water and dip your feet in the mixture for instant relief and muscle relaxation.

Rheumatism:

It is also a diuretic and can treat rheumatism and arthritis. It helps to flush out bacteria and toxins from the body.

Elumichai Thol Podi can be externally used for:

• Dental Care
• Hair Care
• Skin Care
• Burns
• Internal Bleeding
• Corns""",40.00,30.00),
            ("Amman Pacharisi Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/77.jpg","""Description
Benefits of Amman Pacharisi:
• The leaves of Euphorbia are known to be helpful in treating skin irritations. The milky sap, while poisonous, can be used to clear up warts on the surface of the skin. An extract made from the crushed euphorbia flower can heal eye infections and inflammations like conjunctivitis.

• The plant is believed to promote healing in cases of dengue fever by facilitating the production of platelets. It is also known for its anthelmintic properties, and it can be used to get rid of worms and other parasitic organisms. Euphorbia is also considered to boost breast milk production in lactating mothers. Euphorbia can be used in the treatment of venereal diseases like gonorrhea.

• In fact, it has also found use in the treatment of impotency, premature ejaculation, and other sexual disorders. The root of euphorbia can be made into a paste and used for healing stomach pain. However, it should be consumed only in recommended doses, else it can induce vomiting. Euphorbia is also said to possess antiviral properties, and it has been used in the treatment of dysentery and to alleviate the symptoms of diarrhea.

• Euphorbia can also be used to treat snakebites and Paste of the leaves is applied externally to cure swellings and ulcers""",40.00,30.00),
            ("Boomi Sakkaravalli Kizhangu/Sweet Potato Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/78.jpg","""Description
Benefits of Boomi Sakkaravalli Kilangu:
1. Natural way to fight Heart problem: It contain vitamin B6, It helps reduce the chemical homocysteine in our bodies. Homocysteine has been linked with degenerative diseases, including heart attacks.
2. Patti Vaithiyam to maintain skin’s youthful elasticity: While most people know that vitamin C is important to help ward off cold and flu viruses, few people are aware that this crucial vitamin plays an important role in bone and tooth formation, digestion, and blood cell formation. It helps accelerate wound healing, produces collagen which helps maintain skin’s youthful elasticity, and is essential to helping us cope with stress.
3.Siddha Medicine for Healthy Bones: Vitamin D is critical for immune system and overall health at this time of year. Both a vitamin and a hormone, vitamin D is primarily made in our bodies as a result of getting adequate sunlight. You may have heard about seasonal effective disorder (or SAD, as it is also called), which is linked to inadequate sunlight and therefore a vitamin D deficiency.Vitamin D plays an important role in our energy levels, moods, and helps to build healthy bones, heart, nerves, skin, and teeth, and it supports the thyroid gland.
4. Best Natural way to strengthen Immune System: Sweet potatoes contain iron and support a healthy immune system:Most people are aware that we need the mineral iron to have adequate energy, but iron plays other important roles in our body, including red and white blood cell production, resistance to stress, proper immune functioning, and the metabolizing of protein, among other things.
5. Good way to reduce Stress: Sweet potatoes are a good source of magnesium, which is the relaxation and anti-stress mineral: Magnesium is necessary for healthy artery, blood, bone, heart, muscle, and nerve function
6. Tamil Herb to maintain strong Nerves: They are a source of potassium:Potassium is one of the important electrolytes that help regulate heartbeat and nerve signals. Like the other electrolytes, potassium performs many essential functions, some of which include relaxing muscle contractions, reducing swelling, and protecting and controlling the activity of the kidneys.
7. Natural sugar: Sweet potatoes do not cause blood sugar spikes: Sweet potatoes are naturally sweet-tasting but their natural sugars are slowly released into the bloodstream, helping to ensure a balanced and regular source of energy, without the blood sugar spikes linked to fatigue and weight gain.""",80.00,60.00),
            ("Koiyya Ilai/Guava Leaves Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/79.jpg","""Description
Benefits of Thippili:
• It is used for treating depression, weight loss, all kinds of inflammation and diabetes!
• Long pepper has anti oxidant, anti depressant, anti inflammatory, anti microbial, analgesic, anti fungal and cardio protective properties.
• It control Hiccups,controls Headache, Vitamin B1 deficiency, Fever,Headache and Stroke.""",90.00,70.00),
            ("Thippili Powder 25g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/80.jpg","""Description
Benefits of Poduthalai:
• Poduthalai in Siddha: Toasted tender stalks and leaves, in infusion, used for childrens indigestion.

• Poduthalai in Pattivaithiyam: Juice of roots used for gastric problems.

• Used for treatment of hookworms.

• Used for women after childbirth.

• Infusion used in colds with fever; also as diuretic and for lithiasis.

• Poultice of fresh plant used to hasten ripening of boils.

• Used for liver disorders, dandruff control, and indigestion in children

• Poduthalai in Nattumaruthuvam: Plant used for joint pains, constipation, ulcers, boils, swollen cervical glands, and gonorrhea.

• Poduthalai in Siddha Maruthuvam: Used for asthma, bronchitis, diseases of the heart, blood, and eyes.

• Plant vapors inhaled to treat coughs and colds. Root juice used for gastric problems.

• Paste or poultice of plant applied to swollen cervical glands, erysipelas and to chronic indolent ulcers.

• Paste of the leaves applied to swellings and wounds.""",50.00,40.00),
            ("Poduthalai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/81.jpg","""Description
Benefits of Poduthalai:
• Poduthalai in Siddha: Toasted tender stalks and leaves, in infusion, used for childrens indigestion.

• Poduthalai in Pattivaithiyam: Juice of roots used for gastric problems.

• Used for treatment of hookworms.

• Used for women after childbirth.

• Infusion used in colds with fever; also as diuretic and for lithiasis.

• Poultice of fresh plant used to hasten ripening of boils.

• Used for liver disorders, dandruff control, and indigestion in children

• Poduthalai in Nattumaruthuvam: Plant used for joint pains, constipation, ulcers, boils, swollen cervical glands, and gonorrhea.

• Poduthalai in Siddha Maruthuvam: Used for asthma, bronchitis, diseases of the heart, blood, and eyes.

• Plant vapors inhaled to treat coughs and colds. Root juice used for gastric problems.

• Paste or poultice of plant applied to swollen cervical glands, erysipelas and to chronic indolent ulcers.

• Paste of the leaves applied to swellings and wounds.""",50.00,40.00),
            ("Mathulai/Maadhulai Pomegranate Peel Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/82.jpg","""Description
Benefits:
Mathulai Thol for Stomach Disorders: Pomegranate peel, bark and leaves are used to calm disorders of the stomach or diarrhea caused by any kind of digestive problems.  Drinking tea made from the leaves of this fruit also helps in curing your digestive problems. Pomegranate juice is also used for handling problems like dysentery and cholera.
Mathulai Thol for Heart Problems: Regular intake of pomegranate juice can maintain a good flow of the blood in the body. Because of this property, it subsequently decreases the risk of heart attacks and strokes.
 Regular intake of pomegranate juice can maintain a good flow of the blood in the body. Because of this property, it subsequently decreases the risk of heart attacks and strokes.
The antioxidant components that are contained in this fruit help to keep the bad cholesterol from gaining any significant product.
Mathulai Thol for Dental Care: One of the best benefits of pomegranates is that their juice, along with its antibacterial and antiviral properties, helps to reduce the effects of dental plaque and protects against various oral diseases.
Mathulai Thol for Osteoarthritis: Pomegranates help reduce illnesses of many forms, including atherosclerosis and osteoarthritis. The damages that are caused due to the thickening and hardening of the arterial walls and in the cartilage and joints can be cured. Also, pomegranates are capable of preventing the creation of enzymes that are responsible for breaking down connective tissues within the body.
Mathulai Thol for Anaemia: Healthy blood flow can be maintained in the body by consuming this fruit in any form. Pomegranate supplies iron to the blood, thus helping to reduce symptoms of anemia, including exhaustion, dizziness, weakness, and hearing loss.
Mathulai Thol for Diabetes: For diabetic patients, drinking pomegranate peel juice can reduce the risk of various coronary diseases. Along with this, there is a reduction in the hardening of the arteries, which can inhibit the development of various heart diseases.""",50.00,40.00),
            ("Mint/Pudina/Puthina Leaves Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/83.jpg","""Description
Benefits of Pudina:
Prevents Respiratory Disorders
The strong aroma of this herb is very effective in clearing up congestion of the nose, throat, bronchi, and lungs, which gives relief from respiratory disorders that often result from asthma and common colds.
Treats Asthma
Regular use of mint is very beneficial for asthma patients, as it is a good relaxant and relieves congestion.
Reduces Depression & Fatigue
Mint is a natural stimulant and the smell alone can be enough to charge your energy and get your brain functioning at a higher level again. If you are feeling sluggish, anxious, depressed or simply exhausted, mint and its essential oil can help
Prevents Memory Loss
Mint has on alertness, retention, and cognitive function which works against memory loss.
Weight Loss
Its stimulates the digestive enzymes that absorb nutrients from food and consume fat and turn it into usable energy
Oral Care
Mint has germicidal qualities and quickly freshens breath, it adds to oral health by inhibiting harmful bacterial growth inside the mouth and by cleaning the tongue and teeth.

Search Terms: Pudhina Leaves Powder, Pudina Ilai Podi, Pudhina Ilai Podi, Pudina Leaves Powder, Puthina Leaves Powder, Puthina Ilai Podi, Pudhina Keerai podi""",60.00,50.00),
            ("Carrom Seeds Omam/Ajwain Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/84.jpg","""Description
Benefits of Omam/Carrom Seeds:
1. Fights bacteria and fungi:
Carom seeds have powerful antibacterial and antifungal properties.
This is likely attributed to two of its active compounds, thymol and carvacrol, which have been shown to inhibit the growth of bacteria and fungi.
2. Improve cholesterol levels:
Animal research indicates that carom seeds may lower cholesterol and triglyceride levels. High cholesterol and triglyceride levels are risk factors for heart disease.
3. Lowers blood pressure:
High blood pressure, or hypertension, is a common condition that increases your risk of heart disease
4. Combats peptic ulcers and relieves indigestion:
Carom seeds are commonly used as a household remedy for digestive issues in Ayurvedic medicine. Carom seed extract also helps prevent and treat gas and chronic indigestion. Indigestion is categorized as persistent pain and discomfort in the upper part of your stomach. Delayed stomach emptying is one of the perceived causes of indigestion.
5. May prevent coughing and improve airflow:
Some evidence suggests that carom seeds may provide relief from coughing. Carom seeds also improves airflow to the lungs.
6. Has anti-inflammatory effects:
Inflammation can be good or bad. Short-term inflammation is your body’s natural way of protecting against illness or injury.
On the other hand, chronic inflammation can have negative effects on your body and increase your risk of certain diseases.

""",60.00,40.00),
            ("Atthi Leaves Powder 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/87.jpg","""Description
Benefits of Atthi Ilai:

• Diabetes: This Powder has been shown to offer powerful blood sugar lowering effects by increasing the sensitivity of insulin to glucose. The exact mechanism by which this happens is still unclear, but research in human and animals have consistently demonstrated this effect. In addition, to its blood-sugar-lowering effect, Atthi leaves Powder is strongly antioxidant and anti-inflammatory in nature. And this powder lowers the oxidation stress – typical in diabetes – and help in wound healing via its anti-inflammatory action While one can consider that dealing with diabetes is indeed a tough ask, some cultures actually use fig leaves powder for its anti-diabetic properties, as the consumption of these leaves, reduce the need for insulin injections when it comes to these patients.

• Weight management: Since Atthi leaves powder possess a large amount of fiber, people who are obese and feel the need to drop a few pounds will find that in consuming fig leaves powder, one can actually pursue an effective weight management program.

• Blood pressure: If you are used to consuming packaged foods, researchers have found that the excess sodium in these foods can be one reason why one can get hypertension, and which leads to blood pressure in the long run. Atthi leaves powder, on the other hand, are known to have high levels of potassium, a mineral that is effective in lowering and controlling high blood pressure.

• Strong Bones: Not only are Atthi leaves powder rich in calcium, promoting bone density, but they also prevent the loss of urinary calcium which also prevents bones from thinning out.

• Heart problem: In being able to lower triglyceride levels, Atthi leaves powder has been said to improve cardiac health.""",60.00,40.00),
            ("Thumbai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/88.jpg","""Description
Benefits of Thumbai:
• It cures Jaundice and liver related diseases.
• Thumbai good remedy for nasal congestion, cough, cold, fever, headache etc
• It used to treat for sinusitis and headache.

Thumbai is a good remedy for scorpion bite & snake bite and also used to cure for wind,bile, phlegm""",50.00,40.00),
            ("Paagarkaai Vatthal Powder/Pagarkai Vathal Podi 50g Each", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/89.jpg","""Description
Benefits of Pagarkaai Vatthal:
1.Pagarkaai ( Bitter Gourd ) for Respiratory Disorders: The fresh pods are an excellent remedy for curing respiratory problems like asthma, cold, cough, etc. Drink one glass of bitter melon juice daily to heal liver problems. Keep consuming this continuously for a week to see results.

2. Pagarkaai (Bitter Gourd )for Better Immune System: consume it every day to fight against infections. This also helps to build your immunity

3. Pagarkaai (Bitter Gourd) for Skin care: Consuming bitter gourd can help you get rid of acne, blemishes and deep skin infections. Bitter melon is useful in treating blood disorders like blood boils, scabies, itching, psoriasis, ringworm and other fungal diseases. The free radicals in it are also useful for anti-ageing

4.Pagarkaai (Bitter gourd) for Diabetes: Bitter gourd juice benefits include helping to overcome type 2 diabetes.It has been a part of the Indian ancient medicine for a long time. Type 2 diabetes is caused partially due to the inability of a cell to absorb the sugar in the blood due to insufficient insulin or due to development of resistance to insulin. In both cases, the cells are unable to absorb the sugar due to the ineffectiveness of the insulin produced.The absorption of sugar occurs due to the activation of AMP-activated protein kinase in the cells. Bitter gourd activates these kinase due to which the absorption of sugar increases and hence, aids in bringing diabetes under control.

5.Pagarkaai (Bitter Gourd) for Constipation: Bitter gourd helps in easy digestion as it contains fiber properties. The food is digested and the waste is thrown out of the body which helps in curing indigestion and constipation problems

6. Pagarkaai (Bitter Gourd) for Kidney And Bladder: Bitter gourd- Pakarkkai helps to maintain a healthy liver and bladder. It is also useful in curing kidney stones.

7. Pagarkaai (Bitter Gourd) for Heart Disease: Bitter gourd/Pakarkkai is very good for the heart in many ways. It helps reduce the bad cholesterol levels which clog the arterial walls and thereby reduces the chances of heart attacks. Also, it is known to lower the blood sugar levels that help in maintaining a good heart health.

8.Pagarkaai (Bitter Gourd) for Weight Loss: Bitter gourd contains antioxidants that help to flush out your system. This improves your metabolism and digestive systems, thus helping you lose weight quickly.

9. Pagarkaai (Bitter Gourd) for as Natural Energizer: Regular consumption of bitter gourd juice improves stamina and energy levels of the individual and improves sleeping patterns.

10. Pagarkaai (Bitter Gourd) for Blood Purification: The antimicrobial and antioxidant properties of bitter gourd juice help to treat skin problems, blood disorders, clear toxins from the blood and purify it, and further improves blood circulation throughout the body. It helps to cure issues like itching caused by toxaemia, rashes, acne, psoriasis, blood boils and even inhibits the growth of cancerous cells in the body.

11. Pagarkaai (Bitter Gourd) for Skin Problems: The regular consumption of bitter gourd helps in keeping your skin glowing and free from blemishes. It also helps prevent acne thanks to its blood purifying properties.

12.Pagarkaai (Bitter Gourd) for Skin Infections: Bitter gourd benefits in treating skin diseases or skin infections, eczema and psoriasis and regular consumption of bitter gourd juice helps in improving psoriasis as well as other fungal infections like ringworm and athlete’s foot.

13. Pagarkaai ( Bitter Gourd ) for Anti-Aging: Bitter gourd contains vitamin C, which is a powerful antioxidant. By fighting and eliminating the harmful free radicals, it helps to prevent wrinkles by slowing down the aging process. It also protects the skin from damage by the sun’s ultraviolet rays.

14.Pagarkaai ( Bitter Gourd ) for Healing Wounds: Bitter gourd helps in controlling the blood flow and clotting, causing wounds to heal faster, preventing further infections.""",50.00,40.00),
            ("Great Basil/Thiruneetru Pachilai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/90.jpg","""Description
Benefits of the Great Basil:
Thiruneetru pachilai (Great basil) is a common medicinal herb and used in treatment of various diseases from time immemorial. The leaves of plant contain methylchaylcol, linalol, eugenol, thymol and xanthamicrol. The juice extracted from fresh leaves is folk medicine to treat respiratory disorders, fever, ear pain etc.
The flowers of plant are stimulant, carminative, antispasmodic, diuretic, and demulcent. Seeds are antidysenteric. The Juice obtained from leaf is antibacterial. The essential oil obtained from plant is antibacterial, anti-fungal and insecticidal.""",60.00,40.00),
            ("Vadhamadakki Powder 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/91.jpg","""Description
Benefits of Vadhamadakki Powder:
All kinds of Vaadha noigal & particularly Moottu theivathaal varum vaadham [azhalkeelvadham] & kudhikaal vadham [osteo arthritis].
It is useful to promote the strength of bones and joints.
It acts as an excellent anti-inflammatory and analgesic medicine.
It is used for the treatment of ankle pain, ankle twitch, slipped disc, sprain, back spasm, backache, back injury, stiffness of muscles, Coccyx pain, Bursitis, Bursitis trochanterica, Shoulder dislocation pain.
Post viral fever, when the patient complains of body, muscle, and joint pains.""",55.00,50.00),
            ("Touch-me-not/Thottaalsinungi Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/94.jpg","""Description
Benefits of Thottaal Sinungi:
1. Thottaal Sinungi Wound Healing Activity: Traditionally the leaf extract made by grinding the leaves with little water and extracting the juice is used for treating wounds.
2. Thottaal Sinungi Anti Venom Activity: The water extract of the Thotta Sinungi dried root powder proved that it is very good at inhibiting the activity of the snake venom.
3.Thottaal Sinungi For Ulcers: It has good effect on ulcers.
4. Thottaal Sinungi For Diarrhea: Thotta Sinungi is very good in treating diarrhea. A study done on albino rats by inducing them to diarrhea using castor oil and treating them with Thotta Sinungi extract proved to be very effective in controlling the diarrhea.
5. Thotta Sinungi Anti Diabetic Activity: Mimosa pudicas anti diabetic activity has been proven through research. The research was done using the ethanolic extract but usually the leaf powder or the root powder is taken daily for bringing down the blood sugar levels.
6. Liver Protecting Activity of Thotta Sinungi: Another important medicinal use its protection of liver against toxins . it proved to be very effective in protecting the liver from toxicity.
7. Anti microbial, Anti Fungal & Anti Viral Properties Of Thottaal Sinungi: Mimosa pudica has been proven for its anti microbial, anti fungal and anti viral properties. The research was done using different concentrations of the mimosa pudica ethanol extract on various fungus and bacteria and it proved to be very effective in controlling them.
8. Thottaal Sinungi for Anti fertility Activity: Mimosa pudica has proven to have anti fertility properties. so if you are trying for pregnancy, never consume mimosa pudica in any form.

Mimosa Pudica For Piles:

Mimosa Pudica is very good for treating bleeding piles and has been used as a remedy for it for many many years.""",50.00,40.00),
            ("Naayuruvi Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/95.jpg","""Description
Benefits of Naayuruvi:
1. Relieves nausea and Heal wounds
In case you are suffered from continued attacks of vomiting, you can use the herb to get relief. It will relieve your symptoms of nausea within a short time. The action of the herb on the superficial cuts, scrapes, and wounds helps to improve the healing time.

2. Asthma
Naayuruvi (Chaff Flower) open up the lungs making it wonderful for bronchitis and asthma. In India the flowers are made into a paste with equal amounts of garlic and black pepper to treat asthma and bronchitis. Take 1/2 teaspoon 3 to 4 times a day. It also works well for fevers associated with colds and flues.

3. Weight loss
If you want to lose weight, take the decoction of the herb in morning and evening. Soon, you will experience a loss of weight. This is due to the scraping effect of the herb on the cholesterol. Also, it reduces fat deposition, so your body begins to lose weight.

4. Detoxify the body
It is considered a strong herb that produces effective detoxification for the whole body. You can remove all the overrunning kapha and vatadoshas from the body.

5. Get relief from piles and itching
You can get relief from hemorrhoids and piles by using the Naayuruvi (Chaff Flower) herb. This is due to the balancing action of the doshas that prevents constipation and other conditions that lead to piles. The herb provides relief from external pain, scorpion bites, and itching. You can apply the paste on the site of the wound or bite locally to get relief.

6. Tooth Powder
Naayuruvi (Chaff Flower) seeds can be ground with salt into a find powder, it cleans and whitens your teeth like nothing else and stops your gums from bleeding. And the dried stems of the plant can be used as a toothbrush.

7. Cure infections and Helps decrease sputum
It is useful for curing infections and getting rid of worms in the head and neck region. By having the herb regularly, you can break down and expel sputum.

8. Controls hunger
Naayuruvi (Chaff Flower) has the ability to control the vata and kapha doshas in the body. In those diseases where uncontrollable hunger plays a part, one may use this herb for therapy. Make porridge with the Chaff Flower and feed this to the patient. They will soon recover from their ailment. Also, you can digest the ‘ama’ in the body which is the leftover undigested food in the GI tract.

9. Improve appetite, Cure glandular growths and hiccups
The herb improves taste, and this is useful for relieving anorexia. If you have fibroid and growth in the glands, you can use the Naayuruvi (Chaff Flower) herb to cure this condition. If you develop hiccups, have the decoction of the herb, and your hiccups will vanish.

10. Treat Ear pain and excellent diuretic action
People use the oil of the Naayuruvi (Chaff Flower) to get relief from an earache. Put a few drops of the oil in the ear, and soon your earache will disappear. It helps people suffering from dysuria, urinary retention, water retention, and urinary stones. You can use the herb to break down the stones in the bladder and kidney.

11. Treat Anemia and cure bleeding disorder
This herb can improve the blood count. Make a paste of the herb and add it to the diet. Have it at least two to three times a week to relieve the symptoms of anemia. The fruit of the Naayuruvi (Chaff Flower) herb is difficult to digest. This is useful for controlling and curing bleeding disorders.

12. Relieves gas, cure jaundice and Helpful in Asthma:
When there is an accumulation of gas in the intestines, it can lead to bloating and distension of the abdomen. By adding the paste of Chaff Flower to the diet, one may get relief from the gas problem.

When you have disorders of the liver and remain affected by diseases such as jaundice, you can use the herb to get a cure. Have the herb regularly morning and evening with tea. Your jaundice problem will soon disappear. The leaf helps relieve asthmatic problems. It helps enhance breathing by opening the air passages. You can use the decoction of the herb for this.

13. Helpful women medicine and Help treat many conditions
Chaff Flower finds a use for gynecology and obstetrics for induction of labor and abortion. It helps in the termination of postpartum bleeding. One can use Chaff Flower plant to treat a variety of conditions such as migraines, convulsions, and epilepsy. It also finds a use for treating psychological conditions. This is one of the best herbs for treating conditions affecting the head region.""",50.00,40.00),
            ("Elakkaai Podi/Elaichi/Cardamom Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/96.jpg","""Description
Benefits of Elaichi/Cardamom Powder:
1. Due to its Antioxidant and Diuretic Properties it helps in Lowering Blood Pressure.

2. Protects from Chronic Diseases because of its Anti-Inflammatory nature.

3. Help with Digestive Problems including Ulcers.

4. Treats Bad Breath and prevents ‘Cavities’.

5. Treat Infections because of it Antibacterial nature.

6. Improves Breathing and Oxygen Use.

7. Lowers Blood Sugar Levels significantly.

8. Good for Liver.""",100.00,80.00),
            ("Karunkali Kattai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/97.jpg","""Description
Benefits of Karunkali Kattai Powder:
The Karungali Kattai has immense medicinal benefits, rinse and soak the Karungali Kattai Powder in the water overnight, filter the water and drink it on empty stomach.

Helps to control blood sugar levels, bad cholesterol, aids in digestion and helps regulate the digestive organs, and may help prevent allergies as well as cancer.

Karungali Kattai removes all the toxins from the day and make you feel light like a feather.""",85.00,80.00),
            ("Vellarugu Powder 50g Each", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/98.jpg","""Description
Benefits of Vellarugu:
• It cure cataract naturally and this leaves are helpful in diseases such as cough, colds, flu & Cholera.
• It treats for Urinal problems & Jaundice.
• It is helpful for breathing problems.
• Eye problems,hair lice and itching of head,Migraine,Eczema & Wounds""",60.00,50.00),
            ("Sivanarvembu Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/99.jpg","""Description
Benefits of Sivanar Vembu:
• This plant helps to treat all kinds of skin diseases and acts as a blood purifier.
• It protects the liver and stimulates its function and is a cure for jaundice and Hepatitis.
• Sivanar Vembu relieves any inflammation, pain and lowers blood sugar level.
• This herb’s roots are a natural remedy for tooth ache, gum swelling and all types of ulcer, especially mouth ulcer.
• Preparation of Sivanar Vembu’s leaves and roots can be externally used to heal skin problems like eczema, psoriasis, ringworm and skin allergy and used as tooth powder and it is not bitter in taste, so you can even give to small kids.""",50.00,40.00),
            ("Sirupeelai Podi 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/100.jpg","""Description
Benefits of Sirupeelai:
• In Tamil Maruthuvam: For Urinal Problems; It is diuretic which helps in promoting the production of urine, effective in urethral problems, lithiasis, and gonorrhea.

• In Ayurveda: It acts as a demulcent which helps in getting relief from pain and inflammation.

• As per Paatti Vaithiyam: It acts as an astringent thereby helping in reducing bleeding in piles. It is also used as a treatment for diarrhea and hemorrhages.

• As a Natural Remedy: Sirupeelai’s stem acts as an antioxidant which helps in balancing the free radicals.

• As Great Natural relief for Kidney Stone: It is lithontriptic and antilithic which gives the plant the power to destroy stones in kidneys and bladder.

• As a Herbal booster: It is also known for increasing memory power and used to treat a headache, abdomen and digestion problems.

• In Siddha Maruthuvam for Back pain: It is effective for neck and back pain, fever, urine problems and also regulates body metabolism.

• As a Herb for Liver disease: Aerva Lanata is considered to be effective for hepatitis and inflammation of the liver.

• Natural way for fat burning: Aerva Lanata is also used for the treatment of many health problems like Anemia, Alzheimer, Arthritis, Cholesterol, lung problems, bone problems and also blood circulation.

• Helps to fight against pathogens: It protects both the skin and the body from pathogens and it is anthelmintic which helps in destroying parasitic worms and reducing sores and injuries on the skin.""",60.00,50.00),
            ("Papaya Leaves Powder/Pappali Ilai Podi 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/101.jpg","""Description
Benefits of Pappali Ilai:
Treats Dengue fever:
A common remedy that is advised by all to dengue patients is papaya leaf juice.

Dengue is caused by infected Aedes mosquitoes, who transmit the disease into our blood.

Dengue fever severely brings down the blood platelet count, and the extracts from papaya leaf are known to help increase the count.

Anti-Malarial Properties:
Papaya leaves have strong anti-malarial properties. A compound found in papaya leaf is acetogenin, which can help prevent dangerous disease like malaria and dengue.

Good for Liver:
Just as papaya, papaya leaf juice also acts as a potent cleansing agent for the liver, thereby healing many chronic liver diseases,jaundice and liver cirrhosis. Lowers Blood Sugar LevelsPapaya leaf juice can work wonders for diabetics as well, as it regulates the production of insulin, which in turn checks blood sugar levels. Its strong antioxidant nature also helps to bring down the consequent complications of diabetes like kidney damage and fatty liver.

Cure to Your Menstrual Pain:
Are you a victim of excruciating menstrual cramps and lower abdominal pain during your periods? Papaya leaf juice works wonders to ease the menstrual flow and reduce the pain. Drinking this juice also brings down PMS symptoms. Its potent healing properties balance hormones, and regulate menstruation cycles. You can try this concoction to treat your menstrual pain: take one papaya leaf, a pinch of salt and tamarind, mix them all in a glass of water and bring it to boil. This juice should ease your pain greatly.

Supports Digestion:
Papaya leaves are also rich in protease and amylase. These enzymes help break down proteins, carbs and minerals aiding digestion. Its high anti-inflammatory properties also reduce the inflammation of stomach and colon

Helps Treat Skin Problems:
Papaya leaf juice has a rich content of vitamin C and A, which boost skin health and lend you a healthier and radiant skin. Papaya leaf juice suppresses the activity of free radicals. The presence of karpain compounds checks the growth of excess micro-organisms, and cleanses your skin of the toxins, providing protection against skin problems like pimples, freckles and acne.

Promotes Hair Growth:
The extract of papaya leaf is said to promote hair growth, prevent balding and thinning of hair. It is an important ingredient used in anti-dandruff shampoos because of the karpain compound. This alkaloid component is effective in removing dirt and oil from your scalp. It can also serve as a natural conditioner and bring back the lost sheen to your hair.""",50.00,40.00),
            ("Mukkarattai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/102.jpg","""Description
Benefits of Mukkarattai Powder:
• Mukkarattai Powder may cure the problems related to dryness or coldness like fever can be cured.
• Mukkarattai Powder strengthens male reproductive system.
• Mukkarattai Powder is good for the liver.
• Mukkarattai Powder fights obesity.
• Mukkarattai Powder is good for diabetes.
• Mukkarattai Powder prevents heart failure.
• Mukkarattai Powder cures impotence.""",80.00,60.00),
            ("Cinnamon Bark Powder/Lavangapattai Podi 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/103.jpg","""Description
Benefits: 
Lavangapattai is used to cure,

• Chronic cough

• Vomiting

• Indigestion""",80.00,90.00),
            ("Karuvelampattai Powder 50g ", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/104.jpg","""Description
Benefits of Karuvelam Pattai:
• It used for Dhatu rog, Night fall, Leucorrhoea, Prameha, Pradar.
• It cures Spermatorrhoea, loss of viscidity of semen, frequent night discharges and premature ejaculation

Other benefits:

1. Karuvelam for Tooth and gum related problems:
• Bark of babul for acts good in teeth and gum problems.

2. Karuvelam for mouth care:
• Antimicrobial action that causes reduction in oral problems
• Reduces plaque formation
• Reduces gingival inflammation (inflammation of the gums )
• Causes alkalinity of saliva that is pH of saliva increases which helps in protecting teeth from cavities, decay
• Prevents cavities, gum swelling

3.Eye diseases :
• Eye infection
• Redness""",80.00,60.00),
            ("Siriyaanangai Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/105.jpg","""Description
About:
Siriyaanangai can be consumed in case of a snakebite. It is said to possess the power of absorbing the venom.
"When a fight breaks out between a mongoose and a snake, if the mongoose gets bitten and poisoned, it is said that it rolls over a small 'Nangai' plant (a medicinal herb) to heal itself from the venomous wound and find relief."
Consuming Siriyaanangai:
Morning:

Mix 5 gms of powder in 100 ml of water, Boil the content for a few minutes, once the water gets warm, filter the content and drink it before food. Repeat the same for Evening after dinner""",35.00,40.00),
            ("Seendhilkodi Powder 50g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/107.jpg","""Description
Benefits of Seenthil Kodi:
As said in Ayurveda, It has anti-diabetic, anti-cancer, anti-HIV, anti-stress, antispasmodic, anti-arthritic, anti-inflammatory, antioxidant, antimicrobial, anti toxic, anti-allergic, antipyretic, anti malarial, anti-tumor, and liver-protective properties.

In Naattu Maruthuvam, It used for indigestion and stomach problems.

It helps to boost up the body’s defense power.
In Tamil Maruthuvam, It helps to promote the power of mind and rejuvenate it.

In Siddha Maruthuvam, It helps to maintain healthy blood sugar level and blood pressure level which is already within the normal limits.
It helps to maintain normal body temperature due to its bitter taste.""",50.00,40.00),
            ("Nocchi Leaves Powder 50g Each", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/108.jpg","""Description
Benefits of Nocchi Leaf:
In Ayurveda: It helps to reduce the swelling and pains of joints and Muscle sprains.
As Herbal Medicine: Helps in digestion and Its used for burns,post childbirth problems,fever,muscle sprains, scandy urine, antiseptic, nervine, emmenagogue ,migraine.
In Nattu Maruthuvam: Due to its warm potency it helps to increase the menstrual flow in those who have scanty periods (menstrual flow).
As one of its Herbal Remedies: Helps to control the discharge through ears.
Eye sight: Helps to provide healthy eye sight.
Helps to reduce the generalized pains of body.
Helps in stimulating the liver for its healthy secretions.""",50.00,40.00),
            ("Attathi Powder 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all powdered/109.jpg","""Description
Ingredients:
1)Sukku
2)Thippili
3)Milagu
4)Seeragam
5)Karunjeeragam
6)Indhuppu
7)Omam
8)Perunkaayam

Benefits of Attathi Podi:
Indigestion (செரியாமை)
Loss of Appetite (முற்றுடல் வளி)
Quadraplegia""",90.00,80.00),
        ],
     "Raw/Herbal Products":[
            ("Pulukka Pattai 50g Each","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/5.jpg","""Description
Benefits of Pulukka Pattai:
• It is a good solution for hairfall, dandruff and other such hair problems.

• Pulukkapattai along with Vembaada pattai is one of the main ingredients of ‘shikakai’.""",40.00,30.00),
            ("Kariya Polam/Pavalam 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/7.jpg","""Description
Benefits of Kariya polam:
1) Suitable for external wounds and extremely good for “Blood clots“

2) It is used to treat eruptions and skin rashes.

3) Besides the pimples, they are also used extensively and traditionally to correct the growth of the fleshy face.

4) This works best in cut and burns and accelerates the healing process.

5) This is widely used in the treatment of acne and scars and is used in most cosmetics.""",70.00,60.00),
            ("Madhana Poo/Sago Palm 25g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/8.jpg","""Description
Benefits Of Madhana Poo/Flower:
• The major benefit of Madhana Kaama Flower is to eradicate sexual weakness in men.
• It also cures your body’s weaknesses quickly and easily.
• To get relief from pain and inflammation, you need to finely paste the flower and then apply the paste to the affected area.
• Powdered seeds are also used for most culinary purposes.
• You can add this to your regular diet to have a good sleep. Mix the paste with milk and drink it before going to bed.
• Drinking milk mixed with this powder improves the sexual activity in men.""",80.00,60.00),
            ("Poolan Kizhangu Powder 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/12.jpg","""Description
Benefits of Poolan Kizhangu:
• Poolan Kizhangu is helpful in treating liver complaints, indigestion and poor circulation due to thickening of the blood.
• It is used in treating nausea, halitosis, vomiting, diminished appetite, hiccups and local inflammation.
• The rhizomes of Poolan Kizhangu are used in treating asthma and internal injuries.
• The rhizomes are powdered and used as an antiseptic agent and as a poultice for various aches and pains.
• Its rootstalk is used in treating bronchitis and alleviating pain.
• It is good for skin.""",50.00,40.00),
            ("Sadhakuppai/Catakuppai 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/14.jpg","""Description
Benefits of Sathakuppai:

• Help to Reduce Menstrual Cramps
• Helps Reduce Depression
• Treat for Insomnia
• Respiratory disorders
• Lowers Cholesterol
• May Treat Epilepsy Provides a Source of Energy and Aids in Digestion through Beneficial Fatty Acids""",30.00,25.00),
            ("Vetti Ver 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/16.jpg","""Description
Benefits of Vetti Ver:
• Vetti Ver(water) naturally has a cooling effect. It helps to cure painful urination, ulcers and bad breath.

• This aromatic water has a calming effect on the nerves and regular intake of this water helps in general well being and it acts as a blood purifier.

• Eye burning, head ache, fever, hair care & used for bath powder""",50.00,45.00),
            ("Thean Kaai/Thaen Kai 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/17.jpg","""Description
Benefits of Thean kai:
The seeds of this herbal medicinal plant are used to control Blood sugar levels or in the Treatment of Diabetes. The patient has to consume two seeds in the morning and two seeds in the evening for the first week. This dosage can be varied according to the individual’s body conditions. have little water after taking seeds.

In Indian Traditional Medicine this herbal plant is also used to promote Long life, Take care of skin complaints, Reduce fever, Treatment of asthma, Bronchitis treatment. It is very powerful against intestinal worms.""",100.00,80.00),
            ("Sukku Powder 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/18.jpg","""Description
Benefits of Sukku:
• Digestive disorders: This extremely useful herb is used to relieve patients suffering from dyspepsia, flatulence, vomiting, spasms, colic and other stomach problems.
• Cough and Cold: The herb is used to relieve cough.
• Respiratory Disorder: It reducing fever in patients suffering from influenza. It is known to act as an expectorant in relieving asthma, cough and tuberculosis.
• Impotency: The herb is known to be an effective aphrodisiac. It relieve impotency, premature ejaculation, involuntary seminal discharge and also spermatorrhoea.
• Menstrual Disorders: A piece of ginger with a cup of boiled water must be used to relieve menstrual problems.""",33.00,40.00),
            ("Avarampoo/Aavaarampoo 25g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/20.jpg","""Description
Benefits of Sukku:
• Digestive disorders: This extremely useful herb is used to relieve patients suffering from dyspepsia, flatulence, vomiting, spasms, colic and other stomach problems.
• Cough and Cold: The herb is used to relieve cough.
• Respiratory Disorder: It reducing fever in patients suffering from influenza. It is known to act as an expectorant in relieving asthma, cough and tuberculosis.
• Impotency: The herb is known to be an effective aphrodisiac. It relieve impotency, premature ejaculation, involuntary seminal discharge and also spermatorrhoea.
• Menstrual Disorders: A piece of ginger with a cup of boiled water must be used to relieve menstrual problems.""",40.00,30.00),
            ("Pumpkin Seeds/Poosani Vidhai 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/22.jpg","""Description
Pumpkin seeds may be small, but they’re packed full of valuable nutrients.
Eating only a small amount of them can provide you with a substantial quantity of healthy fats, magnesium and zinc.
Because of this, pumpkin seeds have been associated with several health benefits.
These include improved heart health, prostate health and protection against certain cancers.

1. Full of Valuable Nutrients
Pumpkin seeds are also known as “pepita” — a Mexican Spanish term.
Unlike the hard white seeds from a carving pumpkin, most pumpkin seeds bought at the supermarket don’t have a shell.
These shell-free seeds are green, flat and oval.

2. High in Antioxidants
Pumpkin seeds contain antioxidants like carotenoids and vitamin E.
Antioxidants can reduce inflammation and protect your cells from harmful free radicals. That’s why consuming foods rich in antioxidants can help protect against many diseases.
It’s thought that the high levels of antioxidants in pumpkins seeds are partly responsible for their positive effects on health.
In one study, pumpkin seed oil reduced inflammation in rats with arthritis without side effects, whereas animals given an anti-inflammatory drug experienced adverse effects.

3. Linked to a Reduced Risk of Certain Cancers
Diets rich in pumpkin seeds have been associated with a reduced risk of stomach, breast, lung, prostate and colon cancers
A large observational study found that eating them was associated with a reduced risk of breast cancer in postmenopausal women
Others studies suggest that the lignans in pumpkin seeds may play a key role in preventing and treating breast cancer
Further test-tube studies found that a supplement containing pumpkin seeds had the potential to slow down the growth of prostate cancer cells

4. Improve Prostate and Bladder Health
Pumpkin seeds may help relieve symptoms of benign prostatic hyperplasia (BPH), a condition in which the prostate gland enlarges, causing problems with urination.
Several studies in humans found that eating these seeds reduced symptoms associated with BPH.
In a one-year study in over 1,400 men with BPH, pumpkin seed consumption reduced symptoms and improved quality of life.
Further research suggests that taking pumpkin seeds or their products as supplements can help treat symptoms of an overactive bladder.
One study in 45 men and women with overactive bladders found that 10 grams of pumpkin seed extract daily improved urinary function.

5. Very High in Magnesium
Pumpkin seeds are one of the best natural sources of magnesium  — a mineral that is often lacking in the diets of many Western populations.
In the US, around 79% of adults have a magnesium intake below the recommended daily amount
Magnesium is needed for more than 600 chemical reactions in your body. For example, adequate levels of magnesium are important for:
• Controlling blood pressure
• Reducing heart disease risk
• Forming and maintaining healthy bones
• Regulating blood sugar levels

 """,120.00,100.00),
            ("Dried Rose Petals/Roja Idhazh 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/24.jpg","""Description
Benefits of Roja Idhazh(Rose Petal):
• Rose Petal water is an effective astringent that reduces swelling of capillaries beneath the skin.
• Rose Petal tea is efficient in cleansing gall bladder and liver, and it helps improve bile secretion. Rose petals are dried and crushed and the powdered form is added in tea.
• Rose petal tea also helps in alleviating mild sore throats and bronchial infections. The tea cools the body and reduces fever-related rashes.
• Rose essential oil is used along with carrier oils such as almond or grape fruit to treat various illnesses like hemorrhage, liver problems, nausea, fatigue, ulcers, asthma, dehydration, and bacterial infections of the stomach, colon, and urinary tract.
• Rose petals are an important ingredient in eye washes as well, as it is antiseptic in nature.
• Rose Petal water benefits include nourishing the scalp and improving hair growth. It is medicinally used as an antibacterial, antiseptic, and anti-inflammatory product. It is also used to treat dry scaly skin and dermatitis.""",35.00,30.00),
            ("Karunjeeragam 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/25.jpg","""Description
Benefits of Karunjeeragam:
• Weight Loss diet tips: Consuming Karunjeeragam is an easy way to shed extra calories. It may be considered as one of the weight loss diet plans. It helps to make you slim without visiting to gym.

• Type 2 diabetes: Just two grams of Karunjeeragam daily could result in reduced fasting blood sugar levels, along with decreased insulin resistance, and increased beta-cell function in the pancreas.

• Epilepsy: Karunjeeragam will be effective at reducing the frequency of seizures in children who resisted conventional treatment. Karunjeeragam indeed has anti-convulsive properties.

• Protection Against Heart Attack: An extract from Karunjeeragam has been shown to possess heart-protective qualities, dampening damages associated with heart attacks and boosting overall heart health.

• Sinus problems: Karunjeeragam is effective in giving you relief from the frequent occurrence of sinusitis.

• Joint pain home remedies: It is useful in relieving of joint pains, knee pains and arthritis.

• Neck pain remedy: Solve your neck pain and cervical related pains by using Karunjeeragam.

• Sexual problems: Karunjeeragam have effective solution to get rid off from sexual weakness.

• Karunjeeragam for gynecological issues: Karunjeeragam is helpful in treating and curing of many gynecological problems such as Menstrual, Leucorrhoea, White discharge, back pain, stomach pain, etc.""",60.00,50.00),
            ("Semparuthi/Sembaruthi Dried Hibiscus 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/26.jpg","""Description
Benefits of Semparuthipoo(Hibiscus):
Controls High Blood Pressure & Cholesterol Levels

Cures Cold : Hibiscus is rich in Vitamin C and thus it has the capacity to cure cure minor cold related infections like sore throat, cough and headache.

Boosts Energy : As the antioxidants in hibiscus help to repair free radical damage, your energy levels naturally go up.

Calms Hot Flashes : Women who are going through the tough hormonal period of menopause might use the health benefits of hibiscus. Hibiscus can help soothe hot flashes.

Slows Ageing : The antioxidants in hibiscus not only help to fight cancer but also also slow down the ageing of your cells. As a result, it may be the secret to eternal youth.

Boost Immunity : One of the main health benefits of hibiscus flower is that it helps to boost the level of immunity in your body.

Maintains Fluid Balance : According to ancient sources, having hibiscus flower extracts can help to maintain the fluid balance in your body. It was once used as a cure for oedema or excess water retention in the body.

Speeds Up Metabolism : Vitamin C has a very essential place in the digestive system. And as hibiscus is rich in Vitamin C, it helps to increase the rate of metabolism.

Maintains Body Temperature : According to ancient African medicine, having hibiscus flower extracts regulates the body temperature. It helps to flush out excess body heat in summers.

Hair care : It is also used for hair growth.

Cures Acne : Hibiscus has many natural anti-inflammatory substances and also Vitamin C that can stop the growth of acne and even clear the marks left by it.""",30.00,20.00),
            ("Thippili 10g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/27.jpg","""Description
About Thippili:
Thippili is very famous among Tamil people and is used extensively in home remedies. Not only in Tamil Nadu, long pepper has been in use all over the world from ancient times. We use both the dried fruits and the roots of the plant in remedies. The fruits are called “Arisi Thippili ” in Tamil and the roots are called “Kandathippili in Tamil “. Thippili is called Long Pepper in English.

Benefits of Thippili:
• It is used for treating depression, weight loss, all kinds of inflammation and diabetes!
• Long pepper has anti oxidant, anti depressant, anti inflammatory, anti microbial, analgesic, anti fungal and cardio protective properties.
• It control Hiccups,controls Headache, Vitamin B1 deficiency, Fever, Headache and Stroke.""",30.00,25.00),
            ("Sabja Seeds 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/30.jpg","""Description
Benefits of Sabja:
Sabja Seeds for Weight loss:
If you take Sabja Seeds, you will not be hungry for a long time. It may be due to fiber in it. If you do not get hungry for a long time, you can prevent the weight gain. When you are in diet to reduce weight, Sabja seeds will be useful.

Sabja Seeds for body heat:
Generally, It is best to take the Sabja Seeds in summer. Because it reduces body heat and keeps the body cool. So if you are suffering from too much body heat,  soak it in a cool water at night and drink the next morning.

Sabja Seeds for Constipation:
Sabja Seed is the best medicine to get rid of constipation.The elderly people who have constipation should drink a teaspoon of Sabja Seeds  in hot milk. This is also a relief for the constipation during pregnancy.

Sabja Seeds for Diabetes:
Sabja seeds are good for type 2 diabetic patients. Diabetic patients can keep it in the water, add it to cold milk, and drink some drops of vanilla eszines and maintain the level of sugar in the blood.

Sabja Seeds for Acidity:

Sabja Seeds help cure problems in the stomach. If you are stuck with heartburn or acidity, soak these seeds in water at night and drink with milk next morning without drinking tea / coffee.""",33.00,25.00),
            ("Karpooravalli Podi/Powder 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/33.jpg",""" Karpooravalli Podi (Powder)
Natural Remedy for Cold, Cough & Indigestion

Karpooravalli, also known as Indian Borage or Oma Valli, is a powerful traditional herb used for generations in Siddha and Ayurvedic medicine. This aromatic leaf is naturally rich in antimicrobial, anti-inflammatory, and respiratory-supporting properties.

✅ Benefits:
💨 Relieves Cold, Cough, and Congestion
Acts as a natural expectorant – helps clear blocked nose and chest phlegm.

🌬️ Supports Respiratory Health
Soothes sore throat, asthma symptoms, and seasonal allergies.

🧘‍♂️ Improves Digestion
Stimulates appetite and helps relieve indigestion, bloating, and acidity.

🦠 Natural Immunity Booster
Helps protect the body from common infections with regular use.

🧂 How to Use:
Mix 1 spoon of Karpooravalli Podi with warm water or honey twice a day.

Can also be added to hot rasam or herbal teas for added flavor and benefits.

Safe for children (in smaller quantities) and adults.

📦 Ingredients:
100% Pure Dried and Powdered Karpooravalli Leaves (Indian Borage)

🧴 No additives. No preservatives. 100% Natural.""",60.00,50.00),
            ("Licorice/Athimathuram[Adhimathuram] 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/34.jpg","""Description
Benefits of Athimathuram:
• Medicine for Digestion: Athimathuram root has been used for centuries to treat various ailments that involves digestive tract, as it helps to protect the stomach lining.
• Medicine for Cough: Athimathuram tea is amazing home remedy for cough and since it is sweet by itself, it is easier to make the children drink it.
• Paatti Vaithiyam for Menstrual cramps: It also relieves menstrual cramps as it has antispasmodic and anti inflammatory proprieties.
• Medicine for Constipation: It is also a laxative and can relieve a person, who suffers from constipation. Consume this tea daily for 2 to 3 days to get good relief from constipation.
• Herbal remedy for Arthritis: Athimathuram has anti inflammatory properties, so it may help people who are suffering from arthritis.
• Natural Blood purifier: Blood purification and more – Athimathuram is known for its blood cleansing properties & used for blood circulation problem.
• Hair: It is good for your hair too.""",50.00,40.00),
            ("Kalarchikai/Klachikai 100g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/35.jpg","""Description
Benefits of Kalarchikai:
• The root bark has been used for treating intestinal worms, fever, tumors, cough, amenorrhea, and to remove the placenta after childbirth.
• The fruit is used for eliminating piles, wounds, leucorrhea, and urinary disorders.
• Boiled leaves can be used for gargling to relieve a sore throat.
• The juice extract of the leaves is used in controlling elephantiasis and smallpox.
• The leaves and seeds after roasted in castor oil can be applied to reduce piles, inflammatory swellings, orchitis, and hydrocele.
• A paste made from the leaves and twigs is useful in reducing toothache.""",100.00,80.00),
            ("Vembaada Pattai 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/36.jpg","""Description
About:
Vembaada Pattai is a herb in the Borage family, It has a dark red root of blackish appearance externally, but blue-red inside, with a whitish core. The root produces a fine red coloring material, which has been used as a dye in the Mediterranean region since antiquity.

Benefits of Vembaada Pattai:
• Vembaada Pattai is primarily used as a dying and coloring agent.

• Vembaada Pattai along with Pulukka Pattai makes one of the main ingredients of ‘Shikakai’.""",42.00,35.00),
            ("Kadukkai 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/37.jpg","""Description
Benefits of Kadukkai:
Weight loss: Kadukkai is known to remove toxins from the body and keeps the digestive system in peak order. It prevents bloating sensation, acidity and helps in proper assimilation of food. Kadukkai is a natural blood purifier and it helps to remove the toxins in the body. Consuming Kadukkai will regulate hunger and combined together with a sensible diet and exercise will aid in weight loss naturally.

Cough in infants and adults: Kadukkai is amazing for treating cough in both adults and infants.

Constipation: Kadukkai powder is a natural laxative that is available to us. Many suffer from constipation and take medicines for it continuously. Having a traditional diet that is rich in fiber and using natural laxatives like Kadukkai podi / powder will keep our bowels in good health.

Acidity: Kadukkai is known to cure all stomach related problems from acidity and indigestion to constipation very effectively. Kadukkai increases the mucus production in the stomach forming a protective barrier thus preventing acidity and ulcer.

Diabetes: Kadukkai decreases insulin sensitivity and helps to regulate the blood sugar levels in the body effectively. The interesting thing was many of the diabetic medicines had some side effects along with regulating the blood sugar levels whereas Kadukkai did not have any side effects at all. But diabetic patients should consult a medical professional before taking kadukkai daily on a regular basis.

Hair loss: In certain parts of India, Kadukkai oil is used on the hair to prevent lice infection and dandruff. They use it as a daily application hair oil.

Skin allergies: Kadukkai effectively treats skin allergies in the ears caused by earrings. Gold and silver earrings doesn’t produce any allergies. if we wear these earrings for longer duration, the earlobes turn itchy, red and swollen. Usually it gives good relief from pain and swellings due to allergies.

Mouth ulcers: Kadukkai has anti cariogenic properties and can be used for most of the dental problems especially mouth ulcers and bleeding gums.

Consuming Kadukkai Podi:
Mix a teaspoon of Kadukkai powder in either hot water or honey and consume before going to bed.""",40.00,30.00),
            ("Vaalmilagu 10g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/39.jpg","""Description
Benefits of Vaalmilagu:
• It is commonly used to treat problems with the digestive and urinary tract.
• Vaalmilagu relieves gas and bloating in the digestive tract.
• Crushed Vaalmilagu is smoked, and the inhaled smoke produces a soothing effect in certain respiratory ailments.
• Vaalmilagu is used to treat the symptoms of bronchitis.
• Paste of Vaalmilagu is used as a mouthwash.
• Dried Vaalmilagu internally used for oral and dental diseases, loss of voice.
• It is used to cure fevers and cough also.
• It can relieve infections in the urinary system.
• Vaalmilagu has expectorant properties so that it can thin mucus.""",50.00,40.00),
            ("Moringa/Murungai/Drumstick Seeds 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/40.jpg","""Description
Benefits of Murungai Vithai:
1. Ayurvedic Medicine to Lower Blood Pressure: High blood pressure is a serious cardiovascular issue that can lead to heart attacks and stroke if it isn’t managed. While studies have shown that moringa can lower blood pressure, these studies are preliminary and more research needs to be done on humans, so talk to your doctor before stopping any prescribed treatment for high blood pressure.
2. Siddha Medicine to Boost Energy: A single serving of moringa has almost three times the amount of iron as spinach. This is especially important for vegetarians/vegans and those who suffer from low iron issues, as the body needs iron to enrich the blood and carry oxygen to our muscles, organs, and tissues.
3. Paatti Vaithiyam to Lower Blood Sugar Levels: Moringa seeds can lower blood sugar levels, which would provide therapeutic management (or even prevention) of diabetes. However, the study was done on lab rats and research is needed on humans before any recommendations can be made.
4.Natural food with High Fiber: Moringa is high in fiber, and as a result it can do a great job of moving food along your digestive system. Fiber is also a key component in maintaining a healthy cardiovascular system.
5. Natural way to Lower Cholesterol: Too much cholesterol in the blood has been linked to heart disease. In traditional Tamil medicine, moringa is used as a Cardio tonic. Some plants have been known to reverse bad cholesterol and research is showing that moringa is among them.
6.Herb to Promote Healthy and Beautiful Skin: The oil extracted from the seeds contains almost 30 antioxidants. The skin absorbs the oil well and can receive these nourishing antioxidants easily. The oil can be used as a moisturizer and antiseptic.""",100.00,80.00),
            ("Maasakkaai/Masikaai 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/41.jpg","""Description
Masikkai Powder – Traditional Herbal Remedy
Masikkai (Nutgall) is a time-tested natural remedy with a wide range of health benefits, especially for women, skin, digestion, and more.

✅ Womb Health (Uterus Support)
Masikkai is a natural boon for women. Regular intake of Masikkai powder mixed with honey or ghee can help regulate heavy menstrual bleeding. It also purifies the uterus by eliminating toxins and strengthens it.

✅ Healing Wounds
Masikkai powder mixed with water and applied externally on wounds, piles, or sores around the anal area provides excellent relief. It is also effective for skin issues such as eczema, fungal infections, psoriasis, and rashes when applied daily.

✅ Relief from Diarrhea
For stomach upset due to contaminated food or weather changes, taking a pinch of Masikkai powder with honey three times a day can help stop diarrhea. It’s also a gentle remedy for children.

✅ Stopping Bleeding from Cuts
When accidentally wounded and bleeding occurs, roast a few pieces of Masikkai in fire, turn them into ash, and press it on the bleeding wound. It helps control bleeding effectively.

✅ Detoxification (Against Poisoning)
Masikkai acts as a natural antidote against harmful toxins caused by drugs, alcohol, or certain chemical exposures. Taking 5 grams of Masikkai powder three times daily helps detoxify the body from substances like opium, ganja, alcohol, mercury, and arsenic.

✅ Respiratory Problems
Especially in cold seasons, Masikkai helps in relieving respiratory issues such as cold, cough, tonsils, throat pain, and sinus congestion. For best results, mix the powder with Karpooravalli (Indian Borage) leaf juice and consume.

✅ Male Vitality
Due to stress and lifestyle issues, many men face vitality-related problems. A blend of Masikkai, Nutmeg, Avaram Bark Paste, Cardamom, and Vallarai Leaf Powder sautéed in ghee strengthens the nerves and improves male reproductive health.

✅ Skin Care and Anti-Aging
Masikkai, when mixed with nutmeg and clove powders and applied externally, reduces wrinkles and promotes youthful skin. It helps tone and brighten the skin naturally.

✅ Oral Health
Masikkai helps maintain overall oral hygiene. Gargling with Masikkai powder mixed in warm drinking water heals tongue sores, strengthens gums, stops gum bleeding, and cures ulcers caused by excess body heat.

✅ Heart Health
For palpitations caused by anxiety or stress, mixing a small amount of Masikkai powder in cold milk and applying it gently on the tongue calms the heart in just a few seconds.

💡 Note:
Masikkai Powder is a multipurpose herbal powerhouse. For internal consumption or external application, always follow appropriate dosage or consult a traditional practitioner when needed. Safe for daily use in small quantities.

""",80.00,60.00),
            ("Carrom Seeds Ajwain/Omam 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/42.jpg","""Description
Benefits of Omam/Carrom Seeds:
1. Fights bacteria and fungi:

Carom seeds have powerful antibacterial and antifungal properties.
This is likely attributed to two of its active compounds, thymol and carvacrol, which have been shown to inhibit the growth of bacteria and fungi.

2. Improve cholesterol levels:

Animal research indicates that carom seeds may lower cholesterol and triglyceride levels. High cholesterol and triglyceride levels are risk factors for heart disease.
In one rabbit study, carom seed powder reduced total cholesterol, LDL (bad) cholesterol, and triglyceride levels.

3. Lowers blood pressure:

High blood pressure, or hypertension, is a common condition that increases your risk of heart disease

4. Combats peptic ulcers and relieves indigestion:

Carom seeds are commonly used as a household remedy for digestive issues in Ayurvedic medicine. Carom seed extract also helps prevent and treat gas and chronic indigestion. Indigestion is categorized as persistent pain and discomfort in the upper part of your stomach. Delayed stomach emptying is one of the perceived causes of indigestion.

5. May prevent coughing and improve airflow:

Some evidence suggests that carom seeds may provide relief from coughing. Carom seeds also improves airflow to the lungs.

6. Has anti-inflammatory effects:

Inflammation can be good or bad. Short-term inflammation is your body’s natural way of protecting against illness or injury.
On the other hand, chronic inflammation can have negative effects on your body and increase your risk of certain diseases.""",60.00,40.00),
            ("Vasambu/Sweetflag 2 pieces","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/43.jpg","""Description
Benefits of Vasambu(Sweet Flag):
• Vasambu helps to get rid of all gastric problems.
• It stimulating aroma rejuvenates the brain and the nervous system.
• It is also effective against digestive disorders.
• Baby nutrition problems and baby sleep problems are the most common problems in newborns.
• Remedy for acid re-flux, loose motion, hair removal, and flatulence. The other stomach problems like indigestion, stomach, loss of appetite can also be cured with the herb extracts.""",30.00,20.00),
            ("Cucumber Seeds/Vellari Vidhai 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/44.jpg","""Description
Cucumber plants are tendril bearing vines, rooting at the nodes, with triangular prickly hairy leaves and yellow flowers which are either male or female. The female flowers are recognized by the swollen ovary at the base which will become the edible fruit. The fruit is roughly cylindrical, elongated, with tapered ends, and may be as large as 60 cm long and 10 cm in diameter. Cucumber originated in south Asia, but is now cultivated throughout the world.

Benefits of Vellari vithai(Cucumber Seeds):
Hair Benefits:
If you are suffering from hair problems like hair fall and weak hair then cucumber seeds is the key to treat all your problems. The sulphur content of cucumber seeds helps in stimulating the growth of hair and makes them thick and healthy. Regular consumption of cucumber juice (with seeds) helps in preventing the problem of hair fall effectively.

Digestive Health Benefits:
Regular consumption of cucumber seeds is highly recommended as it helps in stimulating the overall digestive health. Cucumber seeds help in preventing a number of digestive problems like acidity, ulcers, gastritis, indigestion etc. The water, fibre and mineral content of cucumber helps in the smooth functioning of the digestive organs and helps in flushing out the toxic materials from the body.

Aids in weight loss:
It helps to shed theextra weight from the body when cucumber seeds are added in diet chart. Cucumber seeds contain less calorie and the water and mineral content of it help in losing weight more efficiently.

Promotes Gum and Teeth Health:
Regular consumption of cucumber seeds helps in improving the overall gum and teeth health. The photo chemical content of cucumber seeds is very useful in fighting off the harmful bacteria from the mouth and thus helps in getting rid of the problem of bad breath and cavities. cucumber seeds also help in increasing the salivation process too.

Promotes Brain Health:
The copper content of cucumber seeds helps in stimulating the process of neurotransmission which in turn improves the overall brain coordination. Regular consumption of cucumber seeds is recommended as it provides all the essential minerals that are required for improving the brain’s health. Regular consumption of cucumber seeds is linked with lower stress level if you have high stress then add cucumber to your daily routine in order to keep yourself up and charged.

Anti Inflammation:
Cucumber seeds possess anti inflammatory properties that help in reducing the inflammation. Regular consumption of cucumber seeds is also helpful in treating the problem of head ache.

Skin Benefits:
Cucumber seeds are very useful in treating a number of sin problems like sunburn, dry skin, tanning, wrinkles etc. The use of these seeds helps in providing a youthful look to your skin. The anti oxidants present in cucumber helps in revitalizing the skin and add a natural glow to it.""",80.00,60.00),
            ("Venkunguliyam/Venkungulingam White Kunguliyam 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/45.jpg","""Description
Benefits:
White Kungiliam is also used in Ayurveda, Siddha and Unani because of its miraculous medicinal power like the ordinary one.
It is good for curing chronic skin disorders, musculoskeletal disorder, tumors, diseases of oral cavity, rheumatism, fever, cough, asthma, epilepsy, ear and hair ailments etc.
It is also used to produced germ killers and perfumes""",80.00,60.00),
            ("White Pepper/Vellai Milagu 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/46.jpg","""Description
Benefits of Vellai Milagu (White Pepper):
• White pepper for indigestion: White pepper enables the body to emit more hydrochloric corrosive, which is fundamental for processing proteins and other nourishment parts. Additionally, white pepper has a lot of fiber. Fiber invigorates peristaltic movement and expanded discharge of gastric juices, which facilitates absorption, avoids conditions like a blockage, and shields the body from more genuine conditions like a colorectal malignancy. Fiber can likewise rub cholesterol out of the courses and veins.
• White pepper can aid vitality generation and cell reinforcement barrier: White pepper has an unpretentious measure of manganese, which is a fundamental cofactor in a few compounds imperative in vitality generation and cancer prevention agent resistance. For instance, a few chemicals incapacitate free radicals delivered inside the mitochondria (the vitality creation plants inside our cells), which require manganese.
• White pepper may enhance dental well-being: White pepper battles tooth rot and gives snappy alleviation from a toothache.
• White pepper may help skin conditions: Piperine, in white pepper, has appeared to be viable against vitiligo, a skin sickness that makes regions of the skin lose their pigmentation.
• White pepper is helpful for improving bone health: White pepper contains minerals, for example, manganese, copper, and magnesium, which are basic for sound bone advancement and quality, especially as individuals start to age, and their bones bit by bit debilitate.""",60.00,50.00),
            ("Sunflower Seeds 100g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/47.jpg","""Description
Sunflower seeds are harvested from the flower head of the sunflower plant. While the seed itself is encased in a black and white striped shell, sunflower seeds are white and have a tender texture. Known for their distinct nutty flavor and high nutritional value, you can eat the seeds raw, roasted, or incorporated into other dishes.

Health Benefits
Studies link the consumption of sunflower seeds to a number of health benefits, including lowering your risk of developing diseases like high blood pressure or heart disease. They also contain nutrients that can support your immune system and boost your energy levels.

Here are some of the health benefits of sunflower seeds:

Reducing Inflammation:

For those with short-term or chronic inflammation, sunflower seeds can offer anti-inflammatory benefits. Sunflower seeds contain vitamin E, flavonoids, and other plant compounds that can reduce inflammation. A study found that consuming sunflower seeds and other seeds five times or more each week resulted in lower levels of inflammation, which also lowered risk factors for several chronic diseases.

Improving Heart Health:

Sunflower seeds are rich in ‘healthy’ fats, including polyunsaturated fat and monounsaturated fat. A three-fourths cup serving of sunflower seeds contains 14 grams of fat. Studies found that consumption of seeds — including sunflower seeds — was linked to lower rates of cardiovascular disease, high cholesterol, and high blood pressure.

Supporting the Immune System:

Sunflower seeds are a source of many vitamins and minerals that can support your immune system and increase your ability to fight off viruses. These include both zinc and selenium. Zinc plays a vital role in the immune system, helping the body maintain and develop immune cells. Selenium also plays a role in reducing inflammation, fighting infection, and boosting immunity.

Boosting Energy Levels:

While the high levels of protein in sunflower seeds already help boost your energy levels, other nutrients like vitamin B and selenium can help keep you energized. The vitamin B1 (also known as thiamin) present in sunflower seeds can help you convert food to energy, which can keep you active throughout the day. Selenium can increase blood flow and deliver more oxygen to your body.""",60.00,50.00),
            ("Nelli Vathal/Dried Amla 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/48.jpg","""Description
Benefits of Dried Indian Gooseberry:
• People using dried Indian gooseberry in many hair oils because it enhances hair growth and pigmentation. Amla hair oil is very famous in India as it prevents hair loss and baldness. You can eat the fresh gooseberry or apply the paste to the root of the hairs that increase hair growth and color.
• By drinking gooseberry juice, you can improve your eyesight and eye problems such as nearsightedness, cataracts, etc. It contains Vitamin A and carotenes that reduce macular degeneration, night blindness and increase your vision.
• Calcium is an important component of your body, teeth, bones, nails, and also hair. The Amla contains Vitamin C that helps the body to absorb Calcium, and it is an effective way to keep your body and great.
• The amla is a combination of the minerals and vitamins that help to cure menstrual cramps.
• The protein content in nelli vathal plays a major role in metabolic activity. Protein is the main for the development of cells, muscles, and organs.
• Dried Indian gooseberry triggers the beta-pancreatic cells and enhances the secretion of Insulin, which in turn reduces the blood sugar level. Besides, this reduces the bad cholesterol level.
• Amla has diuretic properties that increase urination by eliminating excess toxins, water, salts from the body. It maintains a healthy kidney.
• Fibers present in amla helps in digestion by improving bowel movements. It treats constipation, loose stools, and reduces diarrhea.""",100.00,80.00),
            ("Jaadhikkaai/Jathikai Nutmeg 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/49.jpg","""Description
Benefits of Jathikai:
1. Jathikai for sleep:

Jathikai helps to induce sleep. People with sleep disorders prefer Jathikai to get a good night sleep. Nutmeg helps to treat various sleep disorders. It has natural sedative properties and helps you to get sleep naturally without sleeping pills and other chemicals.

Jathikai is a popular natural sleep aid. It provides relaxation and gives a sound sleep.

2. Jathikai for face, skin and hair:

Jathikai is good in treating pimples, blemishes, acne and acne scars. It has anti-inflammatory properties.

Just swipe the jathikai in a wet stone and apply the paste on the pimples. Repeat it daily till the pimple and scars goes off. Make sure that you clean and pat dry your face before applying.

Jathikka is also good for dry skin. You can massage the nutmeg oil before taking bath.

3. Jathikai for babies:

Jathikai is good for babies. But please limit the quantity you give to babies with just a swipe. It induces the sleep in babies. This is a very old home remedy. People give it as a part of Ura marundhu. People give vasambu, sukku, masikkai, kadukkai and few other ingredients also along with nutmeg.

4. Jathikai for Stomach problems:

Nutmeg is good to treat stomach problems like indigestion, diarrhea and flatulence. You can include nutmeg powder in your breakfast cereals or with warm milk.

5. Jathikai for dental problems:

Nutmeg has anti-bacterial properties. It is used in oral care and to treat problems like tooth pain, sore gums.""",100.00,80.00),
            ("Koraikkilangu/Goraikkilangu 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/50.jpg","""Description
Benefits of Koraikkilangu/Goraikkilangu:
• The paste of Goraikkilangu is used in treating skin related ailments like scabies and eczema and helps in relieving itching.
• The paste is used in increasing the size of the breasts. It also purifies the breast milk, improves eyesight and helps in eye related ailments.
• The extract from the roots is instilled into eyes in conjunctivitis, to reduce the pain, redness and ocular discharges.
• Goraikkilangu, when taken in powdered form, improves digestive system, removes worms from the gastro-intestinal tract, curbs infection and purifies blood.
• The powder is massaged to reduce the subcutaneous fat deposition in case of obese people.
• It normalizes the menstrual disturbances and breast discomfort and maintains normal body temperature.
• Goraikkilangu proves useful in diseases like psychosis and epilepsy and mental diseases.
• The herb helps, uterine contraction and provides strength to the body.
• It is used as a diuretic to treat ulcers.
• The herb proves to be a keen stimulant in appetite.
• Goraikkilangu is an effective remedy for distaste, vomiting, diarrhea, colitis and dyspepsia.
• It is considered the best herb for treating any type of fever.
• The root is often used for developing high memory.
• The herb harmonizes liver, spleen, and pancreas. It helps in curing thirst, bronchitis and poisonous affections.
• Used for Skin Acne, Dandruff, Skin Wounds, and Skin Ulcers.""",30.00,20.00),
            ("Lavanga Pattai/Indian Jujube/Cinnamon Bark 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/51.png","""Description
Benefits of Lavanga Pattai:
Lavangam bark is used to cure,
• Chronic cough
• Vomiting
• Indigestion""",80.00,60.00),
            ("Kunguliyam/Kungulingam 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/53.jpg","""Description
Kungiliam, a medicinal tree is a rare and precious specious found all over India. This species is commonly known as Sal tree or Shala. It’s scientific name is Shorea Robusta Gaertn.

Benefits:

Kungiliam is used in Ayurveda, Siddha and Unani because of its miraculous medicinal power.
It is good for curing chronic skin disorders, musculoskeletal disorder, tumors, diseases of oral cavity, rheumatism, fever, cough, asthma, epilepsy, ear and hair ailments etc.
It is also used to produced germ killers and perfumes.""",100.00,80.00),
            ("Velvet Bean/Poonaikaali Seeds 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/54.jpg","""Description
Health Benefits of Poonaikaali Seeds
Increases libido.

Increases sperm count in men and ovulation in women.

Acts as a restorative nutrient for the nervous system.

Increases blood circulation to the genitals.

Decreases symptoms of stress and anxiety.

Calms nerves.

Reduces inflammation.

Strengthens and tones the sexual glands.

Increases stamina.

Releases bound up testosterone, increasing the level of bio-available testosterone.

Reduces fat and improves muscle tone.(By supporting healthy testosterone levels, Poonaikali Seeds[Mucuna pruriens] supports anabolic metabolism increasing your sex and tendency to burn fat and to build muscle.)""",80.00,60.00),
            ("Yellow Mustard/Venkadugu 100g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/55.jpg","""Description
Benefits of Ven Kadugu (Yellow Mustards):
Rheumatic Arthritis:
Mustard seeds are a source of relief for people having rheumatic arthritis.

Migraine:
Migraine occurrence also reduces owing to the magnesium content present in the mustard seed

Respiration Congestion:
Mustard seeds or mustard in general is known to relieve any congestion problems in respiration

Dietary Fibre:
Mustard seeds are a good source of dietary fibres that improve digestion in the body. They make the bowel movements better, thus improving the overall metabolism of the body.

Blood Pressure and Menopausal Relief:
A number of nutrients present in mustard seeds like copper, iron, magnesium and selenium also assist in the treatment of blood pressure and menopause relief""",70.00,65.00),
            ("Shenbaga/Champak Mottu 50g", "C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/57.jpg","""Description
Benefits of Shenbaga Mottu:
Used to treat:

• Abscess
• Colic
• Indigestion
• Fever
• Nausea
• Gonorrhea
• Headache
• Gout
• Rheumatism""",140.00,100.00),
            ("Herbal Country Sugar Naattu Sarkarai 100g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/59.jpg","""Description
Benefits
1. Prevention Of Breathing Troubles
For those who have common respiratory tract problems, jaggery can be one of the maximum useful answers. You’ll save your allergies, bronchitis, and so forth.
By means of along with the same of their diet. It is better if one consumes jaggery at the side of sesame seeds. This mixture is ideal for treating respiration troubles.

2. Helps With Weight Reduction
Weight benefit is an issue most of the people should deal with. A depended on remedy to foster weight reduction is a mild consumption of jaggery.
It is a great supply of potassium that helps balance electrolytes, boosting metabolism as well as constructing muscle groups.
Furthermore, potassium also can assist lessen water retention in one’s body. As a result, playing a main function in weight loss.

3. Controls Blood Pressure
The presence of potassium and sodium in jaggery helps preserve acid degrees within the body. This, in turn, keeps normal blood pressure levels.

4. Blood Circulation
Unlike sugar that gives short-lived electricity raise, jaggery affords slow power that lasts for an extended time.
This is because it’s Unrefined, which guarantees that blood sugar ranges aren’t altered right away and rises slowly as a substitute.
This, in flip, can assist save your fatigue as properly.

5. Relieves Menstrual Pain
Jaggery is a natural treatment to ease pain going on rom menstrual cramps.
Individuals who enjoy temper swings or frustration before their periods must devour the identical in small amounts. It helps to launch endorphins that loosen up one’s body.

6. Prevents Anemia
To save your anemia, it is required that good enough stages of RBCs are maintained inside the frame at the side of iron and folate.
aggery is wealthy in each iron and folate, subsequently, a terrific manner to save anemia. Doctors often advise its intake to adolescents and pregnant women.

7. Purifies The Body
Human beings commonly consume jaggery after food due to the fact that it is one of the great herbal cleansing retailers for the body.
Eating this food can help take away all forms of undesirable particles from the body. Such as intestines, belly, meals pipe, lungs, and the respiration tract effectively.

8. Cleansing The Liver
Jaggery is a natural cleansing agent, specifically for the liver. The herbal sweetener helps flush out dangerous pollution from the body.
This further allows to detoxify the liver. Therefore, the ones stricken by illnesses related to the liver must begin eating jaggery.

9. Prevents Constipation
Consumption of the nutrient-packed sweetener facilitates to stimulate bowel actions and activation of digestive enzymes in one’s body.
After eaten a heavy meal, simply devour a number of this nutritious natural sweetener. It reduce the hazard of constipation.

10. Remedy Of Cold And Cough
Jaggery additionally enables cure flu-like signs consisting of cold and cough. It leads to the production of warmness in one’s body.
Result higher benefits, do mix jaggery in warm milk or use it as a sweetener to your tea.

11. Reduces Joint Ache
For people tormented by arthritis or any form of pain inside the joints, the consumption of jaggery can provide significant ache relief.
When eaten with ginger, the effectiveness most effective improves.

12. Purifies Blood
Intake of jaggery on a normal basis in slight amounts can useful resource in blood purification. That is also the motive why it’s powerful in treating zits or acne as cleanser blood also manner healthier skin. Moreover, the whole hemoglobin count in blood additionally will increase with the consumption of the right quantity of it.

13. Boosts Immunity
Antioxidants and minerals like selenium and zinc are found in considerable portions in jaggery.
his allows in stopping free radical damage along with constructing resistance in opposition to various infections. That is why it is eaten often in winters.

14. Treatments Urinary Tract Issues
Sugarcane is a herbal diuretic, so jaggery too possesses this property. Decreasing inflammation of the bladder, stimulating urination and improving the easy float of urine.
These some issues that regular intake of this nutritious meals object can easily assist with.

15. Maintains Intestinal Fitness
Jaggery is wealthy in magnesium. Each 10 g of the meals includes 16 mg of the mineral. So, if one consumes even 10 grams of it, they would’ve fulfilled 4% each day requirement of this mineral in our lives. Therefore, ingesting it on a every day basis can lead to properly intestinal fitness.""",100.00,80.00),
            ("Marikolunthu/Marjoram 25g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/60.jpg","""Description
Benefits:
Marikolunthu for Sleep:

Some people cannot sleep at night due to depression. This leads to an uneasy feeling throughout the day time. This herb helps inducing sleep in these people.

Marikolunthu for Stomach Pain and Skin:

Mix Marikolunthu(after crushing it well) in a glass of water, and drink it to relieve stomach pain. This also helps you to get rid of several Skin Allergies.""",50.00,40.00),
            ("Magilam Flower/Spanish Cherry 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/61.jpg","""Description
Benefits:

• Magilam Poo is good for Toothache issues.
• It keeps the teeth clean and gums stronger.
• It is good the keep the oral health intact.
• Magilam Poo is good in improving fertility in women
• Spanish Cherry is good to resolve weakness in eyesight and Diseases of Eyes
• Magilam poo is advised for chronic diarrhea and also good in recovering from weakness after diarrhea""",80.00,60.00),
            ("Parangi Chakkai/China root 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/62.png","""Description
Benefits of Parangi Chakkai:
It is used to treat rheumatoid arthritis, gout, enteritis, urinary tract infections, skin ulcers. 
Parangi Chakkai preparation heals skin diseases like psoriasis, eczema and reduces blood sugar level of diabetic patients.""",160.00,120.00),
            ("Bitter Snake Gourd/Peipudal/Peppudal 100g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/63.jpg","""Description
Benefits of Peipudal:
Used to treat:

Anorexia
Asthma
Boils
Bronchitis
Colic
Cough
Dipsia
Hyperacidity
Inflammation
Intermittent Fever
Jaundice
Leucoderma
Ulcer
Wounds""",120.00,90.00),
            ("Beleric/Thandrikaai 100g ","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/64.jpg","""Description
Benefits of Thandrikkai:
• It is an excellent remedy for the catarrhal condition, congestion, cough, bronchitis, asthma, and sore throats.
• The laxative action of fresh fruits is more compared to dried fruits.
• The dried fruits are useful in treating piles, diarrhoea, dysentery, parasitic worms, as these are binding and astringent.
• Thandrikkai fruits have liver protecting action and useful in jaundice and gall bladder stones""",60.00,50.00),
            ("Seemakilangu 50g","C:/Users/shiv shanker/OneDrive/Desktop/all image paths/all raw herbal/65.png","""Description
This wonder herb’s powder takes out the extra waste water(தேவையற்ற நீர்) from your joints!

Steps to apply externally:
Step – 1: Squeeze the juice of a Lemon in this Seemakilangu Powder and make it as a paste.
Step – 2: Then apply it on the painful and affected joint part at night.
It then gets dried by morning which you have to wash and remove with warm water.""",180.00,160.00),
            
            
        ],
}
class CategoryScreen(MDScreen):
    current_category = StringProperty()
    category_buttons = ListProperty()
    product_grid = ObjectProperty()
    sidebar_layout = ObjectProperty()

    def on_kv_post(self, base_widget):
        self.sidebar_layout = self.ids.sidebar_layout
        self.product_grid = self.ids.product_grid
        self.load_categories()
        # Select the first category by default
        if categories:
            first_category = next(iter(categories))
            self.select_category(first_category)

    def load_categories(self):
        self.sidebar_layout.clear_widgets()
        self.category_buttons = []
        for cat in categories:
            is_selected = cat == self.current_category
            btn = Button(
                text=cat,
                size_hint_y=None,
                height=dp(38),
                background_normal='',
                background_color=(0.2, 0.8, 0.2, 1) if is_selected else (1, 1, 1, 1),
                color=(1, 1, 1, 1) if is_selected else (0, 0, 0, 1),
                bold=True if is_selected else False
            )
            btn.bind(on_release=self.on_category_select)
            self.category_buttons.append(btn)
            self.sidebar_layout.add_widget(btn)

    def on_category_select(self, button):
        self.select_category(button.text)

    def select_category(self, cat_name):
        self.current_category = cat_name
        # Update button highlights
        for btn in self.category_buttons:
            is_selected = btn.text == cat_name
            btn.background_color = (0.2, 0.8, 0.2, 1) if is_selected else (1, 1, 1, 1)
            btn.color = (1, 1, 1, 1) if is_selected else (0, 0, 0, 1)
            btn.bold = True if is_selected else False
        self.show_products(cat_name)

    def show_products(self, cat_name):
        self.product_grid.clear_widgets()
        app = App.get_running_app()
        # Get the shared product list from the product_list screen instance
        product_list_screen = app.sm.get_screen('product_list')
        shared_products = product_list_screen.products
        # Build a lookup by name for fast access
        product_lookup = {p['name']: p for p in shared_products}
        for product in categories.get(cat_name, []):
            # product[0] is name
            name = product[0]
            product_info = product_lookup.get(name, {})
            img = product_info.get('image', product[1] if len(product) > 1 else "")
            price = product_info.get('price', product[2] if len(product) > 2 else "")
            description = product_info.get('description', "No description available.")
            images = product_info.get('images', [img])
            # Check if product is in wishlist by name
            is_favorite = False
            if hasattr(app, 'wishlist'):
                is_favorite = any(item.get('name') == name for item in app.wishlist)
            product_dict = {
                'name': name,
                'price': price,
                'image': img,
                'category': cat_name,
                'images': images,
                'description': description
            }
            card = Builder.load_string(f'''
CategoryProductCard:
    image: "{img}"
    name: "{name}"
''')
            card.bind(on_release=lambda instance, prod=product_dict: self.open_product_details(prod))
            self.product_grid.add_widget(card)

    def parse_price(self, price_str):
        if isinstance(price_str, str):
            cleaned = price_str.replace('₹','').replace(',','').replace('.00','').strip()
            try:
                return float(cleaned)
            except Exception:
                return 0
        return 0

    def open_product_details(self, product):
        app = App.get_running_app()
        app.last_screen = self.manager.current
        details_screen = app.sm.get_screen('product_details')
        details_screen.set_product(
            name=product['name'],
            price=self.parse_price(product.get('price', '')),
            images=product.get('images', [product.get('image', '')]),
            description=product.get('description', 'No description available.'),
            category=product.get('category', '')
        )
        app.sm.current = 'product_details'

    def toggle_wishlist(self, product_name, card, is_favorite):
        app = App.get_running_app()
        # Find the product in the current category
        for product in categories.get(self.current_category, []):
            if product[0] == product_name:
                name, img = product[:2]
                price = product[2] if len(product) > 2 else ""
                break
        else:
            return
        if not hasattr(app, 'wishlist'):
            app.wishlist = []
        if is_favorite:
            # Add to wishlist if not already present
            if not any(item.get('name') == name for item in app.wishlist):
                app.wishlist.append({'name': name, 'image': img, 'price': price, 'category': self.current_category})
        else:
            # Remove from wishlist
            app.wishlist = [item for item in app.wishlist if item.get('name') != name]
        # Optionally, refresh the grid to update favorite icons
        self.show_products(self.current_category)

    def switch_tab(self, tab_name):
        app = App.get_running_app()
        if tab_name == "home":
            app.sm.current = "home"
        elif tab_name == "list":
            app.sm.current = "category"
        elif tab_name == "profile":
            if App.get_running_app().user_logged_in:
                app.sm.current = "profile"
            else:
                app.sm.current = "account_prompt"
