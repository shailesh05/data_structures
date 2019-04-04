def calender(month, year):
    """
          This Class is used for calender .
         """

    day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']  # days (used for headings of calender .)

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # list of total days in months.

    values = 1  # start date
    d=1

    m = month
    y = year
    y0 = y - (14 - m) // 12  # Gregorian Calender method .
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7

    row = 5
    col = 7
    arr = [[0 for j in range(col)] for j in range(row)]
    print("calander month \n")

    for i in range(0, 7):
        print(day[i], end=' ')
    print()

    for i in range(row):
        for j in range(col):
            if values <= days[m - 1]:
                if i == 0 and j < d0:
                    arr[i][j] =  ' '
                    continue
                arr[i][j] = values
                values = values + 1
    for i in range(row):
        for j in range(col):
            if arr != 0:
                x = arr[i][j]
                x1 = str(x).center(2)
                print(x1, end=' ')

        print()
if __name__ == "__main__":
    month = int(input("Enter month : "))
    year = int(input("Enter year : "))
calender(month, year)
