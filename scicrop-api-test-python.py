import requests
import json

if __name__ == '__main__':
	data = {
		"full_name": "Richard Medeiro Turra",
		"email": "stdevelopr@gmail.com",
		"mobile_phone": "+447365954569",
		"age": 36,
		"home_address": "Rua Prudente de Moraes 60 Suzano/SP",
		"start_date": 431395200,
		"opportunity_tag": "python developer",
		"past_jobs_experience": "I graduated on geophysics and developed a python software to model seismic reflection data.\
		I also worked for 1 year in a customer success company as python developer",
		"degrees": [{
			"institution_name": "Sao Paulo University (USP)",
			"degree_name": "Geophysics",
			"begin_date":  1359676800,
			"end_date":  1485907200
		}],
		"programming_skills": ["python", "flask", "javascript", "react", "html", "css", "machine learning"],
		"database_skills": ["mongodb", "postgresql"],
		"hobbies": ["studying", "walking"],
		"why": "I enjoy working with data and geo things.",
		"git_url_repositories": "https://github.com/stdevelopr"
	}
	headers = {
		'Content-type': 'application/json'
	}
	r = requests.post('https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume', data=json.dumps(data), headers=headers)
	print(r.text)
