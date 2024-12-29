cnpj=int(input('Digite o CNPJ. (Números apenas): '))
cnpj_str=str(cnpj)
pesos_dv1=5,4,3,2,9,8,7,6,5,4,3,2
pesos_dv2=6,5,4,3,2,9,8,7,6,5,4,3,2
mult_dv1=(
    int(cnpj_str[0])*pesos_dv1[0]+
    int(cnpj_str[1])*pesos_dv1[1]+
    int(cnpj_str[2])*pesos_dv1[2]+
    int(cnpj_str[3])*pesos_dv1[3]+
    int(cnpj_str[4])*pesos_dv1[4]+
    int(cnpj_str[5])*pesos_dv1[5]+
    int(cnpj_str[6])*pesos_dv1[6]+
    int(cnpj_str[7])*pesos_dv1[7]+
    int(cnpj_str[8])*pesos_dv1[8]+
    int(cnpj_str[9])*pesos_dv1[9]+
    int(cnpj_str[10])*pesos_dv1[10]+
    int(cnpj_str[11])*pesos_dv1[11]
)

div_dv1=mult_dv1/11
resto_dv1=mult_dv1%11
if resto_dv1<2:

    resto_dv1=0

else:
    resto_dv1=11-resto_dv1

resto_dv1_str=str(resto_dv1)
cnpj2=cnpj_str+resto_dv1_str
cnpj_str2=str(cnpj2)
mult_dv2=(
    int(cnpj_str2[0])*pesos_dv2[0]+
    int(cnpj_str2[1])*pesos_dv2[1]+
    int(cnpj_str2[2])*pesos_dv2[2]+
    int(cnpj_str2[3])*pesos_dv2[3]+
    int(cnpj_str2[4])*pesos_dv2[4]+
    int(cnpj_str2[5])*pesos_dv2[5]+
    int(cnpj_str2[6])*pesos_dv2[6]+
    int(cnpj_str2[7])*pesos_dv2[7]+
    int(cnpj_str2[8])*pesos_dv2[8]+
    int(cnpj_str2[9])*pesos_dv2[9]+
    int(cnpj_str2[10])*pesos_dv2[10]+
    int(cnpj_str2[11])*pesos_dv2[11]+
    int(cnpj_str2[12])*pesos_dv2[12]
)

div_dv2=mult_dv2/11
resto_dv2=mult_dv2%11
if resto_dv2<2:

    resto_dv2=0

else:
    resto_dv2=11-resto_dv2

resto_dv2_str=str(resto_dv2)
cnpj_final=cnpj_str2+resto_dv2_str
cnpj_final_str=str(cnpj_final)

if cnpj_final_str==cnpj_str:
    print(f'O CNPJ: {cnpj} é válido')

else:
    print(f'O CNPJ: {cnpj} não é valido')