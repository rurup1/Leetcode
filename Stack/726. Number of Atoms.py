class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def key_multiply(table, i) -> None:
            for k, v in table.items():
                table[k] = v * i   
        def merge_table(smaller, main):
            for k, v in smaller.items():
                main[k] = v + main.get(k, 0)

            return main
        def table_to_str(table) -> str:
            table = dict(sorted(table.items()))
            res = ""
            for k, v in table.items():
                if k == "":
                    continue
                if v == 1:
                    v = ""

                res += k + str(v)

            return res
        def find_count(index, skip):
            count = 0
            j = index
            while j < len(formula):
                if formula[j].isdigit():
                    count = (count * 10) + int(formula[j])
                    skip.append(j)
                else:
                    break

                j += 1

            return (count, skip)

        table, stack, atom, count = {}, [], "", 0
        skip = []
        for i, item in enumerate(formula):
            if i in skip:
                count = 0
                continue

            if item == "(":
                if atom:
                    table[atom] = table.get(atom, 0) + (count or 1)
                    atom, count = "", 0
                
                atom = ""
                stack.append(table)
                table = {}

            elif item == ")":
                if atom:
                    table[atom] = table.get(atom, 0) + (count or 1)
                    atom, count = "", 0
                
                main_table = stack.pop()
                count, skip = find_count(i + 1, skip)
                if count != 0:
                    key_multiply(table, count)
                    
                table = merge_table(table, main_table)
            elif item.isalpha():
                if not atom and item.isupper(): # Beginning of a new atom
                    atom += item
                elif item.isupper(): # KN case. K(1)N
                    if atom:
                        table[atom] = table.get(atom, 0) + (count or 1)
                    
                    atom = "" + item
                    count = 0
                else:
                    atom += item

                
            elif item.isdigit():
                count = (10 * count) + int(item)

        if atom:
            table[atom] = table.get(atom, 0) + (count or 1)

        return table_to_str(table)
                
class Solution:
    # Optimization #1:
    # Context: After reaching ')', we need to find the count of what to multiply by. These are to the
    # right of ). For example: Mg(OH)12. We use @find_count for this. After this is done, we must skip past those indices, because they are already processed. Because I was doing: for i, item in enumerate(formula), the only way I could do this is by using a skip_list. I would query the list each time:

    # if i in skipList:
    #   count = 0
    #   continue

    # This was uneffective, O(n) lookup and O(n) extra overhead.
    
    # Solution: Use a while loop, and increment i += 1, or i += (j - i), where j is the index that we 
    # stopped at after searching for the count.
    def countOfAtoms(self, formula: str) -> str:
        def key_multiply(table, i) -> None:
            for k, v in table.items():
                table[k] = v * i
            
        def merge_table(smaller, main):
            for k, v in smaller.items():
                main[k] = v + main.get(k, 0)

            return main
        def table_to_str(table) -> str:
            table = dict(sorted(table.items()))
            res = ""
            for k, v in table.items():
                if k == "":
                    continue
                if v == 1:
                    v = ""

                res += k + str(v)

            return res
        def find_count(index):
            count = 0
            j = index
            while j < len(formula):
                if formula[j].isdigit():
                    count = (count * 10) + int(formula[j])
                else:
                    break

                j += 1

            return (count, j)

        table = {}
        stack = []
        atom = ""
        count = 0
        i, n = 0, len(formula)
        while i < n:
            item = formula[i]
            j = i + 1
            if item == "(":
                if atom:
                    table[atom] = table.get(atom, 0) + (count or 1)
                    atom, count = "", 0
                
                stack.append(table)
                table = {}
            elif item == ")":
                if atom:
                    table[atom] = table.get(atom, 0) + (count or 1)
                    atom, count = "", 0
                
                main_table = stack.pop()
                count, j = find_count(i + 1)
                if count != 0:
                    key_multiply(table, count)

                table = merge_table(table, main_table)
                count = 0
            elif item.isalpha():
                if not atom:
                    atom += item
                elif item.isupper():
                    table[atom] = table.get(atom, 0) + (count or 1)
                    atom = "" + item
                    count = 0
                else:
                    atom += item
            else:
                count = (10 * count) + int(item)

            i += (j - i)

        if atom:
            table[atom] = table.get(atom, 0) + (count or 1)
        return table_to_str(table)
    
class Solution:
    # Optimization #2:
    # This was definitely harder to tackle. The find_count function is not a clean approach because there become two multi-digit
    # number accumulations, for for count, and one for find_count. We can solve this by just interleaving everything into the count variable. When we reach a ")", instead of trying to go ahead and finding the count, we can just mark a boolean flag as true and move on.

    # Then, the loop will iterate to the count eventually. When we hit a boundary: for this problem it is '(', ')', the end of the string, or an uppercase letter, we know that we have fully read the count. So, we can multiply the table we have and merge it into the main_table.
    def countOfAtoms(self, formula: str) -> str:
        def key_multiply(table, i) -> None:
            for k, v in table.items():
                table[k] = v * i
        def merge_table(smaller, main):
            for k, v in smaller.items():
                main[k] = v + main.get(k, 0)

            return main
        def table_to_str(table) -> str:
            table = dict(sorted(table.items()))
            res = ""
            for k, v in table.items():
                if k == "":
                    continue
                if v == 1:
                    v = ""

                res += k + str(v)

            return res

        table = {}
        stack = []
        atom = ""
        count = 0
        i, n = 0, len(formula)
        flag = False
        while i < n:
            item = formula[i]
            if item == "(":
                if atom:
                    table[atom] = table.get(atom, 0) + (count or 1)
                    atom, count = "", 0

                if flag:
                    if count != 0:
                        key_multiply(table, count)
                    table = merge_table(table, main_table)
                    flag, count = False, 0
                
                stack.append(table)
                table = {}
            elif item == ")":
                if atom:
                    table[atom] = table.get(atom, 0) + (count or 1)
                    atom, count = "", 0

                if flag:
                    if count != 0:
                        key_multiply(table, count)
                    table = merge_table(table, main_table)
                    flag, count = False, 0
                
                main_table = stack.pop()
                flag = True
                count = 0
            elif item.isalpha():
                if not atom:
                    atom += item
                    if flag:
                        if count != 0:
                            key_multiply(table, count)

                        table = merge_table(table, main_table)
                        flag, count = False, 0
                elif item.isupper():
                    table[atom] = table.get(atom, 0) + (count or 1)
                    atom = "" + item
                    count = 0
                else:
                    atom += item
            else:
                count = (10 * count) + int(item)

            i += 1

        if atom:
            table[atom] = table.get(atom, 0) + (count or 1)

        if flag:
            if count != 0:
                key_multiply(table, count)
            table = merge_table(table, main_table)

        return table_to_str(table)
     
