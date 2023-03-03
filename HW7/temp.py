header = "Accept-Language:ru X-Turt:er"
list_of_headers = header.split(' ')
header_dict = dict()
for a in list_of_headers:
    s= a.split(':')
    header_name = s[0]
    header_value = s[1]
    header_dict[header_name] = header_value


t= header_dict
