import tkinter
import customtkinter

root= customtkinter.CTk()
root.geometry('900x560')
root.configure(bg_color='#262626')
root.resizable(2,4)
root.title('NXAPI Features')

import requests
import urllib3
import json

host='172.16.1.8'
username=''
password=''

res = nxapi_request(host=host,
                   username=username,
                   password=password,
                   commands=['show vlan brief'],
                   command_type='cli_show')
#res.json()

vlans = res.json()['ins_api']['outputs']['output']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']

#print(vlans)

message1 = ""

for i in vlans:
    message1 += f"Vlan-id:{i['vlanshowbr-vlanid-utf']}" + "\n" + f"Vlan-Name:{i['vlanshowbr-vlanname']}\nVlan-state:{i['vlanshowbr-shutstate']}\n"

    if 'vlanshowplist-ifidx' in i:
        message1 += f"Vlan-interfaces:{i['vlanshowplist-ifidx']}"

    message1 += f"\n{'*'*40}\n\n"

res1 = nxapi_request(host=host,
                   username=username,
                   password=password,
                   commands=['show interface status'],
                   command_type='cli_show')
res1.json()

interfaces = res1.json()['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']

#print(interfaces)

message2 = ""

for i in interfaces:
    message2 += f"interface: {i['interface']}\nstate:{i['state']}\nspeed:{i['speed']}\n{i['type']}\n"
    message2 += f"{'*'*40}\n\n\n"

print(message2)        
 
nxapi_frame = customtkinter.CTkFrame(master=root)
nxapi_frame.pack(pady=20, padx=60, fill="both", expand=True)

nxapi_label = customtkinter.CTkFrame(master=nxapi_frame)
nxapi_label.place(y=10, x=10, width=550, height=750)

nxapi_label = customtkinter.CTkFrame(master=nxapi_frame)
nxapi_label.place(y=10, x=410, width=550, height=750)

nxapi_label1_entry = customtkinter.CTkLabel(master=nxapi_frame, text="show vlan brief")
nxapi_label1_entry.place(y=10, x=20)

nxapi_label1_entry = customtkinter.CTkLabel(master=nxapi_frame, text="show ip int brief")
nxapi_label1_entry.place(y=10, x=420)

customtkinter.set_appearance_mode("dark")

root.mainloop()
