import json
# """If inputs are provided in the json format"""

def BitmapHoles(strArr):
    # code goes here
    strArr = json.loads(strArr)
    # counts the number of holes encountred till now


    main_counter = 0
    inc_flag = False
    for i in list(strArr):

        # counts the number of "0" that have been encountred in inner list
        counter = 0

        # checking for 0 in a row
        for numb in range(len(i) - 1):
            # check if the current index and the next are equal to 0
            if i[numb] == i[numb + 1] == '0' and inc_flag == False:
                inc_flag = True
                counter += 1
            else:
                # incase there are multiple holes in the row
                inc_flag = False

        main_counter += counter
        inc_flag = False
    # checking for 0 in column

    for row in range(numb + 2):
        counter = 0
        for col in range(len(strArr) - 1):
            # check if the current and the next element are same
            if strArr[col][row] == strArr[col + 1][row] == '0' and inc_flag == False:
                counter += 1
                inc_flag = True
            else:
                # incase there are multiple holes in the column
                inc_flag = False

        main_counter += counter
        inc_flag = False

    # not quite clear in the second case how the 3 is considered as
    # after checking all ups and down and left and right the case still returns only 2
    #  taking into consideration the diagnols too the 3 rd case may arise

    # for i in range(1, len(strArr) - 1):  # since only diagnol elements are checked
    #     inc_flag = False
    #     for j in range(len(strArr[i]) - 1):
    #         if strArr[i - 1][j - 1] == '0' and strArr[i][j] == '0' and inc_flag == False:
    #             counter += 1
    #             inc_flag = True
    #         else:
    #             inc_flag = False
    #
    #     main_counter += counter
    #     inc_flag = False

    return main_counter
# keep this function call here
print(BitmapHoles(input()))
