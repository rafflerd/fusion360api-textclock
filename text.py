tableau1=[
            "ILRESTEUDEUX",
            "QUATRE2TROIS",
            "NEUFUNE3SEPT",
            "HUITNSIXCINQ",
            "MIDIX4MINUIT",
            "ONZE75HEURES",
            "MOINSZLE1DIX",
            "CKFETGOUARTJ",
            "HVINGT-CINQK",
            "LMETNDEMIEST"]
txt1 = "IL EST TROIS"
header_tab="<style> table,th,td{font:\"Georgia\";border-collapse:collapse;font-size:7px;border:1px solid black;} th,td{align:center;padding:2px;text-align:center}</style>"
foother_tab=""   
def cherche_mots(tableau,txt):
    liste_txt=txt.split()
    liste_mots=[]
    for mots in liste_txt:
        skip=mots.count("/")
        mots=mots.strip("/")
        liste_mots.append([mots,skip,-1,-1,-1])
    print(len(liste_mots))
    for indice in range(len(liste_mots)):
        skip_mots=liste_mots[indice][1]
        mots=liste_mots[indice][0]
        cpt=0
        for ligne in tableau:
            start=ligne.find(mots)
            largeur_mots=len(mots)
            fin_mots=start+largeur_mots-1
            if start>-1:
                skip_mots-=1
                if skip_mots==-1:
                    liste_mots[indice][2]=cpt
                    liste_mots[indice][3]=start
                    liste_mots[indice][4]=fin_mots
                    
            cpt+=1
    liste_mots.sort(key=lambda liste_mots:liste_mots[2])
    return liste_mots
def create_html_color(header,foother,data,compare):
    html_str=header+"<table>"
    liste_text=str(compare).split()
    compteur_ligne=0
    for ligne in data:
        
        html_str=html_str+"<tr>"
        compteur_char=0
        for char in ligne:
            couleur='<td style="color:black;">'
            for data in compare:
                
                
                if (data[2]==compteur_ligne) and (compteur_char>=data[3]) and (compteur_char<=data[4]):
                    couleur='<td style="color:red;">'
                
            compteur_char+=1
            html_str=html_str+couleur+char+"</td>"
        compteur_ligne+=1

        html_str=html_str+"</tr>"
    html_str=html_str+"</table>"+foother
    return html_str
mots_trouve=cherche_mots(tableau1,txt1)
html=create_html_color(header_tab,foother_tab,tableau1,mots_trouve)
print (mots_trouve)