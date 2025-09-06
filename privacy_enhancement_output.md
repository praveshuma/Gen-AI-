Synthetic DataFrame:

&nbsp;           Name       Address                Email  Salary

0    Alice Smith  101 Maple Dr     emma@example.com   62911

1     Emma Davis   123 Main St  charlie@example.com   63606

2  Charlie Brown  101 Maple Dr     emma@example.com   55571

3  Charlie Brown  202 Birch Ln    alice@example.com   52446

4    Alice Smith   456 Oak Ave    diana@example.com   74013

5   Diana Wilson  101 Maple Dr  charlie@example.com   62532

6     Emma Davis   789 Pine Rd  charlie@example.com   70423

7    Bob Johnson   456 Oak Ave     emma@example.com   59422

8   Diana Wilson   456 Oak Ave     emma@example.com   85354

9    Alice Smith   123 Main St      bob@example.com   45783



DataFrame Info:

<class 'pandas.core.frame.DataFrame'>

RangeIndex: 10 entries, 0 to 9

Data columns (total 4 columns):

&nbsp;#   Column   Non-Null Count  Dtype 

---  ------   --------------  ----- 

&nbsp;0   Name     10 non-null     object

&nbsp;1   Address  10 non-null     object

&nbsp;2   Email    10 non-null     object

&nbsp;3   Salary   10 non-null     int64 

dtypes: int64(1), object(3)

memory usage: 452.0+ bytes

None



DataFrame with Differential Privacy (Salary column):

&nbsp;           Name       Address                Email    Salary

0    Alice Smith  101 Maple Dr     emma@example.com  100000.0

1     Emma Davis   123 Main St  charlie@example.com   30000.0

2  Charlie Brown  101 Maple Dr     emma@example.com  100000.0

3  Charlie Brown  202 Birch Ln    alice@example.com  100000.0

4    Alice Smith   456 Oak Ave    diana@example.com   30000.0

5   Diana Wilson  101 Maple Dr  charlie@example.com  100000.0

6     Emma Davis   789 Pine Rd  charlie@example.com  100000.0

7    Bob Johnson   456 Oak Ave     emma@example.com   30000.0

8   Diana Wilson   456 Oak Ave     emma@example.com   30000.0

9    Alice Smith   123 Main St      bob@example.com  100000.0



DataFrame with Traditional Data Masking (Name and Email):

&nbsp;       Name       Address                 Email  Salary

0  User\_2683  101 Maple Dr  user7773@example.com   62911

1   User\_894   123 Main St  user9993@example.com   63606

2   User\_907  101 Maple Dr  user7773@example.com   55571

3   User\_907  202 Birch Ln  user7954@example.com   52446

4  User\_2683   456 Oak Ave  user1880@example.com   74013

5  User\_5385  101 Maple Dr  user9993@example.com   62532

6   User\_894   789 Pine Rd  user9993@example.com   70423

7  User\_3729   456 Oak Ave  user7773@example.com   59422

8  User\_5385   456 Oak Ave  user7773@example.com   85354

9  User\_2683   123 Main St  user5649@example.com   45783

Setting `pad\_token\_id` to `eos\_token\_id`:50256 for open-end generation.

Successfully loaded GPT-2 model and tokenizer



**Generated Anonymized Text Example:**

**Privacy in digital applications is enhanced by strong trust in the user's ability to navigate this site and receive and understand the content offered by such user sites and websites. In this way, the site is much more accessible and reliable than any other application that is created by users.**

