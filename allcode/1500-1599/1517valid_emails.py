

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    ans = users[users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$', na=False)]
    return ans



data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'], [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'], [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'], [7, 'Shapiro', '.shapo@leetcode.com']]
users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})

print(valid_emails(users))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select * from users where mail like '%@leetcode.com' and SUBSTR(mail, 1, LENGTH(mail) - LENGTH('@leetcode.com')) ~ '^[a-zA-Z][a-zA-Z0-9_.-]*$';




