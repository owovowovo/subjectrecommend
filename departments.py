# 학과 선택 파일

# 학과 딕셔너리
department = {'문예창작과' : '고전문학 감상, 화법과 작문, 현대문학 감상, 영미 문학 읽기, 생활과 윤리, 미술사, 철학, 심리학',
    '웹툰일러스트학과' : '디자인 일반, 미술사, 미술 전공 실기, 심리학, 연극',
    '체육교육과' : '생활과 윤리, 생활과 과학, 체육 전공 실기 기초, 단체 운동, 체육 전공 실기 심화, 기술가정, 보건, 심리학',
    '광고 디자인 / 홍보학과' : '디자인 일반, 미술사, 미술 전공 실기, 미술 창작, 심리학',
    '마케팅학과' : '경제 수학, 확률과 통계, 경제, 사회문화, 사회문제 탐구, 심리학',
    '약학과' : '확률과 통계, 미적분, 기하, 수학과제 탐구, 생명과학1, 물리학1, 화학1, 화학2, 생명과학2, 과학과제 연구, 가정과학, 보건, 심리학, 기술가정',
    '항공운항학과' : '영어 회화, 세계지리, 사회문화, 한국지리, 여행지리, 국제 관계와 국제기구, 지구과학1, 환경, 보건',
    '수학과' : '확률과 통계, 수학과제 탐구, 미적분, 기하, 경제, 과학과제 연구',
    '산업인테리어디자인학과' : '생활과 과학, 가정과학, 디자인 일반, 미술 전공 실기, 미술 창작, 미술사, 기술가정, 심리학',
    '뷰티미용과' : '가정과학, 미술창작, 미술사, 미술 전공 실기, 기술가정',
    '국제관계학과' : ' 경제 수학, 한국지리, 정치와 법, 경제, 세계지리, 동아시아사, 사회문화, 사회문제 탐구, 국제 관계와 국제기구, 심리학',
    '컴퓨터공학과' : '확률과 통계, 미적분, 기하, 인공지능 기초, 인공지능 수학, 물리학1, 물리학2, 과학과제 연구, 정보',
    '가정교육과' : '사회문화, 생활과 과학, 기술가정, 가정과학, 교육학, 환경, 보건, 심리학',
    '사회복지학과' : '경제, 여행지리, 사회문제 탐구, 사회문화, 생활과 과학, 단체 운동, 심리학, 기술가정',
    '경찰학과' : '정치와 법, 한국지리, 사회 문화, 생활과 윤리, 사회문제 탐구, 단체 운동, 체육 전공 실기 기초, 체육 전공 실기 심화, 보건, 심리학, 교육학',
    '식품영양학과' : '확률과 통계, 인공지능 수학, 생명과학1, 화학1, 화학2, 과학과제 연구, 정보',
    '생명과학과' : '미적분, 생명과학1, 생명과학2, 화학1, 화학2, 과학과제 연구, 가정과학, 보건',
    '유아교육학과' : '교육학, 심리학',
    '무역학과' : '경제 수학, 진로 영어, 경제, 한국지리, 정치와 법, 세계지리, 사회문제 탐구',
    '물리치료학과' : '생명과학1, 생명과학2, 물리학1, 물리학2, 화학1, 단체 운동, 보건',
    '작곡과' : '음악 전공 실기, 공연 실습, 음악 연주, 음악사, 심리학',
    '사진영상학과' : '사회문화, 정보, 심리학',
    '행정학과' : '사회문화, 사회문제 탐구, 정치와 법, 교육학, 기술가정, 가정과학',
    '토목공학과' : '미적분, 기하, 생명과학1, 지구과학1, 지구과학2, 물리학1, 물리학2, 생활과 과학, 과학과제 연구',
    '사회복지학과' : '사회문화, 여행지리, 사회문제 탐구, 기술가정, 심리학',
    '패션의류학과' : '사회문화, 화학1, 미술 창작, 디자인 일반, 미술사,  심리학, 가정과학',
    '건축학과' : '미적분, 사회문제 탐구, 물리학1, 물리학2, 지구과학1, 지구과학2, 과학과제 연구, 디자인 일반, 미술 창작, 미술 전공 실기, 기술가정',
    '방송영상학과' : '사회 문화, 사회문제 탐구, 공연 실습',
    '식품공학과' : '생명과학1, 생명과학2, 화학1, 화학2, 과학과제 연구, 환경, 심리학, 정보',
    '미디어 학과' : '사회문제 탐구, 정보, 심리학',
    '응용생명과학부' : '미적분, 생명과학1, 생명과학2, 화학1, 화학2,  과학과제 연구',
    '전자공학과' : '미적분, 기하, 인공지능 기초, 물리학1, 물리학2, 화학1, 화학2, 과학과제 연구, 정보',
    '기계공학부' : '미적분, 기하, 물리학1, 물리학2, 화학1, 화학2, 지구과학1, 지구과학2, 환경',
    '생명공학과' : '인공지능 기초, 생명과학1, 화학1, 화학2, 과학과제 연구',
    '반도체공학과' : '인공지능 기초, 수학과제 탐구, 인공지능 수학, 물리학1, 물리학2, 화학1, 화학2, 생명과학1, 과학과제 연구, 정보',
    '심리학과' : '사회문제 탐구, 생명과학1, 생활과 과학, 보건, 심리학',
    '요리학과' : '여행지리, 기술 가정, 환경, 보건',
    '독어독문학과' : '독일어 독해와 작문1, 독일어 회화1, 독일어권 문화',
    '의예과' : '수학과제 탐구, 생명과학1, 생명과학2, 화학1, 화학2, 과학과제 연구, 보건, 정보',
    '패션디자인학과' : '디자인 일반, 미술사, 미술 창작, 미술 전공 실기',
    '의공학과' : '인공지능 기초, 생명과학1, 생명과학2, 지구과학1, 물리학1, 물리학2, 화학1, 과학과제 연구, 보건, 정보',
    '천문학과' : '미적분, 기하, 수학과제 연구, 세계사, 지구과학1, 지구과학2, 물리학1, 물리학2, 과학과제 연구, 정보',
    '사회학과' : '경제 수학, 사회문화, 사회문제 탐구',
    '영어영문학과' : '언어와 매체, 현대문학 감상, 영어 회화, 영미 문학 읽기',
    '불어불문학과' : '화법과 작문, 사회문제 탐구, 프랑스어 회화1, 프랑스어권 문화',
    '국어교육학과' : '화법과 작문, 언어와 매체, 심화 국어, 사회문제 탐구, 심리학, 교육학',
    '영화영상전공학과' : '현대문학 감상, 고전문학 감상, 사회문제 탐구, 연극',
    '로봇공학과' : '확률과 통계, 물리학1, 물리학2, 인공지능 기초, 정보',
    '경제학과' : '경제 수학, 경제, 사회문화, 사회문제 탐구',
    '법학과' : '정치와 법, 사회문화, 사회문제 탐구, 철학',
    '경호학과' : '단체 운동, 체육 전공 실기 기초, 체육 전공 실기 심화',
    '군사학과' : '단체 운동, 체육 전공 실기 기초, 체육 전공 실기 심화',
    '소방행정학과' : '가정과학, 보건, 심리학, 체육 전공 실기 심화, 단체 운동, 체육 전공 실기 기초',
    '빅데이터응용통계학과' : '확률과 통계, 미적분, 인공지능 수학, 수학과제탐구, 정보',
    '피아노학과' : '공연 실습, 음악 연주, 음악사, 음악 전공 실기',
    '연극영화학과' : '공연 실습, 연극, 음악 연주, 음악사, 음악 전공 실기',
    '물리학과' : '물리학1, 물리학2, 과학과제 연구',
    '교육학과' : '사회문제 탐구, 교육학, 심리학, 철학',
    '경영학과' : '경제, 사회문제 탐구',
    '에너지 공학과' : '지구과학1, 물리학1, 물리학2, 화학1, 화학2, 과학과제 연구',
    '영어교육과' : '진로 영어, 영미 문학 읽기, 영어 회화, 사회문제 탐구, 교육학',
    '유전생명공학과' : '생명과학1, 생명과학2, 화학1, 화학2, 과학과제 연구, 환경',
    '시각디자인학과' : '디자인 일반, 미술 창작, 미술사, 미술 전공 실기',
    '식품영양학과' : '생명과학1, 화학1, 화학2, 과학과제 연구',
    '관광학과' : '진로 영어, 한국지리, 세계지리',
    '뮤지컬과' :  '공연 실습, 연극, 음악사, 음악 전공 실기',
    '보건의료정보학과' : '생명과학1, 생명과학2, 화학1, 화학2, 과학과제 연구, 보건',
    '초등교육학과' : '사회문제 탐구, 생활과 과학, 교육학, 심리학',
    '간호학과' : '생명과학1, 생명과학2, 화학1, 화학2, 보건',
    '신학과' : '윤리와 사상, 사회문화, 사회문제 탐구, 철학, 심리학',
    '화학공학과' : '화학1, 화학2, 과학과제 연구',
    '환경공학과' : '사회문제 탐구, 생활과 과학, 생명과학1, 생명과학2, 화학1, 화학2, 과학과제 연구, 환경',
    '역사학과' : '세계사, 동아시아사, 고전과 윤리, 사회문제 탐구',
    '스포츠과학과' : '생활과 과학, 가정과학, 체육 전공 실기 기초, 단체 운동, 체육 전공 실기 심화',
    '스포츠건강관리학과' : '확률과 통계, 생명과학1, 가정과학, 체육 전공 실기 기초, 체육 전공 실기 심화, 단체 운동, 보건, 심리학',
    '문헌정보학과' : '확률과 통계, 윤리와 사상, 여행지리, 정치와 법, 고전과 윤리, 생활과 과학',
    '동물자원과학과' : '미적분, 기하, 지구과학1, 생명과학1, 생명과학2, 화학1, 화학2, 과학과제 연구, 인공지능 기초, 환경'
    }