# BTCZHalving v1.0 by Zalpader
import time
import subprocess
import os

BLOCK_TIME = 2.5 * 60  # Convert 2.5 minutes to seconds
HALVING_INTERVAL = 840000
INITIAL_REWARD = 12500

def get_remaining_time(current_block):
    halving_count = current_block // HALVING_INTERVAL
    halving_block = (halving_count + 1) * HALVING_INTERVAL
    blocks_remaining = halving_block - current_block
    time_remaining = blocks_remaining * BLOCK_TIME
    remaining_time = time.time() + time_remaining
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(remaining_time))
    reward = INITIAL_REWARD / (2 ** halving_count)
    next_reward = INITIAL_REWARD / (2 ** (halving_count + 1))
    return blocks_remaining, formatted_time, halving_count, reward, next_reward

last_halving_block = -1
formatted_time = ""

while True:
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

    result = subprocess.check_output(["bitcoinz-cli", "getblockcount"], text=True).strip()
    current_block = int(result)

    if current_block != last_halving_block:
        last_halving_block = current_block
        blocks_remaining, formatted_time, halving_count, reward, next_reward = get_remaining_time(current_block)
        next_halving_block = (halving_count + 1) * HALVING_INTERVAL

    print(f"Current block: {current_block}")
    print(f"Next halving block: {next_halving_block}")
    print(f"Blocks remaining until halving: {blocks_remaining}")

    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print(f"Current date UTC+0 Zone: {current_time}")

    remaining_seconds = time.mktime(time.strptime(formatted_time, "%Y-%m-%d %H:%M:%S")) - time.time()

    remaining_days, remaining_seconds = divmod(remaining_seconds, 24 * 60 * 60)
    remaining_hours, remaining_seconds = divmod(remaining_seconds, 60 * 60)
    remaining_minutes, remaining_seconds = divmod(remaining_seconds, 60)
    remaining_years, remaining_days = divmod(remaining_days, 365)
    remaining_months, remaining_days = divmod(remaining_days, 30)

    formatted_remaining_time = f"Remaining time: {int(remaining_years)} years {int(remaining_months)} months {int(remaining_days)} days {int(remaining_hours)} hours {int(remaining_minutes)} minutes {int(remaining_seconds)} seconds"

    print(f"Halving date UTC+0 Zone: {formatted_time}")
    print(formatted_remaining_time)

    print(f"Number of completed halvings: {halving_count}")
    print(f"Number of coins in the current halving: {int(reward)}")
    print(f"Number of coins in the next halving: {int(next_reward)}")

    time.sleep(1)
