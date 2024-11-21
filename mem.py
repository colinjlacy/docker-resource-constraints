def mimic_oom():
    ticker = 1
    huge_list = []
    while True:
        huge_list.append([1] * 100000)
        print(f"added huge list {ticker} times")
        ticker += 1


mimic_oom()
