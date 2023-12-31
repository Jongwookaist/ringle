# Ringle-Tutor Scheduler
이 프로그램은 강사의 수업 일정과 학생이 원하는 수업 시간을 고려하여 그 시간대에 가능한 강사를 선택해주는 프로그램입니다. 강사의 스케쥴 Json 파일 및 학생이 원하는 시간을 인자로 받아서 처리합니다.


사용법
프로그램을 실행하기 전에 명령줄 인자로 다음 정보를 입력해야 합니다.
1. Json 파일 이름
2. 수업 시간 길이 (30분 단위)
3. 학생이 수업을 시작할 수 있는 시간
4. 학생이 수업을 종료해야 하는 시간 

샘플 Json file

<img width="80%" src="https://github.com/Jongwookaist/ringle/assets/96780862/e2194307-986a-4ba6-9c36-1903ca9d12dc/">

Json 파일의 경우 강사의 id와 이름이 담긴 "tutors" 와 slot 번호, 강사가 30분 단위로 수업 시작가능한 시간과 tutor id를 저장한 "slots"로 구성되어 있어야 합니다.

결과 출력
이 프로그램은 학생이 원하는 시간대에 강의가 가능한 강사 이름과 강의 시작 시간을 csv 파일 형식으로 출력합니다.
CSV 파일은 다음 형식으로 구성됩니다.

slot id, 시작 시간, 강사 ID, 강사 이름

실행 예시 1

<img width="80%" src="https://github.com/Jongwookaist/ringle/assets/96780862/26ca08b6-937f-4b80-89eb-1d56e72e8ff4/">


결과 CSV 파일

<img width="80%" src="https://github.com/Jongwookaist/ringle/assets/96780862/c8947615-9735-4e67-b17f-6a132125a375/">


실행 예시 2

<img width="80%" src="https://github.com/Jongwookaist/ringle/assets/96780862/d1f512aa-fb19-4c27-ba91-77aba14c6e5a/">

<img width="80%" src="https://github.com/Jongwookaist/ringle/assets/96780862/4aa00d12-a89c-47de-a8d0-5dc23854959f/">

(실행 예시2는 fuzzer을 통해 만든 sample.json 파일을 사용함)


Fuzzer은 프로그램이 잘 실행되는지 확인하기 위한 다른 프로그램으로 시간 범위(start,end) 와 강사 수, 수업 수를 입력하면 각 강사마다 start 와 end 사이에
수업 수 만큼 정보를 가진 sample.json 파일을 만듭니다.

<img width="80%" src="https://github.com/Jongwookaist/ringle/assets/96780862/22467f4c-0518-4184-8c91-2a22f8d66de9/">

위의 예시에서는 3명의 강사가 각각 3번의 수업 시간이 가능한 Json 파일을 만듭니다.

<img width="80%" src="https://github.com/Jongwookaist/ringle/assets/96780862/a45c7412-d3e4-41c6-afd1-712b000c1f60/">


참고 사항

json 파일의 경로는 프로그램의 파일과 같은 디렉토리에 위치해야 하며 tutor.csv 파일은 같은 폴더에 없어야 만들어 집니다.

프로그램을 실행 할 때 제대로 된 인자를 입력하지 않으면 실행되지 않습니다. 인자 개수를 확인해주세요.

fuzzer의 입력값을 줄 때 기간을 길게 설정하고 수업 수가 적으면 수업이 이어진 json 파일이 나올 확률이 낮아집니다.


