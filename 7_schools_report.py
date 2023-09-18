"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. 

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""
import json

outfile = open('school_data.json','r')


for data in outfile['instnm']:
    grad_rate = data["Graduation rate  women (DRVGR2020)"] > 50
    price = data["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000

    if grad_rate > 50:
        print(f"University: {data['instnm']}")
        print(f"Graduation Rate for Women: {data['instnm']}%\n")
    
    if price > 50000:
        print(f"University: {data['instnm']}")
        print(f"Total price for in-state students living off campus: ${data['instnm']:.2f}\n")

