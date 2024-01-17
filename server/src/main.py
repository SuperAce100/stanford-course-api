import os
import re
import requests
import xmltodict
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def split_query(query):
    pattern = r'([A-Za-z]+)(\d+[A-Za-z]*)'
    match = re.match(pattern, query)
    if match:
        subject = match.group(1)
        code = match.group(2)
        return subject, code
    else:
        return None, None

@app.route('/getjson', methods=['GET'])
def get_json():
    query = request.args.get('q', '')
    multi_select = request.args.get('multiple', 'false')
    subject, code = split_query(query)
    print(subject, code)
    url = f"https://explorecourses.stanford.edu/search?view=xml-20140630&filter-coursestatus-Active=on&page=0&catalog=&q={query}"
    response = requests.get(url)
    data_dict = xmltodict.parse(response.content)
    if multi_select == 'false':

        if(isinstance(data_dict["xml"]["courses"]["course"], dict)) :
            return jsonify({"course": [data_dict["xml"]["courses"]["course"]]})
        filtered_courses = []
        for course in data_dict["xml"]["courses"]["course"]:
            if course["subject"] == subject and course["code"] == code:
                filtered_courses.append(course)
        data_dict["xml"]["courses"]["course"] = filtered_courses

    return jsonify(data_dict["xml"]["courses"])

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
