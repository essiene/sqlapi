import re

"""mysql://username:password@host/database/?param1=value1&param2=value2"""

#TODO: modify this to use grammar/parser techniques
# instead of cowboy regexes
'''
dburl := (mysql|pgsql)://connection_string |
         sqlite://dbpath
connection_string := username(:password)?(@host)?/database(/)?(name=value(&name=value)*)?
dbpath := absolute_path | relative_path
absolute_path := /pathelement
relative_path := pathelement
pathelement := [a-zA-Z0-9_.](/[a-zA-Z0-9_.])*
username := name
password := name
host := name
database := name
'''



def get_connection_properties(dburl):
    pattern_module = r'(mysql|sqlite)://'
    pattern_username = r'(.+):'
    pattern_password = r'(.+)@'
    pattern_host = r'@[a-zA-Z_][a-zA-Z0-9_]*/'
    pattern_database = r'/[a-zA-Z_][a-zA-Z0-9]*(/?)'

    pos = 0
    module_name, pos = extract_pattern(dburl, pattern_module, ':')
    if not module_name:
        raise SystemExit("URL string MUST start with 'dbtype://'")
        
    username, pos = extract_pattern(dburl, pattern_username, ':', pos)

    password, pos = extract_pattern(dburl, pattern_password, '@', pos)

    host, pos = extract_pattern(dburl, pattern_host, '/', pos - 1, 1)

    database, pos = extract_pattern(dburl, pattern_database, '/', pos - 1, 0, 1)

    return (module_name, username, password, host, database)

def extract_pattern(s, pattern, delim, search_pos=0, start_pos=0, result_index=0):
    p = re.compile(pattern)
    m = p.match(s, search_pos)
    if m:
        res = m.group().split(delim)[result_index][start_pos:]
        return res, m.end()
    else:
        return None, search_pos

