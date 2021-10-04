# name = " jason Todd"
# print('apple'+ name)
# print("hello \nyou dumbass")
# 串接、擷取公開資料
from flask import Flask  # 載入Flask
from flask  import request #載入Resquest 物件

app = Flask(
    __name__,
    static_folder="static", #靜態檔案的資料夾名稱
    static_url_path="/www"  #靜態檔案對應的網址路徑
)  # 建立Application物件

#建立路徑/getSum對應的處理函式
#利用要求字串(Query String)提供彈性:/getSum?min=最小數字&max=最大數字
@app.route("/getSum")
def getSum():# min+(mini+1)+(min+2)+....+max
    #接受要求字串中的參數資料
    maxNumber= request.args.get("max",100)
    maxNumber=int(maxNumber)
    minNumber= request.args.get("min",1)
    minNumber=int(minNumber)
    #以下運算 min+(mini+1)+(min+2)+....+max 總和的迴圈邏輯
    result=0
    for n in range(minNumber, maxNumber+1):
        result+=n
    #把結果回傳前端
    return "結果:"+str(result)    


# 建立路徑 / 對應的處理函數
@app.route("/")
def index():  # 用來回應路徑 / 的處理函數
    print("請求方法", request .method)
    print("通訊協定",request. scheme)
    print("主機名稱",request.host)
    print("路徑",request.path)
    print("完整的網址",request.url)
    lang=request.headers.get("accept-language") #多語言設定
    if lang.startswith("en"):
        return "Hello Flask"
    else:
        return "哈囉你好"  # 回傳網站首頁的內容


@app.route("/data")
def database():  # 用來回應路徑 / 的處理函數
    return "My data"  # 回傳網站首頁的內容


# 動態路由:建立路徑/user/使用者名稱 對應的處理函數
@app.route("/user/<Lawrence>")
def handleuser(Lawrence):  # 用來回應路徑 / 的處理函數
    if Lawrence == "香蕉":
        return "My name is " + Lawrence  # 回傳網站首頁的內容
    else:
        return "我的名字" + Lawrence


app.run()
