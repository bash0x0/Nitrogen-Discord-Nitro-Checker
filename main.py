import ctypes
import os
import random
import string
import threading

import requests

from colors import PINK, RED, RESET


class NitroGenerator:
    def __init__(self) -> None:
        self.valids = 0
        self.invalids = 0
        self.retries = 0

        with open("data/proxies.txt", encoding="utf-8") as f:
            self.proxies = [line.strip() for line in f]

    def _save(self, data: str) -> None:
        with open("data/valid.txt", "a+") as f:
            f.write(data + "\n")

    def _update_title(self) -> None:
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW(
                "[Nitrogen] - Checking"
                f" - Checked: {self.valids + self.invalids} |"
                f" Valids: {self.valids} | Invalids: {self.invalids}"
                f" | Retries: {self.retries}"
            )

    def _check(self, nitro: str) -> None:
        while True:
            proxy = random.choice(self.proxies)
            proxies = {"http": f"socks4://{proxy}", "https": f"socks4://{proxy}"}
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
                    break
                elif response.status_code == 404:
                    print(
                        f"{RED}[{RESET}INVALID{RED}]{RESET} Invalid nitro{RED}: {nitro}"
                    )
                    self.invalids += 1
                    break
                else:
                    self.retries += 1

            except Exception:
                self.retries += 1

    def custom_mode(self) -> None:
        with open("data/custom.txt", encoding="utf-8") as f:
            customs = [line.strip() for line in f]

        if not customs:
            print(f"{RED}[{RESET}!{RED}]{RESET} Paste nitro codes in data/custom.txt")
            os.system("pause >nul")
            os._exit(0)

        threading.Thread(target=self._update_title).start()
        for custom in customs:
            threading.Thread(target=self._check, args=(custom,)).start()

    def bruteforce_mode(self) -> None:
        mode = input(
            f"{PINK}[{RESET}1{PINK}] Nitro Classic \n"
            f"{PINK}[{RESET}2{PINK}] Nitro With Boost \n\n"
            f"{PINK}[{RESET}>{PINK}]{RESET} "
        )

        print()

        if mode == "1":
            lenght = 16
        elif mode == "2":
            lenght = 24
        else:
            print(f"{RED}[{RESET}!{RED}]{RESET} Invalid option")
            os.system("pause >nul")
            os._exit(0)

        threading.Thread(target=self._update_title).start()
        while True:
            nitro = "".join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(lenght)
            )
            threading.Thread(target=self._check, args=(nitro,)).start()


if __name__ == "__main__":
    os.system("cls && title [Nitrogen] - Most Advanced Discord Nitro Checker")

    option = input(
        f"{PINK}[{RESET}1{PINK}] Bruteforce codes \n"
        f"{PINK}[{RESET}2{PINK}] Check codes from data/custom.txt \n\n"
        f"{PINK}[{RESET}>{PINK}]{RESET} "
    )

    print()

    if option == "1":
        sex_machine = NitroGenerator()
        sex_machine.bruteforce_mode()
    elif option == "2":
        sex_machine = NitroGenerator()
        sex_machine.custom_mode()
    else:
        print(f"{RED}[{RESET}!{RED}]{RESET} Invalid option")
        os.system("pause >nul")
