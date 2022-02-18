  
def main():
    from  employee import Employee
    data = (Employee().fileImport()).split()
    author = data[0]
    report = open(author + ".txt", "w")
    results = Employee().taskSuccessCheck()
    if results[0] is False:
        report.write('Task | "PMO-13" | Failed\n')
    else:
        report.write('Task | "PMO-13" | Passed\n')
    if results[1] is False:
        report.write('Task | "PMO-666" | Failed')
    else:
        report.write('Task | "PMO-666" | Passed')
    report.close()

main()