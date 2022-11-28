# coding=UTF-8
import sys, json, requests,os;

def resolve_json():
    title_list = []
    
    poemUrl = "https://v2.jinrishici.com/one.json?client=browser-sdk/1.2"
    json_string = requests.get(poemUrl).json()
    print(json_string)
    title = json_string["data"]["origin"]["title"]
    dynasty = json_string["data"]["origin"]["dynasty"]
    author = json_string["data"]["origin"]["author"]
    title_list.append(title)
    title_list.append(dynasty)
    title_list.append(author)
   
    poem_list = json_string["data"]["origin"]["content"]
    translate_list = json_string["data"]["origin"]["translate"]
    
    all_content = ""
    for title in title_list:
        all_content += "\n\t\t" + title
    all_content += "\n"
    for poem in poem_list:
        all_content += "\n\t" + poem

    if translate_list is not None:
        if(len(translate_list) != 0):
            all_content += "\n\n\t" + "解释："
            for translate in translate_list:
                all_content += "\n\t" + translate
    send(all_content)

        

def send(content):
    
    url = os.environ.get("SERVERCHAN_MY_SEND_URL")
    wifeUrl = os.environ.get("SERVERCHAN_WIFE_SEND_URL")
    print(os.environ)
    # jsonData = {"title":"您最爱的老公常先生向您问好❤❤❤：", "desp":content,"channel":1}  # channel=1 企业微信群机器人
    jsonData = {"title":"您最爱的老公常先生向您问好❤❤❤：", "desp":content,"channel":"9"}
    headers = {"content-type":"application/json"}
    requests.post(url, json=jsonData,headers=headers)
    # requests.post(wifeUrl, json=jsonData,headers=headers)
  

if __name__ == "__main__":
    resolve_json()