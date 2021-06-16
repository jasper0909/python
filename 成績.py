math=int(input("數學分數"))
eng=int(input("英文分數:"))
if(math>=90 and eng>=90):
    print("有獎品")
elif(math<60 and eng<60):
    print("有處罰")
elif(math<60 or eng<60):
    print("再加油")
else:
    print("no")