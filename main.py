from api.zoom import ZoomAPI
import pandas as pd 
from datetime import datetime
from pathlib import Path
from extractfile import extract_clients

now_date = datetime.today()
Path(f"./bundle/{now_date}").mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':

    clients = extract_clients('./input/clients.csv')
    client_dict = dict()
    client_dict['id'] = []
    client_dict['recording_start'] = []
    client_dict['recording_end'] = []
    client_dict['download_url'] = []
    client_dict['timestamp'] = []
    client_dict['instructor'] = []
    for client in clients:
        zapi = ZoomAPI(client['access_token'], client['from_date'], client['to_date'])
        instructor = client['instructor'].split("@")[0]
        print(f"Generating bundle file for instructor `{instructor}` from {client['from_date']} to {client['to_date']}")
        urls_dict = zapi.get_client_download_urls()
        if urls_dict is None:
            print(f"Ignored {instructor} - An exception occurred")
            continue
        recn = len(urls_dict['id'])
        client_dict['id'].extend(urls_dict['id'])
        client_dict['recording_start'].extend(urls_dict['recording_start'])
        client_dict['recording_end'].extend(urls_dict['recording_end'])
        client_dict['download_url'].extend(urls_dict['download_url'])
        client_dict['timestamp'].extend(urls_dict['timestamp'])
        client_dict['instructor'].extend([instructor]*recn)
    client_df = pd.DataFrame(client_dict)
    client_df.to_csv(f"./bundle/{now_date}/output.csv")
    print("done...")
