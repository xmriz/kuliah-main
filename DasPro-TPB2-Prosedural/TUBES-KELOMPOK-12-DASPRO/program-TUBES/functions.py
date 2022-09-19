def ngitung_line_csv(csv):
    lines = 0
    for i in csv:
        if i == "\n":
            lines +=1
    return(lines)

def ngitung_kolom_csv(csv) :
    kolom = 0
    for i in csv :
        if i == ";" :
            kolom += 1
        if i =="\n" :
            return kolom + 1

def len_manual(string) :
    count = 0
    for i in string :
        count += 1
    return count

def join_manual(array) :
    string = ""
    for i in array :
        string += i
    return string

def slicing(string) :
    sliced = ""
    length = len_manual(string)
    count = 0
    for i in string :
        if count < length - 1 :
            sliced += i
        count += 1
    return sliced

def split_string(string) :
    string_splitted = [i for i in string]
    return string_splitted

def csv_pars(csv) :
    panjang_line = ngitung_line_csv(csv)
    banyak_kolom = ngitung_kolom_csv(csv)
    file_parsed = [[0 for i in range(banyak_kolom)] for i in range(panjang_line)]
    data = 0
    while data < panjang_line:
        counter = 0
        item = ""
        for j in csv :
            if j == "\n" :   
                file_parsed[data][counter] = item
                data += 1
                counter = 0
                item = ""
            elif j == ";":
                file_parsed[data][counter] = item
                counter += 1
                item = ""
            else:
                item += j
    return(file_parsed)

def ngitung_panjang_matriks(matriks):
    count = 0
    for i in matriks:
        count += 1
    return count