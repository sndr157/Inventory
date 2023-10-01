# SuperPy Code Review Report

## Introduction

I# Issue 1:
**Title:** Disorganized File Structure Causing Import Errors

**Description:**
In your initial submission, all the scripts were placed in the root directory, which resulted in an untidy project structure and caused various import errors throughout the project. When executing the main script `superpy.py`, some of the module imports aren't recognized due to the disorganized file structure.

**Solution:**
To rectify this, reorganize your files by creating folders to categorize your scripts. For example, you might create a folder named "modules" and move the `buy_product.py`, `sell_product.py`, `expire`,`inventory`, `utils`,`profit`, `sold` and other similar scripts into it. Also add a folder name "data" for `bought.csv` and `sold.csv`. Adjust your import statements accordingly in `superpy.py`:

```python
from modules.buy_product import buy_product as buy
from modules.sell_product import sell_product as sell
# ... other imports ...
```


Example:

```python
# If utils.py is also moved to the 'modules' directory
from . import utils
```


# Issue 2:
**Title:** Duplicate IDs generated in the `get_new_id()` function

**Description:**
The `get_new_id()` function in the `buy_product.py` script is meant to assure a unique ID for each new purchase. However, if two instances of the application are running concurrently, this function may generate duplicate IDs.

**Solution:**
To resolve this issue, you can lock the file during the operation to prevent concurrent write operations.

```python
import fcntl

def get_new_id():
    # ... Code to open the file ...
    fcntl.flock(csvfile.fileno(), fcntl.LOCK_EX)
    # ... Rest of the code ...
    fcntl.flock(csvfile.fileno(), fcntl.LOCK_UN)
```

# Issue 3:
**Title:** Product name with special characters causing issues 

**Description:**
In the `buy_product()` function from `buy_product.py`, a product name with special characters (like commas or double quotes) might disrupt the CSV formatting as no sanitization is present to handle such issue.

**Solution:** 
Simple sanitization can be added by escaping special characters from the `product_name` before writing to the CSV file.

```python
# In buy_product function
product_name = csv_escape(product_name)

# Add this function 
def csv_escape(s):
    return '"' + s.replace('"', '""') + '"' if ',' in s or '"' in s else s
```

# Issue 4:
**Title:** Commands executed without any arguments causing program errors

**Description:**
If any of the commands (like 'buy', 'sell', etc.) in the `superpy.py` script are run without the required arguments, it causes the program to terminate unexpectedly without a proper error message.

**Solution:**
To fix this issue, you can add a check in `run_cli()` to see if the required arguments for a command are

## **Summary**

Embarking on the SuperPy.py project, I found myself in the throes of a perplexing puzzle 🧩. Each component acting as a singular piece that made sense on its own, but when it came to weaving them cohesively into one big picture, the real challenge emerged. 😓

Right out of the gate, my spirits were high, full of pep and zeal 🔥. After all, SuperPy.py was no ordinary tool – it held the potential to simplify ongoing tasks like buying and selling products, monitoring inventory, tracking expired items, and calculating profits. Just when I began to hit my stride and things seemed to be going well, my computer system decided to throw a spanner in the works, creating a setback that felt as awkward as forcing the wrong puzzle piece into a spot it did not belong. 💻🙈

The first round was a real eye-opener. My mentor noted the excessive complexity of my code and, to my surprise, the lack of argparse, a basic requirement for testing. His objective and accurate feedback 🎯 felt like a gut punch 🥊. It was a shock to understand that I had missed such a fundamental aspect. It was like I had been meticulously sorting through my puzzle, only to discover that I had pieces from different sets thrown into the mix.

Processing this feedback was a bitter pill to swallow 😩. But instead of wallowing in disappointment, I decided to see this feedback as a silver lining. It was a much-needed wake-up call, allowing me to take a step back, reassess the situation, and correct my course 📝💪. 

After wallowing deep in my sorrows, I was determined to bounce back stronger in the second round 💪🔥, my new mantra was simplicity. I set out to create a more streamlined version, devoid of the earlier complexities. But while it felt like progress (especially given that the new, simplified code was working as expected), my mentor's feedback once again left me flummoxed. He emphasized the importance of seeking guidance and asking for help, pushing me into a vortex of self-doubt. What was I doing wrong this time? Was the code fine but the approach flawed, or was it something else altogether? Wasn't the simpler, working code better than before? Bright as a light was my realization that even a working solution could be improved upon while this might have been a bitter gulp. This feedback felt like a severe blow. It made me feel like I was back at square one, without a clue about my direction. It was like the Earth beneath me was ready to crumble. 🌍😟
But having a study buddy made a world of difference! There's no match for having a companion to brainstorm with, someone who gets the ups and downs of your journey. A big shoutout to **G** 🥰. Thank you for being my rock and always lending an understanding ear! 🙏💖

Confronting reality, I knew I had to brave the storm and give the project one more shot, but my confidence was just not there. My third attempt led me to revisit the revised version of the original project, it was a disarrayed collection of code, much like a box of puzzle pieces jumbled together. As intimidating as it was, this ordeal instilled a new determination within me 😱. This time, I not only optimized the old code but relied on the lessons learned through my past experiences and the wealth of resources available online. Revisiting well-organized files from React projects turned out to be a game-changer. As the confusion began to clear, the light at the end of the tunnel became evident - my 'Aha!' moment 🎉. Myriads of uncertainties and numerous failed stabs at the problem notwithstanding, I passionately forged ahead. If my computer could speak, it would’ve scripted an epic tale of resilience 😅💦!

Calling upon wisdom attained from past errors, I compartmentalized tasks, akin to organizing edge and corner puzzle pieces first during puzzle-solving. This divide-and-conquer approach significantly streamlined application management 🗂✔️.

To make the narrative less complex, I graced my code with a visually-rich Run_App.md. Step-by-step instructions to run the application, supported by diagrams, were included. It provided not only the much-needed assurance that the application worked but was also crucial in explaining the functionality to others ✔️🔍.

Each section served as an individual puzzle piece, waiting to fit perfectly in the grand scheme of things 🎯. The journey was a roller coaster with moments of vexation, countless hours wrestling codes, and building resilience. Each adversary met was transformed into a learning and growing opportunity 🌱💫.

All the efforts finally bore fruit – resulting in an efficient SuperPy.py application capable of executing a myriad of tasks, such as product buying and selling, inventory checks, tracking expired products, and profit calculations 💡.

The journey had its share of thorns, but the experience and learnings amassed were immensely gratifying. In the end, the sense of achievement mirrors the satisfaction felt when completing an arduously complex puzzle 🏅. I genuinely hope 🙏 this project not only meets my mentors' expectations but also aids fellow students 🎓👩‍💻👨‍💻🎉.

My advice to future students venturing on this path: find yourselves a Study Buddy! This companionship could transform your journey, making the ups and downs less arduous and way more enjoyable. Not only does this companionship make your journey less lonely, but it also makes the entire learning process more enriching and rewarding! 🤝🎓💡
