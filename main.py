import ctypes
import os
import random
import string
import threading

import requests

from colors import PINK, RED, RESET


class NitroGenerator:
    def __init__(self, mode: int) -> None:
        self.mode = mode
        self.valids = 0
        self.invalids = 0
        self.retries = 0

    def _save(self, data: str) -> None:
        with open("Valid.txt", "a+") as f:
            f.write(data + "\n")

    def _update_title(self) -> None:
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW(
                "[Most Advanced Nitro Gen] - Checking"
                f" - Checked: {self.valids + self.invalids} |"
                f" Valids: {self.valids} | Invalids: {self.invalids}"
                f" | Retries: {self.retries}"
            )

    def _checker(self) -> None:
        while True:
            nitro = "".join(
                random.choices(string.ascii_letters + string.digits, k=self.mode)
            )

            proxy = random.choice(self.proxies)
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}

            try:
                response = requests.get(
                    f"https://discord.com/api/v9/entitlements/gift-codes/{nitro}",
                    proxies=proxies,
                    timeout=3,
                )
                if response.status_code == 200:
                    print(
                        f"{PINK}[{RESET}VALID{PINK}]{RESET} Valid nitro{PINK}: {nitro}"
                    )
                    self.valids += 1
                    self._save("discord.gift/" + nitro)
                elif response.status_code == 404:
                    print(
                        f"{RED}[{RESET}INVALID{RED}]{RESET} Invalid nitro{RED}: {nitro}"
                    )
                    self.invalids += 1
                else:
                    self.retries += 1

            except Exception:
                self.retries += 1

    def main(self) -> None:
        with open("proxies.txt", encoding="utf-8") as f:
            self.proxies = [line.strip() for line in f]

        threading.Thread(target=self._update_title).start()

        for _ in range(300):
            threading.Thread(target=self._checker).start()


if __name__ == "__main__":
    os.system("cls && title [Most Advanced Nitro Gen] - Main Menu")

    mode = input(
        f"{PINK}[{RESET}1{PINK}] Nitro Classic \n"
        f"{PINK}[{RESET}2{PINK}] Nitro With Boost \n\n"
        f"{PINK}[{RESET}>{PINK}]{RESET} "
    )

    print()

    if mode == "1":
        sex_machine = NitroGenerator(16)
        sex_machine.main()
    elif mode == "2":
        sex_machine = NitroGenerator(24)
        sex_machine.main()
    else:
        print(f"{RED}[{RESET}INVALID{RED}]{RESET} Invalid option")
        os.system("pause >nul")
