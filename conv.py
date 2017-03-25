import re
#="k="


catlist=[["憲法","刑事","財務通則","水産業","観光"],
["国会","警察","国有財産","鉱業","郵務"],
["行政組織","消防","国税","工業","電気通信"],
["国家公務員","国土開発","事業","商業","労働"],
["行政手続","土地","国債","金融・保険","環境保全"],
["統計","都市計画","教育","外国為替・貿易","厚生"],
["地方自治","道路","文化","陸運","社会福祉"],
["地方財政","河川","産業通則","海運","社会保険"],
["司法","災害対策","農業","航空","防衛"],
["民事","建築・住宅","林業","貨物運送","外事"]]

def parse():
    dkt={}
    for l in open('color.txt',encoding='utf8').readlines():
        l=l.strip()
        s=re.findall("k=(.*) r=(.*) g=(.*) b=(.*)",l)
        cat=s[0][0]
        r=int(s[0][1])*1.0/255
        g=int(s[0][2])*1.0/255
        b=int(s[0][3])*1.0/255
        #print("r={}g={}b={}".format(r,g,b))
        dkt[cat]=(r,g,b)
        #print(s)
        #print(s)
    return dkt
def conv(dkt):
    sss=""
    for t in catlist:
        tt=[]
        for p in t:
            if p in dkt:
                v=dkt[p]
                #print(v)
                r=v[0]
                g=v[1]
                b=v[2]
                ddd=dict(r=r,g=g,b=b,cat=p,lf="{",rf="}")
                t="\\cellcolor[rgb]{lf}{r:.6f},{g:.6f},{b:.6f}{rf}  {cat}".format(**ddd)
                #print(t
                tt.append(t)
        pp=" & ".join(tt)
        pp=pp+"\\\\\n"
        sss+=pp
    print(sss)

                #print(p)
            #print(p)
def main():
    dkt=parse()
    conv(dkt)
if __name__=="__main__":main()
