import urllib.request, json, tkinter, tkinter.font  #인터넷 요청, 데이터 처리, GUI 화면, 글꼴 설정을 하기위해 불러옴 
 
API_KEY = "Enter your API key here"   #API 키를 저장하는 변수        
 
def tick1Min():     #1분마다 온도 습도를 갱신하는 함수 정의 
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric"    #서울의 날씨 데이터를 요청하는 URL 생성 
    with urllib.request.urlopen(url) as r:     #위 링크로 요청을 보내고, 응답을 받음 
        data = json.loads(r.read())     #데이터를 파이썬 딕셔너리로 변환  
    temp = data["main"]["temp"]         #json 데이터에서 온도 값만 꺼냄 
    humi = data["main"]["humidity"]     #json 데이터에서 습도 값만 꺼냄 
    label.config(text=f"{temp:.1f}C   {humi}%")   #화면에 온도는 소수점 1자리까지 표시 
    window.after(60000, tick1Min)    #1분 후 함수 재실행 
 
window = tkinter.Tk()   #창 생성 
window.title("TEMP HUMI DISPLAY")   #창 제목 설정 
window.geometry("400x100")     #창 크기 설정  
window.resizable(False, False)   #창 크기 고정 
font = tkinter.font.Font(size=30)   #글자 크기 30으로 설정 
label = tkinter.Label(window, text="", font=font)   #텍스트를 표시할 라벨 생성 
label.pack()   #라벨을 창에 배치 
tick1Min()     #시작할 때 처음 한 번 데이터를 가져오기 실행  
window.mainloop()  #창 유지 
