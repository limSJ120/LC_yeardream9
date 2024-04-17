from datetime import datetime
from gemini import gemini




class Logger:
    def __init__(self):
        
    def logging(self, log_data):
        with open("./" + datetime.today().strftime("%Y%m%d") + "_llm_rag.log", "a") as log: # '20240417_llm_rag.log' 형식으로 append 방식 열기
            log.write(datetime.today().strftime("%Y%m%d %H:%M:%S") + f"{log_data}\n")

    def save_data(self, data):  # data_process.py에서 처리된 데이터를 검증
        try:
            if len(data) > 2:
                self.logging("data_process 작업 완료")   # data_process 정상 실행 시, 출력
            else:
                self.logging("data_process 작업 실패")    # data_process 실행 실패 시, 출력
        except:
            self.logging("data_process 작업 실패")    # data_process 실행 실패 시, 출력

class call_input(gemini):
    def __init__(self, a, b, c):
        super().__init__()








class gemini():
    def _

    def call(a):
        a = input()