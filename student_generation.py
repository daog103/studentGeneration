import random
import csv
#import table headings
def create_list(length):
    total_list = [['uni_email', 'password', 'firstname','middlename', 'surname', 'contact_email', 'phone_number', 'dob',
               'degree1_level', 'degree1_title', 'fos1', 'university1', 'completed1', 'graduation1', 'result1', 
               'degree2_level', 'degree2_title', 'fos2', 'university2', 'completed2', 'graduation2',
               'result2', 'degree3_level', 'degree3_title', 'fos3', 'university3', 'completed3', 'graduation3', 'result3',
               'alevel_instituition', 'alevel_country', 'alevel_insituition_type', 'alevel_start', 'alevel_end',
               'alevel_q1_type', 'alevel_q1_subject', 'alevel_q1_grade', 'alevel_q2_type', 'alevel_q2_subject',
               'alevel_q2_grade', 'alevel_q3_type', 'alevel_q3_subject', 'alevel_q3_grade', 'alevel_q4_type', 'alevel_q4_subject',
               'alevel_q4_grade', 'gcse_instituition', 'gcse_country', 'gcse_instituition_type', 'gcse_q1_type', 'gcse_q1_subject',
               'gcse_q1_grade', 'gcse_q2_type', 'gcse_q2_subject', 'gcse_q2_grade', 'gcse_q3_type', 'gcse_q3_subject',
               'gcse_q3_grade', 'gcse_q4_type', 'gcse_q4_subject', 'gcse_q4_grade', 'gcse_q5_type', 'gcse_q5_subject',
               'gcse_q5_grade', 'gcse_q6_type', 'gcse_q6_subject', 'gcse_q6_grade', 'gcse_q7_type', 'gcse_q7_subject',
               'gcse_q7_grade', 'gcse_q8_type', 'gcse_q8_subject', 'gcse_q8_grade', 'gcse_q9_type', 'gcse_q9_subject',
               'gcse_q9_grade', 'gcse_q10_type', 'gcse_q10_subject', 'gcse_q10_grade', 'gcse_q11_type', 'gcse_q11_subject',
               'gcse_q11_grade', 'gcse_q12_type', 'gcse_q12_subject', 'gcse_q12_grade', 'gcse_q13_type', 'gcse_q13_subject',
               'gcse_q13_grade', 'gcse_q14_type', 'gcse_q14_subject', 'gcse_q14_grade', 'we1_type', 'we1_company_name', 
               'we1_role', 'we1_start_date', 'we1_end_date', 'we1_still_working', 'we1_description', 'we2_type', 'we2_company_name',
               'we2_role', 'we2_start_date', 'we2_end_date', 'we2_still_working', 'we2_description', 'language1_name', 
               'langauge1_proficiency', 'langauge1_description', 'language2_name', 'langauge2_proficiency', 'langauge2_description',
               'skill1_name', 'skill1_proficiency', 'skill1_description', 'skill2_name', 'skill2_proficiency', 'skill2_description',
               'skill3_name', 'skill3_proficiency', 'skill3_description', 'skill4_name', 'skill4_proficiency', 'skill4_description',
               'student_link1', 'student_link2', 'industries_interested', 'macro_roles', 'micro_roles', 'school_meals?', 
               'parents_education?', 'disability?', 'ethinic_group', 'gender', 'sexual_orientation', 'religion', 'year_of_study_1', 
                  'year_of_study_2', 'year_of_study_3', 'link_1_type', 'link_2_type']]

    universities = """Abertay University , Aberystwyth University , AECC University College , Anglia Ruskin University , Aston University ,
                    Bangor University , Bath Spa University , Birkbeck College , Birmingham City University , Bishop Grosseteste University ,
                    Bournemouth University , Brunel University London , Buckinghamshire New University , Canterbury Christ Church University , 
                    Cardiff Metropolitan University , Cardiff University , City, University of London , Conservatoire for Dance and Drama , 
                    Courtauld Institute of Art , Coventry University , Cranfield University , De Montfort University , Edge Hill University , 
                    Edinburgh Napier University , Falmouth University , Glasgow Caledonian University , Glasgow School of Art , 
                    Glyndŵr University , Goldsmiths College , Gower College Swansea , Grŵp Llandrillo Menai , Grŵp NPTC Group , 
                    Guildhall School of Music and Drama , Harper Adams University , Hartpury University , Heriot-Watt University , 
                    Imperial College of Science, Technology and Medicine , Keele University , King's College London , Kingston University ,
                    Leeds Arts University , Leeds Beckett University , Leeds College of Music , Leeds Trinity University , 
                    Liverpool Hope University , Liverpool John Moores University , Liverpool School of Tropical Medicine , 
                    London Business School , London Metropolitan University , London School of Economics and Political Science , 
                    London School of Hygiene and Tropical Medicine , London South Bank University , Loughborough University , 
                    Middlesex University , Newcastle University , Newman University , Norwich University of the Arts , Oxford Brookes University
                    , Plymouth College of Art , Queen Margaret University Edinburgh , Queen Mary University of London ,
                    Queen's University Belfast , Ravensbourne University London , Roehampton University , 
                    Rose Bruford College of Theatre and Performance , Royal Academy of Music , Royal Agricultural University , 
                    Royal College of Art , Royal College of Music , Royal Conservatoire of Scotland , Royal Holloway and Bedford New College , 
                    Royal Northern College of Music , Sheffield Hallam University , SOAS University of London , Solent University , SRUC , 
                    St George's, University of London , St Mary's University College , St Mary's University, Twickenham , Staffordshire University , 
                    Stranmillis University College , Swansea University , Teesside University , The Arts University Bournemouth , 
                    The Institute of Cancer Research , The Liverpool Institute for Performing Arts , The Manchester Metropolitan University ,
                    The National Film and Television School , The Nottingham Trent University , The Open University , 
                    The Robert Gordon University , The Royal Central School of Speech and Drama , The Royal Veterinary College ,
                    The University College of Osteopathy , The University of Aberdeen , The University of Bath , The University of Birmingham ,
                    The University of Bolton , The University of Bradford , The University of Brighton , The University of Bristol , 
                    The University of Buckingham , The University of Cambridge , The University of Central Lancashire ,
                    The University of Chichester , The University of Dundee , The University of East Anglia , The University of East London , 
                    The University of Edinburgh , The University of Essex , The University of Exeter , The University of Glasgow , 
                    The University of Greenwich , The University of Huddersfield , The University of Hull , The University of Kent ,
                    The University of Lancaster , The University of Leeds , The University of Leicester , The University of Lincoln ,
                    The University of Liverpool , The University of Manchester , The University of Northampton , The University of Oxford , 
                    The University of Portsmouth , The University of Reading , The University of Salford , The University of Sheffield , 
                    The University of Southampton , The University of St Andrews , The University of Stirling , The University of Strathclyde , 
                    The University of Sunderland , The University of Surrey , The University of Sussex , The University of the West of Scotland ,
                    The University of Wales, The University of Warwick , The University of West London , The University of Westminster , 
                    The University of Winchester , The University of Wolverhampton , The University of York , 
                    Trinity Laban Conservatoire of Music and Dance , Ulster University , University College Birmingham , 
                    University College London , University for the Creative Arts , University of Bedfordshire , University of Chester ,
                    University of Cumbria , University of Derby , University of Durham , University of Gloucestershire , 
                    University of Hertfordshire , University of London (Institutes and activities) , University of Northumbria at Newcastle ,
                    University of Nottingham , University of Plymouth , University of South Wales , University of St Mark and St John ,
                    University of Suffolk , University of the Arts, London , University of the Highlands and Islands ,
                    University of the West of England, Bristol , University of Wales Trinity Saint David , University of Worcester ,
                    Writtle University College , York St John University , AA School of Architecture , ABI College  , Access to Music  , 
                    ACM Guildford  , Academy of Live and Recorded Arts , Amity Global Education , Apex College London , Arden University , 
                    Arts Educational Schools , BIMM  , Bristol Baptist College , Bloomsbury Institute , BPP University , Brit College , 
                    Trinity College Bristol , UK Business College  , UK College of Business and Computing , London College of Business Sciences ,
                    London College of Business Studies , Cambridge Arts and Sciences  , The Cambridge Theological Federation ,
                    Chicken Shed Theatre Company , The College of Integrated Chinese Medicine , Christie's Education  , 
                    Christ the Redeemer College , The City College , Cliff College , Court Theatre Training Company  , 
                    The Queen's Foundation for Ecumenical Theological Education , Empire College London  , 
                    University College of Estate Management , Fairfield School of Business  , Met Film School  , 
                    ForMission  , Futureworks , GSM London , ICON College of Technology and Management , 
                    London College of International Business Studies  , Institute of Contemporary Music Performance , 
                    The Islamic College , Kaplan Open Learning , Kensington College of Business , KLC School of Design ,
                    Kogan Academy of Dramatic Arts , LCCM AU UK  , London Bridge Business Academy , London Churchill College  , 
                    City and Guilds of London Art School , London School of Commerce &amp; IT  , The London College UCK , 
                    London School of Academics  , London School of Management Education , London School of Theology , 
                    Stratford College London  , London Studio Centre , The London School of Architecture , 
                    The London Institute of Banking &amp; Finance , The Film Education Training Trust  , Luther King House Educational Trust ,
                    Istituto Marangoni  , The Markfield Institute of Higher Education , Matrix College of Counselling and Psychotherapy  , 
                    Mattersey Hall , St Mellitus College , The Metanoia Institute , Millennium Performing Arts  , The Minster Centre , 
                    Mountview Academy of Theatre Arts , Mont Rose College of Management and Sciences , Moorlands College , 
                    All Nations Christian College , Nazarene Theological College , Nelson College London  , Newbold College , 
                    New College of the Humanities , St Nicholas Montessori Training  , Norland College , Northern College of Acupuncture , 
                    Oak Hill College , ICOM , Oxford Business College , St Patrick's International College , Pearson College , 
                    Point Blank Music School , Royal Academy of Dance , Richmond, The American International University in London ,
                    Regent's University London , Regents Theological College , Regent College , SAE Education  , The Salvation Army, 
                    London School of Science and Technology, Spurgeon's College, The University of Law , Waltham International College  ,
                    Waverley Abbey College , West Dean College , West London College of Business and Management Sciences  , Ballet West Scotland"""

    universities_list, running_string = [], ''
    for i in range(len(universities)):
        if universities[i] == ',':
                universities_list.append(running_string)
                running_string = ''
        elif universities[i-1] == ',':
            pass
        else: 
            running_string += universities[i]


    ideal_student = ['oliver.s.graham@durham.ac.uk', 'aD<Dy5G4#y', 'Oliver', 'Samuel', 'Graham', 'oliver.graham103@gmail.com', '07477887862', '13/08/2000',
                    'Bachelors', 'Physics', 'Physics', 'Durham', 'No', '06/22', '1st', "","","","","","","","","","","",
                    "","","",'St Marys School', 'England', 'State', '09/16', '06/18', 'A Level', 'Physics', 'A*',
                    'A Level', 'Maths', 'A*', 'A Level', 'Chemistry', 'A*', "", "","",
                    'St Marys School', 'England', 'State', 'GCSE', 'Physics', 'A*', 'GCSE', 'Chemistry','A', 'GCSE','Biology', 'B',
                    'GCSE', 'RE', 'C', 'GCSE', 'Maths', 'D','GCSE', 
                    'English Lit', 'E', 'GCSE','English Languge', 'F','GCSE', 'Geography', 'U','GCSE',  'History', 'A*','GCSE',  'Further Maths', 'A*', 'GCSE', 'French', 'A',
                    "", "", "", "", "","","","",'Internship', 'Madeup Company', 'Data Analyst', '07/19', '09/19', False, 'I made this up',
                    "","","","","","","", 'French', 'Basic', 'Really bad getting this to 100 characters', "","","",
                    'Python', 'Intermediate', 'I\'m making this right now', "","","","","","","","","",'github.com', "", 
                    'Banking and Finance', 'Technology','Data Analyst', 'No', 'Yes', 'No', 'White Irish', 'Male', 
                     'Heterosexual', 'Atheist', '', '3', "", "", "Github", "Portfolio"]
    for i in range(length):
        total_list += [ideal_student]
    randomlist = random.sample(range(10, 30), 5)
    alphabet ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.'
    alphabet_with_symbols = alphabet + ',?@/\!-_+=()[]&*%$\'<>#'
    letter_list, letter_symbol_list = [], []
    for letter in alphabet:
        letter_list.append(letter)
    for letter in alphabet_with_symbols:
        letter_symbol_list.append(letter)
    letter_space_list = letter_symbol_list + [' ']
    def random_string(length, symbols = False, space = False):
        return_string = ''
        if symbols == False:
            random_list = random.sample(range(53), length)
            for number in random_list:
                return_string += letter_list[number]
        elif symbols ==True:
            random_list = random.sample(range(75), length)
            for number in random_list:
                return_string += letter_symbol_list[number]
        if space == True:
            random_list = random.sample(range(76), length)
            for number in random_list:
                return_string += letter_space_list[number]
        return return_string

        #iterating over students
        #final return is going to be each student with a list of all 97 properties
        #plan to generate 10 different instances of each column, so 10 emails and change only that column from ideal student list
        #suffix shouldn't matter as long as end in 'ac.uk' so need mix of emails that have number letters and '.'s
    months = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    degree_level = ['Bachelors', 'Masters', 'Post Doctorate', 'Further Technical Degree']
    degree_subjects = ["Accounting & Finance", "Aeronautical & Manufacturing Engineering", "Agriculture & Forestry", 
                "American Studies", "Anatomy & Physiology", "Anthropology", "Archaeology", "Architecture", 
                "Art & Design", "Aural & Oral Sciences", "Biological Sciences", "Building", "Business & Management Studies", 
                "Celtic Studies", "Chemical Engineering", "Chemistry", "Civil Engineering", "Classics & Ancient History", 
                "Communication & Media Studies", "Complementary Medicine", "Computer Science", "Creative Writing",
                "Dentistry", "Drama, Dance & Cinematics", "East & South Asian Studies", "Economics", "Education", 
                "Electrical & Electronic Engineering", "English", "Food Science", "Forensic Science", "French", 
                "General Engineering", "Geography ", "Environmental Science", "Geology", "German", "History", 
                "History of Art, Architecture & Design", "Hospitality, Leisure, Recreation & Tourism", 
                "Iberian Languages", "Italian", "Land & Property Management", "Law","Liberal arts", 
                "Librarianship & Information Management", "Linguistics", "Marketing", "Materials Technology", 
                "Mathematics", "Mechanical Engineering", "Medical Technology", "Medicine", "Middle Eastern & African Studies", 
                "Music","Natural Sciences", "Nursing", "Occupational Therapy", "Optometry, Ophthalmology & Orthoptics",
                "Pharmacology & Pharmacy", "Philosophy", "Physics & Astronomy", "Physiotherapy", "Politics", "Psychology", 
                "Russian & East European Languages", "Social sciences","Social Policy", "Social Work", "Sociology", 
                "Sports Science", "Theology & Religious Studies", "Town & Country Planning and Landscape Design", 
                "Veterinary Medicine"]
    results = ['1st', '2:1', '2:2', '3rd', 'pass', 'distinction', 'merit']
    years_of_study = ['1', '2', '3','4','5','6']
    a_level_institution_type = ['selective state school', 'non-selective state school', 'private']
    countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", 
                 "Australia", "Austria", "Azerbaijan", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize",
                 "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", 
                 "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic", 
                 "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Congo (Democratic Republic)", "Costa Rica", 
                 "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", 
                 "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", 
                 "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Georgia", "Germany", "Ghana", "Greece", "Grenada", 
                 "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", 
                 "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", 
                 "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", 
                 "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives",
                 "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
                 "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", 
                 "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", 
                 "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", 
                 "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Samoa", "San Marino", "Sao Tome and Principe", 
                 "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", 
                 "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", 
                 "St Kitts and Nevis", "St Lucia", "St Vincent", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", 
                 "Tajikistan", "Tanzania", "Thailand", "The Bahamas", "The Gambia", "Togo", "Tonga", "Trinidad and Tobago", 
                 "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", 
                 "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
    a_level_type = ["A Level", "AS Level", "AP", "SAT Subject", "SAT Main", "ACT", "Abitur", 
                    "Indian Higher Secondary School Certificate", "European Baccalaureate", "Irish Leaving Certificate", 
                    "Scottish Highers", "Australian GAC", "Cambridge Pre U", "HKDSE", "BTEC", "VWO", "French Baccalaureate", 
                    "Extended Project Qualification"]
    subjects = ['Physics', 'Computer Science', 'English Literature', 'History', 'Geography', 'Chemistry', 'Biology',
               'RE', 'English Language', 'Art', 'Drama', 'DT']
    a_level_subjects = ["Accounting", "Art and Design", "Bengali", "Biology", "Business", "Classical Civilisation", 
                        "Classical Greek", "Chemistry", "Chinese (Mandarin)", "Citizenship Studies", "Computer Science and IT",
                        "Dance", "Design and Technology", "Drama", "Economics", "Engineering", "English", 
                        "Entertainment Technology", "Environmental Sciences", "Film", "Food", "French", "Further Mathematics",
                        "Geography", "German", "Gujarati", "Hebrew (Biblical)", "Hebrew (Modern)", "History", "History of Art",
                        "ICT", "Italian", "Languages", "Latin", "Law", "Mathematics", "Media Studies", "Music", "Panjabi", 
                        "Performing Arts", "Persion", "Philosophy", "Physical Education", "Physics", "Polish", "Politics", 
                        "Portuguese", "Psychology", "Religious Studies", "Sociology", "Spanish", "Statistics", "Turkish", 
                        "Urdu", "General"]
    a_level_grades = ["A*", "A", "B", "C", "D", "E", "1", "2", "3", "4", "5", "6", "7", "Pass", "Merit", 
                      "Distinction", "First Division", "Second Division", "Third Division", "D1", "D2", "D3",
                      "M1", "M2", "M3", "P1", "P2", "P3"]
    gcse_grade = ["A*", "A", "B", "C", "D", "E", "U", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Pass", 
                  "Merit", "Distinction"]
    gcse_subjects = ["Accounting", "Art and Design", "Astronomy", "Bengali", "Biology", "Business", "Classical Civilisation",
                     "Classical Greek", "Chemistry", "Chinese (Mandarin)", "Citizenship Studies", "Computer Science and IT",
                     "Dance", "Design and Technology", "Drama", "Economics", "Engineering",
                     "English", "Entertainment Technology", "Environmental Sciences", "Film", "Food", "French",
                     "Further Mathematics", "Geography", "German", "Gujarati", "Hebrew (Biblical)", "Hebrew (Modern)",
                     "History", "History of Art", "ICT", "Italian", "Languages", "Latin", "Law", "Mathematics", 
                     "Media Studies", "Music", "Panjabi", "Performing Arts", "Persion", "Philosophy", "Physical Education", 
                     "Physics", "Polish", "Politics", "Portuguese", "Psychology", "Religious Studies", "Science - Core", 
                     "Science - Additional", "Sociology", "Spanish", "Statistics", "Turkish", "Urdu"]
    gcse_type = ["GCSE", "iGCSE", "Free-standing Maths Qualification", "Level 2 Diploma", "Other Level 2 Qualification"]
    we_type = ["Internship", "Virtual Internship", "Unpaid Work Experience", "Part-time Job", "Full-time Job", "Freelance/Gig Work"]
    #we_role = ['Data Analyst', 'Engineer', 'Doctor', 'Teacher', 'Tutor']
    yes_no = ['yes', 'no']
    languages = ["Acholi", "Afrikaans", "Akan", "Albanian", "Amharic", "Arabic", "Ashante", "Asl", 
                 "Assyrian", "Azerbaijani", "Azeri", "Bajuni", "Basque", "Behdini", "Belorussian", 
                 "Bengali", "Berber", "Bosnian", "Bravanese", "Bulgarian", "Burmese", "Cakchiquel", "Cambodian", 
                 "Cantonese", "Catalan", "Chaldean", "Chamorro", "Chao-chow", "Chavacano", "Chin", "Chuukese", "Cree", 
                 "Croatian", "Czech", "Dakota", "Danish", "Dari", "Dinka", "Diula", "Dutch", "Edo", "English", "Estonian", 
                 "Ewe", "Fante", "Farsi", "Fijian Hindi", "Finnish", "Flemish", "French", "French Canadian", "Fukienese", 
                 "Fula", "Fulani", "Fuzhou", "Ga", "Gaddang", "Irish Gaelic", "Scottish Gaelic", "Georgian", "German",
                 "Gorani", "Greek", "Gujarati", "Haitian Creole", "Hakka", "Hausa", "Hebrew", "Hindi", "Hmong", "Hungarian",
                 "Ibanag", "Icelandic", "Igbo", "Ilocano", "Indonesian", "Inuktitut", "Italian", "Jakartanese", "Japanese", 
                 "Javanese", "Kanjobal", "Karen", "Karenni", "Kashmiri", "Kazakh", "Kikuyu", "Kinyarwanda", "Kirundi", 
                 "Korean", "Kosovan", "Kotokoli", "Krio", "Kurdish", "Kurmanji", "Kyrgyz", "Lakota", "Laotian", "Latvian", 
                 "Lingala", "Lithuanian", "Luganda", "Luo", "Maay", "Macedonian", "Malay", "Malayalam", "Maltese", "Mandarin", 
                 "Mandingo", "Mandinka", "Marathi", "Marshallese", "Mien", "Mina", "Mirpuri", "Mixteco", "Moldavan", 
                 "Mongolian", "Montenegrin", "Navajo", "Neapolitan", "Nepali", "Nigerian Pidgin", "Norwegian", "Oromo", 
                 "Pahari", "Papago", "Papiamento", "Pashto", "Patois", "Pidgin English", "Polish", "Portug.creole", 
                 "Portuguese", "Pothwari", "Pulaar", "Punjabi", "Putian", "Quichua", "Romanian", "Russian", "Samoan", 
                 "Serbian", "Shanghainese", "Shona", "Sichuan", "Sicilian", "Sinhalese", "Slovak", "Somali", "Sorani",
                 "Spanish", "Sudanese Arabic", "Sundanese", "Susu", "Swahili", "Swedish", "Sylhetti", "Tagalog", "Taiwanese",
                 "Tajik", "Tamil", "Telugu", "Thai", "Tibetan", "Tigre", "Tigrinya", "Toishanese", "Tongan", "Toucouleur", 
                 "Trique", "Tshiluba", "Turkish", "Twi", "Ukrainian", "Urdu", "Uyghur", "Uzbek", "Vietnamese", "Visayan", 
                 "Welsh", "Wolof", "Yiddish", "Yoruba", "Yupik"]
    language_prof = ["Elementary","Intermediate","Full Working Proficiency", "Native/Bilingual"]
    proficiency = ['Advanced', 'Intermediate', 'Beginner']
    skills = ['Python', 'Java', 'Critical Thinking', 'Data Analysis', 'Market Research', 'Administration', 
              'Business Analysis', 'Bloomberg Terminal', 'Business Development', 'Business Intelligence', 
              'Business Management', 'Business Storytelling', 'Communication', 'Adobe Photoshop', 'Adobe Lightroom', 
              'American Sign Language', 'British Sign Language', 'Presentation', 'Writing', 'Active Listening', 
              'Information Technology (IT)', 'Content Management', 'Data Presentation', 'Middleware and Integration Software', 
              'Mobile Development', 'Network and Information Security', 'Enterprise Architecture', 
              'Geographical Imaging Software', 'Windows CMD', 'Bash', 'C', 'C++', 'Visual Basic ', 
              'Visual Basic .Net', 'Perl', 'Ruby', 'Object Pascal', 'JavaScript', 'C#', 'PHP', 'Objective – C', 
              'SQL', 'Node JS', 'Matlab', 'Go', 'R', 'HTML', 'CSS', 'Assembly Language', 'Rust', 'MQL4', 'Sas', 
              'C Shell', 'Power Shell', 'Hack', 'Kotlin', 'XML', 'Idl', 'Standard ML', 'Swift', 'Docker', 'Scala', 
              'Kubernetes', 'Sklearn', 'Data scraping', 'Android', 'Tech Support', 'UI/UX', 'Solution Architecture',
              'Web Architecture and Development Framework', 'Management', 'Coaching', 'Leadership', 'Negotiation', 
              'Project Management', 'Salesforce', 'Strategic Planning', 'Marketing', 'Content Strategy', 'Digital Media',
              'Market Research', 'Media Planning', 'Online Marketing', 'Public Relations', 'Social Media', 'Adaptability',
              'Analytical Reasoning', 'Natural Language Processing', 'Machine Learning', 'PyTorch', 'Keras', 'TensorFlow',
              'Amazon Web Services', 'Google Cloud Platform', 'Microsoft Azure', 'Collaboration', 'People Management', 
              'Time Management', 'SalesForce', 'Mobile Application Development', 'Translation', 'Video Production', 
              'Adobe Premiere', 'CyberLink Power Director', 'Final Cut', 'Corporate Communications', 'Industrial Design',
              'Competitive Strategies', 'Digital Marketing', 'Animation', 'Sales Leadership', 'Software Testing',
              'Customer Service Systems', 'Graphic Design', 'Adobe After Effects', 'Database Administration', 'Tableau', 
              'PowerBI']
    link_types = ["Portfolio_website", "Github", "Linkedin","Other"]

    industries = ["Academia", "Agriculture", "Architecture", "Art", "Banking & Finance", "Consulting",
                  "Professional Services", "Marketing", "Media ", "HR", "Consumer & Retail", "Automotive & Transport", 
                  "Charity & Public Sector", "Education", "Energy", "Engineering & Industrial", "Hospitality", 
                  "Insurance", "Law ", "Pharmaceutical ", "Property & Construction", "Supply Chain and Logistics", 
                  "Other Sectors"]
    macro_roles = ['Technology', 'Doctor', 'Developer', 'Teacher']
    roles = ['Administrative - General', 'Accounting - General', 'Accounting - Audit', 'Accounting - Tax', 
                   'Accounting - Advisory', 'Engineering - General', 'Engineering - Design', 'Engineering - Aerospace', 
                   'Engineering - Geophysical', 'Engineering - Electrical', 'Engineering - Hardware', 'Engineering - Civil',
                   'Engineering - Chemical', 'Engineering - Environmental', 'Engineering - Mechanical', 
                   'Financial Analyst - General', 'Financial Analyst - Risk', 'Financial Analyst - Compliance',
                   'Financial Analyst - Business Analyst', 'Commercial Banking - General', 
                   'Commercial Banking - Corporate Banking', 'Commercial Banking - Client Management', 
                   'Investment Banking - General', 'Investment Banking - Mergers and Acquisitions', 
                   'Investment Banking - Quantitative Research', 'Investment Banking - Markets', 
                   'Investment Banking - Asset Management', 'Investment Banking - Wealth Management', 
                   'Investment Banking - Sales', 'Marketing - General', 'Software Engineering - General',
                   'Software Engineering - Backend', 'Software Engineering - Frontend', 'Software Engineering - Full Stack',
                   'Software Engineering - DevOps', 'Software Engineering - UI/UX', 
                   'Data Science and Analytics - Machine Learning', 'Data Science and Analytics - Forensic Analytics ',
                   'Data Science and Analytics - General', 'Consulting and Strategy - General', 'Customer Service - General',
                   'Insurance and Actuarial - General', 'Operations - General', 'Research and Development - General',
                   'Teaching - General', 'Language and Translation - General', 'Technology - General',
                   'Technology - Network Engineering', 'Technology - Cyber Security', 'Product Design - General',
                   'Other - Other', 'Law - General']
    ethnic_group = ["White - British", "White - Irish", "White - Gypsy", "Any Other White Background", 
                    "White and Black Carribean", "White and Black African", "White and Asian", 
                    "Any Other Mixed/Multiple Ethnic Background","Asian - Indian", "Asian - Pakistani", 
                    "Asian - Bangladeshi", "Asian - Chinese", "Any Other Asian Background", "Black - African",
                    "Black - Carribean", "Any Other Black/African/Carribean Background", "Arab", "Other Ethnicity",
                    "Prefer not to Say"]
    gender = ["Male", "Female", "Non-Binary", "Other", "Prefer not to say"]
    sexual_orientation = ['Heterosexual', 'Homosexual', 'Bisexual', 'Asexual', 'Other', 'Prefer not to say']
    religion = ["Atheist", "Christian", "Muslim", "Hindu", "Sikh", "Buddhist", "Jewish", "Jain", "Bahai", "Other"]
    # First row, up to degree education randomised , change number range on a to change number of rows changed  
    # for i in range(length):
    #     total_list += [ideal_student]
    for a in range(1,length):
        length = random.randint(12,20)
        string = random_string(length, True)
        
        total_list[a][1] = string
        string = '07' + str(random.randint(100000000,999999999))
        total_list[a][6] = string
        day = random.randint(1,32)
        if day < 10:
            day = str(day)
            day = '0' + day
        day = str(day)
        month = months[random.randint(0,11)]
        string = str(day)+ '/' + month + '/' + str(random.randint(1990, 2004))
        total_list[a][7] = string
        length = random.randint(10,20)
        string = random_string(length)
        prefix_length = random.randint(3,10)
        prefix = random_string(prefix_length)
        string += '@' + prefix + '.ac.uk'
        total_list[a][0] = string
        prefix_length = random.randint(3,10)
        prefix = random_string(prefix_length)
        string += '@' + prefix + '.co.uk'
        total_list[a][5] = string
        for i in range(3):
            string = random_string(random.randint(6,15))
            total_list[a][i+2] = string
            if i == 1:
                if random.randint(1,2) == 1:
                    total_list[a][i+2] = ""


        # Uni section - degree level Bachelor's, Master's etc - degree title random string - field of study pick of subjects - 
        # university random from list - completed yes/no - graduation date - result choice of 1st, 21, 22, 3rd
        for i in range(3):
            idx = random.randint(0,2)
            change = degree_level[idx]
            total_list[a][(8 + 7*i)] = change
            #degree title
            length = random.randint(10,50)
            change = random_string(length, True, True)
            total_list[a][(9 + 7*i)] = change
            #degree subject
            idx = random.randint(0,len(subjects)-1)
            change = degree_subjects[idx]
            total_list[a][(10 + 7*i)] = change
            #university
            idx = random.randint(0,len(universities_list)-1)
            change = universities_list[idx]
            total_list[a][(11+7*i)] = change
            #finished?
            if random.randint(0,1) == 1:
                change = 'yes'
            else:
                change = 'no'
            total_list[a][(12+7*i)] = change
            #year of study
            if total_list[a][(12+7*i)] == "yes":
                total_list[a][135+i] = "n_a"
            else:
                total_list[a][135+i] = years_of_study[random.randint(0,len(years_of_study)-1)]
            #graduation day
            month = months[random.randint(0,11)]
            year = str(random.randint(2018, 2026))
            change = month + '/' + year
            total_list[a][(13 + 7*i)] = change
            #result
            idx = random.randint(0,len(results)-1)
            change = results[idx]
            total_list[a][14 + 7*i] = change
            #Accounting for people with one degree
            if i ==1 and random.randint(1,6) == 4:
                for j in range(7):
                    total_list[a][15+j] = ""
            if i ==2 and random.randint(1,2) == 2:
                for j in range(7):
                    total_list[a][22+j] = ""


       # A level and GCSE education start questions before results
        total_list[a][29] = random_string(random.randint(7,20))
        total_list[a][30] = countries[random.randint(0,len(countries)-1)]
        total_list[a][31] = a_level_institution_type[random.randint(0, len(a_level_institution_type)-1)]
        for k in range(32,34):
            year, month = random.randint(2011,2020), months[random.randint(0,11)]
            year, month = str(year), str(month)
            date = month + '/' + year
            total_list[a][k] = date
        total_list[a][46] = random_string(random.randint(7,20))
        total_list[a][47] = countries[random.randint(0,len(countries)-1)]
        total_list[a][48] = a_level_institution_type[random.randint(0, len(a_level_institution_type)-1)]
        #A level results
        for i in range(34,46,3):
            total_list[a][i] = a_level_type[random.randint(0, len(a_level_type)-1)]
            total_list[a][i+1] = a_level_subjects[random.randint(0,len(a_level_subjects)-1)]
            total_list[a][i+2] = a_level_grades[random.randint(0,len(a_level_grades)-1)]
            if i ==43 and random.randint(0,1) == 1:
                total_list[a][43] = ""
                total_list[a][44] = ""
                total_list[a][45] = ""
        for i in range(49,91,3):
            total_list[a][i] = gcse_type[random.randint(0,len(gcse_type)-1)]
            total_list[a][i+1] = gcse_subjects[random.randint(0,len(gcse_subjects)-1)]
            total_list[a][i+2] = gcse_grade[random.randint(0,len(gcse_grade)-1)]

        #Work experience
        for i in range(2):
            #type
            total_list[a][91 + 7*i] = we_type[random.randint(0,len(we_type)-1)]
            #company
            total_list[a][92 + 7*i] = random_string(random.randint(5,20))
            #role
            total_list[a][93 + 7*i] = random_string(random.randint(5,20))
            #total_list[a][93+ 7*i] = we_role[random.randint(0,4)]
            #start and end dates
            month, year = months[random.randint(0,11)], random.randint(2011, 2020)
            month2, year2 = months[random.randint(0,11)], random.randint(2011, 2020)
            if year > year2:
                total_list[a][94 + 7*i] = month2 + '/' + str(year2)
                total_list[a][95 + 7*i] = month + '/' + str(year)
            elif year2 > year:
                total_list[a][94 + 7*i] = month + '/' + str(year)
                total_list[a][95 + 7*i] = month2 + '/' + str(year2)
            else:
                if month2 > month:
                    total_list[a][94 + 7*i] = month + '/' + str(year)
                    total_list[a][95 + 7*i] = month2 + '/' + str(year2)
                else:
                    total_list[a][94 + 7*i] = month + '/' + str(year)
                    total_list[a][95 + 7*i] = month2 + '/' +str(year2)

            total_list[a][96 + 7*i] = 'yes'
            total_list[a][97 + 7*i] = random_string(random.randint(10,50), False, True)
        #Languages
            total_list[a][105 + 3*i] = languages[random.randint(0,len(languages)-1)]
            total_list[a][106 + 3*i] = language_prof[random.randint(0,len(language_prof)-1)]
            total_list[a][107 + 3*i] = random_string(random.randint(10,50), False, True)
            status = random.randint(0,2)
            if status == 1:
                for j in range(105,111):
                    total_list[a][j] = ""
            elif status == 2:
                for j in range(108,111):
                    total_list[a][j] = ""

        #Skills
        for i in range(4):
            total_list[a][111 + 3*i] = skills[random.randint(0,len(skills)-1)]
            total_list[a][112 + 3*i] = proficiency[random.randint(0,2)]
            total_list[a][113 + 3*i] = random_string(random.randint(10,50))
        for s in range(111+3*random.randint(0,4),123):
            total_list[a][s] = ""

        #Links starts with www or https:/ then random string with at least 1 '.'
        for i in range(2):
            link = 'www.' + random_string(random.randint(10,20)) + '.co.uk'
            total_list[a][123+i] = link
            total_list[a][138+i] = link_types[random.randint(0,len(link_types)-1)]

        #Industries
        no_of_industries = random.randint(0,5)
        industries_interested = []
        for i in range(no_of_industries):
            industries_interested.append(industries[random.randint(0,len(industries)-1)])
        total_list[a][125] = industries_interested
        #roles
#         no_of_macro = random.randint(0,4)
#         macro_interested = []
#         for i in range(no_of_macro):
#             macro_interested.append(macro_roles[random.randint(0,3)])
#         total_list[a][126] = macro_interested
        no_of_micro = random.randint(0,len(roles))
        micro_interested = []
        for i in range(no_of_micro):
            micro_interested.append(roles[random.randint(0,len(roles)-1)])
        total_list[a][127] = micro_interested
        if random.randint(0,1) == 1:
            total_list[a][128] = 'yes'
        else:
            total_list[a][128] = 'no'
        if random.randint(0,1) == 1:
            total_list[a][129] = 'yes'
        else:
            total_list[a][129] = 'no'
        if random.randint(0,1) == 1:
            total_list[a][130] = 'yes'
        else:
            total_list[a][130] = 'no'

        #ethnic group
        total_list[a][131] = ethnic_group[random.randint(0,len(ethnic_group)-1)]
        #gender
        total_list[a][132] = gender[random.randint(0,len(gender)-1)]
        #sex orientation
        total_list[a][133] = sexual_orientation[random.randint(0,len(sexual_orientation)-1)]
        #religion
        total_list[a][134] = religion[random.randint(0,len(religion)-1)]
    return total_list
    
        
        
           
       

total_list = create_list(10)
print(len(total_list))
for i in range(len(total_list)):
    total_list[i] = total_list[i][:126] + total_list[i][127:]
# total_list[0] = total_list[0][:12] + ["graduation_month_1", "graduation_year_1"] + total_list[0][14:20] + ["graduation_month_2", "graduation_year_2"]+ total_list[0][21:27] + ["graduation_month_3", "graduation_year_3"] + total_list[0][28:32] + ["a_level_start_month", "a_level_start_year", "a_level_end_month", "a_level_end_year"]  + total_list[0][34:94] + ["we_start_month_1", "we_start_year_1", "we_end_month_1", "we_end_year_1"] + total_list[0][96:102] + ["we_start_month_2", "we_start_year_2", "we_end_month_2", "we_end_year_2"] + total_list[0][104:]
total_dict = [total_list[0]]
for a in range(len(total_list)-1, 0, -1):
    student_dict = {}
    #Reverse through the elements so the indexing isn't messed up
    for i in range(len(total_list[a])-1, 0, -1):
        if type(total_list[a][i]) == str:
            total_list[a][i] = total_list[a][i].strip()
#         #Changing degree dates to month and year separately
#         if i == 13:
#             for j in range(len(total_list[a][i])):
#                 if total_list[a][i][j] == "/":
#                     month = total_list[a][i][:j]
#                     year = total_list[a][i][j+1:]
#             total_list[a][i] = total_list[a][:13] + [month, year] + total_list[a][14:]
#         if i == 20 and type(total_list[a][i]) == str :
#             for j in range(len(total_list[a][i])):
#                 if total_list[a][i][j] == "/":
#                     month = total_list[a][i][:j]
#                     year = total_list[a][i][j+1:]
#             total_list[a][i] = total_list[a][:20] + [month, year] + total_list[a][21:]
#         if i == 27 and type(total_list[a][i]) == str:
#             for j in range(len(total_list[a][i])):
#                 if total_list[a][i][j] == "/":
#                     month = total_list[a][i][:j]
#                     year = total_list[a][i][j+1:]
#             total_list[a][i] = total_list[a][:27] + [month, year] + total_list[a][28:]
#         if i == 32:
#             print(total_list[a][i])
#             for j in range(len(total_list[a][i])):
#                 if total_list[a][i][j] == "/":
#                     month_1 = total_list[a][i][:j]
#                     year_1 = total_list[a][i][j+1:]
#             for j in range(len(total_list[a][i+1])):
#                 if total_list[a][i+1][j] == "/":
#                     month_2 = total_list[a][i+1][:j]
#                     year_2 = total_list[a][i+1][j+1:]
#             total_list[a][i+1] = total_list[a][:32] + [month_1, year_1, month_2, year_2] + total_list[a][34:]
        student_dict[total_list[0][i]] = total_list[a][i]
    total_dict.append(student_dict)
for a in range(2, len(total_dict)):
    #print(a)
    for j in range(len(total_dict[a]["alevel_start"])):
        if total_dict[a]["alevel_start"][j] == "/":
                month_1 = total_dict[a]["alevel_start"][:j]
                year_1 = total_dict[a]["alevel_start"][j+1:]
    for j in range(len(total_dict[a]["alevel_end"])):
        if total_dict[a]["alevel_end"][j] == "/":
                month_2 = total_dict[a]["alevel_end"][:j]
                year_2 = total_dict[a]["alevel_end"][j+1:]
    total_dict[a]["a_level_start_month"] = month_1
    total_dict[a]["a_level_start_year"] = year_1
    total_dict[a]["a_level_end_month"] = month_2
    total_dict[a]["a_level_end_year"] = year_2
    
    #Looping thorugh all of the graduation dates (3)
    for p in range(1,4):
        if total_dict[a]["graduation" + str(p)] == "":
            continue
        for j in range(len(total_dict[a]["graduation"+str(p)])):
            if total_dict[a]["graduation"+str(p)][j] == "/":
                    month_1 = total_dict[a]["graduation"+str(p)][:j]
                    year_1 = total_dict[a]["graduation"+str(p)][j+1:]
        total_dict[a]["graduation_month"+str(p)] = month_1
        total_dict[a]["graduation_year"+str(p)] = year_1
    
    #Looping through all of the wes (2)
    for p in range(1,3):
        if total_dict[a]["we" + str(p)+"_start_date"] == "":
            continue
        for j in range(len(total_dict[a]["we" + str(p)+"_start_date"])):
            if total_dict[a]["we" + str(p)+"_start_date"][j] == "/":
                    month_1 = total_dict[a]["we" + str(p)+"_start_date"][:j]
                    year_1 = total_dict[a]["we" + str(p)+"_start_date"][j+1:]
        total_dict[a]["we" + str(p)+"_start_month"] = month_1
        total_dict[a]["we" + str(p)+"_start_year"] = year_1
        
        for j in range(len(total_dict[a]["we" + str(p)+"_end_date"])):
            if total_dict[a]["we" + str(p)+"_end_date"][j] == "/":
                    month_1 = total_dict[a]["we" + str(p)+"_end_date"][:j]
                    year_1 = total_dict[a]["we" + str(p)+"_end_date"][j+1:]
        total_dict[a]["we" + str(p)+"_end_month"] = month_1
        total_dict[a]["we" + str(p)+"_end_year"] = year_1
        
total_dict.pop(0)
print(total_dict[0])