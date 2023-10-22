from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())


def unique_koala_facts(number_facts: int):
    loops, max_loops = 0, 1000
    facts = []
    while len(facts < number_facts):
        fact = random_koala_fact
        if fact not in facts:
            facts.append(fact)
        if loops > max_loops:
            break
        loops  += 1
    return facts