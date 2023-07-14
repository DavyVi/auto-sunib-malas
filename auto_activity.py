import requests
import traceback
import pandas as pd

data = pd.read_csv("logbook.csv", dtype = 'string', keep_default_na = False)
ssourl = "https://activity-enrichment.apps.binus.ac.id/Auth/SSOStudentLogin?token=XXXX&strm=XXXX" # get your own token
base_url = "https://activity-enrichment.apps.binus.ac.id/LogBook"

logbook_id_mapping = {}
session = requests.session()
session.get(ssourl)

def get_months():
	try:
		response = session.get(base_url + "/GetMonths")
		raw_month_mapping = response.json()

		if response.status_code != 200:
			raise Exception(f"{response.text}")

		for month in raw_month_mapping['data']:
			logbook_id_mapping.update({
				f"{month['monthInt']:02d}" : f"{month['logBookHeaderID']}"
			})
	except Exception:
		exception_message = traceback.format_exc()
		print(f"Failed to get logbook ID. Reason: {exception_message}")

def send_request(date, clock_in, clock_out, activity, description):
	try:
		payload = {
			'model[ID]': "00000000-0000-0000-0000-000000000000",
			'model[LogBookHeaderID]': logbook_id_mapping[date[5:7]],
			'model[Date]': f"{date}T00:00:00",
			'model[Activity]': activity,
			'model[ClockIn]': clock_in,
			'model[ClockOut]': clock_out,
			'model[Description]': description
		}
		response = session.post(base_url + "/StudentSave", data = payload)
		print(f"{date}: {response.text}")
	except Exception:
		exception_message = traceback.format_exc()
		print(f"{date}: {exception_message}")
		
def main():
	get_months()

	for key, log in data.iterrows():
		if log['activity'] == "":
			continue
		elif log['activity'] == "OFF":
			send_request(str(log['date']), "OFF", "OFF", "OFF", "OFF")
		else:
			send_request(str(log['date']), "09:00 am", "06:00 pm", log['activity'], log['description'])

if __name__ == '__main__':
	main()
