An incident report/ postmortem report on Web Stack Outage on January 15th, 2024

Postmortem: When the Web Stack Went on a Coffee Break

Issue Summary:

Duration: January 15, 2024, 09:30 AM - 01:45 PM (WAT)
Impact: User authentication service decided to play hide and seek, causing a 30% login failure party.
Root Cause: The database connection pool threw a wild party with too many idle connections, leading to a temporary digital lockdown.
Timeline:

09:30 AM: The user authentication service declared it needed a vacation, causing a stir in the system.
09:45 AM: Monitoring alerts started screaming louder than a toddler in a candy store, indicating something was amiss.
10:00 AM: Initial investigation pointed fingers at a potential DDoS attack—turns out, it was just the system having a caffeine crash.
11:00 AM: The network team played detective, ruling out the DDoS theory and suspecting a backend rebellion.
12:00 PM: Database team unmasked the culprit - a misconfiguration in the database connection pool settings. Idle connections were partying too hard.
01:00 PM: Incident escalated to senior engineers who promised to have a stern talk with the misbehaving database.
01:45 PM: Issue resolved after the system was reminded that we are here to work, not party.
Root Cause and Resolution:

Root Cause: The database connection pool got too comfortable, resulting in a chaos of idle connections that overwhelmed the database resources and triggered the authentication rebellion.
Resolution: The system was sternly reminded of its responsibilities by rolling back the recent server update and teaching the database connection pool some manners.
Corrective and Preventative Measures:

Improvements/Fixes:

Enhance Monitoring: We're adding more monitoring tools than an over-caffeinated barista, ensuring we catch misbehaving components before they start a rebellion.
Automated Rollback Mechanism: Developing an automated rollback mechanism, because rolling back updates should be as easy as hitting "Undo" in a document.
Documentation Review: Going through our documentation like a hawk-eyed editor to catch potential misconfigurations before they can cause trouble.
Tasks to Address the Issue:

Implement Automated Rollback: Because we want our system to have the grace of a cat, always landing on its feet even when updates go awry.
Database Connection Pool Tuning: We're giving the database connection pool a crash course in etiquette, making sure it doesn't invite too many idle connections to the party.
Enhanced Monitoring Implementation: Adding more eyes on our system than a potato has eyes, ensuring we catch issues before they become full-blown problems.
Training and Awareness: Educating our operations team to be the Sherlock Holmes of misconfigurations, detecting them before they can wreak havoc.
Conclusion:
Our web stack decided to take a coffee break, but we quickly reminded it that work comes before play. With enhanced monitoring, automated rollback mechanisms, and a stern talk with the misbehaving components, we're confident our system will stay focused and keep the digital partying to a minimum. After all, we're here to work hard and code harder!
