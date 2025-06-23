{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from collections import defaultdict\
\
THRESHOLD = 3\
failed_logins = defaultdict(int)\
success_after_fail = \{\}\
\
with open('log_sample.txt.txt', 'r') as log_file:\
    for line in log_file:\
        if "Failed password" in line:\
            parts = line.strip().split()\
            ip = parts[parts.index("from") + 1]\
            failed_logins[ip] += 1\
\
        elif "Accepted password" in line:\
            parts = line.strip().split()\
            ip = parts[parts.index("from") + 1]\
            if failed_logins[ip] >= THRESHOLD:\
                success_after_fail[ip] = True\
\
# Display suspicious IPs\
print("\\n\uc0\u55357 \u56589  Suspicious IPs Detected:\\n")\
for ip in success_after_fail:\
    print(f"\uc0\u9888 \u65039   \{ip\} had \{failed_logins[ip]\} failed attempts before a successful login.")\
}