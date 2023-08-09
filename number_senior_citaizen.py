def countSeniors(details):
    count = 0
    for info in details:
        age = info[11:13]
        if int(age) > 60:
            count += 1
    return count

    #     if int(age) > 60:
    #         count+=1
    # return count


print(countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
