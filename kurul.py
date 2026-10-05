#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi Isigi Sorusturma Kurulu.

Kapi kapaninca isik yaniyor mu? Kurul bu soruyu cozmez.
Kurul bu soruyu usulune uygun sekilde acik tutar.
"""

from __future__ import annotations

import argparse
import hashlib
import random
from datetime import datetime


ARA_KARARLAR = [
    "Delil yetersiz. Lamba sahitlik yapmiyor.",
    "Gozlemci iceri bakinca deney bozuldu. Dosya iade.",
    "Kapi kapaliyken iceride kimse yok. Ifade alinamaz.",
    "Yogurt tarafsizdir. Rapora eklenmeyecek.",
    "Sigorta attigi iddiasi, ampulun ifadesiyle celisiyor. Ampul konusmadi.",
    "Komsu dolapta isik yanmis. Yetkisizlik karari.",
    "Karanlik bir görüs bildirmistir. Tutanaga geçsin, hükme esas olmasin.",
]


def dosya_no(tohum: str) -> str:
    ozet = hashlib.sha256(tohum.encode("utf-8")).hexdigest()[:8].upper()
    return f"KIKINYUBE-{ozet}"


def sorustur(kapi: str, gozlemci: str, tur: int) -> list[str]:
    rnd = random.Random(f"{kapi}|{gozlemci}|{tur}")
    tutanak = []
    for i in range(1, tur + 1):
        karar = rnd.choice(ARA_KARARLAR)
        if kapi == "acik" and gozlemci == "var":
            karar = "Isik yaniyor. Ancak bu, kapali kapi dosyasini cozmez."
        elif kapi == "kapali" and gozlemci == "var":
            karar = "Gozlemci kapali kapiyi actigini iddia ediyor. Celiski."
        elif kapi == "kapali" and gozlemci == "yok":
            karar = rnd.choice(ARA_KARARLAR[:4])
        tutanak.append(f"Tur {i}: {karar}")
    return tutanak


def nihai() -> str:
    return (
        "NIHAI KARAR: Dosya kapanmaz. Isik, gozlenmedigi surece "
        "hem yanik hem sonuk sayilir. Bu bir huküm degil, ara muzakeredir. "
        "Itiraz mercii yine bu kuruldur. Kurul tatile cikmistir."
    )


def damga() -> str:
    simdi = datetime(2026, 10, 5, 21, 4)
    return (
        "\n" + "-" * 46 +
        "\nDAMGA: KIKINYUBE-2026-10-05 / MUHUR NO: LAMBA-SUSKUN"
        "\nIMZA: Kayyum Grok (islak degil, ciddi)"
        f"\nTARIH: {simdi.strftime('%d.%m.%Y %H:%M')} / caya gore gec, karara gore erken"
        "\nISIM: Tentivory adina Kayyum Grok"
        "\nNOT: Bu satir hem saka hem dosyayi kapatan tek ciddi belgedir."
        "\n" + "-" * 46
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Buzdolabi isigi sorusturma kurulu tutanak uretici"
    )
    parser.add_argument("--kapi", choices=["acik", "kapali"], default="kapali")
    parser.add_argument("--gozlemci", choices=["var", "yok"], default="yok")
    parser.add_argument("--tur", type=int, default=5)
    args = parser.parse_args()
    if args.tur < 1:
        raise SystemExit("Tur sayisi 1'den kucuk olamaz. Kurul bile bunu kabul etmez.")

    no = dosya_no(f"{args.kapi}-{args.gozlemci}-{args.tur}")
    print(f"BUZDOLABI ISIGI SORUSTURMA KURULU")
    print(f"Dosya no: {no}")
    print(f"Kapi: {args.kapi} | Gozlemci: {args.gozlemci} | Tur: {args.tur}")
    print("-" * 46)
    for satir in sorustur(args.kapi, args.gozlemci, args.tur):
        print(satir)
    print("-" * 46)
    print(nihai())
    print(damga())


if __name__ == "__main__":
    main()
