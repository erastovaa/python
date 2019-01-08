def sum1(num):
    sum1 = 0
    for i in range(0, 3):
        sum1 += num[i]
    return sum1


def sum2(num):
    sum2 = 0
    for i in range(3, 6):
        sum2 += num[i]
    return sum2


def get_nearest_happy_ticket(current_ticket: str) -> str:
    num = [int(i) for i in current_ticket]
    diff = sum1(num) - sum2(num)
    if diff == 0:
        return current_ticket
    else:
        diff = 1
        ticket_up = int(current_ticket)
        while diff != 0:
            ticket_up += 1
            num = [int(i) for i in str(ticket_up)]
            diff = sum1(num) - sum2(num)
        diff = 1
        ticket_down = int(current_ticket)
        while diff != 0:
            if current_ticket == '100000':
                current_ticket = '100001'
                return current_ticket
            ticket_down -= 1
            num = [int(i) for i in str(ticket_down)]
            diff = sum1(num) - sum2(num)
        if (abs(int(current_ticket) - ticket_up)
                > abs(int(current_ticket) - ticket_down)):
            return str(ticket_down)
        else:
            return str(ticket_up)
