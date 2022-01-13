def get_min_calory(n, total_cal, carb_cal,protein_cal, min_carb, min_protein):
    dp = {}
    if n ==0:
        return [-1]
    def helper(index, p, c):
        if p<=0 and c<=0:
            return 0
        if index ==0:
            return float("inf")

        if (index, p, c) in dp:
            return dp[(index, p, c)]
        ans = min(total_cal[index-1] + helper(index-1, p-protein_cal[index-1], c - carb_cal[index-1]), helper(index-1,p,c))
        dp[(index, p, c)] = ans
        return dp[(index, p, c)]
    ans = helper(n, min_protein, min_carb)
    if ans == float("inf"):
        return [-1]
    return [ans]

import json
def get_min_calory_api(input_req):
    input_dic = json.loads(input_req)
    number_of_request = input_dic.get('Total Test Cases', 0)
    ans = {}
    for i in range(1, number_of_request+1):
        request_detail = input_dic.get(str(i), {})
        n = request_detail.get('N',0)
        total_cal = request_detail.get('Total Calories',[])
        carb_cal = request_detail.get('Carbohydrate Calories',[])
        protein_cal = request_detail.get('Protein Calories',[])
        min_carb = request_detail.get('Minimum Carbohydrate requirement', 0)
        min_protein = request_detail.get('Minimum Protein requirement', 0)

        ans[str(i)] = get_min_calory(n, total_cal, carb_cal,protein_cal, min_carb, min_protein)
        
    return json.dumps(ans)


if __name__ == "__main__":
    input_req = '''{
"Total Test Cases":1,
"1":{"N":100,
"Total Calories":
[102,172,162,143,126,120,73,131,94,149,141,110,156,144,111,97,77,99,132,168,114,129,110,102,113,89,173,164,154,185,81,99,109,84,98,107,131,174,97,90,90,115,96,153,82,149,117,139,153,117,75,90,159,139,164,89,93,91,175,150,181,136,163,102,162,112,125,132,180,120,91,144,148,126,111,88,124,124,85,164,178,139,133,122,143,139,145,126,83,92,152,142,102,149,95,124,139,126,149,113],
"Carbohydrate Calories":
[38,42,45,45,48,47,38,48,42,38,34,44,32,34,38,44,42,42,31,40,44,33,38,37,31,46,38,46,37,44,39,49,49,36,39,48,31,39,30,41,42,40,34,36,42,44,45,35,42,36,37,32,36,46,38,30,37,41,46,42,43,35,45,49,45,44,31,41,43,43,30,30,32,44,45,38,35,46,38,36,49,33,48,34,31,30,37,40,41,37,49,36,36,41,46,30,31,36,38,48],
"Protein Calories":
[37,48,41,31,43,42,32,40,31,33,47,38,43,35,42,47,34,41,34,32,39,46,36,37,42,41,47,33,35,49,31,38,48,32,48,42,43,47,42,37,44,31,34,44,32,44,42,31,31,36,38,35,40,43,45,39,31,43,43,30,49,45,43,38,36,46,32,38,44,31,46,41,32,45,36,40,43,34,43,34,30,32,38,30,36,31,47,31,30,30,41,37,45,43,41,30,47,44,38,36],
"Minimum Carbohydrate requirement":200,
"Minimum Protein requirement":200}}'''
    print(get_min_calory_api(input_req))
        # https://assessment.hackerearth.com/challenges/hiring/healthifyme-senior-backend-developer-hiring-challenge/problems/
        
        
    
