# Health Assistant Chatbot - Disease Information Database

DISEASE_DATABASE = {
    'cancer': {
        'explanation': 'Cancer is a group of diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body. It occurs when genetic changes interfere with normal cell division and growth.',
        'solutions': [
            'Consult an oncologist for proper diagnosis and treatment',
            'Follow recommended treatment plan (surgery, chemotherapy, radiation, or immunotherapy)',
            'Regular medical checkups and screenings',
            'Join support groups for emotional support',
            'Maintain a positive mindset and follow medical advice'
        ],
        'foods': [
            'Cruciferous vegetables (broccoli, cauliflower, cabbage)',
            'Berries rich in antioxidants (blueberries, strawberries)',
            'Green leafy vegetables (spinach, kale)',
            'Fatty fish (salmon, mackerel) rich in omega-3',
            'Nuts and seeds',
            'Turmeric and green tea',
            'Whole grains and legumes'
        ],
        'exercises': [
            'Light to moderate walking (30 minutes daily)',
            'Yoga and stretching exercises',
            'Swimming or water aerobics',
            'Breathing exercises and meditation',
            'Strength training with light weights (as approved by doctor)',
            'Tai chi for balance and relaxation'
        ]
    },
    'diabetes': {
        'explanation': 'Diabetes is a chronic condition that affects how your body processes blood sugar (glucose). Type 1 diabetes is when the body doesn\'t produce insulin, while Type 2 is when the body doesn\'t use insulin properly.',
        'solutions': [
            'Monitor blood sugar levels regularly',
            'Take prescribed medications or insulin as directed',
            'Maintain a healthy weight',
            'Follow a balanced diet with controlled carbohydrate intake',
            'Regular exercise routine',
            'Manage stress levels',
            'Regular checkups with endocrinologist'
        ],
        'foods': [
            'Non-starchy vegetables (broccoli, carrots, peppers)',
            'Whole grains (brown rice, quinoa, oats)',
            'Lean proteins (chicken, fish, tofu)',
            'Legumes (beans, lentils, chickpeas)',
            'Nuts and seeds in moderation',
            'Greek yogurt (unsweetened)',
            'Berries and citrus fruits',
            'Avoid: sugary drinks, white bread, processed foods'
        ],
        'exercises': [
            'Brisk walking (150 minutes per week)',
            'Cycling or stationary bike',
            'Swimming',
            'Strength training 2-3 times per week',
            'Yoga for stress management',
            'Dancing or aerobic classes',
            'Gardening or active household chores'
        ]
    },
    'fever': {
        'explanation': 'Fever is a temporary increase in body temperature, often due to an illness. It\'s a sign that your body is fighting an infection. Normal body temperature is around 98.6°F (37°C).',
        'solutions': [
            'Rest and get plenty of sleep',
            'Stay hydrated with water and fluids',
            'Take over-the-counter fever reducers (acetaminophen, ibuprofen)',
            'Use cool compresses on forehead',
            'Wear light, breathable clothing',
            'Keep room temperature comfortable',
            'Consult doctor if fever persists beyond 3 days or reaches 103°F (39.4°C)'
        ],
        'foods': [
            'Clear broths and soups',
            'Coconut water for electrolytes',
            'Fresh fruits (watermelon, oranges)',
            'Herbal teas (ginger, chamomile)',
            'Bananas and rice (easy to digest)',
            'Yogurt with probiotics',
            'Honey and lemon water',
            'Avoid: spicy foods, caffeine, alcohol'
        ],
        'exercises': [
            'Complete rest is recommended during fever',
            'Avoid strenuous activities',
            'Light stretching only after fever subsides',
            'Gradual return to normal activity after recovery',
            'Walking slowly once temperature normalizes'
        ]
    },
    'headache': {
        'explanation': 'Headaches are pain or discomfort in the head or face area. Common types include tension headaches, migraines, and cluster headaches. They can be caused by stress, dehydration, eye strain, or underlying conditions.',
        'solutions': [
            'Rest in a quiet, dark room',
            'Apply cold or warm compress to head or neck',
            'Take over-the-counter pain relievers',
            'Practice relaxation techniques',
            'Maintain good posture',
            'Stay hydrated',
            'Identify and avoid triggers',
            'See a doctor for frequent or severe headaches'
        ],
        'foods': [
            'Water (drink plenty to stay hydrated)',
            'Magnesium-rich foods (almonds, spinach, avocado)',
            'Foods with riboflavin (eggs, dairy, leafy greens)',
            'Ginger tea',
            'Peppermint tea',
            'Fatty fish (salmon, tuna)',
            'Bananas',
            'Avoid: aged cheese, processed meats, alcohol, caffeine (if sensitive)'
        ],
        'exercises': [
            'Neck stretching exercises',
            'Shoulder rolls and relaxation',
            'Gentle yoga poses',
            'Deep breathing exercises',
            'Progressive muscle relaxation',
            'Short walks in fresh air',
            'Eye exercises to reduce strain',
            'Avoid intense workouts during headache'
        ]
    },
    'hypertension': {
        'explanation': 'Hypertension (high blood pressure) is a condition where the force of blood against artery walls is consistently too high. It can lead to serious health problems like heart disease and stroke if left untreated.',
        'solutions': [
            'Take prescribed blood pressure medications',
            'Monitor blood pressure regularly at home',
            'Reduce sodium intake',
            'Maintain healthy weight',
            'Limit alcohol consumption',
            'Quit smoking',
            'Manage stress through relaxation techniques',
            'Regular checkups with healthcare provider'
        ],
        'foods': [
            'Leafy greens (spinach, kale, collard greens)',
            'Berries (especially blueberries)',
            'Beets and beet juice',
            'Fatty fish (salmon, mackerel)',
            'Oats and whole grains',
            'Bananas and potatoes (potassium-rich)',
            'Garlic and herbs for flavoring instead of salt',
            'Low-fat dairy products',
            'Avoid: salty foods, processed meats, fast food'
        ],
        'exercises': [
            'Aerobic exercise (walking, jogging, cycling) 30 minutes daily',
            'Swimming or water aerobics',
            'Dancing',
            'Strength training 2 days per week',
            'Yoga and meditation',
            'Tai chi',
            'Hiking',
            'Avoid: heavy weightlifting and isometric exercises'
        ]
    },
    'asthma': {
        'explanation': 'Asthma is a chronic respiratory condition where airways become inflamed and narrowed, making breathing difficult. It can be triggered by allergens, exercise, cold air, or stress.',
        'solutions': [
            'Use prescribed inhalers (rescue and maintenance)',
            'Identify and avoid triggers',
            'Keep a peak flow meter to monitor lung function',
            'Have an asthma action plan',
            'Avoid smoke and air pollution',
            'Keep home clean and dust-free',
            'Get vaccinated (flu, pneumonia)',
            'Regular follow-ups with pulmonologist'
        ],
        'foods': [
            'Fruits and vegetables rich in vitamins C and E',
            'Omega-3 fatty acids (salmon, flaxseeds)',
            'Magnesium-rich foods (spinach, pumpkin seeds)',
            'Apples and tomatoes',
            'Foods with beta-carotene (carrots, sweet potatoes)',
            'Turmeric and ginger',
            'Avoid: sulfites (dried fruits, wine), processed foods, dairy if sensitive'
        ],
        'exercises': [
            'Swimming (humid environment is beneficial)',
            'Walking at a comfortable pace',
            'Yoga with breathing exercises',
            'Cycling on flat terrain',
            'Warm-up before exercise (very important)',
            'Cool-down after exercise',
            'Always carry rescue inhaler during exercise',
            'Avoid: exercising in cold, dry air; high-intensity interval training without proper preparation'
        ]
    },
    'arthritis': {
        'explanation': 'Arthritis is inflammation of one or more joints, causing pain, stiffness, and swelling. The most common types are osteoarthritis (wear-and-tear) and rheumatoid arthritis (autoimmune condition).',
        'solutions': [
            'Take prescribed anti-inflammatory medications',
            'Physical therapy exercises',
            'Maintain healthy weight to reduce joint stress',
            'Use hot and cold therapy',
            'Consider joint protection techniques',
            'Use assistive devices if needed',
            'Get adequate rest',
            'Regular consultations with rheumatologist'
        ],
        'foods': [
            'Fatty fish (salmon, sardines, mackerel)',
            'Berries and cherries',
            'Broccoli and other cruciferous vegetables',
            'Green tea',
            'Olive oil',
            'Nuts (walnuts, almonds)',
            'Garlic and ginger',
            'Whole grains',
            'Avoid: processed foods, red meat, sugar, fried foods'
        ],
        'exercises': [
            'Low-impact aerobics',
            'Swimming and water exercises',
            'Cycling or stationary bike',
            'Tai chi',
            'Gentle stretching exercises',
            'Range-of-motion exercises',
            'Strength training with light weights',
            'Walking on even surfaces',
            'Avoid: high-impact activities like running or jumping'
        ]
    },
    'cold': {
        'explanation': 'The common cold is a viral infection of the upper respiratory tract. It\'s characterized by runny nose, sore throat, cough, and congestion. Most colds resolve on their own within 7-10 days.',
        'solutions': [
            'Get plenty of rest',
            'Stay hydrated with fluids',
            'Use saline nasal drops or spray',
            'Gargle with salt water for sore throat',
            'Take over-the-counter cold medications if needed',
            'Use a humidifier',
            'Wash hands frequently to prevent spread',
            'See doctor if symptoms worsen or persist beyond 10 days'
        ],
        'foods': [
            'Chicken soup (helps with hydration and inflammation)',
            'Honey (soothes throat)',
            'Garlic (immune-boosting properties)',
            'Ginger tea',
            'Citrus fruits (vitamin C)',
            'Hot herbal teas',
            'Yogurt with probiotics',
            'Spicy foods (can clear sinuses)',
            'Plenty of water and warm liquids'
        ],
        'exercises': [
            'Rest is most important',
            'Avoid strenuous exercise during acute phase',
            'Light walking once symptoms improve',
            'Gentle stretching',
            'Deep breathing exercises',
            'Wait until fever is gone before resuming normal exercise',
            'Gradually return to regular routine after recovery'
        ]
    },
    'aids': {
        'explanation': 'AIDS (Acquired Immunodeficiency Syndrome) is the most advanced stage of HIV (Human Immunodeficiency Virus) infection. HIV attacks the immune system, specifically CD4 cells (T cells), weakening the body\'s ability to fight infections and diseases. With proper antiretroviral therapy (ART), many people with HIV never develop AIDS.',
        'solutions': [
            'Start antiretroviral therapy (ART) immediately as prescribed',
            'Take medications consistently at the same time daily',
            'Regular monitoring of CD4 count and viral load',
            'Prevent opportunistic infections with prophylactic medications',
            'Get vaccinated against preventable diseases',
            'Practice safe behaviors to prevent transmission',
            'Regular medical checkups with HIV specialist',
            'Join support groups and counseling services',
            'Mental health support and stress management',
            'Disclose status to sexual partners and healthcare providers'
        ],
        'foods': [
            'High-protein foods (lean meats, eggs, beans, tofu)',
            'Whole grains (brown rice, quinoa, whole wheat)',
            'Fresh fruits and vegetables (rich in vitamins)',
            'Healthy fats (avocados, nuts, olive oil)',
            'Probiotic-rich foods (yogurt, kefir)',
            'Foods high in iron (spinach, red meat, lentils)',
            'Foods rich in zinc (pumpkin seeds, chickpeas)',
            'Foods with vitamin B12 (fish, fortified cereals)',
            'Stay well-hydrated with clean water',
            'Avoid: raw or undercooked foods, unpasteurized dairy, unwashed produce'
        ],
        'exercises': [
            'Moderate aerobic exercise (walking, swimming) 30 minutes, 3-5 times/week',
            'Strength training 2-3 times per week',
            'Yoga for flexibility and stress reduction',
            'Tai chi for balance and mental wellness',
            'Stretching exercises daily',
            'Light cycling or stationary bike',
            'Listen to your body and rest when needed',
            'Avoid overexertion if CD4 count is low',
            'Consult doctor before starting new exercise program',
            'Stay hydrated during exercise'
        ]
    },
    'hiv': {
        'explanation': 'HIV (Human Immunodeficiency Virus) is a virus that attacks the body\'s immune system. If untreated, it can lead to AIDS. HIV is transmitted through contact with infected blood, sexual fluids, or from mother to child. Modern antiretroviral therapy allows people with HIV to live long, healthy lives.',
        'solutions': [
            'Start antiretroviral therapy (ART) as soon as diagnosed',
            'Maintain undetectable viral load (U=U: Undetectable = Untransmittable)',
            'Take medications daily without missing doses',
            'Regular blood tests to monitor CD4 count and viral load',
            'Practice safe sex using condoms',
            'Don\'t share needles or personal items',
            'Regular screening for other STIs',
            'Inform sexual and needle-sharing partners',
            'Work closely with HIV specialist',
            'Consider PrEP for HIV-negative partners'
        ],
        'foods': [
            'Lean proteins (chicken, fish, legumes)',
            'Colorful fruits and vegetables',
            'Whole grains and complex carbohydrates',
            'Healthy fats (nuts, seeds, avocado)',
            'Foods rich in omega-3 (salmon, walnuts)',
            'Calcium-rich foods (dairy, fortified alternatives)',
            'Foods high in vitamin D (eggs, fortified milk)',
            'Selenium-rich foods (Brazil nuts, tuna)',
            'Plenty of water throughout the day',
            'Avoid: alcohol in excess, raw meats, unpasteurized products'
        ],
        'exercises': [
            'Regular cardio exercise (walking, jogging, cycling)',
            'Resistance training to maintain muscle mass',
            'Flexibility exercises (yoga, stretching)',
            'Low-impact activities if experiencing fatigue',
            'Swimming or water aerobics',
            'Dancing for cardio and enjoyment',
            'Breathing exercises and meditation',
            'Gradual increase in intensity as tolerated',
            'Rest adequately between workouts',
            'Consult healthcare provider about exercise plan'
        ]
    },
    'tuberculosis': {
        'explanation': 'Tuberculosis (TB) is a bacterial infection caused by Mycobacterium tuberculosis that primarily affects the lungs but can affect other organs. It spreads through airborne droplets when infected people cough or sneeze. TB is curable with proper antibiotic treatment.',
        'solutions': [
            'Complete full course of antibiotics (6-9 months typically)',
            'Take medications exactly as prescribed without missing doses',
            'Directly Observed Therapy (DOT) recommended',
            'Isolate during active infection period',
            'Cover mouth when coughing or sneezing',
            'Regular chest X-rays to monitor progress',
            'Get tested if exposed to TB',
            'BCG vaccination for prevention in high-risk areas',
            'Inform close contacts for testing'
        ],
        'foods': [
            'High-calorie, protein-rich diet',
            'Eggs, lean meats, fish, poultry',
            'Whole grains (brown rice, oats, whole wheat)',
            'Fresh fruits (oranges, bananas, apples)',
            'Green leafy vegetables (spinach, kale)',
            'Nuts and seeds',
            'Milk and dairy products',
            'Foods rich in vitamins A, C, E',
            'Avoid: alcohol, tobacco, processed foods'
        ],
        'exercises': [
            'Rest during active phase of disease',
            'Breathing exercises to strengthen lungs',
            'Light walking after symptoms improve',
            'Gradual return to activity as tolerated',
            'Yoga for lung capacity',
            'Avoid strenuous exercise during treatment',
            'Focus on recovery first'
        ]
    },
    'malaria': {
        'explanation': 'Malaria is a life-threatening disease caused by Plasmodium parasites transmitted through bites of infected Anopheles mosquitoes. Symptoms include high fever, chills, sweating, headache, and fatigue. It\'s preventable and curable with proper treatment.',
        'solutions': [
            'Take antimalarial medications as prescribed',
            'Complete full course of treatment',
            'Use mosquito nets (insecticide-treated)',
            'Apply mosquito repellent on exposed skin',
            'Wear long-sleeved clothing in endemic areas',
            'Use indoor insecticide sprays',
            'Eliminate standing water around home',
            'Seek immediate medical care for fever in endemic areas',
            'Take preventive antimalarials when traveling to malaria zones'
        ],
        'foods': [
            'High-protein foods (chicken, fish, eggs)',
            'Iron-rich foods (red meat, spinach, lentils)',
            'Fruits rich in vitamin C (oranges, guava)',
            'Easily digestible foods during illness',
            'Plenty of fluids (water, coconut water, soups)',
            'Bananas for energy',
            'Yogurt with probiotics',
            'Avoid: spicy and oily foods during acute phase'
        ],
        'exercises': [
            'Complete rest during acute phase',
            'No exercise during fever',
            'Light walking after recovery begins',
            'Gradual increase in activity',
            'Wait 2-3 weeks post-recovery for normal exercise',
            'Stay hydrated if exercising'
        ]
    },
    'obesity': {
        'explanation': 'Obesity is a medical condition characterized by excessive body fat accumulation that presents health risks. It\'s defined as having a BMI of 30 or higher. Obesity increases risk of diabetes, heart disease, stroke, and certain cancers.',
        'solutions': [
            'Create sustainable calorie deficit through diet and exercise',
            'Set realistic weight loss goals (1-2 lbs per week)',
            'Work with nutritionist for meal planning',
            'Track food intake and physical activity',
            'Behavioral therapy to address eating patterns',
            'Consider medical interventions if BMI > 40',
            'Get adequate sleep (7-9 hours)',
            'Manage stress through healthy coping mechanisms',
            'Join support groups',
            'Regular medical monitoring'
        ],
        'foods': [
            'Vegetables (non-starchy): broccoli, spinach, peppers',
            'Lean proteins (chicken breast, fish, tofu)',
            'Whole grains in moderation (quinoa, brown rice)',
            'Fruits (berries, apples, citrus)',
            'Legumes (beans, lentils)',
            'Greek yogurt (low-fat)',
            'Nuts in small portions',
            'Drink plenty of water',
            'Avoid: sugary drinks, fried foods, processed snacks, fast food'
        ],
        'exercises': [
            'Walking 30-60 minutes daily',
            'Swimming or water aerobics (low-impact)',
            'Cycling or stationary bike',
            'Strength training 2-3 times per week',
            'Gradual increase in intensity',
            'Find activities you enjoy',
            'Start slow and build consistency',
            'Consider personal trainer initially'
        ]
    },
    'alzheimer': {
        'explanation': 'Alzheimer\'s disease is a progressive neurological disorder that causes brain cells to degenerate and die, leading to memory loss, cognitive decline, and behavioral changes. It\'s the most common cause of dementia, typically affecting people over 65.',
        'solutions': [
            'Medications to manage symptoms (cholinesterase inhibitors)',
            'Establish daily routines and structure',
            'Keep environment safe and familiar',
            'Use memory aids (calendars, labels, reminders)',
            'Cognitive stimulation activities',
            'Social engagement and interaction',
            'Caregiver support and respite care',
            'Legal and financial planning early',
            'Regular medical monitoring',
            'Join Alzheimer\'s support groups'
        ],
        'foods': [
            'Mediterranean diet recommended',
            'Fatty fish (salmon, sardines, mackerel)',
            'Berries (blueberries, strawberries)',
            'Leafy greens (kale, spinach, collards)',
            'Nuts (walnuts, almonds)',
            'Olive oil',
            'Whole grains',
            'Foods rich in antioxidants',
            'Avoid: processed foods, excess sugar, saturated fats'
        ],
        'exercises': [
            'Regular aerobic exercise (walking, swimming)',
            'Balance and coordination activities',
            'Tai chi or gentle yoga',
            'Dancing (social and physical benefits)',
            'Gardening',
            'Brain exercises (puzzles, memory games)',
            'Social activities combined with physical movement',
            '150 minutes moderate exercise per week recommended'
        ]
    },
    'parkinson': {
        'explanation': 'Parkinson\'s disease is a progressive nervous system disorder affecting movement. It causes tremors, stiffness, and difficulty with balance and coordination. Symptoms start gradually and worsen over time due to decreased dopamine production in the brain.',
        'solutions': [
            'Medications to manage symptoms (Levodopa, dopamine agonists)',
            'Physical therapy for mobility',
            'Occupational therapy for daily activities',
            'Speech therapy if needed',
            'Deep brain stimulation in advanced cases',
            'Regular exercise program',
            'Fall prevention strategies',
            'Assistive devices when needed',
            'Support groups',
            'Regular neurologist visits'
        ],
        'foods': [
            'High-fiber foods (whole grains, vegetables)',
            'Adequate protein (distribute throughout day)',
            'Fruits and vegetables',
            'Foods rich in antioxidants',
            'Omega-3 fatty acids (fish, flaxseeds)',
            'Plenty of water for hydration',
            'Foods with vitamin D and calcium',
            'Take Levodopa 30 mins before protein meals',
            'Avoid: alcohol, processed foods'
        ],
        'exercises': [
            'Walking daily',
            'Tai chi for balance',
            'Swimming or water therapy',
            'Cycling or stationary bike',
            'Strength training',
            'Stretching exercises',
            'Dance therapy',
            'Boxing for Parkinson\'s programs',
            'Focus on large, exaggerated movements',
            'Regular exercise improves symptoms'
        ]
    },
    'stroke': {
        'explanation': 'A stroke occurs when blood supply to part of the brain is interrupted or reduced, preventing brain tissue from getting oxygen and nutrients. Brain cells begin to die within minutes. It\'s a medical emergency requiring immediate treatment.',
        'solutions': [
            'Call emergency services immediately (time = brain)',
            'Remember FAST: Face drooping, Arm weakness, Speech difficulty, Time to call 911',
            'Clot-busting drugs if ischemic stroke (within 3-4.5 hours)',
            'Surgery or procedures for certain types',
            'Rehabilitation: physical, occupational, speech therapy',
            'Blood pressure management',
            'Anticoagulant or antiplatelet medications',
            'Lifestyle modifications',
            'Regular medical follow-ups',
            'Prevent second stroke'
        ],
        'foods': [
            'Fruits and vegetables (5+ servings daily)',
            'Whole grains',
            'Lean proteins (fish, poultry, legumes)',
            'Low-fat dairy',
            'Foods rich in potassium (bananas, sweet potatoes)',
            'Omega-3 fatty acids (salmon, walnuts)',
            'Reduce sodium intake',
            'Limit saturated and trans fats',
            'Avoid: processed foods, excessive salt, red meat'
        ],
        'exercises': [
            'Rehabilitation exercises as prescribed',
            'Walking with assistance if needed',
            'Range-of-motion exercises',
            'Strength training for affected limbs',
            'Balance exercises',
            'Aerobic exercise as tolerated',
            'Swimming or water therapy',
            'Gradual progression under supervision',
            'Consistency is key for recovery'
        ]
    },
    'copd': {
        'explanation': 'COPD (Chronic Obstructive Pulmonary Disease) is a chronic inflammatory lung disease causing obstructed airflow from the lungs. It includes emphysema and chronic bronchitis. Main cause is long-term smoking. Symptoms include breathing difficulty, cough, mucus production.',
        'solutions': [
            'Quit smoking immediately (most important)',
            'Bronchodilator inhalers for symptom relief',
            'Inhaled corticosteroids',
            'Pulmonary rehabilitation program',
            'Oxygen therapy if needed',
            'Avoid air pollutants and irritants',
            'Get flu and pneumonia vaccines',
            'Breathing techniques and exercises',
            'Regular pulmonologist visits',
            'Have action plan for exacerbations'
        ],
        'foods': [
            'High-protein foods (fish, poultry, eggs)',
            'Complex carbohydrates (whole grains)',
            'Healthy fats (avocado, olive oil, nuts)',
            'Fresh fruits and vegetables',
            'Foods rich in antioxidants',
            'Smaller, frequent meals (easier on breathing)',
            'Stay hydrated with water',
            'Avoid: gas-producing foods, fried foods, excessive salt',
            'Limit simple carbs'
        ],
        'exercises': [
            'Pulmonary rehabilitation exercises',
            'Walking (most beneficial)',
            'Pursed-lip breathing technique',
            'Diaphragmatic breathing',
            'Light strength training',
            'Stretching exercises',
            'Stationary cycling',
            'Start slow and gradually increase',
            'Use supplemental oxygen if prescribed during exercise',
            'Stop if short of breath and rest'
        ]
    },
    'kidney stones': {
        'explanation': 'Kidney stones are hard deposits of minerals and salts that form inside the kidneys. They can affect any part of the urinary tract. Stones form when urine becomes concentrated, allowing minerals to crystallize and stick together. Very painful when passing.',
        'solutions': [
            'Drink plenty of water (2-3 liters daily)',
            'Pain medications for discomfort',
            'Alpha blockers to help pass stones',
            'Small stones usually pass on their own',
            'Lithotripsy (sound waves) to break up stones',
            'Surgery for large stones',
            'Strain urine to catch stone for analysis',
            'Identify stone type to prevent recurrence',
            'Medical evaluation if recurrent'
        ],
        'foods': [
            'Drink plenty of water (most important)',
            'Lemon juice or lemonade (citric acid helps)',
            'Calcium-rich foods (contrary to myth, helps prevent stones)',
            'Fruits and vegetables',
            'Moderate protein intake',
            'Avoid: excessive salt, animal protein, oxalate-rich foods (spinach, rhubarb, nuts) if prone to calcium oxalate stones',
            'Limit vitamin C supplements',
            'Reduce sugar intake'
        ],
        'exercises': [
            'Regular physical activity helps prevent stones',
            'Walking 30 minutes daily',
            'Moderate exercise routine',
            'Stay active to prevent obesity (risk factor)',
            'Avoid dehydration during exercise',
            'Drink extra water when exercising'
        ]
    },
    'osteoporosis': {
        'explanation': 'Osteoporosis is a bone disease where bones become weak and brittle, making them fragile and more likely to break. It occurs when the body loses too much bone, makes too little bone, or both. Most common in postmenopausal women.',
        'solutions': [
            'Calcium and vitamin D supplementation',
            'Bisphosphonate medications to strengthen bones',
            'Weight-bearing exercises regularly',
            'Fall prevention measures at home',
            'Stop smoking and limit alcohol',
            'Bone density tests (DEXA scan) for monitoring',
            'Hormone therapy in some cases',
            'Adequate protein intake',
            'Regular medical checkups'
        ],
        'foods': [
            'Dairy products (milk, yogurt, cheese)',
            'Calcium-fortified foods (orange juice, cereals)',
            'Leafy greens (kale, collard greens, bok choy)',
            'Fatty fish (salmon, sardines with bones)',
            'Eggs (vitamin D)',
            'Almonds and seeds',
            'Beans and legumes',
            'Foods rich in vitamin K',
            'Avoid: excessive caffeine, alcohol, high sodium'
        ],
        'exercises': [
            'Weight-bearing exercises (walking, jogging, dancing)',
            'Resistance training with weights',
            'Balance exercises (tai chi, yoga)',
            'Strength training 2-3 times per week',
            'Flexibility exercises',
            'Avoid: high-impact activities if severe osteoporosis',
            'Exercise improves bone density'
        ]
    },
    'depression': {
        'explanation': 'Depression is a common and serious mental health disorder characterized by persistent sadness, loss of interest in activities, and various physical and emotional problems. It affects how you feel, think, and handle daily activities.',
        'solutions': [
            'Psychotherapy (cognitive behavioral therapy, talk therapy)',
            'Antidepressant medications if recommended',
            'Combination of therapy and medication often most effective',
            'Regular exercise routine',
            'Maintain social connections',
            'Set realistic goals and priorities',
            'Avoid alcohol and drugs',
            'Establish regular sleep schedule',
            'Join support groups',
            'Seek help immediately if suicidal thoughts occur'
        ],
        'foods': [
            'Omega-3 rich foods (fatty fish, walnuts, flaxseeds)',
            'Foods with vitamin D (eggs, fortified milk, salmon)',
            'Complex carbohydrates (whole grains, oats)',
            'Protein-rich foods (lean meats, legumes)',
            'Foods with folate (leafy greens, beans)',
            'Foods with magnesium (nuts, seeds, dark chocolate)',
            'Probiotic foods (yogurt, kefir)',
            'Avoid: excessive sugar, processed foods, alcohol'
        ],
        'exercises': [
            'Aerobic exercise (walking, jogging, swimming)',
            'Aim for 30 minutes most days',
            'Yoga for mind-body connection',
            'Group fitness classes for social interaction',
            'Dancing',
            'Outdoor activities in nature',
            'Consistency more important than intensity',
            'Exercise releases endorphins (natural mood lifters)'
        ]
    },
    'anxiety': {
        'explanation': 'Anxiety disorders involve more than temporary worry or fear. They include excessive anxiety that doesn\'t go away and can worsen over time. Symptoms interfere with daily activities such as work, school, and relationships.',
        'solutions': [
            'Cognitive behavioral therapy (CBT)',
            'Medications (SSRIs, benzodiazepines) if needed',
            'Stress management techniques',
            'Deep breathing exercises',
            'Meditation and mindfulness',
            'Progressive muscle relaxation',
            'Limit caffeine and alcohol',
            'Adequate sleep',
            'Regular exercise',
            'Support groups'
        ],
        'foods': [
            'Complex carbohydrates (whole grains, quinoa)',
            'Foods rich in omega-3 (salmon, chia seeds)',
            'Probiotic foods (yogurt, kefir, fermented foods)',
            'Magnesium-rich foods (leafy greens, nuts, legumes)',
            'Foods with tryptophan (turkey, eggs, cheese)',
            'Antioxidant-rich foods (berries, dark chocolate)',
            'Herbal teas (chamomile, green tea)',
            'Avoid: caffeine, alcohol, processed foods, sugar'
        ],
        'exercises': [
            'Aerobic exercise (reduces anxiety)',
            'Walking or jogging',
            'Yoga (combines physical and mental benefits)',
            'Swimming',
            'Tai chi',
            'Cycling',
            'Any regular physical activity helps',
            'Breathing exercises',
            '21 minutes of exercise can reduce anxiety'
        ]
    },
    'thyroid': {
        'explanation': 'Thyroid disorders include hypothyroidism (underactive thyroid) causing fatigue, weight gain, and depression; and hyperthyroidism (overactive thyroid) causing weight loss, rapid heartbeat, and anxiety. The thyroid gland regulates metabolism.',
        'solutions': [
            'Hypothyroidism: thyroid hormone replacement (levothyroxine)',
            'Hyperthyroidism: anti-thyroid medications, radioactive iodine, or surgery',
            'Regular blood tests to monitor thyroid levels',
            'Take medications consistently at same time',
            'Regular endocrinologist visits',
            'Manage stress',
            'Adequate sleep',
            'Monitor symptoms and report changes'
        ],
        'foods': [
            'For Hypothyroidism: iodine-rich foods (seafood, dairy, eggs)',
            'Selenium-rich foods (Brazil nuts, tuna, sardines)',
            'Zinc-rich foods (shellfish, legumes, seeds)',
            'For Hyperthyroidism: avoid excessive iodine',
            'Cruciferous vegetables in moderation',
            'Fruits and vegetables',
            'Lean proteins',
            'Whole grains',
            'Avoid: excessive soy if hypothyroid, processed foods'
        ],
        'exercises': [
            'Regular moderate exercise',
            'Walking, swimming, cycling',
            'Strength training',
            'Yoga for stress management',
            'Adjust intensity based on energy levels',
            'Hyperthyroid: avoid overexertion',
            'Hypothyroid: exercise helps boost metabolism',
            'Consistency is important'
        ]
    },
    'anemia': {
        'explanation': 'Anemia is a condition where you lack enough healthy red blood cells to carry adequate oxygen to body tissues. Common types include iron-deficiency anemia, vitamin deficiency anemia, and anemia of chronic disease. Symptoms include fatigue, weakness, pale skin.',
        'solutions': [
            'Iron supplements if iron-deficiency anemia',
            'Vitamin B12 or folate supplements if deficient',
            'Treat underlying cause',
            'Blood transfusions in severe cases',
            'Medications to stimulate red blood cell production',
            'Dietary changes to increase iron intake',
            'Regular blood tests to monitor levels',
            'Consult hematologist if chronic'
        ],
        'foods': [
            'Iron-rich foods: red meat, liver, poultry',
            'Plant sources: spinach, lentils, beans, tofu',
            'Vitamin C foods to enhance iron absorption (citrus, tomatoes)',
            'Vitamin B12: meat, fish, eggs, dairy',
            'Folate: leafy greens, legumes, fortified grains',
            'Foods with vitamin A (carrots, sweet potatoes)',
            'Avoid: tea and coffee with meals (inhibit iron absorption)',
            'Cook in cast iron pans'
        ],
        'exercises': [
            'Light to moderate exercise as tolerated',
            'Walking at comfortable pace',
            'Avoid strenuous exercise until anemia improves',
            'Gradually increase activity as levels improve',
            'Listen to your body',
            'Rest when fatigued',
            'Swimming or water aerobics',
            'Yoga and stretching'
        ]
    },
    'pneumonia': {
        'explanation': 'Pneumonia is an infection that inflames air sacs in one or both lungs, which may fill with fluid. It can be caused by bacteria, viruses, or fungi. Symptoms include cough with phlegm, fever, chills, and difficulty breathing.',
        'solutions': [
            'Antibiotics for bacterial pneumonia',
            'Antivirals for viral pneumonia if applicable',
            'Rest and hydration',
            'Fever reducers and pain relievers',
            'Hospitalization if severe',
            'Oxygen therapy if needed',
            'Get pneumonia vaccine (especially if high-risk)',
            'Complete full course of antibiotics',
            'Follow-up chest X-ray to ensure clearing'
        ],
        'foods': [
            'Plenty of fluids (water, herbal teas, broths)',
            'Easy-to-digest foods',
            'Protein-rich foods (eggs, chicken, fish)',
            'Fruits rich in vitamin C (citrus, berries)',
            'Vegetables (carrots, sweet potatoes)',
            'Warm soups and stews',
            'Yogurt with probiotics',
            'Honey (soothes throat)',
            'Avoid: dairy if mucus is excessive, cold foods'
        ],
        'exercises': [
            'Rest during acute phase',
            'Deep breathing exercises',
            'Coughing exercises to clear mucus',
            'Light walking once fever subsides',
            'Gradual return to activity',
            'Avoid strenuous exercise during recovery',
            'Wait 6-8 weeks before resuming normal exercise',
            'Consult doctor before resuming activities'
        ]
    },
    'cholesterol': {
        'explanation': 'High cholesterol is a condition where you have too much fatty substance (cholesterol) in your blood, particularly LDL (bad cholesterol). It can lead to fatty deposits in blood vessels, increasing risk of heart disease and stroke.',
        'solutions': [
            'Statin medications to lower cholesterol',
            'Lifestyle modifications (diet and exercise)',
            'Lose excess weight',
            'Quit smoking',
            'Limit alcohol consumption',
            'Regular cholesterol screening',
            'Manage diabetes and blood pressure',
            'Stress reduction',
            'Monitor lipid levels regularly'
        ],
        'foods': [
            'Oats and whole grains (soluble fiber)',
            'Fatty fish (salmon, mackerel, sardines)',
            'Nuts (almonds, walnuts)',
            'Olive oil',
            'Fruits (apples, berries, citrus)',
            'Vegetables (especially leafy greens)',
            'Legumes (beans, lentils, chickpeas)',
            'Avocados',
            'Avoid: trans fats, saturated fats, fried foods, processed meats, full-fat dairy'
        ],
        'exercises': [
            'Aerobic exercise 150 minutes per week',
            'Brisk walking',
            'Running or jogging',
            'Swimming',
            'Cycling',
            'Dancing',
            'Strength training 2 days per week',
            'Exercise raises HDL (good cholesterol)',
            'Consistency is key'
        ]
    },
    'brain cancer': {
        'explanation': 'Brain cancer refers to malignant tumors that grow in the brain or central nervous system. Types include gliomas, meningiomas, and metastatic brain tumors. Symptoms vary based on tumor location and may include headaches, seizures, vision problems, personality changes, and cognitive difficulties.',
        'solutions': [
            'Neurosurgery to remove tumor if possible',
            'Radiation therapy (external beam or stereotactic radiosurgery)',
            'Chemotherapy medications',
            'Targeted drug therapy',
            'Immunotherapy in some cases',
            'Steroids to reduce brain swelling',
            'Anti-seizure medications if needed',
            'Physical therapy for mobility issues',
            'Occupational therapy for daily activities',
            'Speech therapy if language affected',
            'Regular MRI scans to monitor tumor',
            'Pain management',
            'Psychological counseling and support',
            'Clinical trials for advanced treatments'
        ],
        'foods': [
            'Antioxidant-rich foods (berries, dark leafy greens)',
            'Cruciferous vegetables (broccoli, cauliflower, Brussels sprouts)',
            'Turmeric with black pepper (curcumin)',
            'Green tea (antioxidant properties)',
            'Fatty fish rich in omega-3 (salmon, sardines)',
            'Walnuts and flaxseeds',
            'Garlic and onions',
            'Tomatoes (lycopene)',
            'Whole grains',
            'Lean proteins (chicken, fish, legumes)',
            'Foods high in vitamin D',
            'Plenty of water for hydration',
            'Avoid: processed meats, excessive sugar, alcohol, fried foods'
        ],
        'exercises': [
            'Light to moderate exercise as tolerated',
            'Walking (short distances initially)',
            'Gentle yoga or stretching',
            'Balance exercises with supervision',
            'Seated exercises if mobility limited',
            'Physical therapy exercises as prescribed',
            'Deep breathing exercises',
            'Range-of-motion exercises',
            'Avoid high-risk activities that could cause falls',
            'Rest when fatigued',
            'Exercise helps with mood and energy',
            'Always consult medical team before starting exercise',
            'Adjust based on treatment side effects'
        ]
    },
    'brain tumor': {
        'explanation': 'A brain tumor is an abnormal growth of cells in the brain. It can be benign (non-cancerous) or malignant (cancerous). Tumors can originate in the brain (primary) or spread from other parts of the body (metastatic). Symptoms depend on size, type, and location.',
        'solutions': [
            'Complete medical evaluation including MRI/CT scans',
            'Biopsy to determine tumor type',
            'Surgery to remove tumor if accessible',
            'Watch and wait approach for some benign tumors',
            'Radiation therapy',
            'Chemotherapy for malignant tumors',
            'Medications to control symptoms (steroids, anti-seizure)',
            'Rehabilitation therapy (physical, occupational, speech)',
            'Regular neurological monitoring',
            'Multidisciplinary care team (neurosurgeon, oncologist, radiologist)',
            'Support groups for patients and families',
            'Palliative care if needed'
        ],
        'foods': [
            'Brain-healthy foods (salmon, blueberries, walnuts)',
            'Vegetables (especially dark leafy greens)',
            'Fruits rich in antioxidants',
            'Whole grains for sustained energy',
            'Lean proteins',
            'Foods with omega-3 fatty acids',
            'Green tea',
            'Turmeric and ginger',
            'Foods rich in folate (beans, lentils)',
            'Adequate calorie intake during treatment',
            'Small, frequent meals if appetite is poor',
            'Avoid: alcohol, processed foods, excess caffeine'
        ],
        'exercises': [
            'Individualized exercise plan based on abilities',
            'Gentle walking',
            'Seated exercises',
            'Stretching for flexibility',
            'Balance training with support',
            'Physical therapy exercises',
            'Cognitive exercises (puzzles, memory games)',
            'Avoid activities with fall risk',
            'Gradual progression as tolerated',
            'Rest is important during treatment',
            'Consult healthcare team before any exercise program'
        ]
    },
    'breast cancer': {
        'explanation': 'Breast cancer is uncontrolled growth of cells in breast tissue. It\'s the most common cancer in women but can occur in men too. Symptoms include lumps, changes in breast shape, nipple discharge, and skin dimpling. Early detection through mammography significantly improves outcomes.',
        'solutions': [
            'Surgery (lumpectomy or mastectomy)',
            'Radiation therapy',
            'Chemotherapy',
            'Hormone therapy (for hormone-receptor-positive cancers)',
            'Targeted therapy (Herceptin for HER2-positive)',
            'Immunotherapy in some cases',
            'Regular mammograms for screening',
            'Self-breast examination monthly',
            'Genetic counseling if family history (BRCA genes)',
            'Support groups and counseling',
            'Reconstruction surgery if desired',
            'Regular follow-up with oncologist'
        ],
        'foods': [
            'Cruciferous vegetables (broccoli, cauliflower, kale)',
            'Berries (antioxidants)',
            'Fatty fish (omega-3)',
            'Whole grains',
            'Legumes (beans, lentils)',
            'Green tea',
            'Turmeric',
            'Garlic and onions',
            'Tomatoes (lycopene)',
            'Flaxseeds',
            'Avoid: alcohol, processed meats, high-fat foods, excess sugar'
        ],
        'exercises': [
            'Regular aerobic exercise (150 min/week)',
            'Walking, swimming, cycling',
            'Strength training',
            'Yoga for flexibility and stress relief',
            'Post-surgery exercises for arm mobility',
            'Lymphedema prevention exercises',
            'Exercise reduces recurrence risk',
            'Start slowly after treatment'
        ]
    },
    'lung cancer': {
        'explanation': 'Lung cancer is malignant growth in lung cells, most commonly caused by smoking. Symptoms include persistent cough, coughing blood, chest pain, shortness of breath, and weight loss. Two main types: small cell and non-small cell lung cancer.',
        'solutions': [
            'Quit smoking immediately',
            'Surgery to remove tumor',
            'Radiation therapy',
            'Chemotherapy',
            'Targeted therapy (EGFR, ALK inhibitors)',
            'Immunotherapy (checkpoint inhibitors)',
            'Palliative care for symptom management',
            'Breathing exercises and oxygen therapy',
            'Regular CT scans for monitoring',
            'Clinical trials for advanced cases'
        ],
        'foods': [
            'Antioxidant-rich fruits and vegetables',
            'Cruciferous vegetables',
            'Berries',
            'Green tea',
            'Fatty fish',
            'Turmeric',
            'Garlic',
            'Whole grains',
            'High-protein foods during treatment',
            'Avoid: smoking, alcohol, processed foods'
        ],
        'exercises': [
            'Breathing exercises (pursed-lip breathing)',
            'Walking at comfortable pace',
            'Pulmonary rehabilitation',
            'Light strength training',
            'Yoga for breathing and relaxation',
            'Avoid strenuous activity if short of breath',
            'Oxygen support during exercise if needed'
        ]
    },
    'prostate cancer': {
        'explanation': 'Prostate cancer affects the prostate gland in males. Common in older men. Symptoms include frequent urination, weak urine flow, blood in urine, and pelvic pain. Often slow-growing; detected through PSA blood test and digital rectal exam.',
        'solutions': [
            'Active surveillance for slow-growing tumors',
            'Surgery (prostatectomy)',
            'Radiation therapy (external beam or brachytherapy)',
            'Hormone therapy (androgen deprivation)',
            'Chemotherapy for advanced cases',
            'Regular PSA testing',
            'Cryotherapy or HIFU in some cases',
            'Manage side effects (incontinence, erectile dysfunction)',
            'Regular follow-ups'
        ],
        'foods': [
            'Tomatoes (lycopene)',
            'Cruciferous vegetables',
            'Green tea',
            'Fatty fish',
            'Soy products',
            'Pomegranate juice',
            'Berries',
            'Nuts and seeds',
            'Avoid: high-fat dairy, red meat, calcium supplements in excess'
        ],
        'exercises': [
            'Regular physical activity',
            'Walking, jogging, cycling',
            'Strength training',
            'Pelvic floor exercises (Kegels)',
            'Exercise improves outcomes',
            'Stay active during treatment'
        ]
    },
    'colon cancer': {
        'explanation': 'Colorectal cancer is a tumor in the colon or rectum lining. Symptoms include blood in stool, changes in bowel habits, abdominal pain, and weight loss. Screening with colonoscopy starting at age 45-50 is crucial for early detection.',
        'solutions': [
            'Surgery to remove tumor and affected colon',
            'Chemotherapy',
            'Radiation therapy (especially for rectal cancer)',
            'Targeted therapy (for metastatic disease)',
            'Immunotherapy (for MSI-high tumors)',
            'Regular colonoscopy screening',
            'Colostomy if needed',
            'Follow-up surveillance',
            'Treatment of polyps to prevent cancer'
        ],
        'foods': [
            'High-fiber diet (whole grains, vegetables)',
            'Cruciferous vegetables',
            'Garlic and onions',
            'Fish and poultry',
            'Legumes',
            'Fruits',
            'Limit red meat and processed meats',
            'Avoid: alcohol, fried foods, processed foods'
        ],
        'exercises': [
            'Regular physical activity reduces risk',
            'Walking, jogging, swimming',
            'Strength training',
            'Yoga',
            '30 minutes daily recommended',
            'Exercise improves survival rates'
        ]
    },
    'stomach cancer': {
        'explanation': 'Gastric cancer affects the stomach lining. Symptoms include persistent indigestion, stomach pain, nausea, vomiting blood, and weight loss. Risk factors include H. pylori infection, smoking, and diet high in smoked/salted foods.',
        'solutions': [
            'Surgery (partial or total gastrectomy)',
            'Chemotherapy',
            'Radiation therapy',
            'Targeted therapy (Herceptin for HER2-positive)',
            'Treatment of H. pylori infection',
            'Endoscopic procedures for early-stage',
            'Nutritional support',
            'Palliative care for advanced cases'
        ],
        'foods': [
            'Fresh fruits and vegetables',
            'Whole grains',
            'Lean proteins',
            'Vitamin C-rich foods',
            'Green tea',
            'Avoid: smoked foods, salted fish, pickled vegetables, processed meats',
            'Small, frequent meals after surgery'
        ],
        'exercises': [
            'Light to moderate exercise',
            'Walking',
            'Gentle stretching',
            'Yoga',
            'Rest during acute treatment',
            'Gradually increase activity'
        ]
    },
    'liver cancer': {
        'explanation': 'Hepatocellular carcinoma (HCC) is malignant tumor in liver cells. Often occurs in people with chronic liver disease or cirrhosis. Symptoms include upper right abdominal pain, jaundice, swelling, and fatigue.',
        'solutions': [
            'Surgery (hepatectomy or liver transplant)',
            'Ablation therapy (radiofrequency or microwave)',
            'Embolization procedures',
            'Targeted therapy (Sorafenib, Lenvatinib)',
            'Immunotherapy',
            'Radiation therapy',
            'Treat underlying liver disease',
            'Hepatitis B/C vaccination and treatment',
            'Avoid alcohol completely'
        ],
        'foods': [
            'Low-sodium diet',
            'Fresh fruits and vegetables',
            'Whole grains',
            'Lean proteins',
            'Foods rich in antioxidants',
            'Green tea',
            'Avoid: alcohol, fatty foods, processed foods, excessive salt'
        ],
        'exercises': [
            'Light exercise as tolerated',
            'Walking',
            'Gentle yoga',
            'Rest when fatigued',
            'Avoid strenuous activity',
            'Consult doctor before exercise'
        ]
    },
    'pancreatic cancer': {
        'explanation': 'Pancreatic cancer is aggressive cancer of pancreas tissues. Often detected late due to lack of early symptoms. Symptoms include severe back and abdominal pain, jaundice, weight loss, and digestive issues. Has poor prognosis.',
        'solutions': [
            'Surgery (Whipple procedure) if operable',
            'Chemotherapy (FOLFIRINOX, Gemcitabine)',
            'Radiation therapy',
            'Targeted therapy',
            'Immunotherapy',
            'Pain management',
            'Enzyme supplements for digestion',
            'Nutritional support',
            'Palliative care',
            'Clinical trials'
        ],
        'foods': [
            'Small, frequent meals',
            'Easily digestible foods',
            'Lean proteins',
            'Cooked vegetables',
            'Low-fat foods',
            'Pancreatic enzyme supplements',
            'Adequate calories and protein',
            'Avoid: fatty foods, alcohol, spicy foods'
        ],
        'exercises': [
            'Light walking as tolerated',
            'Gentle stretching',
            'Rest when needed',
            'Avoid strenuous activity',
            'Focus on maintaining strength',
            'Physical therapy if needed'
        ]
    },
    'cervical cancer': {
        'explanation': 'Cervical cancer affects the cervix, often caused by HPV (Human Papillomavirus) infection. Symptoms include abnormal vaginal bleeding, pelvic pain, and pain during intercourse. Preventable with HPV vaccination and regular Pap smears.',
        'solutions': [
            'HPV vaccination (Gardasil) for prevention',
            'Regular Pap smear screening',
            'Surgery (hysterectomy, cone biopsy)',
            'Radiation therapy',
            'Chemotherapy',
            'Targeted therapy',
            'Immunotherapy',
            'Treatment of precancerous lesions',
            'Follow-up surveillance'
        ],
        'foods': [
            'Foods rich in folate (leafy greens, legumes)',
            'Vitamin C-rich fruits',
            'Carotenoid-rich vegetables',
            'Green tea',
            'Whole grains',
            'Lean proteins',
            'Antioxidant-rich foods',
            'Avoid: smoking, excessive alcohol'
        ],
        'exercises': [
            'Regular physical activity',
            'Walking, swimming, cycling',
            'Pelvic floor exercises',
            'Yoga',
            'Maintain healthy weight',
            'Exercise reduces risk'
        ]
    },
    'ovarian cancer': {
        'explanation': 'Ovarian cancer is tumor developing in the ovaries. Often called "silent killer" due to vague early symptoms. Symptoms include abdominal bloating, pelvic pain, feeling full quickly, and frequent urination.',
        'solutions': [
            'Surgery (removal of ovaries, uterus, lymph nodes)',
            'Chemotherapy (Carboplatin, Paclitaxel)',
            'Targeted therapy (PARP inhibitors, Bevacizumab)',
            'Genetic testing (BRCA1/BRCA2)',
            'Preventive surgery for high-risk women',
            'Regular pelvic exams',
            'CA-125 blood test monitoring',
            'Clinical trials'
        ],
        'foods': [
            'Cruciferous vegetables',
            'Colorful fruits and vegetables',
            'Whole grains',
            'Lean proteins',
            'Green tea',
            'Foods rich in vitamin D',
            'Omega-3 fatty acids',
            'Avoid: high-fat dairy, red meat, processed foods'
        ],
        'exercises': [
            'Regular physical activity',
            'Walking, swimming',
            'Strength training',
            'Yoga',
            'Exercise may reduce risk',
            'Stay active during treatment as able'
        ]
    },
    'skin cancer': {
        'explanation': 'Skin cancer includes basal cell carcinoma (slow-growing), squamous cell carcinoma, and melanoma (most dangerous). Symptoms include changes in moles, new lumps, non-healing wounds, and irregular pigmentation. Caused primarily by UV exposure.',
        'solutions': [
            'Surgical excision of tumor',
            'Mohs surgery for certain types',
            'Cryotherapy for precancerous lesions',
            'Radiation therapy',
            'Topical chemotherapy (5-FU)',
            'Immunotherapy for melanoma',
            'Targeted therapy (BRAF inhibitors)',
            'Regular skin checks',
            'Sun protection (SPF 30+, protective clothing)',
            'Avoid tanning beds'
        ],
        'foods': [
            'Antioxidant-rich foods',
            'Colorful fruits and vegetables',
            'Green tea',
            'Tomatoes (lycopene)',
            'Fatty fish (omega-3)',
            'Dark chocolate (flavonoids)',
            'Nuts and seeds',
            'Foods with vitamin D',
            'Stay hydrated'
        ],
        'exercises': [
            'Regular outdoor exercise with sun protection',
            'Early morning or evening activities',
            'Wear protective clothing and sunscreen',
            'Stay active for overall health',
            'Exercise in shaded areas when possible'
        ]
    },
    'melanoma': {
        'explanation': 'Melanoma is dangerous cancer of pigment-producing melanocytes. Most aggressive skin cancer. Symptoms include asymmetrical moles, irregular edges, changing color/size, and itchy or bleeding moles. Can spread quickly if not caught early.',
        'solutions': [
            'Wide surgical excision',
            'Sentinel lymph node biopsy',
            'Immunotherapy (Pembrolizumab, Nivolumab)',
            'Targeted therapy (BRAF/MEK inhibitors)',
            'Radiation therapy',
            'Regular full-body skin exams',
            'ABCDE rule for mole monitoring',
            'Sun protection crucial',
            'Early detection saves lives'
        ],
        'foods': [
            'Antioxidant-rich berries',
            'Green leafy vegetables',
            'Fatty fish',
            'Green tea',
            'Turmeric',
            'Tomatoes',
            'Dark chocolate',
            'Nuts (especially walnuts)',
            'Foods with vitamin D and E'
        ],
        'exercises': [
            'Regular physical activity',
            'Exercise during low UV hours',
            'Always use sunscreen (SPF 50+)',
            'Wear protective clothing',
            'Stay active indoors if midday',
            'Swimming (with waterproof sunscreen)'
        ]
    },
    'leukemia': {
        'explanation': 'Leukemia is blood cancer affecting white blood cells. Types include ALL (Acute Lymphoblastic), AML (Acute Myeloid), CLL (Chronic Lymphocytic), and CML (Chronic Myeloid). Symptoms include frequent infections, fatigue, bleeding, bruising, and bone pain.',
        'solutions': [
            'Chemotherapy (main treatment)',
            'Targeted therapy (Imatinib for CML)',
            'Immunotherapy',
            'Stem cell (bone marrow) transplant',
            'Radiation therapy',
            'CAR T-cell therapy',
            'Supportive care (transfusions, antibiotics)',
            'Regular blood tests',
            'Infection prevention measures',
            'Clinical trials'
        ],
        'foods': [
            'High-protein foods for cell repair',
            'Iron-rich foods if anemic',
            'Fruits and vegetables (well-washed)',
            'Avoid raw foods during treatment (infection risk)',
            'Pasteurized dairy only',
            'Well-cooked meats',
            'Stay hydrated',
            'Small frequent meals',
            'Foods rich in folate and B vitamins'
        ],
        'exercises': [
            'Light exercise as tolerated',
            'Walking',
            'Gentle stretching',
            'Yoga',
            'Avoid contact sports (bleeding risk)',
            'Rest when fatigued',
            'Exercise improves quality of life',
            'Consult doctor about activity level'
        ]
    },
    'lymphoma': {
        'explanation': 'Lymphoma is cancer of the lymphatic system. Two main types: Hodgkin (with Reed-Sternberg cells) and Non-Hodgkin lymphoma. Symptoms include painless swollen lymph nodes, night sweats, fever, and weight loss.',
        'solutions': [
            'Chemotherapy (CHOP, ABVD regimens)',
            'Radiation therapy',
            'Immunotherapy (Rituximab)',
            'Stem cell transplant',
            'CAR T-cell therapy',
            'Targeted therapy',
            'Watch and wait for slow-growing types',
            'Regular monitoring with CT/PET scans',
            'Infection prevention'
        ],
        'foods': [
            'High-protein diet',
            'Fruits and vegetables',
            'Whole grains',
            'Lean meats and fish',
            'Foods to boost immune system',
            'Adequate hydration',
            'Avoid raw/undercooked foods during treatment',
            'Small frequent meals if appetite poor'
        ],
        'exercises': [
            'Moderate exercise as tolerated',
            'Walking, swimming',
            'Yoga',
            'Strength training (light)',
            'Rest during fatigue',
            'Exercise improves treatment outcomes',
            'Gradually increase activity'
        ]
    },
    'thyroid cancer': {
        'explanation': 'Thyroid cancer affects the thyroid gland. Most common types: papillary and follicular (usually treatable). Symptoms include lump in neck, voice changes, difficulty swallowing. Generally has good prognosis.',
        'solutions': [
            'Surgery (thyroidectomy)',
            'Radioactive iodine therapy',
            'Thyroid hormone therapy (suppression)',
            'External radiation therapy',
            'Targeted therapy for advanced cases',
            'Regular monitoring of thyroglobulin levels',
            'Ultrasound surveillance',
            'Lifelong thyroid hormone replacement'
        ],
        'foods': [
            'Iodine-rich foods (seafood, dairy)',
            'Selenium-rich foods (Brazil nuts, fish)',
            'Fruits and vegetables',
            'Whole grains',
            'Lean proteins',
            'Low-iodine diet before radioactive iodine treatment',
            'Avoid: excessive soy, cruciferous vegetables in large amounts'
        ],
        'exercises': [
            'Regular physical activity',
            'Walking, swimming, cycling',
            'Strength training',
            'Yoga',
            'Exercise helps manage weight (important with hypothyroidism)',
            'Stay active post-surgery'
        ]
    },
    'kidney cancer': {
        'explanation': 'Renal cell carcinoma is tumor forming in kidney tissues. Symptoms include blood in urine, flank pain, lump on side of abdomen, and weight loss. Often discovered incidentally on imaging.',
        'solutions': [
            'Surgery (nephrectomy - partial or complete)',
            'Targeted therapy (Sunitinib, Pazopanib)',
            'Immunotherapy (Nivolumab, Pembrolizumab)',
            'Ablation therapy for small tumors',
            'Radiation therapy',
            'Active surveillance for small tumors',
            'Regular imaging follow-up'
        ],
        'foods': [
            'Plenty of water',
            'Fruits and vegetables',
            'Whole grains',
            'Lean proteins',
            'Limit salt intake',
            'Avoid: processed foods, excessive protein if kidney function reduced',
            'Low-potassium diet if needed'
        ],
        'exercises': [
            'Regular physical activity',
            'Walking, swimming',
            'Moderate exercise',
            'Stay hydrated during exercise',
            'Avoid dehydration',
            'Post-surgery: gradual return to activity'
        ]
    },
    'bladder cancer': {
        'explanation': 'Bladder cancer affects the bladder lining. Most common symptom is blood in urine. Other symptoms include painful urination and frequent urination. Smoking is major risk factor.',
        'solutions': [
            'Transurethral resection (TURBT)',
            'Intravesical chemotherapy or BCG immunotherapy',
            'Cystectomy for invasive cancer',
            'Chemotherapy',
            'Immunotherapy (checkpoint inhibitors)',
            'Radiation therapy',
            'Regular cystoscopy surveillance',
            'Quit smoking'
        ],
        'foods': [
            'Plenty of water (dilutes urine)',
            'Fruits and vegetables',
            'Cruciferous vegetables',
            'Green tea',
            'Whole grains',
            'Avoid: smoking, processed meats, fried foods',
            'Limit caffeine and alcohol'
        ],
        'exercises': [
            'Regular physical activity',
            'Walking, cycling, swimming',
            'Pelvic floor exercises',
            'Stay hydrated',
            'Exercise reduces risk',
            'Maintain healthy weight'
        ]
    }
}


def get_disease_info(disease_name):
    """
    Get information about a disease from the database.
    
    Args:
        disease_name (str): Name of the disease to look up
        
    Returns:
        dict: Disease information or None if not found
    """
    disease_name = disease_name.lower().strip()
    return DISEASE_DATABASE.get(disease_name)


def format_response(disease_name):
    """
    Format a chatbot response for a given disease.
    
    Args:
        disease_name (str): Name of the disease
        
    Returns:
        str: Formatted response message
    """
    info = get_disease_info(disease_name)
    
    if not info:
        # Handle general health questions
        return handle_general_query(disease_name)
    
    response = f"<strong>{disease_name.title()}</strong><br><br>"
    response += f"<strong>📋 What is it?</strong><br>{info['explanation']}<br><br>"
    
    response += "<strong>💊 Solutions & Treatment:</strong><br><ul>"
    for solution in info['solutions']:
        response += f"<li>{solution}</li>"
    response += "</ul>"
    
    response += "<strong>🥗 Recommended Foods:</strong><br><ul>"
    for food in info['foods']:
        response += f"<li>{food}</li>"
    response += "</ul>"
    
    response += "<strong>🏃 Recommended Exercises:</strong><br><ul>"
    for exercise in info['exercises']:
        response += f"<li>{exercise}</li>"
    response += "</ul>"
    
    response += "<br><em>⚠️ Note: This information is for educational purposes only. Always consult a healthcare professional for proper diagnosis and treatment.</em>"
    
    return response


def handle_general_query(query):
    """
    Handle general health-related questions using pattern matching.
    
    Args:
        query (str): User's question
        
    Returns:
        str: Response to the query
    """
    query_lower = query.lower()
    
    # Common health questions
    if any(word in query_lower for word in ['symptom', 'symptoms', 'signs']):
        return """<strong>Understanding Symptoms</strong><br><br>
        Symptoms are physical or mental features that indicate a condition or disease. Common symptoms include:<br><ul>
        <li>Fever - body temperature above 100.4°F (38°C)</li>
        <li>Pain - can indicate inflammation or injury</li>
        <li>Fatigue - unusual tiredness or weakness</li>
        <li>Cough - respiratory system response</li>
        <li>Nausea/vomiting - digestive system issues</li>
        <li>Headache - can have various causes</li>
        </ul><br>
        <strong>⚠️ When to see a doctor:</strong> Severe symptoms, symptoms lasting more than a few days, or worsening symptoms.<br><br>
        <em>For specific diseases, type the disease name (e.g., diabetes, cancer, fever).</em>"""
    
    elif any(word in query_lower for word in ['diet', 'food', 'nutrition', 'eat']):
        return """<strong>Healthy Diet Guidelines</strong><br><br>
        <strong>🥗 General Nutrition Tips:</strong><br><ul>
        <li>Eat a variety of colorful fruits and vegetables (5+ servings daily)</li>
        <li>Choose whole grains over refined grains</li>
        <li>Include lean proteins (fish, poultry, beans, nuts)</li>
        <li>Limit processed foods, sugar, and salt</li>
        <li>Stay hydrated (8 glasses of water daily)</li>
        <li>Eat healthy fats (olive oil, avocados, nuts)</li>
        <li>Control portion sizes</li>
        <li>Limit alcohol consumption</li>
        </ul><br>
        <strong>Foods to prioritize:</strong> Leafy greens, berries, fatty fish, nuts, whole grains, legumes<br>
        <strong>Foods to limit:</strong> Processed meats, sugary drinks, fried foods, excess salt<br><br>
        <em>For disease-specific diets, type the disease name.</em>"""
    
    elif any(word in query_lower for word in ['exercise', 'workout', 'fitness', 'physical activity']):
        return """<strong>Exercise & Fitness Guidelines</strong><br><br>
        <strong>🏃 Recommended Physical Activity:</strong><br><ul>
        <li>Adults: 150 minutes moderate aerobic activity per week</li>
        <li>Or 75 minutes vigorous aerobic activity per week</li>
        <li>Strength training 2+ days per week</li>
        <li>Include flexibility and balance exercises</li>
        </ul><br>
        <strong>Types of Exercise:</strong><br><ul>
        <li><strong>Aerobic:</strong> Walking, jogging, swimming, cycling</li>
        <li><strong>Strength:</strong> Weight training, resistance bands, bodyweight exercises</li>
        <li><strong>Flexibility:</strong> Yoga, stretching</li>
        <li><strong>Balance:</strong> Tai chi, stability exercises</li>
        </ul><br>
        <strong>Benefits:</strong> Improves heart health, strengthens bones, boosts mood, helps weight management, reduces disease risk<br><br>
        <em>For disease-specific exercises, type the disease name.</em>"""
    
    elif any(word in query_lower for word in ['prevent', 'prevention', 'avoid']):
        return """<strong>Disease Prevention Tips</strong><br><br>
        <strong>🛡️ Key Prevention Strategies:</strong><br><ul>
        <li><strong>Healthy Diet:</strong> Balanced nutrition with fruits, vegetables, whole grains</li>
        <li><strong>Regular Exercise:</strong> Stay physically active</li>
        <li><strong>Don't Smoke:</strong> Avoid tobacco in all forms</li>
        <li><strong>Limit Alcohol:</strong> Moderate consumption or avoid</li>
        <li><strong>Maintain Healthy Weight:</strong> BMI 18.5-24.9</li>
        <li><strong>Get Vaccinated:</strong> Stay up-to-date on immunizations</li>
        <li><strong>Regular Checkups:</strong> Screenings and health monitoring</li>
        <li><strong>Manage Stress:</strong> Meditation, relaxation techniques</li>
        <li><strong>Good Hygiene:</strong> Hand washing, dental care</li>
        <li><strong>Adequate Sleep:</strong> 7-9 hours per night</li>
        <li><strong>Safe Practices:</strong> Use seat belts, practice safe sex</li>
        </ul><br>
        <em>Prevention is better than cure!</em>"""
    
    elif any(word in query_lower for word in ['vitamin', 'supplement', 'minerals']):
        return """<strong>Vitamins & Supplements</strong><br><br>
        <strong>💊 Essential Vitamins:</strong><br><ul>
        <li><strong>Vitamin A:</strong> Vision, immune function (carrots, sweet potatoes)</li>
        <li><strong>Vitamin C:</strong> Immunity, antioxidant (citrus, berries)</li>
        <li><strong>Vitamin D:</strong> Bone health (sunlight, fatty fish, fortified milk)</li>
        <li><strong>Vitamin E:</strong> Antioxidant (nuts, seeds, oils)</li>
        <li><strong>B Vitamins:</strong> Energy, brain function (whole grains, meat, eggs)</li>
        </ul><br>
        <strong>Important Minerals:</strong><br><ul>
        <li><strong>Calcium:</strong> Bone health (dairy, leafy greens)</li>
        <li><strong>Iron:</strong> Blood health (red meat, spinach, legumes)</li>
        <li><strong>Magnesium:</strong> Muscle/nerve function (nuts, seeds, whole grains)</li>
        <li><strong>Zinc:</strong> Immunity (shellfish, meat, beans)</li>
        </ul><br>
        <strong>⚠️ Note:</strong> Get nutrients from food first. Consult doctor before taking supplements.<br><br>
        <em>Balanced diet usually provides all necessary nutrients.</em>"""
    
    elif any(word in query_lower for word in ['water', 'hydration', 'drink']):
        return """<strong>Hydration & Water Intake</strong><br><br>
        <strong>💧 Importance of Hydration:</strong><br><ul>
        <li>Regulates body temperature</li>
        <li>Transports nutrients and oxygen</li>
        <li>Removes waste products</li>
        <li>Lubricates joints</li>
        <li>Protects organs and tissues</li>
        <li>Maintains blood pressure</li>
        </ul><br>
        <strong>How Much Water:</strong><br><ul>
        <li>General guideline: 8 glasses (2 liters) daily</li>
        <li>Men: About 3.7 liters (125 oz) per day</li>
        <li>Women: About 2.7 liters (91 oz) per day</li>
        <li>Increase during exercise, hot weather, illness</li>
        </ul><br>
        <strong>Signs of Dehydration:</strong> Dark urine, dry mouth, fatigue, dizziness, headache<br>
        <strong>Hydration sources:</strong> Water, herbal teas, fruits (watermelon, oranges), vegetables (cucumber, lettuce)<br><br>
        <em>Listen to your body - drink when thirsty!</em>"""
    
    elif any(word in query_lower for word in ['sleep', 'insomnia', 'rest']):
        return """<strong>Sleep & Rest</strong><br><br>
        <strong>😴 Importance of Sleep:</strong><br><ul>
        <li>Physical recovery and healing</li>
        <li>Memory consolidation</li>
        <li>Immune system support</li>
        <li>Hormone regulation</li>
        <li>Mental health maintenance</li>
        </ul><br>
        <strong>Recommended Sleep:</strong><br><ul>
        <li>Adults: 7-9 hours per night</li>
        <li>Teenagers: 8-10 hours</li>
        <li>Children: 9-12 hours</li>
        </ul><br>
        <strong>Tips for Better Sleep:</strong><br><ul>
        <li>Maintain consistent sleep schedule</li>
        <li>Create dark, quiet, cool environment</li>
        <li>Avoid screens 1 hour before bed</li>
        <li>Limit caffeine after 2 PM</li>
        <li>Exercise regularly (not close to bedtime)</li>
        <li>Avoid large meals before bed</li>
        <li>Practice relaxation techniques</li>
        </ul><br>
        <em>Quality sleep is essential for health!</em>"""
    
    elif any(word in query_lower for word in ['stress', 'anxiety', 'mental health', 'depression']):
        return """<strong>Mental Health & Stress Management</strong><br><br>
        <strong>🧠 Managing Stress & Mental Health:</strong><br><ul>
        <li><strong>Relaxation Techniques:</strong> Deep breathing, meditation, progressive muscle relaxation</li>
        <li><strong>Physical Activity:</strong> Exercise releases endorphins</li>
        <li><strong>Social Connection:</strong> Talk to friends, family, support groups</li>
        <li><strong>Healthy Lifestyle:</strong> Good sleep, nutrition, limit alcohol</li>
        <li><strong>Time Management:</strong> Prioritize tasks, set boundaries</li>
        <li><strong>Hobbies:</strong> Engage in enjoyable activities</li>
        <li><strong>Mindfulness:</strong> Stay present, practice gratitude</li>
        </ul><br>
        <strong>⚠️ Warning Signs:</strong><br><ul>
        <li>Persistent sadness or anxiety</li>
        <li>Changes in sleep or appetite</li>
        <li>Loss of interest in activities</li>
        <li>Difficulty concentrating</li>
        <li>Thoughts of self-harm</li>
        </ul><br>
        <strong>🆘 Seek professional help if symptoms persist or worsen.</strong><br>
        <em>For specific conditions, type: depression, anxiety, stress</em>"""
    
    elif any(word in query_lower for word in ['weight', 'lose weight', 'gain weight', 'bmi']):
        return """<strong>Weight Management</strong><br><br>
        <strong>⚖️ Healthy Weight Guidelines:</strong><br><ul>
        <li><strong>BMI (Body Mass Index):</strong><br>
        - Underweight: Below 18.5<br>
        - Normal: 18.5-24.9<br>
        - Overweight: 25-29.9<br>
        - Obese: 30 and above</li>
        </ul><br>
        <strong>Weight Loss Tips:</strong><br><ul>
        <li>Create calorie deficit (500-750 cal/day for 1-1.5 lbs/week loss)</li>
        <li>Eat whole, unprocessed foods</li>
        <li>Control portion sizes</li>
        <li>Regular exercise (cardio + strength training)</li>
        <li>Stay hydrated</li>
        <li>Get adequate sleep</li>
        <li>Track food intake</li>
        <li>Avoid crash diets</li>
        </ul><br>
        <strong>Weight Gain Tips (Healthy):</strong><br><ul>
        <li>Calorie surplus with nutritious foods</li>
        <li>Frequent, protein-rich meals</li>
        <li>Strength training to build muscle</li>
        <li>Nutrient-dense foods (nuts, avocados, whole grains)</li>
        </ul><br>
        <em>Sustainable changes lead to lasting results!</em>"""
    
    elif any(word in query_lower for word in ['vaccine', 'vaccination', 'immunization']):
        return """<strong>Vaccines & Immunization</strong><br><br>
        <strong>💉 Importance of Vaccines:</strong><br><ul>
        <li>Prevent serious infectious diseases</li>
        <li>Protect vulnerable populations</li>
        <li>Reduce healthcare costs</li>
        <li>Achieve community immunity</li>
        </ul><br>
        <strong>Common Vaccines:</strong><br><ul>
        <li><strong>Children:</strong> MMR, DTaP, Polio, Hepatitis B, HPV</li>
        <li><strong>Adults:</strong> Flu (annual), Tdap booster, Pneumonia, Shingles (50+)</li>
        <li><strong>Travel:</strong> Hepatitis A, Typhoid, Yellow Fever (depending on destination)</li>
        </ul><br>
        <strong>Safety:</strong> Vaccines are thoroughly tested and monitored. Side effects are usually mild (soreness, low fever).<br><br>
        <strong>⚠️ Consult healthcare provider for personalized vaccination schedule.</strong><br>
        <em>Vaccines save millions of lives annually!</em>"""
    
    else:
        # If no pattern matches, show available diseases
        available_diseases = ', '.join(sorted(list(DISEASE_DATABASE.keys())[:15]))
        return f"""<strong>Health Assistant</strong><br><br>
        I can help you with:<br><br>
        <strong>🔍 Ask about specific diseases:</strong><br>
        {available_diseases}, and more...<br><br>
        <strong>💡 Ask general health questions about:</strong><br><ul>
        <li>Symptoms and signs</li>
        <li>Diet and nutrition</li>
        <li>Exercise and fitness</li>
        <li>Disease prevention</li>
        <li>Vitamins and supplements</li>
        <li>Hydration and water intake</li>
        <li>Sleep and rest</li>
        <li>Mental health and stress</li>
        <li>Weight management</li>
        <li>Vaccines and immunization</li>
        </ul><br>
        <em>Type a disease name or ask a health question!</em>"""
