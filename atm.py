account = 500
request = 277
def ATM(request,account):
    if request <=0:
        print "you must try with valid number "
    elif account > request :
            account -= request
            while request > 0:
                    if request>100 :
                        print "give 100"
                        request-=100
                    elif request>50 :
                        print "give 50"
                        request-=50
                    elif request>20 :
                        print "give 20"
                        request-=20
                    elif request>10 :
                        print "give 10"
                        request-=10
                    elif request>5 :
                         print "give 5"
                         request-=5
                    else :
                          print "give " , request
                          request=0
    print "New account = " +str(account )



ATM (request,account )
