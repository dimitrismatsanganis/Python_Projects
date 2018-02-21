#eisodos ari8mou apo to xrhsth(an den einai 8etikos h einai megaluteros tou 1000000,den 8a emfanisei tipota)
n = input('Dwse enan thetiko arithmo: ')

#dhmiourgia ths synarthshs roman_num, pou 8a antistoixei tous ari8mous me tous latinikous 
def roman_num(num):
        #lista twn ari8mwn
        ari8moi = [1000000,500000,100000,50000,10000,5000,1000,900,500,400,100,90,50,40,10,9,5,4,1]
        #lista latinikwn ari8mwn
        roman_num = ['-M','-D','-C','-L','-X','-V','M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        
        i = 0
        apo = ""
        #proupo8esh askhshs
        while num > 0 and num <= 1000000 :
                    for j in range(num//ari8moi[i]):
                        apo += roman_num[i]
                        num -= ari8moi[i]
                    i += 1
        #e3odos twn apotelesmatwn ths synarthshs           
        print apo
        
#kalesma ths synarthshs roman_num gia ton ari8mo pou exei dwsei o xrhsths, ton "n"
roman_num(int(n))


