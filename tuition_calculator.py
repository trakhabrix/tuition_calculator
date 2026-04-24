print ('=' * 41)
print ('Subject Cost: ')
print ('- Subject 1: ₱7000')
print ('- Subject 2: ₱8000 ')
print ('- Subject 3: ₱8000')
print ('- Subject 4: ₱8000')
print ('- Subject 5: ₱4000')
print ('- Subject 6: ₱2000\n')
#Input
print('Choose type of education:')
print('1 - Tertiary (3% discount)')
print('2 - Elem to Highschool (10% discount)')
choice_educ = int(input('Enter your choice (1 or 2): '))
#If-Else Discount
if choice_educ == 1:
    discount_rate = 0.03
elif choice_educ == 2:
    discount_rate = 0.10
else:
    print('Invalid Choice')
#Calculation
print ('\n========== Tuition Calculation ==========')
total = 0
def add_subjects (sub1,sub2,sub3,sub4,sub5,sub6):
    print(f'Subject 1: {20 * ' '}₱{sub1}')
    print(f'Subject 2: {20 * ' '}₱{sub2}')
    print(f'Subject 3: {20 * ' '}₱{sub3}')
    print(f'Subject 4: {20 * ' '}₱{sub4}')
    print(f'Subject 5: {20 * ' '}₱{sub5}')
    print(f'Subject 6: {20 * ' '}₱{sub6}')
    total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
    print (41 * '=')
    print (f'Total: {24 * ' '}₱{total}')

    return total

def discount_formula(total):
    if choice_educ == 1:
        print (f'Discount: {21 * ' '}3%')
    else:
        print (f'Discount: {20 * ' '} 10%')

    discount = total * discount_rate
    final_total = total - discount

    print (41 * '=')
    print (f'Discount Computation: {9 * ' '}₱{total} * {discount_rate}')
    print (f'Discount: {20 * ' '} ₱{discount}')
    print (f'Final Computation:{13 * ' '}₱{total} - ₱{discount} ')
    print (f'Final Total:{19 * ' '}₱{final_total}')
    
total = add_subjects(7000, 8000, 8000, 8000, 4000, 2000)
discount_formula(total)
