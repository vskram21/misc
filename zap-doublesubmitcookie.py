"""
Script to handle double submit cookie.
"""
def proxyRequest(msg):
    print('proxyRequest called for url=' + msg.getRequestHeader().getURI().toString());
    CookieString=msg.getCookieParamsAsString()
    tokensplit=CookieString.split('token=')[1]
    token=tokensplit.split(';')[0]
    header=msg.getRequestHeader().getHeader('X-CSRF-TOKEN')
    if (header==token):
        print "Token and Header are same!"
        return  True;
    elif  header  is  None:
        print "Header not found!"
        msg.getRequestHeader().setHeader("X-CSRF-TOKEN", token)
        return  True;
    elif (header!=token):
        print "Xid is not same as Header!"
        msg.getRequestHeader().setHeader("X-CSRF-TOKEN", token)
        return  True;

def proxyResponse(msg):
    print('proxyResponse  called for ur1=' + msg.getRequestHeader().getURI().toString());
    return  True;
