print("A WARM WELCOME ON BEHALF OF KARTIKEY CHAWLA ")
predefined_name =["ishika","gauri","jeeyansh"]
name=input("HELLO, KINDLY ENTER YOUR NAME:")
if name in predefined_name:
    print("hey ,there",name)
else:
    print("kindly, reopen the link & enter name in small letters:")
    #name=input("HELLO, KINDLY ENTER YOUR NAME:")
    
predefined_sub=["EP","P.ED","BST","ENGLISH","ECONOMICS","ACCOUNTANCY"]
sub=input("kripya karke apna subject jiska paper hai wo dale::")
if sub in predefined_sub:
    print("ohhhhhhh",sub,"ka paper dene ja rahe ho, ALL THE VERY BEST , DO WELL SCORE WELL !!!")
else:
    print("kindly , choose subject from this table",predefined_sub)
    sub=input("kripya karke apna subject jiska paper hai wo dubara daliye::")
    if sub in predefined_sub:
        print("ohhhhhhh",sub,"ka paper dene ja rahe ho, ALL THE VERY BEST , DO WELL SCORE WELL !!!")
    
    

