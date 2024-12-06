from flask import Blueprint, url_for, render_template, flash, request, redirect, session, g

from train2 import db
from train2.forms import TestForm
from train2.models import Result, User

import json
import subprocess

bp = Blueprint('test', __name__, url_prefix='')

@bp.route('/test/')
def main():
  return render_template('test/testing.html')

@bp.route('/test/result/', methods=['POST'])
def result():
    form = TestForm()
    form_data = request.form.to_dict()  # form 데이터를 딕셔너리로 변환

    # 사용자 설정 가중치
    user = g.user
    category_weight = {
        "economy": 2 if user.economy else 1,
        "welfare": 2 if user.welfare else 1,
        "security": 2 if user.security else 1,
        "environment": 2 if user.environment else 1,
        "political_reform": 2 if user.political_reform else 1,
        "technology": 2 if user.technology else 1,
        "human_rights": 2 if user.human_rights else 1,
        "defense": 2 if user.defense else 1,
        "legislation": 2 if user.legislation else 1
    }

    # C 프로그램에 전달할 데이터 생성
    c_data = {
        "form_data": form_data,
        "category_weights": category_weight
    }
    json_data = json.dumps(c_data)  # JSON 직렬화

    try:
        # C 프로그램 실행
        result = subprocess.run(
            ['C:/Users/yeram/Desktop/training/training2/train2/C_program/my_program'],  # 실행할 C 프로그램 경로
            input=json_data,        # JSON 데이터를 표준 입력으로 전달
            stdout=subprocess.PIPE,  # 표준 출력 캡처
            stderr=subprocess.PIPE,  # 표준 에러 캡처
            text=True,              # 입력과 출력을 텍스트로 처리
            encoding='utf-8',  # UTF-8로 디코딩
            errors='ignore',   # 디코딩 오류 무시
            timeout=10              # 실행 시간 제한 (10초)
        )

        print("C Program Stdout:", result.stdout)
        print("C Program Stderr:", result.stderr)

        # 결과 처리
        if result.returncode == 0:
            try:
                # JSON 출력 파싱
                json_output = json.loads(result.stdout)
            except json.JSONDecodeError:
                json_output = {"error": "C 프로그램에서 반환된 JSON이 유효하지 않습니다."}
        else:
            # C 프로그램 에러 메시지 처리
            json_output = {"error": result.stderr.strip()}
    except subprocess.TimeoutExpired:
        json_output = {"error": "C 프로그램 실행이 시간 초과되었습니다."}
    except Exception as e:
        json_output = {"error": f"예기치 않은 오류 발생: {str(e)}"}

    value_list = [v for k, v in json_output.items()]

    # 리스트 값을 변수로 분리
    economy = value_list[0]
    welfare = value_list[1]
    security = value_list[2]
    environment = value_list[3]
    political_reform = value_list[4]
    technology = value_list[5]
    human_rights = value_list[6]
    defense = value_list[7]
    legislation = value_list[8]
    total = value_list[9]

    db_list = []

    for i in value_list:
        if '50%' in i:
            db_list.append(True)
        if '트럼프'  in i:
            db_list.append(True)
        if '해리스' in i:
            db_list.append(False)


    test_result = Result(
            economy=db_list[0],
            welfare=db_list[1],
            security=db_list[2],
            environment=db_list[3],
            political_reform=db_list[4],
            technology=db_list[5],
            human_rights=db_list[6],
            defense=db_list[7],
            legislation=db_list[8],
            total=db_list[9],
            user_id=g.user.id
        )
    db.session.add(test_result)
    db.session.commit()

    return render_template(
        'test/result.html',
        economy=economy,
        welfare=welfare,
        security=security,
        environment=environment,
        political_reform=political_reform,
        technology=technology,
        human_rights=human_rights,
        defense=defense,
        legislation=legislation,
        total=total
    )
    
    # 카테고리별 초기화
    '''
    economy_count = 0
    welfare_count = 0
    security_count = 0
    environment_count = 0
    political_reform_count = 0
    technology_count = 0
    human_rights_count = 0
    defense_count = 0
    legislation_count = 0

    # 결과 렌더링
    return render_template(
    'test/result.html',
    form_data=form_data,
    category_weight=category_weight,
    c_data=c_data
    )
    '''
