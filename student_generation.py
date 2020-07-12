import random
import numpy as np
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
           'student_link1', 'student_link2', 'industries_intersted', 'macro_roles', 'micro_roles', 'school_meals?', 
           'parents_education?', 'disability?', 'ethinic_group', 'gender', 'sexual_orientation', 'religion']]

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
                'Bachelors', 'Physics', 'Physics', 'Durham', 'No', '06/22', '1st', None,None,None,None,None,None,None,None,None,None,None,
                None,None,None,'St Marys School', 'England', 'State', '09/16', '06/18', 'A Level', 'Physics', 'A*',
                'A Level', 'Maths', 'A*', 'A Level', 'Chemistry', 'A*', None, None,None,
                'St Marys School', 'England', 'State', 'GCSE', 'Physics', 'A*', 'GCSE', 'Chemistry','A', 'GCSE','Biology', 'B',
                'GCSE', 'RE', 'C', 'GCSE', 'Maths', 'D','GCSE', 
                'English Lit', 'E', 'GCSE','English Languge', 'F','GCSE', 'Geography', 'U','GCSE',  'History', 'A*','GCSE',  'Further Maths', 'A^', 'GCSE', 'French', 'A',
                None, None, None, None, None,None,None,None,'Internship', 'Madeup Company', 'Data Analyst', '07/19', '09/19', False, 'I made this up',
                None,None,None,None,None,None,None, 'French', 'Basic', 'Really bad getting this to 100 characters', None,None,None,
                'Python', 'Intermediate', 'I\'m making this right now', None,None,None,None,None,None,None,None,None,'github.com', None, 
                'Banking and Finance', 'Technology','Data Analyst', 'No', 'Yes', 'No', 'White Irish', 'Male', 
                 'Heterosexual', 'Atheist']
for i in range(1000):
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
degree_level = ['Bachelors', 'Masters', 'Post Doctorate']
subjects = ['Physics', 'Computer Science', 'Maths', 'English', 'Drama', 'Geography']
results = ['1st', '2:1', '2:2', '3rd']
a_level_institution_type = ['State', 'Grammar', 'Private']
a_level_grade = ['A*', 'A','B','C','D','E','F','U']
a_level_countries = ['England', 'Wales', 'Scotland', 'Northern Ireland']
a_level_type = ['A Level', 'BTEC', 'Scottish Highers', 'International Baccalaureate']
subjects = ['Physics', 'Computer Science', 'English Literature', 'History', 'Geography', 'Chemistry', 'Biology',
           'RE', 'English Language', 'Art', 'Drama', 'DT']
gcse_grade = ['1','2','3','4','5','6','7','8','9','A*', 'A','B','C','D','E','F','U']
gcse_type = ['Higher', 'Foundation']
we_type = ['Internship', 'Summer Job', 'Virtual Internship', 'Work Experience']
we_role = ['Data Analyst', 'Engineer', 'Doctor', 'Teacher', 'Tutor']
yes_no = ['Yes', 'No']
languages = ['French', 'Mandarin', 'Spanish', 'German', 'Japan', 'Italian', 'Latin', 'Polish']
proficiency = ['Advanced', 'Intermediate', 'Beginner']
skills = ['Python', 'Java', 'HTML', 'Excel', 'Word', 'CrItIcAl ThInKiNg']
industries = ['Banking and Finance', 'Medical', 'Education', 'Academia', 'Education', 'Consultancy']
macro_roles = ['Technology', 'Doctor', 'Developer', 'Teacher']
micro_roles = ['Front End Developer', 'Anaesthetist', 'Back End Developer', 'Supply Teacher']
ethnic_group = ['White British', 'Black British', 'Indian', 'Pakistani', 'Chinese']
gender = ['Male', 'Female', 'Other', 'Prefer not to say']
sexual_orientation = ['Heterosexual', 'Homosexual', 'Bisexual', 'Asexual', 'Other', 'Prefer not to say']
religion = ['Atheist', 'Christian', 'Muslim', 'Hindi', 'Buddist', 'Jewish', 'Agnostic']

# First row, up to degree education randomised , change number range on a to change number of rows changed  
for a in range(1,50):
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
    month = random.randint(1,13)
    if month<10:
        month = str(month)
        month = '0' + month
    month = str(month)
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
                total_list[a][i+2] = None
    

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
        change = subjects[idx]
        total_list[a][(10 + 7*i)] = change
        #university
        idx = random.randint(0,len(universities_list)-1)
        change = universities_list[idx]
        total_list[a][(11+7*i)] = change
        #finished?
        if random.randint(0,1) == 1:
            change = 'Yes'
        else:
            change = 'No'
        total_list[a][(12+7*i)] = change
        #graduation day
        month = random.randint(0,13)
        if month < 10:
            month = str(month)
            month = '0' + month
        month = str(month)
        year = str(random.randint(2000, 2030))
        change = month + '/' + year
        total_list[a][(13 + 7*i)] = change
        #result
        idx = random.randint(0,3)
        change = results[idx]
        total_list[a][14 + 7*i] = change
        #Accounting for people with one degree
        if i ==1 and random.randint(1,6) == 4:
            for j in range(7):
                total_list[a][15+j] = [None]
        if i ==2 and random.randint(1,2) == 2:
            for j in range(7):
                total_list[a][22+j]
            
    
   # A level and GCSE education start questions before results
    total_list[a][29] = random_string(random.randint(7,20))
    total_list[a][30] = a_level_countries[random.randint(0,3)]
    total_list[a][31] = a_level_institution_type[random.randint(0,2)]
    for k in range(32,34):
        year, month = random.randint(2000,2020), random.randint(1,12)
        if month < 10:
            month =str(month)
            month = '0' + month
        year, month = str(year), str(month)
        date = month + '/' + year
        total_list[a][k] = date
    total_list[a][46] = random_string(random.randint(7,20))
    total_list[a][47] = a_level_countries[random.randint(0,3)]
    total_list[a][48] = a_level_institution_type[random.randint(0,2)]
    #A level results
    for i in range(34,46,3):
        total_list[a][i] = a_level_type[random.randint(0,3)]
        total_list[a][i+1] = subjects[random.randint(0,11)]
        total_list[a][i+2] = a_level_grade[random.randint(0,7)]
        if i ==43 and random.randint(0,1) == 1:
            total_list[a][43] = None
            total_list[a][44] = None
            total_list[a][45] = None
    for i in range(49,91,3):
        total_list[a][i] = gcse_type[random.randint(0,1)]
        total_list[a][i+1] = subjects[random.randint(0,11)]
        total_list[a][i+2] = gcse_grade[random.randint(0,16)]
    
    #Work experience
    for i in range(2):
        total_list[a][91 + 7*i] = we_type[random.randint(0,3)]
        total_list[a][92 + 7*i] = random_string(random.randint(5,20))
        total_list[a][93+ 7*i] = we_role[random.randint(0,4)]
        month, year = random.randint(1,12), random.randint(1990, 2020)
        month2, year2 = random.randint(1,12), random.randint(1990, 2020)
        if month < 10:
            month = str(month)
            month = '0' + month
        year, month = str(year), str(month)
        if month2 < 10:
            month2 = str(month2)
            month2 = '0' + month2
        year2, month2 = str(year2), str(month2)
        if year > year2:
            total_list[a][94 + 7*i] = month2 + '/' + year2
            total_list[a][95 + 7*i] = month + '/' + year
        elif year2 > year:
            total_list[a][94 + 7*i] = month + '/' + year
            total_list[a][95 + 7*i] = month2 + '/' + year2
        else:
            if month2 > month:
                total_list[a][94 + 7*i] = month + '/' + year
                total_list[a][95 + 7*i] = month2 + '/' + year2
            else:
                total_list[a][94 + 7*i] = month + '/' + year
                total_list[a][95 + 7*i] = month2 + '/' + year2

        total_list[a][96 + 7*i] = 'Yes'
        total_list[a][97 + 7*i] = random_string(random.randint(10,50), False, True)
    #Languages
        total_list[a][105 + 3*i] = languages[random.randint(0,7)]
        total_list[a][106 + 3*i] = proficiency[random.randint(0,2)]
        total_list[a][107 + 3*i] = random_string(random.randint(10,50), False, True)
        status = random.randint(0,2)
        if status == 1:
            for j in range(105,111):
                total_list[a][j] = None
        elif status == 2:
            for j in range(108,111):
                total_list[a][j] = None
        
    #Skills
    for i in range(4):
        total_list[a][111 + 3*i] = skills[random.randint(0,5)]
        total_list[a][112 + 3*i] = proficiency[random.randint(0,2)]
        total_list[a][113 + 3*i] = random_string(random.randint(10,50))
    for s in range(111+3*random.randint(0,4),123):
        total_list[a][s] = None
        
    #Links starts with www or https:/ then random string with at least 1 '.'
    for i in range(2):
        link = 'www.' + random_string(random.randint(10,20)) + '.co.uk'
        total_list[a][123+i] = link
    
    #Industries
    no_of_industries = random.randint(0,5)
    industries_interested = []
    for i in range(no_of_industries):
        industries_interested.append(industries[random.randint(0,5)])
    total_list[a][125] = industries_interested
    #roles
    no_of_macro = random.randint(0,4)
    macro_interested = []
    for i in range(no_of_macro):
        macro_interested.append(macro_roles[random.randint(0,3)])
    total_list[a][126] = macro_interested
    no_of_micro = random.randint(0,4)
    micro_interested = []
    for i in range(no_of_micro):
        micro_interested.append(micro_roles[random.randint(0,3)])
    total_list[a][127] = micro_interested
    if random.randint(0,1) == 1:
        total_list[a][128] = 'Yes'
    else:
        total_list[a][128] = 'No'
    if random.randint(0,1) == 1:
        total_list[a][129] = 'Yes'
    else:
        total_list[a][129] = 'No'
    if random.randint(0,1) == 1:
        total_list[a][130] = 'Yes'
    else:
        total_list[a][130] = 'No'
    
    #ethnic group
    total_list[a][131] = ethnic_group[random.randint(0,3)]
    #gender
    total_list[a][132] = gender[random.randint(0,3)]
    #sex orientation
    total_list[a][133] = sexual_orientation[random.randint(0,5)]
    #religion
    total_list[a].append(religion[random.randint(0,6)])
        
        
        
        
        
        
        
        
       
#testing print statements:       
print(total_list[0][123])        
for i in range(100,135):
    print(total_list[0][i],':', total_list[1][i])