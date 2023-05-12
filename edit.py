
def reduction(Nu, De):
    m = 'this fraction is already simplification'
    total_number = 0
    run = True
    if (Nu/De)%1 == 0:
        m = int(Nu/De)
        run = False
    else:
        total_number = Nu
        while run:
            if (Nu/De)%1 != 0:
                if (Nu/total_number)%1 == 0 and (De/total_number)%1 == 0:
                    x = int(Nu/total_number)
                    y = int(De/total_number)
                    m = f'{x} / {y} || total_number: {total_number}'
                    break
                else:
                    total_number -= 1
                    #print(total_number)
                    if total_number <= 1:
                        break
            else:
                m = 'nothing'
    return m

