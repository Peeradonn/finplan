from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BLUE=Font(name='Arial',size=10,color='0000FF'); BLACK=Font(name='Arial',size=10)
BOLD=Font(name='Arial',size=10,bold=True); H1=Font(name='Arial',size=13,bold=True)
GREEN=Font(name='Arial',size=10,color='008000')
YEL=PatternFill('solid',fgColor='FFFF00'); GREY=PatternFill('solid',fgColor='EEEEEE')
NUM='#,##0'; PCT='0.00%'; THIN=Border(bottom=Side(style='thin'))

wb=Workbook()

# ============ INPUTS ============
ws=wb.active; ws.title='Inputs'
ws['A1']='Wong Family model — INPUTS'; ws['A1'].font=H1
ws['A2']='Blue = hardcoded input. Edit only blue cells. Source in column D.'; ws['A2'].font=Font(name='Arial',size=9,italic=True)
rows=[
 ('ECONOMIC',None,None,None),
 ('CPI inflation','B',0.025,PCT,"Pete lock table; HK 2006-25 avg 2.52%"),
 ('Wage growth — Adrian','B',0.03,PCT,"Pete lock table"),
 ('Wage growth — Carmen','B',0.03,PCT,"Pete lock table"),
 ('Education escalation (overseas)','B',0.05,PCT,"Pete lock table"),
 ('RETURNS (nominal)',None,None,None),
 ('Equities','B',0.06,PCT,"Fahtai 27 Sep: conservative vs Pete's 7.0%"),
 ('Equity volatility','B',0.17,PCT,"Pete lock table 16-18%"),
 ('Bonds / IG','B',0.04,PCT,"Pete lock table"),
 ('Treasury ladder','B',0.04,PCT,"held to maturity, vol ~2%"),
 ('MPF','B',0.05,PCT,"Pete lock table"),
 ('Cash — time deposits','B',0.028,PCT,"Pete: 3.0% 2027-28 -> 2.5% by 2031"),
 ('Cash — idle balances','B',0.002,PCT,"Pete lock table"),
 ('TAX 2026/27',None,None,None),
 ('Basic allowance','B',145000,NUM,"IR (Amendment) Ordinance 2026"),
 ('Married allowance','B',290000,NUM,"IR (Amendment) Ordinance 2026"),
 ('Child allowance','B',140000,NUM,"IR (Amendment) Ordinance 2026"),
 ('Dependent parent 60+ (each)','B',55000,NUM,"2 parents assumed, claimed by Adrian"),
 ('MPF deduction cap','B',18000,NUM,"per person"),
 ('Top marginal rate','B',0.17,PCT,"progressive 2/6/10/14 then 17"),
 ('Tax on first 200,000','B',16000,NUM,"2%+6%+10%+14% on 50k bands"),
 ('Mortgage rate (for HLI deduction)','B',0.035,PCT,"Pete lock table"),
 ('FAMILY',None,None,None),
 ("Adrian's salary",'B',1050000,NUM,"case"),
 ("Adrian's bonus (planning = low end)",'B',150000,NUM,"case 150-300k; conservative"),
 ("Carmen's salary / dividend",'B',720000,NUM,"case; treated as all salary"),
 ("Ryan's salary (EXCLUDED from base case)",'B',300000,NUM,"case; Goal 3 treats him separately"),
 ('Household expenses (annual)','B',984000,NUM,"case 82,000/month"),
 ('Retirement spending (today money)','B',780000,NUM,"case"),
 ('Retirement income floor %','B',0.40,PCT,"Pete, C&SD HES 2024/25 top quartile"),
 ('MODEL LEVERS',None,None,None),
 ('Portfolio return — plan (nominal)','B',0.048,PCT,"mix 2: 40% eq @6% + 60% ladder @4%"),
 ('Portfolio return — status quo (nominal)','B',0.042,PCT,"unmanaged, cash-heavy. TEAM TO AGREE"),
 ('Emergency reserve target (months)','B',12,'0',"vs 30.5 today"),
 ('Annuity purchase cost at 2037','B',4120000,NUM,"Pete: MPF 2.31M (A) + 1.81M (C)"),
 ('Annuity income (HKMC, annual)','B',268000,NUM,"Pete: HKMC payout at 65"),
 ('Education — overseas annual (today)','B',600000,NUM,"case high end, conservative"),
 ('Education — years','B',4,'0',"4-year degree"),
 ('Insurance premiums (Lookbua, TBC)','B',0,NUM,"PLACEHOLDER — reduces surplus"),
 ('DATES',None,None,None),
 ('Base year','B',2026,'0',"model start"),
 ('Adrian retires (age 65)','B',2037,'0',"case"),
 ('Carmen retires (age 62)','B',2039,'0',"case"),
 ('Chloe starts university','B',2028,'0',"age 18"),
 ('Carmen age 89','B',2066,'0',"base horizon"),
 ('Carmen age 95','B',2072,'0',"stress horizon"),
]
r=4
ref={}
for row in rows:
    if row[1] is None:
        ws.cell(r,1,row[0]).font=BOLD; ws.cell(r,1).fill=GREY
        for c in range(2,5): ws.cell(r,c).fill=GREY
    else:
        ws.cell(r,1,row[0]).font=BLACK
        c=ws.cell(r,2,row[2]); c.font=BLUE; c.number_format=row[3]
        ws.cell(r,4,row[4]).font=Font(name='Arial',size=8,italic=True,color='666666')
        ref[row[0]]=f'Inputs!$B${r}'
    r+=1
ws.column_dimensions['A'].width=38; ws.column_dimensions['B'].width=14
ws.column_dimensions['D'].width=55

# ============ BALANCE SHEET ============
bs=wb.create_sheet('BalanceSheet')
bs['A1']='Balance sheet — case validation'; bs['A1'].font=H1
items=[('LIQUID',None),('Savings and current accounts',620000),('Time deposits',1480000),
 ('Money market / short bond fund',400000),('__SUB_LIQ',None),
 ('INVESTMENT',None),('HK equity funds',1000000),('Global equity funds',1350000),
 ('Investment-grade bond funds',900000),('ESG / sustainable equity funds',700000),
 ('Green / sustainable bond products',450000),('Listed stocks and REITs',800000),
 ("Adrian's MPF",1050000),("Carmen's MPF",620000),("Ryan's MPF",180000),
 ('Digital assets (all Ryan)',500000),('Cash value of life policies',420000),('__SUB_INV',None),
 ('FIXED',None),('Residential property',11500000),("Carmen's business",5000000),
 ('Motor vehicle',220000),('__SUB_FIX',None),
 ('LIABILITIES',None),('Mortgage',1800000),('Business term loan',900000),
 ('Credit card / revolving',85000),('__SUB_LIAB',None)]
r=3; marks={}
for name,val in items:
    if val is None and not name.startswith('__'):
        bs.cell(r,1,name).font=BOLD; bs.cell(r,1).fill=GREY; bs.cell(r,2).fill=GREY
        marks[name]=r+1
    elif name.startswith('__'):
        key=name[2:]
        start=marks[{'SUB_LIQ':'LIQUID','SUB_INV':'INVESTMENT','SUB_FIX':'FIXED','SUB_LIAB':'LIABILITIES'}[key]]
        lbl={'SUB_LIQ':'Total liquid','SUB_INV':'Total investment',
             'SUB_FIX':'Total fixed','SUB_LIAB':'Total liabilities'}[key]
        bs.cell(r,1,lbl).font=BOLD
        c=bs.cell(r,2,f'=SUM(B{start}:B{r-1})'); c.font=BOLD; c.number_format=NUM; c.border=THIN
        marks[key]=r
    else:
        bs.cell(r,1,name).font=BLACK
        c=bs.cell(r,2,val); c.font=BLUE; c.number_format=NUM
    r+=1
r+=1
bs.cell(r,1,'TOTAL ASSETS').font=BOLD
bs.cell(r,2,f"=B{marks['SUB_LIQ']}+B{marks['SUB_INV']}+B{marks['SUB_FIX']}").font=BOLD
bs.cell(r,2).number_format=NUM; TA=r; r+=1
bs.cell(r,1,'NET WORTH').font=BOLD
bs.cell(r,2,f"=B{TA}-B{marks['SUB_LIAB']}").font=BOLD; bs.cell(r,2).number_format=NUM; NW=r; r+=2
bs.cell(r,1,'CHECK vs case (should be 0)').font=BOLD
bs.cell(r,2,f'=B{NW}-24405000').number_format=NUM; bs.cell(r,2).fill=YEL
r+=2
bs.cell(r,1,"Parents' investable pool (ex Ryan's MPF and digital)").font=BOLD
bs.cell(r,2,f"=B{marks['SUB_LIQ']}+B{marks['SUB_INV']}-B{marks['INVESTMENT']+8}-B{marks['INVESTMENT']+9}").font=BOLD
bs.cell(r,2).number_format=NUM; POOL=r
bs.column_dimensions['A'].width=40; bs.column_dimensions['B'].width=15

# ============ TAX ============
tx=wb.create_sheet('Tax')
tx['A1']='Salaries tax 2026/27 — separate vs joint assessment'; tx['A1'].font=H1
tx['A2']='Confirms Pete: separate beats joint by exactly HK$18,000'; tx['A2'].font=Font(name='Arial',size=9,italic=True)
I=ref
tx['A4']='HLI total (mortgage x rate)'; tx['B4']='=BalanceSheet!B'+str(marks['LIABILITIES'])+'*'+I['Mortgage rate (for HLI deduction)']
tx['B4'].number_format=NUM
hdr=['','Adrian','Carmen','Joint','Ryan']
for j,h in enumerate(hdr): 
    c=tx.cell(6,j+1,h); c.font=BOLD; c.border=THIN
# build explicitly
A_SAL=I["Adrian's salary"]; A_BON=I["Adrian's bonus (planning = low end)"]
C_SAL=I["Carmen's salary / dividend"]; R_SAL=I["Ryan's salary (EXCLUDED from base case)"]
MPFCAP=I['MPF deduction cap']; BAS=I['Basic allowance']; MAR=I['Married allowance']
CHI=I['Child allowance']; DPA=I['Dependent parent 60+ (each)']
T200=I['Tax on first 200,000']; TOPR=I['Top marginal rate']; EXPN=I['Household expenses (annual)']
tx['A7']='Income'; tx['B7']='='+A_SAL+'+'+A_BON; tx['C7']='='+C_SAL; tx['D7']='=B7+C7'; tx['E7']='='+R_SAL
tx['A8']='less MPF';          tx['B8']='=-'+MPFCAP; tx['C8']='=-'+MPFCAP; tx['D8']='=B8+C8'; tx['E8']='=-MIN('+MPFCAP+',E7*0.05)'
tx['A9']='less home loan int';tx['B9']='=-$B$4/2'; tx['C9']='=-$B$4/2'; tx['D9']='=B9+C9'; tx['E9']=0
tx['A10']='Net income';       
for col in 'BCDE': tx[f'{col}10']=f'=SUM({col}7:{col}9)'
tx['A11']='less allowances'
tx['B11']='=-('+BAS+'+'+CHI+'+2*'+DPA+')'
tx['C11']='=-'+BAS
tx['D11']='=-('+MAR+'+'+CHI+'+2*'+DPA+')'
tx['E11']='=-'+BAS
tx['A12']='Net chargeable income'
for col in 'BCDE': tx[f'{col}12']=f'=MAX({col}10+{col}11,0)'
tx['A13']='TAX (progressive)'
for col in 'BCDE':
    tx[col+'13']=('=IF('+col+'12>200000,'+T200+'+('+col+'12-200000)*'+TOPR+','
                  'IF('+col+'12>150000,9000+('+col+'12-150000)*0.14,'
                  'IF('+col+'12>100000,4000+('+col+'12-100000)*0.1,'
                  'IF('+col+'12>50000,1000+('+col+'12-50000)*0.06,'+col+'12*0.02))))')
for rr in range(7,14):
    for col in 'BCDE': tx[f'{col}{rr}'].number_format=NUM; tx[f'{col}{rr}'].font=BLACK
    tx[f'A{rr}'].font=BLACK
for col in 'BCDE': tx[f'{col}13'].font=BOLD; tx[f'{col}13'].border=THIN
tx['A15']='COUPLE — separate';  tx['B15']='=B13+C13'; tx['B15'].font=BOLD; tx['B15'].number_format=NUM; tx['B15'].fill=YEL
tx['A16']='COUPLE — joint';     tx['B16']='=D13';     tx['B16'].font=BOLD; tx['B16'].number_format=NUM
tx['A17']='Separate saves';     tx['B17']='=B16-B15'; tx['B17'].font=BOLD; tx['B17'].number_format=NUM
tx['A19']='CHECK separate = 181,770'; tx['B19']='=B15-181770'; tx['B19'].number_format=NUM; tx['B19'].fill=YEL
tx['A20']='CHECK joint = 199,770';    tx['B20']='=B16-199770'; tx['B20'].number_format=NUM; tx['B20'].fill=YEL
tx['A22']='ANNUAL SURPLUS (parents, after tax and MPF)'; tx['A22'].font=BOLD
tx['A23']='Gross income';  tx['B23']='=D7'
tx['A24']='less tax';      tx['B24']='=-B15'
tx['A25']='less MPF';      tx['B25']='=D8'
tx['A26']='less expenses'; tx['B26']='=-'+EXPN
tx['A27']='SURPLUS';       tx['B27']='=SUM(B23:B26)'; tx['B27'].font=BOLD; tx['B27'].fill=YEL
for rr in range(23,28): tx[f'B{rr}'].number_format=NUM; tx[f'A{rr}'].font=BLACK
tx.column_dimensions['A'].width=34
for col in 'BCDE': tx.column_dimensions[col].width=14


# ============ PROJECTION ============
pj=wb.create_sheet('Projection')
pj['A1']='Year-by-year projection 2026-2072 — every cell driven by the Inputs tab'; pj['A1'].font=H1
pj['A2']='Black = formula. Change nothing here; change Inputs.'; pj['A2'].font=Font(name='Arial',size=9,italic=True)
cols=['Year','Age A','Age C','Income A','Income C','Allow A','Allow C','Tax A','Tax C','MPF',
      'Living exp','Education','Retire spend','Annuity inc','Net cash flow','Portfolio open',
      'Investment return','Annuity purchase','Portfolio close']
for j,h in enumerate(cols):
    c=pj.cell(3,j+1,h); c.font=BOLD; c.border=THIN; c.alignment=Alignment(wrap_text=True,horizontal='center')
    pj.column_dimensions[get_column_letter(j+1)].width=13 if j>2 else 7

CPIr=I['CPI inflation']; WA=I['Wage growth — Adrian']; WC=I['Wage growth — Carmen']
EDUe=I['Education escalation (overseas)']; RETA=I['Adrian retires (age 65)']; RETC=I['Carmen retires (age 62)']
EDUy=I['Chloe starts university']; EDUn=I['Education — years']; EDUa=I['Education — overseas annual (today)']
RSPEND=I['Retirement spending (today money)']; ANNC=I['Annuity purchase cost at 2037']
ANNI=I['Annuity income (HKMC, annual)']; RPLAN=I['Portfolio return — plan (nominal)']
PREM=I['Insurance premiums (Lookbua, TBC)']; HLI='Tax!$B$4'; BY=I['Base year']

def prog_formula(cell):
    return (f'IF({cell}>200000,{T200}+({cell}-200000)*{TOPR},'
            f'IF({cell}>150000,9000+({cell}-150000)*0.14,'
            f'IF({cell}>100000,4000+({cell}-100000)*0.1,'
            f'IF({cell}>50000,1000+({cell}-50000)*0.06,MAX({cell},0)*0.02))))')

START_POOL="BalanceSheet!$B$"+str(POOL)
r0=4
for i in range(47):
    r=r0+i; y=2026+i; n=f'($A{r}-{BY})'
    pj.cell(r,1,y).number_format='0'
    pj.cell(r,2,f'=$A{r}-1972'); pj.cell(r,3,f'=$A{r}-1977')
    pj.cell(r,4,f'=IF($A{r}<{RETA},({A_SAL}+{A_BON})*(1+{WA})^{n},0)')
    pj.cell(r,5,f'=IF($A{r}<{RETC},{C_SAL}*(1+{WC})^{n},0)')
    pj.cell(r,6,f'=({BAS}+{CHI}+2*{DPA})*(1+{CPIr})^{n}')
    pj.cell(r,7,f'={BAS}*(1+{CPIr})^{n}')
    pj.cell(r,8,f'=IF(D{r}=0,0,{prog_formula(f"MAX(D{r}-{MPFCAP}-{HLI}/2-F{r},0)")})')
    pj.cell(r,9,f'=IF(E{r}=0,0,{prog_formula(f"MAX(E{r}-{MPFCAP}-{HLI}/2-G{r},0)")})')
    pj.cell(r,10,f'=IF(D{r}>0,{MPFCAP},0)+IF(E{r}>0,{MPFCAP},0)')
    pj.cell(r,11,f'=IF($A{r}<{RETA},{EXPN}*(1+{CPIr})^{n},0)')
    pj.cell(r,12,f'=IF(AND($A{r}>={EDUy},$A{r}<{EDUy}+{EDUn}),{EDUa}*(1+{EDUe})^{n},0)')
    pj.cell(r,13,f'=IF($A{r}>={RETA},{RSPEND}*(1+{CPIr})^{n},0)')
    pj.cell(r,14,f'=IF($A{r}>={RETA},{ANNI},0)')
    pj.cell(r,15,f'=D{r}+E{r}-H{r}-I{r}-J{r}-K{r}-L{r}-M{r}+N{r}-{PREM}')
    pj.cell(r,16, f'={START_POOL}' if i==0 else f'=S{r-1}')
    pj.cell(r,17,f'=P{r}*{RPLAN}')
    pj.cell(r,18,f'=IF($A{r}={RETA},-{ANNC},0)')
    pj.cell(r,19,f'=MAX(P{r}+Q{r}+O{r}+R{r},0)')
    for j in range(4,20): pj.cell(r,j).number_format=NUM; pj.cell(r,j).font=BLACK
    for j in (2,3): pj.cell(r,j).number_format='0'
    if y in (2037,2039,2066,2072):
        for j in range(1,20): pj.cell(r,j).fill=PatternFill('solid',fgColor='FFF2CC')
pj.freeze_panes='D4'
LAST=r0+46

# ============ OUTPUTS ============
op=wb.create_sheet('Outputs')
op['A1']='OUTPUTS — the only numbers that go in the proposal'; op['A1'].font=H1
op['A2']='Green = pulled from another tab. Quote these, not your own arithmetic.'; op['A2'].font=Font(name='Arial',size=9,italic=True)
outs=[('POSITION TODAY',None,None),
 ('Net worth',f'=BalanceSheet!B{NW}',NUM),
 ("Parents' investable pool",f'={START_POOL}',NUM),
 ('Annual surplus (after tax, MPF, premiums)','=Tax!B27-'+PREM,NUM),
 ('Emergency reserve, months','=BalanceSheet!B'+str(marks['SUB_LIQ'])+'/('+EXPN+'/12)','0.0'),
 ('TAX',None,None),
 ('Couple — separate assessment','=Tax!B15',NUM),
 ('Couple — joint assessment','=Tax!B16',NUM),
 ('Saving from separate','=Tax!B17',NUM),
 ('PROJECTION',None,None),
 ("Portfolio at Adrian's retirement (2037, nominal)",f'=INDEX(Projection!S:S,MATCH({RETA},Projection!A:A,0))',NUM),
 ('Portfolio at Carmen 89 (2066)','=INDEX(Projection!S:S,MATCH('+I['Carmen age 89']+',Projection!A:A,0))',NUM),
 ('Portfolio at Carmen 95 (2072)','=INDEX(Projection!S:S,MATCH('+I['Carmen age 95']+',Projection!A:A,0))',NUM),
 ('Portfolio at 2037 in TODAY money','=INDEX(Projection!S:S,MATCH('+RETA+',Projection!A:A,0))/(1+'+CPIr+')^('+RETA+'-'+BY+')',NUM),
 ('Retirement need at 2037 (today money)','=780000*(1-(1+0.02)^-29)/0.02',NUM),
 ('Funded ratio','=B17/B18','0%'),
 ('Total education cost (nominal)',f'=SUM(Projection!L{r0}:L{LAST})',NUM),
 ('Money lasts to 89? (deterministic)','=IF(INDEX(Projection!S:S,MATCH('+I['Carmen age 89']+',Projection!A:A,0))>0,"YES","NO")',None),
 ('Money lasts to 95? (deterministic)','=IF(INDEX(Projection!S:S,MATCH('+I['Carmen age 95']+',Projection!A:A,0))>0,"YES","NO")',None),
]
r=4
for lbl,f,fmt in outs:
    if f is None:
        op.cell(r,1,lbl).font=BOLD; op.cell(r,1).fill=GREY; op.cell(r,2).fill=GREY
    else:
        op.cell(r,1,lbl).font=BLACK
        c=op.cell(r,2,f); c.font=GREEN
        if fmt: c.number_format=fmt
    r+=1
op.column_dimensions['A'].width=48; op.column_dimensions['B'].width=18


wb.save('/home/claude/wong/wong_model.xlsx')
print('saved')
