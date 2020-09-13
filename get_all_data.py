import json
import pymysql
from utilities import rds
import logging
import sys
# import aws_creds
# import boto3
from datetime import datetime

def get_data(student_id):
    #try:
    # db connection
    try:
        conn = rds.connect("read")
        if conn == None:
            return {"statusCode":500, "error_code": 1, "body":"Internal server error"}
        cur = conn.cursor()
    except:
        return {"statusCode":500, "error_code": 1, "body":"Internal server error"}

    try:
        personal_SQL ="""SELECT first_name, middle_name, last_name, contact_email, phone_number, dob,
        alevel_institution, alevel_country_id, 
        gcse_institution, gcse_country_id,
        hex, visa_sponsorship, allowed_to_work_in_uk, alevel_institution_type, alevel_start_month, alevel_start_year, alevel_end_month, alevel_end_year,
        gcse_institution_type, free_school_meals, parents_higher_education, disability, ethnic_group, gender sexual_orientation, religion
        FROM student_personal_data
        WHERE student_id = %s;"""
        cur.execute(personal_SQL, student_id)
        info = cur.fetchall()[0]
        info_sorted = list(info)

        #Check that middle name exists
        if info_sorted[1] == None:
            info_sorted[1] = ""
        personal_data_json = {"first_name": info_sorted[0], "middle_name": info_sorted[1], "last_name": info_sorted[2], "contact_email": info_sorted[3], "phone_number": info_sorted[4], "dob": datetime.strftime(info_sorted[5], "%d/%m/%Y")}
        a_level_inst, a_level_country_id =  info_sorted[6], info_sorted[7]
        gcse_inst, gcse_country_id = info_sorted[8], info_sorted[9]
        student_hex, visa, allowed_to_work =  info_sorted[10], info_sorted[11], info_sorted[12]
        a_level_inst_type, start_month, start_year, end_month, end_year = info_sorted[13], info_sorted[14], info_sorted[15], info_sorted[16], info_sorted[17]
        gcse_inst_type= info_sorted[18]
        free_school_meals, parents_higher_education, disability, ethnic_group = info_sorted[19], info_sorted[20], info_sorted[21], info_sorted[22]
        gender, sexual_orientation, religion = info_sorted[23], info_sorted[24], info_sorted[25]

        #Statement for university education
        uni_SQL = """SELECT level, title, university_id, completed, year_of_study, graduation_month, graduation_year, grade, field_of_study_id
        FROM student_degrees
        WHERE student_id = %s;"""
        cur.execute(uni_SQL, student_id)
        uni_info = list(cur.fetchall())
        uni_id_to_name = """SELECT university_name 
        FROM universities
        WHERE university_id = %s"""
        
        select_field = "SELECT field_name FROM fields_of_study WHERE field_of_study_id = %s;"
        unis, fields = [], []
        for i in range(len(uni_info)):
            cur.execute(uni_id_to_name, uni_info[i][2])
            uni_name = list(cur.fetchall())[i][0]
            if uni_name != None:
                unis.append(uni_name)
            cur.execute(select_field, uni_info[i][8])
            field = list(cur.fetchall())[i][0]
            if field != None:
                fields.append(field)
        
        unis_json = []
        for i in range(len(uni_info)):
            uni_info[i] = list(uni_info[i])
            # if uni_info[i][3] == "yes":
            #     uni_info[i][4] = "Completed"
            unis_json.append({ 
                                    "field_of_study": fields[i],
                                    "degree_level": uni_info[i][0].capitalize(),
                                    "degree_name": uni_info[i][1],
                                    "university": unis[i],
                                    "year_of_study": uni_info[i][4],
                                    "grade": uni_info[i][7],
                                    "graduation_month":uni_info[i][5].title(),
                                    "graduation_year":uni_info[i][6],
                                    "completed": uni_info[i][3]})

        print("here1")
        #Statement for A_levels
        country_id_to_name = """SELECT country_name
        FROM countries_list
        WHERE country_id = %s"""
        cur.execute(country_id_to_name, a_level_country_id)
        a_level_country = cur.fetchone()[0]

        a_level_sql = """SELECT alev.grade ,alevel_subject_name, alevel_type_name
                        FROM student_alevels alev LEFT OUTER JOIN a_level_subjects als on alev.alevel_subject_id = als.alevel_subject_id
                        LEFT OUTER JOIN a_level_types alt on alev.alevel_type_id = alt.alevel_type_id
                        WHERE student_id = %s;"""
        cur.execute(a_level_sql,student_id)
        a_level_info = list(cur.fetchall())

        a_level_json = {"institution_name": a_level_inst,
                         "country": a_level_country,
                         "institution_type": a_level_inst_type,
                         "start_month": start_month,
                         "start_year": start_year,
                         "end_month": end_month,
                         "end_year": end_year,
                         "grades": []}
        for a_level in a_level_info:
            a_level_json["grades"].append({"qualification_type": a_level[2],
                                            "subject": a_level[1],
                                            "grade": a_level[0]})

        #Statement for GCSEs
        gcse_SQL = """SELECT gcs.grade , gcse_subject_name, gcs.type
                        FROM student_gcses gcs LEFT OUTER JOIN gcse_subjects gcses on gcs.gcse_subject_id = gcses.gcse_subject_id
                        WHERE student_id = %s;"""

        cur.execute(country_id_to_name, gcse_country_id)
        gcse_country = cur.fetchone()[0]

        #Statement for gcses
        cur.execute(country_id_to_name, gcse_country_id)
        gcse_country = cur.fetchone()[0]

        cur.execute(gcse_SQL,student_id)
        gcse_info = list(cur.fetchall())
        gcse_json = {   "institution_name": gcse_inst, "institution_country": gcse_country, "institution_type": gcse_inst_type,
                        "grades": []}
        for i in range(len(gcse_info)):
            gcse_json["grades"].append({"qualification_type": gcse_info[i][2],
                                        "subject": gcse_info[i][1],
                                        "grade": gcse_info[i][0].upper()})
        
        print("here2")
        #Statement for we
        we_SQL = """SELECT type, company, role, location, start_date, end_date, description
        FROM student_we
        WHERE student_id = %s;"""
        cur.execute(we_SQL,student_id)
        we_info = cur.fetchall()
        we_json = []
        for we in we_info:
            we_json.append({"type": we[0],
                            "organisation_name": we[1],
                            "role": we[2],
                            "location": we[3],
                            "start_date": datetime.strftime(we[4], "%d/%m/%Y"),
                            "end_date": datetime.strftime(we[5], "%d/%m/%Y"),
                            "description": we[6]})
        #Statement for languages
        languages_SQL = """SELECT language_name, lang.proficiency, lang.description
                        FROM student_languages lang LEFT OUTER JOIN languages la on lang.language_id = la.language_id
                        WHERE student_id = %s;"""
        cur.execute(languages_SQL,student_id)
        language_info = list(cur.fetchall())

        language_json = []
        for i in range(len(language_info)):
            language_json.append({  "language_name": language_info[i][0],
                                    "proficiency": language_info[i][1],
                                    "description": language_info[i][2]})
        
        #Statement for skills
        skills_SQL = """SELECT skill_name, skill.proficiency, skill.description
                        FROM student_skills skill LEFT OUTER JOIN skills ski on skill.skill_id = ski.skill_id
                        WHERE student_id = %s;"""
        cur.execute(skills_SQL,student_id)
        skill_info = list(cur.fetchall())

        skill_json = []
        for i in range(len(skill_info)):
            skill_json.append({  "skill_name": skill_info[i][0],
                                    "proficiency": skill_info[i][1],
                                    "description": skill_info[i][2]})
        
        #Statement for files

        #files_SQL = """SELECT file_type, file_url, file_name
        #FROM student_documents
        #WHERE student_id = %s;"""
        #cur.execute(files_SQL,student_id)
        #files_info = cur.fetchall()

        # client = boto3.client('s3', aws_access_key_id=aws_creds.AWS_ACCESS_KEY,
        #                       aws_secret_access_key=aws_creds.AWS_SECRET_KEY)

        # file_types = ['cv','certificates','other','statement_of_marks','portfolio']
        # files_json = []

        # for file_type in file_types:
        #     response = client.list_objects(Bucket=aws_creds.BUCKET_NAME, Prefix=str(student_id)+'/'+file_type)
    
        #     content = response.get('Contents', [])

        #     if len(content)>1:
        #         for file in content[1:]:
        #             s3_filename = file['Key']
        #             print(s3_filename)
        #             s3_signed_url = client.generate_presigned_url('get_object',
        #                                                         Params={'Bucket': aws_creds.BUCKET_NAME,
        #                                                                 'Key': s3_filename})

        #         files_json.append({"document_type": file_type, "URL": s3_signed_url, "document_name": s3_filename})
        #Statement for links
        links_SQL = """SELECT link_type, link_url
        FROM student_links
        WHERE student_id = %s;"""
        cur.execute(links_SQL, student_id)
        links_info = cur.fetchall()
        link_json = []
        for link in links_info:
            link_json.append({"link_type": link[0], "URL":link[1]})



        #Statement for industries
        industry_SQL = """SELECT industry_name
                        FROM student_industries studind LEFT OUTER JOIN industries ind on studind.industry_id = ind.industry_id
                        WHERE student_id = %s;"""
        cur.execute(industry_SQL,student_id)
        industry_info = list(cur.fetchall())
        industry_names = []
        for i in range(len(industry_info)):
            if industry_info[i][0] == None:
                continue
            else:
                industry_names.append(industry_info[i][0])

        #Statement for roles
        role_SQL = """SELECT role_name
                        FROM student_roles studrol LEFT OUTER JOIN roles role on studrol.role_id = role.role_id
                        WHERE student_id = %s;"""
        cur.execute(role_SQL,student_id)
        role_info = list(cur.fetchall())
        role_names = []
        for i in range(len(role_info)):
            if role_info[i][0] == None:
                continue
            else:
                role_names.append(role_info[i][0])

        return_JSON = {"hex": student_hex,
                        "personal_info": personal_data_json,
                        "degree_name": unis_json[-1]["degree_name"],
                        "university": unis_json[-1]["university"],
                        "year_of_study": unis_json[-1]["year_of_study"],
                        "test_taken": "false", # to do: sql to check if test taken yet
                        "test_score": "n_a", # to do: sql to get test score if test_taken = true
                        "has_cv": "false", # to do: sql to check then get link
                        "roles": role_names,
                        "past_education" : {"degrees": unis_json,
                                            "a_levels" : a_level_json,
                                            "gcses": gcse_json},
                       "skills": skill_json,
                        "experience": we_json,
                        "languages": language_json,
                        "links" : link_json,
                        "industries" : industry_names,
                        "diversity": {"free_school_meals": free_school_meals, "parents_higher_education": parents_higher_education, "disability": disability,
                        "ethnic_group": ethnic_group, "gender": gender, "sexual_orientation": sexual_orientation, "religion": religion},
                        "visa" : visa,
                        "allowed_to_work" : allowed_to_work}
        
        # return_JSON["statusCode"] = 200
        # return_JSON["headers"] = {"Access-Control-Allow-Origin": "*"}
        return return_JSON
    
    except Exception as err:
        print(err)
        return {"statusCode": 400, "body": "Internal error", "error_code": 1}
