import requests
import pandas as pd

data = pd.read_csv("logbook.csv")
ssourl = "https://activity-enrichment.apps.binus.ac.id/Auth/SSOStudentLogin?token=TODO" # get your own token
url = "https://activity-enrichment.apps.binus.ac.id/LogBook/StudentSave"
logbook_id = "b8e6f0e8-74a3-4974-b2af-4261e7917cd2" # change every month
session = requests.session()
session.get(ssourl)

def send_request(date, clock_in, clock_out, activity, description):
  global session
  try:
    payload = {
      'model[ID]': "00000000-0000-0000-0000-000000000000",
      'model[LogBookHeaderID]': logbook_id,
      'model[Date]': f"{date}T00:00:00",
      'model[Activity]': activity,
      'model[ClockIn]': clock_in,
      'model[ClockOut]': clock_out,
      'model[Description]': description
    }
    response = session.post(url, data = payload)
    print(f"{date}: {response.text}")
  except Exception as e:
    print(e)
    
def main():
  for key, log in data.iterrows():
    if log['activity'] == "null":
      continue
    elif log['activity'] == "OFF":
      send_request(log['date'], "OFF", "OFF", "OFF", "OFF")
    else:
      send_request(log['date'], "09:00 am", "06:00 pm", log['activity'], log['description'])

if __name__ == '__main__':
  main()
