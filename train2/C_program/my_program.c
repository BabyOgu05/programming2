#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <json.h>
#include <math.h>

// 강지민, 김하람, 민경준

// 카테고리 목록 정의
typedef struct {
    const char* name;
    const char** questions;
    size_t size;
    double weight;
    int count;
} Category;

const char* economy_list[] = {"q1", "q2", "q4", "q5", "q10", "q15", "q18", "q24", "q25", "q34", "q35", "q37", "q40", "q53", "q57", "q59"};
const char* welfare_list[] = {"q8", "q19", "q30", "q37", "q42", "q45", "q49", "q50", "q52", "q57"};
const char* security_list[] = {"q4", "q6", "q7", "q11", "q12", "q13", "q15", "q18", "q21", "q22", "q23", "q31", "q38", "q39", "q40", "q41", "q60"};
const char* environment_list[] = {"q3", "q14", "q26", "q33", "q44", "q51", "q58"};
const char* political_reform_list[] = {"q16", "q28", "q29"};
const char* technology_list[] = {"q17", "q24", "q36"};
const char* human_rights_list[] = {"q7", "q8", "q9", "q19", "q20", "q30", "q32", "q42", "q43", "q45", "q50", "q52", "q55"};
const char* defense_list[] = {"q4", "q6", "q11", "q12", "q22", "q56"};
const char* legislation_list[] = {"q27", "q32", "q34", "q46", "q47", "q48", "q54"};

// 카테고리 배열
Category categories[] = {
    {"economy", economy_list, sizeof(economy_list) / sizeof(economy_list[0]), 1.0, 0},
    {"welfare", welfare_list, sizeof(welfare_list) / sizeof(welfare_list[0]), 1.0, 0},
    {"security", security_list, sizeof(security_list) / sizeof(security_list[0]), 1.0, 0},
    {"environment", environment_list, sizeof(environment_list) / sizeof(environment_list[0]), 1.0, 0},
    {"political_reform", political_reform_list, sizeof(political_reform_list) / sizeof(political_reform_list[0]), 1.0, 0},
    {"technology", technology_list, sizeof(technology_list) / sizeof(technology_list[0]), 1.0, 0},
    {"human_rights", human_rights_list, sizeof(human_rights_list) / sizeof(human_rights_list[0]), 1.0, 0},
    {"defense", defense_list, sizeof(defense_list) / sizeof(defense_list[0]), 1.0, 0},
    {"legislation", legislation_list, sizeof(legislation_list) / sizeof(legislation_list[0]), 1.0, 0}
};

#define CATEGORY_COUNT (sizeof(categories) / sizeof(categories[0]))

int is_in_list(const char* item, const char** list, size_t list_size) {
    for (size_t i = 0; i < list_size; i++) {
        if (strcmp(item, list[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

void calculate_and_print_match() {
    int total_score = 0;
    for (size_t i = 0; i < CATEGORY_COUNT; i++) {
        total_score += categories[i].count;
    }

    struct json_object *result = json_object_new_object();

    for (size_t i = 0; i < CATEGORY_COUNT; i++) {
        char score_str[7];
        snprintf(score_str, 7, "%06d", categories[i].count);
        int harris_score = atoi(score_str) / 1000;
        int trump_score = atoi(score_str) % 1000;
        double harris_match = 0.0;
        double trump_match = 0.0;

        if (harris_score + trump_score > 0) {
            harris_match = (double)harris_score / (harris_score + trump_score) * 100;
            trump_match = (double)trump_score / (harris_score + trump_score) * 100;
        }

        if (harris_match > trump_match) {
            char buffer[100];
            snprintf(buffer, sizeof(buffer), "당신은 해리스와 정치 성향이 %.0f%% 일치합니다", round(harris_match));
            json_object_object_add(result, categories[i].name, json_object_new_string(buffer));
        } else {
            char buffer[100];
            snprintf(buffer, sizeof(buffer), "당신은 트럼프와 정치 성향이 %.0f%% 일치합니다", round(trump_match));
            json_object_object_add(result, categories[i].name, json_object_new_string(buffer));
        }
    }

    char total_score_str[7];
    snprintf(total_score_str, 7, "%06d", total_score);
    int harris_total_score = atoi(total_score_str) / 1000;
    int trump_total_score = atoi(total_score_str) % 1000;
    double harris_total_match = 0.0;
    double trump_total_match = 0.0;

    if (harris_total_score + trump_total_score > 0) {
        harris_total_match = (double)harris_total_score / (harris_total_score + trump_total_score) * 100;
        trump_total_match = (double)trump_total_score / (harris_total_score + trump_total_score) * 100;
    }

    if (harris_total_match > trump_total_match) {
        char buffer[100];
        snprintf(buffer, sizeof(buffer), "당신은 해리스와 정치 성향이 %.0f%% 일치합니다", round(harris_total_match));
        json_object_object_add(result, "total", json_object_new_string(buffer));
    } else {
        char buffer[100];
        snprintf(buffer, sizeof(buffer), "당신은 트럼프와 정치 성향이 %.0f%% 일치합니다", round(trump_total_match));
        json_object_object_add(result, "total", json_object_new_string(buffer));
    }

    // 결과 출력
    printf("%s\n", json_object_to_json_string_ext(result, JSON_C_TO_STRING_PRETTY));

    // 메모리 해제
    json_object_put(result);
}

int main() {
    char buffer[1024];
    size_t len = fread(buffer, 1, sizeof(buffer) - 1, stdin);
    buffer[len] = '\0';

    struct json_object *parsed_json = json_tokener_parse(buffer);
    struct json_object *form_data, *category_weights;

    if (!json_object_object_get_ex(parsed_json, "form_data", &form_data) ||
        !json_object_object_get_ex(parsed_json, "category_weights", &category_weights)) {
        fprintf(stderr, "[Error] JSON 구조가 올바르지 않습니다.\n");
        json_object_put(parsed_json);
        return 1;
    }

    // 사용자 지정 가중치 적용
    struct json_object_iterator iter = json_object_iter_begin(category_weights);
    struct json_object_iterator iter_end = json_object_iter_end(category_weights);

    for (; !json_object_iter_equal(&iter, &iter_end); json_object_iter_next(&iter)) {
        const char *cat_key = json_object_iter_peek_name(&iter);
        struct json_object *cat_val = json_object_iter_peek_value(&iter);
        for (size_t i = 0; i < CATEGORY_COUNT; i++) {
            if (strcmp(cat_key, categories[i].name) == 0) {
                categories[i].weight = json_object_get_double(cat_val); // double 타입으로 가져오기
                break;
            }
        }
    }

    // 설문 데이터를 읽고 점수 계산
    iter = json_object_iter_begin(form_data);
    iter_end = json_object_iter_end(form_data);

    for (; !json_object_iter_equal(&iter, &iter_end); json_object_iter_next(&iter)) {
        const char *ques_key = json_object_iter_peek_name(&iter);
        struct json_object *ques_val = json_object_iter_peek_value(&iter);
        int score = json_object_get_int(ques_val); // int 타입으로 가져오기
        for (size_t i = 0; i < CATEGORY_COUNT; i++) {
            if (is_in_list(ques_key, categories[i].questions, categories[i].size)) {
                categories[i].count += (int)(score * categories[i].weight);
                break;
            }
        }
    }

    // 결과 계산 및 출력
    calculate_and_print_match();

    // 메모리 해제
    json_object_put(parsed_json);

    return 0;
}
